from fastapi import APIRouter
from app.api.v1.endpoints import tasks, health

api_router = APIRouter()

# 包含各个端点路由
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
