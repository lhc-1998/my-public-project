# 考试系统 - 技术规格文档

## 1. 项目概述

- **项目名称**: 在线考试系统
- **项目类型**: 全栈 Web 应用
- **核心功能**: 题库管理、在线答题、自动评分
- **技术栈**: FastAPI (后端) + SQLite (数据库) + 原生 HTML/JS (前端)

## 2. 题库范围

| 类别 | 描述 |
|------|------|
| MySQL | 数据库查询、索引、事务、优化等 |
| Python | 语法、面向对象、模块、异常处理等 |
| Linux Shell | 命令行操作、脚本编写、文件系统等 |

## 3. 支持题型

- [x] 单选题
- [x] 多选题
- [x] 判断题
- [x] 简答题/填空题

## 4. 功能模块

### 4.1 用户管理
- 用户登录/注册（需管理员审批）
- 角色区分：学生、教师、管理员
- 密码加密存储
- 注册申请审批（管理员后台审批）
- 申请超时自动过期（24小时后）

### 4.2 题库管理
- 题目 CRUD 操作
- 按类别筛选题目
- 题目难度标记

### 4.3 试卷生成
- 按类别随机抽题
- 设定题目数量
- 生成唯一试卷

### 4.4 在线答题
- 实时计时
- 答题进度保存
- 提交答案

### 4.5 自动评分
- 选择题/判断题：即时评分
- 简答题：关键词匹配评分

## 5. 数据模型

### 5.1 用户表 (users)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER | 主键 |
| username | VARCHAR(50) | 用户名 |
| password | VARCHAR(255) | 密码(哈希) |
| role | VARCHAR(20) | 角色(student/teacher/admin) |
| created_at | DATETIME | 创建时间 |

### 5.2 题目表 (questions)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER | 主键 |
| category | VARCHAR(50) | 类别(MySQL/Python/Linux) |
| type | VARCHAR(20) | 题型 |
| content | TEXT | 题目内容 |
| options | TEXT | 选项(JSON) |
| answer | TEXT | 正确答案 |
| analysis | TEXT | 解析 |
| difficulty | INTEGER | 难度(1-3) |

### 5.3 试卷表 (exams)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER | 主键 |
| title | VARCHAR(100) | 试卷标题 |
| user_id | INTEGER | 考生ID |
| score | FLOAT | 得分 |
| status | VARCHAR(20) | 状态 |
| created_at | DATETIME | 创建时间 |

### 5.4 答题表 (answers)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER | 主键 |
| exam_id | INTEGER | 试卷ID |
| question_id | INTEGER | 题目ID |
| user_answer | TEXT | 用户答案 |
| is_correct | BOOLEAN | 是否正确 |
| score | FLOAT | 得分 |

### 5.5 注册申请表 (registration_requests)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER | 主键 |
| username | VARCHAR(50) | 用户名 |
| password | VARCHAR(255) | 密码(哈希) |
| status | VARCHAR(20) | 状态(pending/approved/rejected/expired) |
| created_at | DATETIME | 申请时间 |
| reviewed_at | DATETIME | 审批时间 |
| reviewed_by | INTEGER | 审批人ID |
| reject_reason | VARCHAR(255) | 拒绝原因 |

## 6. API 接口

### 认证
- `POST /api/auth/register` - 用户注册（提交申请）
- `POST /api/auth/login` - 用户登录
- `GET /api/auth/register/status/{username}` - 查询注册申请状态

### 管理员
- `GET /api/admin/registration-requests` - 获取注册申请列表
- `POST /api/admin/registration-requests/{id}/approve` - 批准注册申请
- `POST /api/admin/registration-requests/{id}/reject` - 拒绝注册申请
- `DELETE /api/admin/registration-requests/cleanup` - 清理过期申请
- `GET /api/admin/registration-requests/pending-count` - 获取待审批数量

### 题库
- `GET /api/questions` - 获取题目列表
- `POST /api/questions` - 创建题目
- `PUT /api/questions/{id}` - 更新题目
- `DELETE /api/questions/{id}` - 删除题目

### 考试
- `POST /api/exam/generate` - 生成试卷
- `GET /api/exam/{id}` - 获取试卷详情
- `POST /api/exam/{id}/submit` - 提交试卷
- `GET /api/exam/history` - 考试历史

### 评分
- `POST /api/exam/{id}/grade` - 评分

## 7. 验收标准

- [x] 用户可以注册和登录
- [x] 教师可以管理题库（增删改查）
- [x] 学生可以开始考试，系统随机生成试卷
- [x] 支持全部四种题型
- [x] 自动评分功能正常
- [x] 考试历史可查询
- [x] 题库包含 MySQL、Python、Linux Shell 三类题目
