# UGC Agent - AI视频解说生成器

一个开源的AI驱动视频解说生成工具，专为个人内容创作者设计，帮助用户快速将优质的YouTube视频和博客文章转换为中文解说视频。

## 功能特性

- **视频翻译**：将YouTube视频转换为中文配音版本
- **视频解读**：生成视频内容的中文解读视频
- **博客转视频**：将博客文章转换为解说视频
- **预览确认**：关键步骤支持预览和调整
- **批量处理**：支持多任务并行处理

## 技术栈

### 后端
- **框架**: FastAPI
- **工作流**: LangGraph + LangChain
- **AI服务**: DeepSeek API、Kimi API、Whisper API
- **视频处理**: FFmpeg、yt-dlp
- **任务队列**: Python threading

### 前端
- **框架**: React
- **状态管理**: TBD
- **UI组件**: TBD

## 快速开始

### 环境要求
- Python 3.9+
- Node.js 16+
- FFmpeg

### 后端安装

1. 创建虚拟环境
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置环境变量
```bash
cp .env.example .env
# 编辑 .env 文件，填入API密钥
```

4. 启动服务
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### API文档

启动后端服务后，访问以下地址查看API文档：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 开发指南

### 项目结构
```
ugc-agent/
├── backend/
│   ├── app/
│   │   ├── api/           # API路由
│   │   ├── core/          # 核心配置
│   │   ├── models/        # 数据模型
│   │   ├── services/      # 业务服务
│   │   └── workflows/     # LangGraph工作流
│   ├── requirements.txt
│   └── main.py
├── frontend/              # React前端（待开发）
├── docs/                  # 文档
├── prd.md                 # 产品需求文档
└── tasks.md              # 开发任务清单
```

### 开发阶段

当前进度：**MVP v1.0 开发中**

- [x] 项目基础架构搭建
- [x] FastAPI后端框架
- [x] LangGraph工作流框架
- [ ] YouTube视频翻译功能
- [ ] 前端界面开发
- [ ] 端到端集成测试

## 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 致谢

- [LangGraph](https://github.com/langchain-ai/langgraph) - 工作流框架
- [FastAPI](https://fastapi.tiangolo.com/) - 现代Python Web框架
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube下载工具
- [FFmpeg](https://ffmpeg.org/) - 视频处理工具
