"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Progress, Analytics & Reports Router   ║
║         Weekly synthesis, 7-day mood graphs, streaks & XP    ║
╚══════════════════════════════════════════════════════════════╝
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_db
from routers.auth_router import get_current_user
from services import progress_service

router = APIRouter()


@router.get('/overview')
async def overview(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await progress_service.overview(db, u)


@router.get('/mood-graph')
async def mood_graph(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await progress_service.mood_graph(db, u)


@router.get('/patterns')
async def patterns(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await progress_service.patterns(db, u)


@router.get('/weekly-report')
async def weekly_report(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await progress_service.weekly_report(db, u)


@router.post('/checkin')
async def checkin(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await progress_service.checkin(db, u, body)


@router.get('/milestones')
async def milestones(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await progress_service.milestones(db, u)
