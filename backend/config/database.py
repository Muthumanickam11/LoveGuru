"""
╔══════════════════════════════════════════════════════════════╗
║           LOVEGURU AI — Database Connection Setup            ║
║    SQLAlchemy async engine + session factory + Supabase      ║
╚══════════════════════════════════════════════════════════════╝
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import NullPool
from .settings import settings
import logging

logger = logging.getLogger(__name__)


# ── SQLAlchemy Async Engine ───────────────────────────────────
engine_kwargs = {
    "echo": settings.DEBUG,
    "future": True,
}
if settings.DATABASE_URL.startswith("sqlite"):
    engine_kwargs["connect_args"] = {"check_same_thread": False}
else:
    engine_kwargs["poolclass"] = NullPool

engine = create_async_engine(
    settings.DATABASE_URL,
    **engine_kwargs,
)

# SQLite: enable WAL + a busy timeout so concurrent sessions (request session
# vs. memory modules) don't trip over "database is locked".
if settings.DATABASE_URL.startswith("sqlite"):
    from sqlalchemy import event

    @event.listens_for(engine.sync_engine, "connect")
    def _set_sqlite_pragma(dbapi_connection, connection_record):
        try:
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA journal_mode=WAL")
            cursor.execute("PRAGMA busy_timeout=5000")
            cursor.close()
        except Exception as e:  # pragma: no cover
            logger.warning(f"Could not set SQLite PRAGMAs: {e}")

# ── Session Factory ───────────────────────────────────────────
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)


# ── Base Model ────────────────────────────────────────────────
class Base(DeclarativeBase):
    pass


# ── Dependency Injection ─────────────────────────────────────
async def get_db() -> AsyncSession:
    """FastAPI dependency — yields an async DB session per request."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            logger.error(f"Database session error: {e}")
            raise
        finally:
            await session.close()


# ── Health Check ──────────────────────────────────────────────
async def check_db_connection() -> bool:
    """Verify the database is reachable on startup."""
    from sqlalchemy import text
    try:
        async with AsyncSessionLocal() as session:
            await session.execute(text("SELECT 1"))
        logger.info("✅ Database connection successful")
        return True
    except Exception as e:
        logger.error(f"❌ Database connection failed: {e}")
        return False


async def init_db() -> None:
    """Initialize database tables if they do not exist."""
    try:
        import models.database_models  # Ensure models are loaded
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("✅ Database schema verified / initialized")
    except Exception as e:
        logger.warning(f"⚠️  Database initialization warning: {e}")

