# -*- coding: utf-8 -*-
from database import SessionLocal, init_database
from models import User, Question, RegistrationRequest
from auth import get_password_hash
import json
import os


def check_questions_exist():
    """检查题库是否有数据"""
    db = SessionLocal()
    try:
        count = db.query(Question).count()
        return count > 0
    finally:
        db.close()


def load_questions_from_backup():
    """从备份文件加载题目到数据库"""
    backup_dir = os.path.join(os.path.dirname(__file__), 'backups')
    backup_file = os.path.join(backup_dir, 'all_questions.json')
    
    if not os.path.exists(backup_file):
        print('[WARN] 备份文件不存在，跳过题库恢复')
        return 0
    
    db = SessionLocal()
    try:
        with open(backup_file, 'r', encoding='utf-8') as f:
            questions_data = json.load(f)
        
        count = 0
        for q in questions_data:
            exists = db.query(Question).filter(
                Question.content == q['content']
            ).first()
            if not exists:
                db.add(Question(**q))
                count += 1
        
        db.commit()
        print(f'[OK] 从备份恢复 {count} 道题目')
        return count
    except Exception as e:
        print(f'[ERROR] 恢复题库失败: {e}')
        return 0
    finally:
        db.close()


def init_data():
    """初始化数据（用户+题库）"""
    db = SessionLocal()

    # 创建默认用户
    users = [
        User(username='admin', password=get_password_hash('admin123'), role='admin'),
        User(username='teacher', password=get_password_hash('teacher123'), role='teacher'),
        User(username='student', password=get_password_hash('student123'), role='student'),
    ]
    for u in users:
        if not db.query(User).filter(User.username == u.username).first():
            db.add(u)

    # 初始化题目 - 优先从备份恢复
    if not check_questions_exist():
        print('[INFO] 题库为空，正在从备份文件恢复...')
        load_questions_from_backup()
    else:
        print(f'[INFO] 题库已有数据，跳过备份恢复 (共 {db.query(Question).count()} 题)')

    db.commit()
    print(f'[OK] Users: {db.query(User).count()}')
    print(f'[OK] Questions: {db.query(Question).count()}')
    db.close()


if __name__ == '__main__':
    print('=' * 50)
    print('初始化数据库')
    print('=' * 50)
    init_database()
    init_data()
    print('=' * 50)
    print('[完成] 数据库初始化完成')
    print('=' * 50)
