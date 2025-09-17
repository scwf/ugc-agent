"""
文件管理工具
"""
import os
import shutil
from typing import Optional
from pathlib import Path
from app.core.config import settings

class FileManager:
    """文件管理器"""
    
    @staticmethod
    def ensure_dir(path: str) -> None:
        """确保目录存在"""
        Path(path).mkdir(parents=True, exist_ok=True)
    
    @staticmethod
    def get_task_dir(task_id: str, dir_type: str = "temp") -> str:
        """获取任务目录路径"""
        base_dir = getattr(settings, f"{dir_type.upper()}_DIR")
        task_dir = os.path.join(base_dir, task_id)
        FileManager.ensure_dir(task_dir)
        return task_dir
    
    @staticmethod
    def cleanup_task_files(task_id: str) -> None:
        """清理任务相关文件"""
        for dir_type in ["temp", "upload"]:
            task_dir = os.path.join(getattr(settings, f"{dir_type.upper()}_DIR"), task_id)
            if os.path.exists(task_dir):
                shutil.rmtree(task_dir)
    
    @staticmethod
    def get_file_size(file_path: str) -> Optional[int]:
        """获取文件大小"""
        try:
            return os.path.getsize(file_path)
        except OSError:
            return None
    
    @staticmethod
    def file_exists(file_path: str) -> bool:
        """检查文件是否存在"""
        return os.path.isfile(file_path)
