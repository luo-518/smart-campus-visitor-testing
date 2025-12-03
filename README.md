智慧校园访客管理系统
一个作为软件测试学习准备的真实可运行项目Demo。
它不仅是一个小功能，而是一个端到端可运行的测试环境：

1. 需求分析 & 测试设计能力
对访客预约 → 审批 → 门禁验证的完整流程进行建模
设计等价类、边界值、场景法等测试思路
项目逻辑完全贴合真实业务

2. 自动化测试能力（Selenium + Pytest）
使用Selenium Grid远程执行浏览器自动化
Pytest结构清晰，可扩展性强
UI自动化框架搭建

3. Docker 容器化测试环境
Flask后端服务
Selenium Hub + Chrome Node
自动化测试容器（test-runner）
通过docker-compose一键启动完整环境

4. 缺陷定位 & Debug 能力
使用Flask原型构建可运行业务流程
通过日志、断点、容器日志定位并修复问题
Selenium Grid + Docker健康检查


项目架构
smart-campus-visitor-testing/
├─ app/
│  ├─ templates/        # 前端页面（访客预约 / 管理审批 / 门禁验证）
│  ├─ storage.py        # 内存数据库（简化模型）
│  └─ main.py           # Flask 业务逻辑：预约、审批、门禁验证
│
├─ automation/
│  └─ test_e2e_booking.py   # Selenium + Pytest UI 自动化测试
│
├─ Dockerfile               # Flask 应用容器
├─ Dockerfile.tests         # 自动化测试容器
├─ docker-compose.yml       # 一键启动 Selenium Grid + Flask + 自动化测试
├─ requirements.txt         # Flask 依赖
├─ requirements.test.txt    # 自动化测试依赖
└─ README.md                # 项目说明（本文）

Q:如何一键运行整个测试环境
A:克隆项目
git clone https://github.com/你的用户名/smart-campus-visitor-testing.git
cd smart-campus-visitor-testing

A:启动全部服务（Flask + Selenium Grid + 自动化测试）
docker-compose up --build
系统会自动启动以下服务：
smart-campus-flask → Web 系统（预约/审批/门禁）
selenium-hub → Selenium Hub
selenium-chrome → Chrome Node
selenium-tests → 自动执行 UI 自动化测试

查看自动化测试结果
你会看到类似输出：
selenium-tests | ============================== test session starts ===============================
selenium-tests | collected 1 item
selenium-tests | test_e2e_booking.py PASSED
selenium-tests | ============================== 1 passed in 0.80s ===============================
表示自动化测试成功执行。

PS:
手动访问系统，访问：http://localhost:5000
可以手工体验完整流程：
访客预约
管理员审批
门禁验证
