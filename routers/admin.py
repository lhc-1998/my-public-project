from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User, RegistrationRequest
from schemas import RegisterRequestResponse, RegisterRequestListResponse, ApprovalRequest
from auth import get_current_user

router = APIRouter(prefix="/api/admin", tags=["管理员"])


def require_admin(current_user: User = Depends(get_current_user)):
    """验证管理员权限"""
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="需要管理员权限")
    return current_user


@router.get("/registration-requests", response_model=RegisterRequestListResponse)
def list_registration_requests(
    status: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """获取注册申请列表"""
    query = db.query(RegistrationRequest)
    
    if status:
        query = query.filter(RegistrationRequest.status == status)
    else:
        # 默认只显示待审批和未过期的申请
        query = query.filter(RegistrationRequest.status.in_(["pending", "approved", "rejected"]))
    
    requests = query.order_by(RegistrationRequest.created_at.desc()).all()
    
    return RegisterRequestListResponse(
        total=len(requests),
        requests=[RegisterRequestResponse.model_validate(r) for r in requests]
    )


@router.post("/registration-requests/{request_id}/approve")
def approve_registration(
    request_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """批准注册申请"""
    # 查找申请
    reg_request = db.query(RegistrationRequest).filter(
        RegistrationRequest.id == request_id
    ).first()
    
    if not reg_request:
        raise HTTPException(status_code=404, detail="申请不存在")
    
    if reg_request.status != "pending":
        raise HTTPException(status_code=400, detail=f"该申请状态为 {reg_request.status}，无法审批")
    
    # 检查用户名是否已被占用
    existing_user = db.query(User).filter(User.username == reg_request.username).first()
    if existing_user:
        reg_request.status = "rejected"
        reg_request.reviewed_at = datetime.utcnow()
        reg_request.reviewed_by = current_user.id
        reg_request.reject_reason = "用户名已被注册"
        db.commit()
        raise HTTPException(status_code=400, detail="用户名已被注册，已自动拒绝")
    
    # 创建用户
    new_user = User(
        username=reg_request.username,
        password=reg_request.password,
        role="student"
    )
    db.add(new_user)
    
    # 更新申请状态
    reg_request.status = "approved"
    reg_request.reviewed_at = datetime.utcnow()
    reg_request.reviewed_by = current_user.id
    
    db.commit()
    
    return {"message": "已批准注册申请，用户已创建"}


@router.post("/registration-requests/{request_id}/reject")
def reject_registration(
    request_id: int,
    approval_data: ApprovalRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """拒绝注册申请"""
    reg_request = db.query(RegistrationRequest).filter(
        RegistrationRequest.id == request_id
    ).first()
    
    if not reg_request:
        raise HTTPException(status_code=404, detail="申请不存在")
    
    if reg_request.status != "pending":
        raise HTTPException(status_code=400, detail=f"该申请状态为 {reg_request.status}，无法审批")
    
    reg_request.status = "rejected"
    reg_request.reviewed_at = datetime.utcnow()
    reg_request.reviewed_by = current_user.id
    reg_request.reject_reason = approval_data.reject_reason or "管理员拒绝"
    
    db.commit()
    
    return {"message": "已拒绝注册申请"}


@router.delete("/registration-requests/cleanup")
def cleanup_expired_requests(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """清理过期的注册申请（超过1天）"""
    expire_time = datetime.utcnow() - timedelta(days=1)
    
    # 查找并删除过期的待审批申请
    expired_requests = db.query(RegistrationRequest).filter(
        RegistrationRequest.status == "pending",
        RegistrationRequest.created_at < expire_time
    ).all()
    
    count = len(expired_requests)
    for req in expired_requests:
        req.status = "expired"  # 标记为过期而不是直接删除（保留记录）
    
    db.commit()
    
    return {
        "message": f"已处理 {count} 条过期申请",
        "expired_count": count
    }


@router.get("/registration-requests/pending-count")
def get_pending_count(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """获取待审批申请数量"""
    count = db.query(RegistrationRequest).filter(
        RegistrationRequest.status == "pending"
    ).count()
    
    return {"pending_count": count}


@router.get("/users")
def list_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """获取用户列表"""
    users = db.query(User).order_by(User.created_at.desc()).all()
    
    return {
        "total": len(users),
        "users": [
            {
                "id": u.id,
                "username": u.username,
                "role": u.role,
                "created_at": u.created_at.isoformat() if u.created_at else None
            }
            for u in users
        ]
    }
