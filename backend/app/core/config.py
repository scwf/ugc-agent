from typing import List, Optional
from pydantic import BaseSettings, AnyHttpUrl, validator
import os

class Settings(BaseSettings):
    # API设置
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "UGC Agent"
    
    # CORS设置
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: str | List[str]) -> List[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    # AI服务配置
    DEEPSEEK_API_KEY: Optional[str] = None
    DEEPSEEK_BASE_URL: str = "https://api.deepseek.com"
    
    KIMI_API_KEY: Optional[str] = None
    KIMI_BASE_URL: str = "https://api.moonshot.cn"
    
    WHISPER_API_KEY: Optional[str] = None
    
    # 存储配置
    UPLOAD_DIR: str = "uploads"
    OUTPUT_DIR: str = "outputs"
    TEMP_DIR: str = "temp"
    
    # 任务队列配置
    MAX_CONCURRENT_TASKS: int = 3
    TASK_TIMEOUT: int = 3600  # 1小时
    
    # TTS接口配置（预留）
    TTS_SERVICE_URL: Optional[str] = None
    TTS_API_KEY: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
