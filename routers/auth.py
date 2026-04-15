from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import User, RegistrationRequest
from schemas import (
    UserCreate, UserLogin, UserResponse, Token,
    RegisterRequest, RegisterStatusResponse
)
from auth import verify_password, get_password_hash, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(prefix="/api/auth", tags=["认证"])


@router.post("/register", response_model=RegisterStatusResponse)
def register(user_data: RegisterRequest, db: Session = Depends(get_db)):
    """用户注册 - 提交申请等待管理员审批"""
    # 检查用户名是否已存在（用户表）
    existing_user = db.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="用户名已存在")

    # 检查是否有待审批的申请
    existing_request = db.query(RegistrationRequest).filter(
        RegistrationRequest.username == user_data.username,
        RegistrationRequest.status == "pending"
    ).first()
    if existing_request:
        raise HTTPException(status_code=400, detail="该用户名已有待审批的申请，请等待审批")

    # 检查是否有过期但未处理的申请（超过1天）
    old_request = db.query(RegistrationRequest).filter(
        RegistrationRequest.username == user_data.username,
        RegistrationRequest.status.in_(["pending", "expired"])
    ).first()
    if old_request:
        # 删除过期申请
        db.delete(old_request)

    # 创建注册申请
    hashed_password = get_password_hash(user_data.password)
    new_request = RegistrationRequest(
        username=user_data.username,
        password=hashed_password,
        status="pending"
    )
    db.add(new_request)
    db.commit()

    return RegisterStatusResponse(
        status="pending",
        message="注册申请已提交，请等待管理员审批"
    )


@router.get("/register/status/{username}", response_model=RegisterStatusResponse)
def check_register_status(username: str, db: Session = Depends(get_db)):
    """查询注册申请状态"""
    request = db.query(RegistrationRequest).filter(
        RegistrationRequest.username == username
    ).order_by(RegistrationRequest.created_at.desc()).first()

    if not request:
        return RegisterStatusResponse(
            status="not_found",
            message="未找到注册申请记录"
        )

    return RegisterStatusResponse(
        status=request.status,
        message=_get_status_message(request.status),
        reviewed_at=request.reviewed_at,
        reject_reason=request.reject_reason
    )


def _get_status_message(status: str) -> str:
    messages = {
        "pending": "申请正在等待审批",
        "approved": "申请已通过，请登录",
        "rejected": "申请被拒绝",
        "expired": "申请已过期"
    }
    return messages.get(status, "未知状态")


@router.post("/login", response_model=Token)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_data.username).first()
    if not user or not verify_password(user_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误"
        )

    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return Token(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse.model_validate(user)
    )


@router.get("/me", response_model=UserResponse)
def get_current_user_info(current_user: User = Depends(__import__('auth', fromlist=['get_current_user']).get_current_user)):
    return UserResponse.model_validate(current_user)
