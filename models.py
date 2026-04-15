from sqlalchemy import Column, Integer, String, Text, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(20), default="student")  # student, teacher, admin
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    exams = relationship("Exam", back_populates="user")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(50), nullable=False)  # MySQL, Python, Linux
    type = Column(String(20), nullable=False)  # single, multiple, judge, short
    content = Column(Text, nullable=False)
    options = Column(Text)  # JSON string
    answer = Column(Text, nullable=False)
    analysis = Column(Text)
    difficulty = Column(Integer, default=1)  # 1-3

    answers = relationship("Answer", back_populates="question")


class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category = Column(String(50), default="all")  # 考试类别
    total_score = Column(Float, default=0)
    score = Column(Float, default=0)
    status = Column(String(20), default="pending")  # pending, submitted, graded
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="exams")
    answers = relationship("Answer", back_populates="exam", cascade="all, delete-orphan")


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    user_answer = Column(Text)
    is_correct = Column(Boolean, default=False)
    score = Column(Float, default=0)

    exam = relationship("Exam", back_populates="answers")
    question = relationship("Question", back_populates="answers")


class RegistrationRequest(Base):
    """注册申请表"""
    __tablename__ = "registration_requests"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)  # 加密后的密码
    status = Column(String(20), default="pending")  # pending, approved, rejected, expired
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    reviewed_at = Column(DateTime(timezone=True), nullable=True)  # 审批时间
    reviewed_by = Column(Integer, nullable=True)  # 审批人ID
    reject_reason = Column(String(255), nullable=True)  # 拒绝原因
