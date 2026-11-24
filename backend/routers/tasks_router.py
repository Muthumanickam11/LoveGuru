from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_db
from routers.auth_router import get_current_user
from services import tasks_service

router = APIRouter()


@router.get('/today')
async def today_tasks(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await tasks_service.today_tasks(db, u)


@router.post('/complete/{task_id}')
async def complete_task(task_id: str, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await tasks_service.complete(db, u, task_id)


@router.post('/skip/{task_id}')
async def skip_task(task_id: str, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await tasks_service.skip(db, u, task_id)


@router.get('/history')
async def task_history(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await tasks_service.history(db, u)
