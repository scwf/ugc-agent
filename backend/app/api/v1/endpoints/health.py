from fastapi import APIRouter
from typing import Dict, Any

router = APIRouter()

@router.get("/")
async def health_check() -> Dict[str, Any]:
    """
    健康检查端点
    """
    return {
        "status": "healthy",
        "service": "UGC Agent API",
        "version": "1.0.0"
    }
