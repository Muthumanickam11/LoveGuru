"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Stage 3 Router (In a Relationship)    ║
║         Gottman Method, Love Languages, Conflict Resolution  ║
╚══════════════════════════════════════════════════════════════╝
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_db
from routers.auth_router import get_current_user
from services import stage3_service

router = APIRouter()


@router.post('/gottman-check')
async def gottman_assessment(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage3_service.gottman_assessment(db, u, body)


@router.post('/conflict-script')
async def conflict_script(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage3_service.conflict_script(db, u, body)


@router.post('/problem-analysis')
async def problem_analysis(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage3_service.problem_analysis(db, u, body)


@router.get('/love-language')
async def get_love_language(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage3_service.get_love_language(db, u)


@router.post('/love-language')
async def submit_love_language(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage3_service.submit_love_language(db, u, body)


@router.get('/date-night-ideas')
async def get_date_night_ideas(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage3_service.get_date_ideas(db, u)


@router.get('/health-dashboard')
async def health_dashboard(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage3_service.health_dashboard(db, u)
