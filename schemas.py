from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


# ============ 用户 Schema ============
class UserCreate(BaseModel):
    username: str
    password: str
    role: str = "student"


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    role: str
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse


# ============ 题目 Schema ============
class QuestionBase(BaseModel):
    category: str
    type: str
    content: str
    options: Optional[str] = None
    answer: str
    analysis: Optional[str] = None
    difficulty: int = 1


class QuestionCreate(QuestionBase):
    pass


class QuestionResponse(QuestionBase):
    id: int

    class Config:
        from_attributes = True


# ============ 试卷 Schema ============
class ExamGenerate(BaseModel):
    category: str = "all"
    question_count: int = 10


class AnswerSubmit(BaseModel):
    question_id: int
    user_answer: str


class ExamSubmit(BaseModel):
    answers: List[AnswerSubmit]


class AnswerResponse(BaseModel):
    id: int
    question_id: int
    user_answer: Optional[str]
    is_correct: bool
    score: float
    question: Optional[QuestionResponse] = None

    class Config:
        from_attributes = True


class ExamResponse(BaseModel):
    id: int
    title: str
    category: str
    total_score: float
    score: float
    status: str
    created_at: datetime
    answers: List[AnswerResponse] = []

    class Config:
        from_attributes = True


class ExamListResponse(BaseModel):
    id: int
    title: str
    category: str
    total_score: float
    score: float
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


# ============ 统计 Schema ============
class StatsResponse(BaseModel):
    total_users: int
    total_questions: int
    total_exams: int
    category_stats: dict


# ============ 注册申请 Schema ============
class RegisterRequest(BaseModel):
    """注册请求（申请）"""
    username: str
    password: str


class RegisterRequestResponse(BaseModel):
    """注册申请响应"""
    id: int
    username: str
    status: str
    created_at: datetime
    reviewed_at: Optional[datetime] = None
    reject_reason: Optional[str] = None

    class Config:
        from_attributes = True


class RegisterRequestListResponse(BaseModel):
    """申请列表"""
    total: int
    requests: List[RegisterRequestResponse]


class ApprovalRequest(BaseModel):
    """审批请求"""
    action: str  # approve, reject
    reject_reason: Optional[str] = None  # 拒绝时填写原因


class RegisterStatusResponse(BaseModel):
    """查询注册状态"""
    status: str
    message: str
    reviewed_at: Optional[datetime] = None
    reject_reason: Optional[str] = None
