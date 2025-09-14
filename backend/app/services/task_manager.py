import asyncio
import uuid
from datetime import datetime
from typing import Dict, List, Optional
from concurrent.futures import ThreadPoolExecutor
import threading

from app.models.task import TaskCreate, TaskResponse, TaskStatus, TaskType, TaskUpdate
from app.core.config import settings
from app.services.workflow_manager import WorkflowManager

class TaskManager:
    """任务管理器"""
    
    def __init__(self):
        self.tasks: Dict[str, TaskResponse] = {}
        self.executor = ThreadPoolExecutor(max_workers=settings.MAX_CONCURRENT_TASKS)
        self.workflow_manager = WorkflowManager()
        self._lock = threading.Lock()
    
    async def create_task(self, task_data: TaskCreate) -> TaskResponse:
        """创建新任务"""
        task_id = str(uuid.uuid4())
        
        task = TaskResponse(
            id=task_id,
            task_type=task_data.task_type,
            input_url=task_data.input_url,
            title=task_data.title or f"Task {task_id[:8]}",
            status=TaskStatus.PENDING,
            progress=0.0,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            config=task_data.config or {}
        )
        
        with self._lock:
            self.tasks[task_id] = task
        
        return task
    
    async def get_task(self, task_id: str) -> Optional[TaskResponse]:
        """获取任务"""
        return self.tasks.get(task_id)
    
    async def get_all_tasks(self) -> List[TaskResponse]:
        """获取所有任务"""
        return list(self.tasks.values())
    
    async def update_task(self, task_id: str, update_data: TaskUpdate) -> Optional[TaskResponse]:
        """更新任务"""
        with self._lock:
            if task_id not in self.tasks:
                return None
            
            task = self.tasks[task_id]
            update_dict = update_data.dict(exclude_unset=True)
            
            for field, value in update_dict.items():
                setattr(task, field, value)
            
            task.updated_at = datetime.now()
            
            if update_data.status == TaskStatus.COMPLETED:
                task.completed_at = datetime.now()
        
        return task
    
    async def delete_task(self, task_id: str) -> bool:
        """删除任务"""
        with self._lock:
            if task_id in self.tasks:
                # TODO: 清理相关文件
                del self.tasks[task_id]
                return True
            return False
    
    async def process_task(self, task_id: str):
        """处理任务（在后台执行）"""
        task = await self.get_task(task_id)
        if not task:
            return
        
        try:
            # 更新任务状态为处理中
            await self.update_task(task_id, TaskUpdate(
                status=TaskStatus.PROCESSING,
                current_step="Initializing workflow"
            ))
            
            # 根据任务类型选择工作流
            if task.task_type == TaskType.VIDEO_TRANSLATE:
                await self.workflow_manager.run_video_translate_workflow(task_id, task)
            elif task.task_type == TaskType.VIDEO_INTERPRET:
                await self.workflow_manager.run_video_interpret_workflow(task_id, task)
            elif task.task_type == TaskType.BLOG_TO_VIDEO:
                await self.workflow_manager.run_blog_to_video_workflow(task_id, task)
            
            # 如果没有异常，标记为完成
            await self.update_task(task_id, TaskUpdate(
                status=TaskStatus.COMPLETED,
                progress=100.0,
                current_step="Task completed"
            ))
            
        except Exception as e:
            # 处理异常
            await self.update_task(task_id, TaskUpdate(
                status=TaskStatus.FAILED,
                error_message=str(e),
                current_step="Task failed"
            ))
