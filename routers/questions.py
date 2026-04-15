from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Question, User
from schemas import QuestionCreate, QuestionResponse
from auth import get_current_user, require_teacher

router = APIRouter(prefix="/api/questions", tags=["题库"])


@router.get("", response_model=dict)
def get_questions(
    category: str = None,
    type: str = None,
    difficulty: int = None,
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    query = db.query(Question)
    if category:
        query = query.filter(Question.category == category)
    if type:
        query = query.filter(Question.type == type)
    if difficulty:
        query = query.filter(Question.difficulty == difficulty)
    
    total = query.count()
    questions = query.offset(skip).limit(limit).all()
    
    # 转换为字典用于序列化
    questions_data = []
    for q in questions:
        questions_data.append({
            "id": q.id,
            "category": q.category,
            "type": q.type,
            "content": q.content,
            "options": q.options,
            "answer": q.answer,
            "analysis": q.analysis,
            "difficulty": q.difficulty
        })
    
    return {
        "total": total,
        "page": skip // limit + 1,
        "page_size": limit,
        "total_pages": (total + limit - 1) // limit,
        "questions": questions_data
    }


@router.get("/{question_id}", response_model=QuestionResponse)
def get_question(question_id: int, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="题目不存在")
    return question


@router.post("", response_model=QuestionResponse)
def create_question(
    question_data: QuestionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_teacher)
):
    question = Question(**question_data.model_dump())
    db.add(question)
    db.commit()
    db.refresh(question)
    return question


@router.put("/{question_id}", response_model=QuestionResponse)
def update_question(
    question_id: int,
    question_data: QuestionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_teacher)
):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="题目不存在")

    for key, value in question_data.model_dump().items():
        setattr(question, key, value)

    db.commit()
    db.refresh(question)
    return question


@router.delete("/{question_id}")
def delete_question(
    question_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_teacher)
):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="题目不存在")

    db.delete(question)
    db.commit()
    return {"message": "题目已删除"}
