"""
╔══════════════════════════════════════════════════════════════╗
║            LOVEGURU AI — Settings & Configuration            ║
║         Pydantic Settings with environment validation        ║
╚══════════════════════════════════════════════════════════════╝
"""

from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import model_validator
from typing import List, Optional

_BACKEND_DIR = Path(__file__).resolve().parent.parent
_ROOT_DIR = _BACKEND_DIR.parent
_ENV_LOCATIONS = [
    str(_BACKEND_DIR / ".env"),
    str(_ROOT_DIR / ".env"),
    ".env",
]



class Settings(BaseSettings):
    # ── Application ──────────────────────────────────────────
    APP_NAME: str = "LoveGuru AI"
    APP_ENV: str = "development"
    DEBUG: bool = True
    AUTH_DISABLED: bool = True  # Set False in production to enforce JWT auth
    ALLOWED_ORIGINS: str = "http://localhost:5173,http://localhost:3000,http://127.0.0.1:5173"
    TRUSTED_HOSTS: str = "localhost,127.0.0.1,testserver,*.localhost"

    # ── Database (Supabase PostgreSQL / SQLite fallback) ─────
    DATABASE_URL: str = "sqlite+aiosqlite:///./loveguru.db"
    SUPABASE_URL: str = "https://placeholder-project.supabase.co"
    SUPABASE_ANON_KEY: str = "placeholder-anon-key"
    SUPABASE_SERVICE_KEY: str = "placeholder-service-key"

    # ── Cache (Upstash Redis) ────────────────────────────────
    UPSTASH_REDIS_URL: Optional[str] = None
    UPSTASH_REDIS_TOKEN: Optional[str] = None

    # ── AI — Groq (Primary) ──────────────────────────────────
    GROQ_API_KEY: str = "placeholder-groq-key"
    GROQ_PRIMARY_MODEL: str = "openai/gpt-oss-120b"
    GROQ_FAST_MODEL: str = "qwen/qwen3.8-27b"

    # ── AI — Google Gemini (Secondary) ───────────────────────
    GEMINI_API_KEY: str = "placeholder-gemini-key"
    GEMINI_MODEL: str = "gemini-2.0-flash"

    # ── JWT ──────────────────────────────────────────────────
    JWT_SECRET_KEY: str = "loveguru-jwt-secret-key-development-secure-32chars"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    # ── Google OAuth (optional) ──────────────────────────────
    GOOGLE_CLIENT_ID: Optional[str] = None

    # ── RAG ──────────────────────────────────────────────────
    CHROMA_PERSIST_DIR: str = "./chroma_db"
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    RAG_TOP_K: int = 10
    RAG_SCORE_THRESHOLD: float = 0.35
    RAG_FINAL_CHUNKS: int = 3
    # When False (default), uses instant offline deterministic embeddings,
    # avoiding HuggingFace model downloads that can hang startup.
    RAG_EMBEDDING_REQUIRED: bool = False

    # ── Rate Limiting ─────────────────────────────────────────
    RATE_LIMIT_PER_MINUTE: int = 60
    CRISIS_RATE_LIMIT_PER_MINUTE: int = 120

    # ── File Upload ───────────────────────────────────────────
    MAX_IMAGE_SIZE_MB: int = 10
    MAX_AUDIO_SIZE_MB: int = 25
    UPLOAD_DIR: str = "./uploads"

    @property
    def allowed_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",") if origin.strip()]

    @property
    def trusted_hosts_list(self) -> List[str]:
        return [host.strip() for host in self.TRUSTED_HOSTS.split(",") if host.strip()]

    @property
    def is_production(self) -> bool:
        return self.APP_ENV.lower() in ("production", "prod")

    @model_validator(mode="after")
    def _guard_production_secrets(self) -> "Settings":
        """Refuse to boot in production with development/placeholder secrets."""
        if not self.is_production:
            return self

        weak_markers = ("placeholder", "change-in-production", "development", "your-")
        if any(m in self.JWT_SECRET_KEY.lower() for m in weak_markers) or len(self.JWT_SECRET_KEY) < 32:
            raise ValueError(
                "JWT_SECRET_KEY must be a strong, unique value (>=32 chars) in production.")
        if "*" in self.allowed_origins_list:
            raise ValueError("ALLOWED_ORIGINS must not contain '*' in production.")
        return self

    class Config:
        env_file = _ENV_LOCATIONS
        env_file_encoding = "utf-8"
        case_sensitive = True
        extra = "ignore"


# Global singleton
settings = Settings()
