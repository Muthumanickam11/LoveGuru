"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Stage 2 Router (Finding Love)          ║
║         Dating Profile Review, Flirt Coach, Flag Analyzer    ║
╚══════════════════════════════════════════════════════════════╝
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_db
from routers.auth_router import get_current_user
from services import stage2_service

router = APIRouter()


@router.post('/profile-review')
async def profile_review(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage2_service.review_profile(db, u, body)


@router.post('/conversation-analysis')
async def analyze_conversation(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage2_service.analyze_conversation(db, u, body)


@router.post('/flirt-coaching')
async def flirt_coaching(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage2_service.flirt_coaching(db, u, body)


@router.post('/opening-message')
async def opening_message(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage2_service.opening_message(db, u, body)


@router.get('/red-green-flags')
async def get_flags(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage2_service.get_flags(db, u)


@router.post('/red-green-flags')
async def check_flags(body: dict = None, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage2_service.get_flags(db, u)


@router.post('/date-prep')
async def date_prep(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage2_service.date_prep(db, u, body)


@router.post('/date-debrief')
async def date_debrief(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage2_service.date_debrief(db, u, body)


@router.get('/conversation-starters')
async def conversation_starters(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage2_service.get_conversation_starters(db, u)
