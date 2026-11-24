"""
╔══════════════════════════════════════════════════════════════╗
║   LOVEGURU AI — app.main re-export shim                       ║
║   Allows `uvicorn app.main:app --reload` (and main:app).     ║
╚══════════════════════════════════════════════════════════════╝
"""

import importlib

_main = importlib.import_module("main")
app = _main.app

__all__ = ["app"]