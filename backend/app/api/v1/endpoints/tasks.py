from fastapi import APIRouter, HTTPException, BackgroundTasks
from typing import Dict, Any, List
from app.models.task import TaskCreate, TaskResponse, TaskStatus
from app.services.task_manager import TaskManager
from app.core.config import settings

router = APIRouter()
task_manager = TaskManager()

@router.post("/", response_model=TaskResponse)
async def create_task(
    task_data: TaskCreate,
    background_tasks: BackgroundTasks
) -> TaskResponse:
    """
    创建新的视频处理任务
    """
    try:
        task = await task_manager.create_task(task_data)
        # 在后台启动任务处理
        background_tasks.add_task(task_manager.process_task, task.id)
        return task
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[TaskResponse])
async def get_tasks() -> List[TaskResponse]:
    """
    获取所有任务列表
    """
    return await task_manager.get_all_tasks()

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(task_id: str) -> TaskResponse:
    """
    获取特定任务详情
    """
    task = await task_manager.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}")
async def delete_task(task_id: str) -> Dict[str, str]:
    """
    删除任务
    """
    success = await task_manager.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}

@router.get("/{task_id}/status")
async def get_task_status(task_id: str) -> Dict[str, Any]:
    """
    获取任务状态
    """
    task = await task_manager.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return {
        "task_id": task_id,
        "status": task.status,
        "progress": task.progress,
        "current_step": task.current_step,
        "error_message": task.error_message
    }
