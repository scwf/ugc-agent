"""
LangGraph工作流状态定义
"""
from typing import Dict, Any, Optional, TypedDict
from app.models.task import TaskType, TaskStatus

class WorkflowState(TypedDict):
    """工作流状态"""
    # 任务基本信息
    task_id: str
    task_type: TaskType
    input_url: str
    config: Dict[str, Any]
    
    # 状态信息
    status: TaskStatus
    progress: float
    current_step: str
    
    # 文件路径
    files: Dict[str, str]  # {"video": "path/to/video.mp4", "audio": "path/to/audio.wav", ...}
    
    # 预览数据
    preview_data: Dict[str, Any]  # 存储各个预览节点的数据
    
    # 错误信息
    error_message: Optional[str]
