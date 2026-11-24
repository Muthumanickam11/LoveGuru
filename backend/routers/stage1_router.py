"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Stage 1 Router (Single & Searching)   ║
║         Dream Partner, Reality Check, Love Readiness Hub    ║
╚══════════════════════════════════════════════════════════════╝
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_db
from routers.auth_router import get_current_user
from services import stage1_service

router = APIRouter()


@router.post('/partner-description')
async def submit_partner_description(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage1_service.analyze_partner_description(db, u, body)


@router.get('/readiness-score')
async def get_readiness_score(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage1_service.get_readiness(db, u)


@router.post('/readiness-assessment')
async def submit_readiness_assessment(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage1_service.compute_readiness(db, u, body)


@router.get('/improvement-plan')
async def get_improvement_plan(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage1_service.get_improvement_plan(db, u)


@router.get('/daily-task')
async def get_daily_task(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage1_service.get_daily_task(db, u)

@router.post('/grooming-analysis')
async def grooming_analysis(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    image_url = body.get('image_url') or body.get('selfie_url')
    preferences = body.get('preferences') or {}
    from services import stage1_service
    return await stage1_service.analyze_grooming(db, u, image_url, preferences)
