import random
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db
from models import Question, Exam, Answer, User
from schemas import (
    ExamGenerate, ExamSubmit, ExamResponse, ExamListResponse,
    AnswerSubmit, AnswerResponse, StatsResponse
)
from auth import get_current_user

router = APIRouter(prefix="/api/exam", tags=["考试"])


def grade_answer(question: Question, user_answer: str, options: str = None) -> tuple:
    """评分函数
    
    Args:
        question: 题目对象
        user_answer: 用户答案（选项字母）
        options: 题目选项（JSON字符串），用于匹配完整答案
    """
    import json
    
    if question.type in ["single", "multiple", "judge"]:
        given = user_answer.strip().upper()
        
        # 判断题：兼容中文答案
        if question.type == "judge":
            correct = question.answer.strip().upper()
            correct_map = {'正确': 'TRUE', '错误': 'FALSE'}
            if correct in correct_map:
                correct = correct_map[correct]
            given_map = {'正确': 'TRUE', '错误': 'FALSE'}
            if given in given_map:
                given = given_map[given]
            is_correct = correct == given
            
        # 多选题：排序后比较
        elif question.type == "multiple":
            correct = question.answer.strip().upper()
            correct_sorted = ','.join(sorted(correct.split(',')))
            given_sorted = ','.join(sorted(given.split(','))) if given else ''
            is_correct = correct_sorted == given_sorted
            
        # 单选题
        else:
            correct = question.answer.strip()
            
            # 情况1：标准格式 - 答案就是选项字母（A/B/C/D）
            if len(correct) == 1 and correct.upper() in ['A', 'B', 'C', 'D', 'E']:
                is_correct = given == correct.upper()
            else:
                # 情况2：答案是完整文本
                answer_letter = None
                if options:
                    try:
                        opts = json.loads(options)
                        correct_lower = correct.lower()
                        # 定义字母映射
                        letter_map = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
                        
                        for i, opt in enumerate(opts):
                            if opt:
                                opt = opt.strip()
                                # 提取选项字母和文本
                                if '.' in opt:
                                    # 格式: "A. 张三"
                                    opt_letter = opt[0].upper()
                                    opt_text = opt[opt.index('.')+1:].strip().lower()
                                elif len(opt) > 0 and opt[0].isalpha() and len(opt) <= 2:
                                    # 格式: "A" 或 "AB"
                                    opt_letter = opt[0].upper()
                                    opt_text = opt.lower()
                                else:
                                    # 格式: "张三" (无字母前缀)
                                    opt_letter = letter_map.get(i, chr(65+i))
                                    opt_text = opt.lower()
                                
                                # 检查这个选项是否匹配正确答案
                                if opt_text == correct_lower or correct_lower in opt_text or opt_text in correct_lower:
                                    answer_letter = opt_letter
                                    break
                    except Exception as e:
                        pass
                
                if answer_letter:
                    is_correct = given == answer_letter
                else:
                    # 无法匹配，直接比较文本
                    is_correct = given == correct.upper()
                
        score = 5 if is_correct else 0  # 选择题每题5分
    else:
        # 简答题：关键词匹配
        keywords = question.answer.lower().split(",")
        user_lower = user_answer.lower()
        matched = sum(1 for kw in keywords if kw.strip() in user_lower)
        score = (matched / len(keywords)) * 5 if keywords else 0
        is_correct = score >= 3  # 简答题需要匹配一半以上关键词
        score = round(score, 2)

    return is_correct, score


@router.post("/generate", response_model=ExamResponse)
def generate_exam(
    exam_data: ExamGenerate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # 查询符合条件的题目
    query = db.query(Question)
    if exam_data.category != "all":
        query = query.filter(Question.category == exam_data.category)

    all_questions = query.all()
    if len(all_questions) < exam_data.question_count:
        raise HTTPException(status_code=400, detail="题库中题目数量不足")

    # 随机抽取题目
    selected = random.sample(all_questions, exam_data.question_count)

    # 创建试卷
    category_name = "综合测试" if exam_data.category == "all" else exam_data.category
    exam = Exam(
        title=f"{category_name}考试",
        user_id=current_user.id,
        category=exam_data.category,
        total_score=len(selected) * 5,
        status="pending"
    )
    db.add(exam)
    db.commit()
    db.refresh(exam)

    # 创建答题记录（空的）
    for q in selected:
        answer = Answer(exam_id=exam.id, question_id=q.id)
        db.add(answer)
    db.commit()
    db.refresh(exam)

    # 返回完整的试卷信息
    exam_dict = {
        "id": exam.id,
        "title": exam.title,
        "category": exam.category,
        "total_score": exam.total_score,
        "score": exam.score,
        "status": exam.status,
        "created_at": exam.created_at,
        "answers": []
    }

    for ans in exam.answers:
        exam_dict["answers"].append({
            "id": ans.id,
            "question_id": ans.question_id,
            "user_answer": ans.user_answer,
            "is_correct": ans.is_correct,
            "score": ans.score,
            "question": {
                "id": ans.question.id,
                "category": ans.question.category,
                "type": ans.question.type,
                "content": ans.question.content,
                "options": ans.question.options,
                "answer": ans.question.answer,
                "analysis": ans.question.analysis,
                "difficulty": ans.question.difficulty
            }
        })

    return exam_dict


@router.get("/{exam_id}", response_model=ExamResponse)
def get_exam(exam_id: int, db: Session = Depends(get_db)):
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="试卷不存在")

    exam_dict = {
        "id": exam.id,
        "title": exam.title,
        "category": exam.category,
        "total_score": exam.total_score,
        "score": exam.score,
        "status": exam.status,
        "created_at": exam.created_at,
        "answers": []
    }

    for ans in exam.answers:
        exam_dict["answers"].append({
            "id": ans.id,
            "question_id": ans.question_id,
            "user_answer": ans.user_answer,
            "is_correct": ans.is_correct,
            "score": ans.score,
            "question": {
                "id": ans.question.id,
                "category": ans.question.category,
                "type": ans.question.type,
                "content": ans.question.content,
                "options": ans.question.options,
                "answer": ans.question.answer,
                "analysis": ans.question.analysis,
                "difficulty": ans.question.difficulty
            }
        })

    return exam_dict


@router.post("/{exam_id}/submit")
def submit_exam(
    exam_id: int,
    exam_data: ExamSubmit,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    exam = db.query(Exam).filter(Exam.id == exam_id, Exam.user_id == current_user.id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="试卷不存在")
    if exam.status == "graded":
        raise HTTPException(status_code=400, detail="试卷已评分")

    total_score = 0
    for answer_data in exam_data.answers:
        answer = db.query(Answer).filter(
            Answer.exam_id == exam_id,
            Answer.question_id == answer_data.question_id
        ).first()

        if answer:
            answer.user_answer = answer_data.user_answer
            question = answer.question
            is_correct, score = grade_answer(question, answer_data.user_answer, question.options)
            answer.is_correct = is_correct
            answer.score = score
            total_score += score

    exam.score = total_score
    exam.status = "graded"
    db.commit()

    return {
        "message": "试卷已提交",
        "score": total_score,
        "total": exam.total_score,
        "status": "graded"
    }


@router.get("/history/list", response_model=List[ExamListResponse])
def get_exam_history(
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    exams = db.query(Exam).filter(Exam.user_id == current_user.id)\
        .order_by(Exam.created_at.desc())\
        .offset(skip).limit(limit).all()
    return exams


@router.get("/stats", response_model=StatsResponse)
def get_stats(db: Session = Depends(get_db)):
    total_users = db.query(User).count()
    total_questions = db.query(Question).count()
    total_exams = db.query(Exam).count()

    # 各类别题目数量
    category_stats = {}
    for cat in ["MySQL", "Python", "Linux"]:
        count = db.query(Question).filter(Question.category == cat).count()
        category_stats[cat] = count

    return StatsResponse(
        total_users=total_users,
        total_questions=total_questions,
        total_exams=total_exams,
        category_stats=category_stats
    )
