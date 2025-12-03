# 智慧校园访客管理系统
一个作为软件测试学习准备的真实可运行项目Demo，它不仅是一个小功能，而是一个端到端可运行的测试。

- **需求分析 & 测试设计能力**
- **UI 自动化测试（Selenium + Pytest）**
- **测试环境容器化（Docker + Selenium Grid）**
- **缺陷定位与调试能力**
- **可一键启动的端到端测试环境**

## 项目特点
### ✔ 1. 业务需求分析 & 测试场景设计  
包含访客预约 → 管理员审批 → 门禁验证的完整测试流程。

### ✔ 2. 自动化测试框架搭建  
使用 Selenium + Pytest 实现 E2E 自动化测试。

### ✔ 3. 测试环境容器化  
使用 Docker Compose 启动包括以下组件的完整测试平台：
- Flask Web 系统
- Selenium Grid Hub
- Chrome Node
- 自动化测试 Runner

### ✔ 4. 缺陷定位与调试  
项目内包含 Flask 后端 + 前端，从 UI 到后端都可调试。

### ✔ 5. 一键运行  
一个命令即可启动测试环境，并自动执行 UI 自动化测试。

## 如何一键运行整个测试环境
### 克隆项目
- git clone http
- cd smart-campus-visitor-testing

### 启动全部服务（Flask + Selenium Grid + 自动化测试）
- docker-compose up --build
#### 系统会自动启动以下服务：
- smart-campus-flask → Web 系统（预约/审批/门禁）
- selenium-hub → Selenium Hub
- selenium-chrome → Chrome Node
- selenium-tests → 自动执行 UI 自动化测试

### 查看自动化测试结果
#### 你会看到类似输出：
- selenium-tests | test session starts
- selenium-tests | collected 1 item
- selenium-tests | test_e2e_booking.py PASSED
- selenium-tests | 1 passed in 0.80s 

表示自动化测试成功执行。

### 手动访问系统，访问：http://localhost:5000

可以手工体验完整流程：
- 访客预约
- 管理员审批
- 门禁验证
