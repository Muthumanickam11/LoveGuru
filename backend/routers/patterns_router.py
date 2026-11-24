from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_db
from routers.auth_router import get_current_user
from services import patterns_service

router = APIRouter()


@router.get('/active')
async def active_patterns(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await patterns_service.get_active(db, u)


@router.post('/analyze')
async def analyze_patterns(u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await patterns_service.analyze(db, u)


@router.post('/confirm/{pattern_id}')
async def confirm_pattern(pattern_id: str, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    from models.database_models import UserPattern
    import uuid as _uuid
    from sqlalchemy import select
    try:
        pid = _uuid.UUID(str(pattern_id))
    except (ValueError, TypeError):
        return {"confirmed": False}
    row = (await db.execute(
        select(UserPattern).where(UserPattern.id == pid, UserPattern.user_id == u.id)
    )).scalar_one_or_none()
    if row is None:
        return {"confirmed": False}
    row.is_confirmed = True
    await db.commit()
    return {"confirmed": True}


@router.post('/dismiss/{pattern_id}')
async def dismiss_pattern(pattern_id: str, u=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await patterns_service.dismiss(db, u, pattern_id)
    return {"dismissed": result.get("status") == "dismissed"}
