"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Emergency & SOS Crisis Router          ║
║         Zero-barrier immediate mental health assistance      ║
╚══════════════════════════════════════════════════════════════╝
"""

from fastapi import APIRouter, Depends
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_db
from routers.auth_router import get_current_user
from services import emergency_service

router = APIRouter()


@router.get('/resources')
async def get_resources(region: Optional[str] = "india"):
    """Public endpoint — no auth required for emergency assistance."""
    return await emergency_service.get_resources(region or "india")


@router.post('/sos-trigger')
async def sos_trigger(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await emergency_service.trigger_sos(db, u, body)


@router.post('/log')
async def log_emergency(body: dict, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await emergency_service.log_crisis(db, u, body)