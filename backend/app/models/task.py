from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from enum import Enum
from datetime import datetime

class TaskType(str, Enum):
    """任务类型"""
    VIDEO_TRANSLATE = "video_translate"  # 视频翻译
    VIDEO_INTERPRET = "video_interpret"  # 视频解读  
    BLOG_TO_VIDEO = "blog_to_video"     # 博客转视频

class TaskStatus(str, Enum):
    """任务状态"""
    PENDING = "pending"        # 等待中
    PROCESSING = "processing"  # 处理中
    PAUSED = "paused"         # 暂停（等待用户确认）
    COMPLETED = "completed"    # 已完成
    FAILED = "failed"         # 失败
    CANCELLED = "cancelled"    # 已取消

class TaskCreate(BaseModel):
    """创建任务的请求模型"""
    task_type: TaskType
    input_url: str = Field(..., description="输入URL（YouTube视频链接或博客链接）")
    title: Optional[str] = Field(None, description="任务标题")
    config: Optional[Dict[str, Any]] = Field(default_factory=dict, description="任务配置参数")

class TaskResponse(BaseModel):
    """任务响应模型"""
    id: str
    task_type: TaskType
    input_url: str
    title: Optional[str] = None
    status: TaskStatus
    progress: float = Field(0.0, ge=0.0, le=100.0, description="任务进度百分比")
    current_step: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    result_files: Optional[Dict[str, str]] = Field(default_factory=dict, description="结果文件路径")
    config: Optional[Dict[str, Any]] = Field(default_factory=dict)

class TaskUpdate(BaseModel):
    """更新任务的请求模型"""
    status: Optional[TaskStatus] = None
    progress: Optional[float] = Field(None, ge=0.0, le=100.0)
    current_step: Optional[str] = None
    error_message: Optional[str] = None
    result_files: Optional[Dict[str, str]] = None

class PreviewData(BaseModel):
    """预览数据模型"""
    task_id: str
    preview_type: str  # subtitle, translation, audio, video, script, images
    data: Dict[str, Any]
    created_at: datetime
