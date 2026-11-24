"""
╔══════════════════════════════════════════════════════════════╗
║           LOVEGURU AI — FastAPI Application Entry Point      ║
║           67+ REST Endpoints, CORS, JWT, WebSocket           ║
╚══════════════════════════════════════════════════════════════╝
"""

from contextlib import asynccontextmanager
import asyncio
import logging
import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from config.settings import settings
from config.database import check_db_connection
from routers.auth_router import router as auth_router
from routers.chat_router import router as chat_router
from routers.stage1_router import router as stage1_router
from routers.stage2_router import router as stage2_router
from routers.stage3_router import router as stage3_router
from routers.stage4_router import router as stage4_router
from routers.progress_router import router as progress_router
from routers.emergency_router import router as emergency_router
from routers.tasks_router import router as tasks_router
from routers.patterns_router import router as patterns_router

logging.basicConfig(
    level=logging.DEBUG if settings.DEBUG else logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────
# LIFESPAN — Startup & Shutdown
# ─────────────────────────────────────────────────────────────

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager — runs on startup and shutdown."""
    logger.info("🚀 LoveGuru AI backend starting up...")

    # Ensure required directories exist
    import os
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    os.makedirs("./chroma_db", exist_ok=True)
    logger.info("📁 Storage directories verified")

    # ── LLM Diagnostic — shows which AI providers are active ──
    try:
        from config.llm_config import LLMFactory
        LLMFactory.diagnose()
    except Exception as e:
        logger.warning(f"LLM diagnostic failed: {e}")

    # Check database connection
    db_ok = await check_db_connection()
    if not db_ok:
        logger.warning("⚠️  Database not connected — running in limited mode")
    else:
        try:
            from config.database import init_db
            await init_db()
        except Exception as e:
            logger.warning(f"⚠️  Database initialization skipped: {e}")

    # Initialize RAG — time-boxed so slow corpus/model loads never block startup
    try:
        from rag.rag_pipeline import initialize_rag
        await asyncio.wait_for(initialize_rag(), timeout=20)
        logger.info("✅ RAG pipeline initialized")
    except Exception as e:
        logger.warning(f"⚠️  RAG warm-up skipped/timed out: {e}")

    logger.info(f"✅ LoveGuru AI backend ready — {settings.APP_ENV} mode")
    yield

    # Shutdown
    logger.info("👋 LoveGuru AI backend shutting down...")


# ─────────────────────────────────────────────────────────────
# APP FACTORY
# ─────────────────────────────────────────────────────────────

app = FastAPI(
    title="LoveGuru AI API",
    description=(
        "Your AI Guru For Every Stage of Love. "
        "Empathetic AI companion for singles, daters, couples, and heartbroken individuals. "
        "Powered by LangGraph 12-node pipeline with Groq + Gemini."
    ),
    version="1.0.0",
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
    lifespan=lifespan,
)


# ─────────────────────────────────────────────────────────────
# MIDDLEWARE
# ─────────────────────────────────────────────────────────────

class RequestTimingMiddleware(BaseHTTPMiddleware):
    """Adds an X-Response-Time header and debug-logs request latency."""

    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        latency = round((time.time() - start) * 1000, 2)
        response.headers["X-Response-Time"] = f"{latency}ms"
        logger.debug(f"{request.method} {request.url.path} → {response.status_code} [{latency}ms]")
        return response


# Starlette applies the LAST-registered middleware as the OUTERMOST layer, so
# the stack is registered innermost-first and CORS is added last to guarantee
# CORS headers on every response — including 429/400 emitted by inner layers.

# Innermost: crisis logging, then rate limiting, then request timing.
try:
    from middleware.rate_limiter import RateLimiterMiddleware
    from middleware.crisis_logger import CrisisLoggerMiddleware

    app.add_middleware(CrisisLoggerMiddleware)
    app.add_middleware(RateLimiterMiddleware)
except Exception as e:  # pragma: no cover
    logger.warning(f"Middleware load skipped: {e}")

app.add_middleware(RequestTimingMiddleware)

# Reject requests with unexpected Host headers (DNS-rebinding / host-spoofing).
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.trusted_hosts_list,
)

# Outermost: CORS (must wrap everything so error responses stay CORS-valid).
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
    expose_headers=["X-Response-Time"],
)


# ─────────────────────────────────────────────────────────────
# ROUTERS — Base URL: /api/v1
# ─────────────────────────────────────────────────────────────

PREFIX = "/api/v1"

app.include_router(auth_router,      prefix=f"{PREFIX}/auth",      tags=["Authentication"])
app.include_router(chat_router,      prefix=f"{PREFIX}/chat",      tags=["Chat"])
app.include_router(stage1_router,    prefix=f"{PREFIX}/stage1",    tags=["Stage 1 — Single"])
app.include_router(stage2_router,    prefix=f"{PREFIX}/stage2",    tags=["Stage 2 — Finding Love"])
app.include_router(stage3_router,    prefix=f"{PREFIX}/stage3",    tags=["Stage 3 — Relationship"])
app.include_router(stage4_router,    prefix=f"{PREFIX}/stage4",    tags=["Stage 4 — Heartbreak"])
app.include_router(progress_router,  prefix=f"{PREFIX}/progress",  tags=["Progress"])
app.include_router(emergency_router, prefix=f"{PREFIX}/emergency", tags=["Emergency SOS"])
app.include_router(tasks_router,     prefix=f"{PREFIX}/tasks",     tags=["Tasks & Challenges"])
app.include_router(patterns_router,  prefix=f"{PREFIX}/patterns",  tags=["AI Patterns"])


# ─────────────────────────────────────────────────────────────
# ROOT & HEALTH
# ─────────────────────────────────────────────────────────────

@app.get("/", tags=["Health"])
async def root():
    return {
        "app": "LoveGuru AI",
        "tagline": "Your AI Guru For Every Stage of Love",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs",
    }


@app.get("/health", tags=["Health"])
@app.get("/api/v1/health", tags=["Health"])
async def health_check():
    """Health check endpoint for deployment monitoring."""
    db_ok = await check_db_connection()
    return {
        "status": "healthy" if db_ok else "degraded",
        "database": "connected" if db_ok else "disconnected",
        "environment": settings.APP_ENV,
        "version": "1.0.0",
    }


@app.get("/api/v1/user/onboarding", tags=["User"])
async def get_onboarding_status():
    """Alias endpoint for onboarding status check."""
    return {"message": "Use /api/v1/user/onboarding-status with auth token"}


# ─────────────────────────────────────────────────────────────
# DOCS & FAVICON — friendly aliases for the Swagger UI
# ─────────────────────────────────────────────────────────────

from fastapi.responses import RedirectResponse
from fastapi.responses import Response as FastAPIResponse


@app.get("/api/docs", include_in_schema=False)
async def docs_alias():
    """Redirect /api/docs → /docs (real Swagger UI)."""
    return RedirectResponse(url="/docs")


@app.get("/api/redoc", include_in_schema=False)
async def redoc_alias():
    """Redirect /api/redoc → /redoc."""
    return RedirectResponse(url="/redoc")


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """Minimal inline favicon so browsers stop 404ing."""
    svg = (
        b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
        b'<circle cx="16" cy="16" r="15" fill="#ff5c8a"/>'
        b'<text x="16" y="21" font-size="13" text-anchor="middle" fill="white">&#x1F493;</text>'
        b"</svg>"
    )
    return FastAPIResponse(content=svg, media_type="image/svg+xml", headers={"Cache-Control": "max-age=86400"})


# ─────────────────────────────────────────────────────────────
# GLOBAL EXCEPTION HANDLER
# ─────────────────────────────────────────────────────────────

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error on {request.url.path}: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "message": "Something went wrong. Our team has been notified.",
            "path": str(request.url.path),
        },
    )
