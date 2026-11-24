"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Stage 4 Router (After a Breakup)       ║
║         No-Contact Counter, Grief Weather, Urge Surfing Vault║
╚══════════════════════════════════════════════════════════════╝
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_db
from routers.auth_router import get_current_user
from services import stage4_service

router = APIRouter()


@router.get('/nc-tracker')
async def get_no_contact_tracker(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage4_service.nc_tracker(db, u)


@router.post('/urge-surfing')
async def log_urge_surfing(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage4_service.log_urge(db, u, body)


@router.get('/grief-guidance')
async def get_grief_guidance(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage4_service.grief_guidance(db, u, {})


@router.post('/grief-weather')
async def log_grief_weather(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage4_service.log_grief_weather(db, u, body)


@router.post('/journal-entry')
async def submit_journal(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage4_service.journal_entry(db, u, body)


@router.post('/breakup-analysis')
async def breakup_analysis(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage4_service.breakup_analysis(db, u, body)


@router.post('/closure-letter')
async def closure_letter(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage4_service.closure_letter(db, u, body)


@router.get('/self-worth')
async def self_worth(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage4_service.self_worth(db, u, {})


@router.get('/healing-exercises')
async def healing_exercises(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage4_service.healing_exercises(db, u, {})


@router.get('/readiness-for-love')
async def readiness_for_love(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await stage4_service.readiness_for_love(db, u, {})
