#!/usr/bin/env python3
"""
UGC Agent 后端启动脚本
"""
import uvicorn
import os
from app.core.config import settings

if __name__ == "__main__":
    # 创建必要的目录
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    os.makedirs(settings.OUTPUT_DIR, exist_ok=True)
    os.makedirs(settings.TEMP_DIR, exist_ok=True)
    
    # 启动服务
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
