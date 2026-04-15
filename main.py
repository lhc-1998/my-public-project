import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import engine, SessionLocal, init_database
from models import Base, User, Question, RegistrationRequest
from auth import get_password_hash

# 初始化数据库（创建数据库和表）
init_database()

app = FastAPI(title="在线考试系统", version="1.0.0")

# 静态文件和模板
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
async def root():
    return RedirectResponse(url="/login")


@app.get("/index", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/exam", response_class=HTMLResponse)
async def exam_page(request: Request):
    return templates.TemplateResponse("exam.html", {"request": request})


@app.get("/exam/{exam_id}", response_class=HTMLResponse)
async def exam_detail_page(request: Request, exam_id: int):
    return templates.TemplateResponse("exam_detail.html", {"request": request, "exam_id": exam_id})


@app.get("/history", response_class=HTMLResponse)
async def history_page(request: Request):
    return templates.TemplateResponse("history.html", {"request": request})


@app.get("/questions", response_class=HTMLResponse)
async def questions_page(request: Request):
    return templates.TemplateResponse("questions.html", {"request": request})


@app.get("/admin", response_class=HTMLResponse)
async def admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})


@app.get("/api/stats/public")
async def public_stats():
    db = SessionLocal()
    try:
        total_questions = db.query(Question).count()
        category_stats = {}
        for cat in ["MySQL", "Python", "Linux"]:
            count = db.query(Question).filter(Question.category == cat).count()
            category_stats[cat] = count
        return {"total_questions": total_questions, "category_stats": category_stats}
    finally:
        db.close()


# 导入路由
from routers.auth import router as auth_router
from routers.questions import router as questions_router
from routers.exam import router as exam_router
from routers.admin import router as admin_router

app.include_router(auth_router)
app.include_router(questions_router)
app.include_router(exam_router)
app.include_router(admin_router)


def init_data():
    """初始化数据"""
    db = SessionLocal()
    try:
        # 检查是否已有用户
        if db.query(User).count() == 0:
            users = [
                User(username="admin", password=get_password_hash("admin123"), role="admin"),
                User(username="teacher", password=get_password_hash("teacher123"), role="teacher"),
                User(username="student", password=get_password_hash("student123"), role="student"),
            ]
            for u in users:
                db.add(u)

        # 检查是否已有题目
        if db.query(Question).count() == 0:
            questions = get_initial_questions()
            for q in questions:
                db.add(Question(**q))

        db.commit()
        print("[OK] Data initialization complete")
    except Exception as e:
        print(f"[ERROR] Initialization error: {e}")
        db.rollback()
    finally:
        db.close()


def get_initial_questions():
    """初始题目数据"""
    return [
        # ============ MySQL 题目 ============
        {"category": "MySQL", "type": "single", "content": "以下哪个命令用于查看 MySQL 数据库的所有表？",
         "options": json.dumps(["A. SHOW TABLES", "B. LIST TABLES", "C. DISPLAY TABLES", "D. VIEW TABLES"]),
         "answer": "A", "analysis": "SHOW TABLES 是 MySQL 查看当前数据库所有表的命令", "difficulty": 1},

        {"category": "MySQL", "type": "single", "content": "MySQL 中用于创建索引的关键字是？",
         "options": json.dumps(["A. INDEX", "B. KEY", "C. Both A and B", "D. CREATE INDEX"]),
         "answer": "C", "analysis": "INDEX、KEY 和 CREATE INDEX 都可以用于创建索引", "difficulty": 1},

        {"category": "MySQL", "type": "single", "content": "在 MySQL 中，INT 类型占用多少字节？",
         "options": json.dumps(["A. 2字节", "B. 4字节", "C. 8字节", "D. 16字节"]),
         "answer": "B", "analysis": "INT 在 MySQL 中占用 4 个字节，范围是 -2^31 到 2^31-1", "difficulty": 1},

        {"category": "MySQL", "type": "multiple", "content": "以下哪些是 MySQL 的存储引擎？",
         "options": json.dumps(["A. InnoDB", "B. MyISAM", "C. MongoDB", "D. MEMORY"]),
         "answer": "A,B,D", "analysis": "InnoDB、MyISAM 和 MEMORY 都是 MySQL 的存储引擎，MongoDB 不是", "difficulty": 1},

        {"category": "MySQL", "type": "judge", "content": "MySQL 的 InnoDB 存储引擎支持外键约束。",
         "answer": "TRUE", "analysis": "InnoDB 支持外键，而 MyISAM 不支持", "difficulty": 1},

        {"category": "MySQL", "type": "judge", "content": "DELETE 语句可以回滚，而 TRUNCATE 语句不可以回滚。",
         "answer": "TRUE", "analysis": "DELETE 可以回滚，TRUNCATE 是 DDL 语句，不可回滚", "difficulty": 2},

        {"category": "MySQL", "type": "short", "content": "请写出查询 student 表中 age 大于 20 的所有字段的 SQL 语句。",
         "answer": "select,*from,where,age,>,20", "analysis": "标准答案是 SELECT * FROM student WHERE age > 20", "difficulty": 2},

        {"category": "MySQL", "type": "single", "content": "用于连接字符串的 MySQL 函数是？",
         "options": json.dumps(["A. CONCAT()", "B. JOIN()", "C. MERGE()", "D. COMBINE()"]),
         "answer": "A", "analysis": "CONCAT() 函数用于连接多个字符串", "difficulty": 1},

        {"category": "MySQL", "type": "single", "content": "哪个命令用于修改表结构？",
         "options": json.dumps(["A. ALTER TABLE", "B. MODIFY TABLE", "C. CHANGE TABLE", "D. UPDATE TABLE"]),
         "answer": "A", "analysis": "ALTER TABLE 用于修改表结构，如添加列、修改列等", "difficulty": 1},

        {"category": "MySQL", "type": "judge", "content": "PRIMARY KEY 和 UNIQUE 约束都允许空值。",
         "answer": "FALSE", "analysis": "PRIMARY KEY 不允许空值，UNIQUE 允许一个空值", "difficulty": 2},

        # ============ Python 题目 ============
        {"category": "Python", "type": "single", "content": "Python 中列表的索引从哪个数字开始？",
         "options": json.dumps(["A. 0", "B. 1", "C. -1", "D. 由开发者指定"]),
         "answer": "A", "analysis": "Python 列表的索引从 0 开始，第一个元素索引为 0", "difficulty": 1},

        {"category": "Python", "type": "single", "content": "以下哪个是 Python 的不可变数据类型？",
         "options": json.dumps(["A. list", "B. dict", "C. tuple", "D. set"]),
         "answer": "C", "analysis": "tuple 是不可变的，创建后不能修改；list、dict、set 都是可变的", "difficulty": 1},

        {"category": "Python", "type": "single", "content": "Python 中用于输出到控制台的函数是？",
         "options": json.dumps(["A. echo()", "B. print()", "C. printf()", "D. console()"]),
         "answer": "B", "analysis": "print() 是 Python 的标准输出函数", "difficulty": 1},

        {"category": "Python", "type": "multiple", "content": "以下哪些是 Python 的数据类型？",
         "options": json.dumps(["A. int", "B. str", "C. array", "D. bool"]),
         "answer": "A,B,D", "analysis": "int、str、bool 都是 Python 内置数据类型；array 需要导入", "difficulty": 1},

        {"category": "Python", "type": "judge", "content": "Python 支持多继承。",
         "answer": "TRUE", "analysis": "Python 允许多继承，即一个类可以继承多个父类", "difficulty": 1},

        {"category": "Python", "type": "judge", "content": "在 Python 中，字符串是不可变的。",
         "answer": "TRUE", "analysis": "字符串创建后不能直接修改，必须创建新的字符串", "difficulty": 1},

        {"category": "Python", "type": "short", "content": "请写出使用列表推导式生成 1-10 平方数的代码。",
         "answer": "[x**2,for x,in range,range(1,11)]", "analysis": "答案是 [x**2 for x in range(1, 11)]", "difficulty": 2},

        {"category": "Python", "type": "single", "content": "用于定义类的方法是？",
         "options": json.dumps(["A. def", "B. function", "C. method", "D. class"]),
         "answer": "A", "analysis": "def 用于定义函数和方法", "difficulty": 1},

        {"category": "Python", "type": "single", "content": "哪个关键字用于异常处理？",
         "options": json.dumps(["A. try", "B. catch", "C. except", "D. A 和 C"]),
         "answer": "D", "analysis": "Python 使用 try-except 进行异常处理", "difficulty": 1},

        {"category": "Python", "type": "judge", "content": "Python 中的 self 参数指向类本身。",
         "answer": "FALSE", "analysis": "self 指向类的实例对象，而不是类本身", "difficulty": 2},

        # ============ Linux 题目 ============
        {"category": "Linux", "type": "single", "content": "哪个命令用于显示当前工作目录？",
         "options": json.dumps(["A. cd", "B. pwd", "C. dir", "D. cwd"]),
         "answer": "B", "analysis": "pwd (print working directory) 显示当前目录", "difficulty": 1},

        {"category": "Linux", "type": "single", "content": "Linux 中哪个命令用于创建目录？",
         "options": json.dumps(["A. mkdir", "B. makedir", "C. createdir", "D. mkfolder"]),
         "answer": "A", "analysis": "mkdir (make directory) 用于创建目录", "difficulty": 1},

        {"category": "Linux", "type": "single", "content": "哪个命令用于查看文件内容？",
         "options": json.dumps(["A. cat", "B. cp", "C. mv", "D. rm"]),
         "answer": "A", "analysis": "cat 用于查看文件内容，cp 复制，mv 移动，rm 删除", "difficulty": 1},

        {"category": "Linux", "type": "multiple", "content": "以下哪些是 Linux 的权限？",
         "options": json.dumps(["A. read (r)", "B. write (w)", "C. execute (x)", "D. delete (d)"]),
         "answer": "A,B,C", "analysis": "Linux 权限包括 r (读)、w (写)、x (执行)，没有 delete", "difficulty": 1},

        {"category": "Linux", "type": "judge", "content": "在 Linux 中，ls -la 命令可以显示隐藏文件。",
         "answer": "TRUE", "analysis": "ls -la 中的 -a 选项显示所有文件，包括以 . 开头的隐藏文件", "difficulty": 1},

        {"category": "Linux", "type": "judge", "content": "Linux 是开源操作系统。",
         "answer": "TRUE", "analysis": "Linux 是开源项目，遵循 GPL 许可证", "difficulty": 1},

        {"category": "Linux", "type": "short", "content": "请写出递归复制目录的命令。",
         "answer": "cp,-r,cp -r", "analysis": "答案是 cp -r 源目录 目标目录", "difficulty": 2},

        {"category": "Linux", "type": "single", "content": "哪个命令用于查找文件？",
         "options": json.dumps(["A. find", "B. search", "C. locate", "D. A 和 C"]),
         "answer": "D", "analysis": "find 和 locate 都用于查找文件，find 更强大", "difficulty": 1},

        {"category": "Linux", "type": "single", "content": "哪个命令用于修改文件权限？",
         "options": json.dumps(["A. chmod", "B. chown", "C. chgrp", "D. chperm"]),
         "answer": "A", "analysis": "chmod 修改权限，chown 修改所有者，chgrp 修改组", "difficulty": 1},

        {"category": "Linux", "type": "judge", "content": "在 Linux 中，root 用户可以删除所有文件。",
         "answer": "TRUE", "analysis": "root 用户拥有最高权限，可以删除任何文件", "difficulty": 1},
    ]


if __name__ == "__main__":
    import uvicorn
    from datetime import datetime, timedelta
    from models import RegistrationRequest

    init_data()

    # 启动时清理过期申请
    def cleanup_expired_requests():
        db = SessionLocal()
        try:
            expire_time = datetime.utcnow() - timedelta(days=1)
            expired = db.query(RegistrationRequest).filter(
                RegistrationRequest.status == "pending",
                RegistrationRequest.created_at < expire_time
            ).all()
            for req in expired:
                req.status = "expired"
            db.commit()
            if expired:
                print(f"[CLEANUP] 清理了 {len(expired)} 条过期申请")
        except Exception as e:
            print(f"[CLEANUP ERROR] {e}")
            db.rollback()
        finally:
            db.close()

    cleanup_expired_requests()
    uvicorn.run(app, host="0.0.0.0", port=8000)
