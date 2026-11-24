import asyncio
import sys
import traceback

sys.path.insert(0, r"C:\Users\msdmu\LoveGuru\backend")

from config.database import init_db
asyncio.run(init_db())

from fastapi.testclient import TestClient
import main

client = TestClient(main.app)


def show(label, resp):
    ok = resp.status_code < 400
    print(f"[{'PASS' if ok else 'FAIL'}] {label} -> {resp.status_code}")
    if not ok:
        print("   ", resp.text[:500])
    return resp


# 1. register
r = show("register", client.post("/api/v1/auth/register", json={
    "email": "smoke@example.com", "password": "secret123", "display_name": "Smoke"
}))
if r.status_code == 409:
    r = show("login(existing)", client.post("/api/v1/auth/login", json={
        "email": "smoke@example.com", "password": "secret123"}))

data = r.json()
tok = data["access_token"]
H = {"Authorization": f"Bearer {tok}"}

show("me", client.get("/api/v1/auth/me", headers=H))
show("onboarding", client.post("/api/v1/auth/onboarding", headers=H, json={
    "stage": "heartbreak", "ai_personality": "gentle_coach", "display_name": "Smoke"
}))

show("chat/text", client.post("/api/v1/chat/text", headers=H, json={
    "message": "I just broke up and I want to text my ex so badly.", "mode": "general"
}))
show("chat/text(crisis)", client.post("/api/v1/chat/text", headers=H, json={
    "message": "I want to die, I can't take this anymore.", "mode": "general"
}))
show("chat/sessions", client.get("/api/v1/chat/sessions", headers=H))

for ep, method in [
    ("/api/v1/stage1/readiness-score", "get"),
    ("/api/v1/stage1/improvement-plan", "get"),
    ("/api/v1/stage1/daily-task", "get"),
    ("/api/v1/stage2/red-green-flags", "get"),
    ("/api/v1/stage3/love-language", "get"),
    ("/api/v1/stage3/date-night-ideas", "get"),
    ("/api/v1/stage4/nc-tracker", "get"),
    ("/api/v1/stage4/grief-guidance", "get"),
    ("/api/v1/progress/overview", "get"),
    ("/api/v1/progress/mood-graph", "get"),
    ("/api/v1/emergency/resources", "get"),
    ("/api/v1/tasks/today", "get"),
    ("/api/v1/patterns/active", "get"),
    ("/api/v1/health", "get"),
]:
    show(ep, getattr(client, method)(ep, headers=H))

show("stage1/partner-description", client.post("/api/v1/stage1/partner-description", headers=H,
     json={"description": "Someone tall, rich, always available, super ambitious, never busy", "traits": ["tall", "rich", "always free"]}))
show("stage1/readiness-assessment", client.post("/api/v1/stage1/readiness-assessment", headers=H,
     json={"answers": {"emotional_independence": 7, "closure": 6}}))

show("stage2/profile-review", client.post("/api/v1/stage2/profile-review", headers=H,
     json={"bio": "I love travel and coffee", "app": "Hinge"}))
show("stage2/conversation-analysis", client.post("/api/v1/stage2/conversation-analysis", headers=H,
     json={"history": "Me: hi\nThem: hey\nMe: how are you"}))
show("stage2/flirt-coaching", client.post("/api/v1/stage2/flirt-coaching", headers=H, json={"scenario": "approaching"}))
show("stage2/opening-message", client.post("/api/v1/stage2/opening-message", headers=H,
     json={"their_profile": "Loves hiking and indie films"}))
show("stage2/date-prep", client.post("/api/v1/stage2/date-prep", headers=H, json={"venue": "cozy cafe"}))
show("stage2/date-debrief", client.post("/api/v1/stage2/date-debrief", headers=H, json={"notes": "felt good"}))

show("stage3/gottman-check", client.post("/api/v1/stage3/gottman-check", headers=H,
     json={"criticism_freq": 4, "contempt_freq": 2, "defensiveness_freq": 3, "stonewalling_freq": 2}))
show("stage3/conflict-script", client.post("/api/v1/stage3/conflict-script", headers=H,
     json={"trigger_incident": "chores", "user_feelings": "unappreciated", "desired_outcome": "shared planning"}))
show("stage3/problem-analysis", client.post("/api/v1/stage3/problem-analysis", headers=H, json={"topic": "money"}))
show("stage3/love-language(POST)", client.post("/api/v1/stage3/love-language", headers=H,
     json={"primary": "quality_time", "secondary": "words_of_affirmation"}))
show("stage3/health-dashboard", client.get("/api/v1/stage3/health-dashboard", headers=H))

show("stage4/urge-surfing", client.post("/api/v1/stage4/urge-surfing", headers=H, json={"trigger": "late night", "intensity": 8}))
show("stage4/grief-weather", client.post("/api/v1/stage4/grief-weather", headers=H, json={"weather": "clearing"}))
show("stage4/journal-entry", client.post("/api/v1/stage4/journal-entry", headers=H, json={"content": "today was hard but I wrote"}))
show("stage4/breakup-analysis", client.post("/api/v1/stage4/breakup-analysis", headers=H,
     json={"what_happened": "They left me after 2 years", "relationship_duration_months": 24}))
show("stage4/closure-letter", client.post("/api/v1/stage4/closure-letter", headers=H, json={"unsent_message": "I miss you"}))
show("stage4/self-worth", client.get("/api/v1/stage4/self-worth", headers=H))
show("stage4/healing-exercises", client.get("/api/v1/stage4/healing-exercises", headers=H))
show("stage4/readiness-for-love", client.get("/api/v1/stage4/readiness-for-love", headers=H))

show("progress/checkin", client.post("/api/v1/progress/checkin", headers=H, json={"checkin_type": "evening", "mood_score": 6}))
show("progress/patterns", client.get("/api/v1/progress/patterns", headers=H))
show("progress/weekly-report", client.get("/api/v1/progress/weekly-report", headers=H))
show("progress/milestones", client.get("/api/v1/progress/milestones", headers=H))

show("patterns/analyze", client.post("/api/v1/patterns/analyze", headers=H))

today = show("tasks/today(get)", client.get("/api/v1/tasks/today", headers=H))
try:
    tid = today.json()["tasks"][0]["id"]
    show("tasks/complete", client.post(f"/api/v1/tasks/complete/{tid}", headers=H))
except Exception as e:
    print("   task id error:", e)
show("tasks/history", client.get("/api/v1/tasks/history", headers=H))

show("emergency/sos-trigger", client.post("/api/v1/emergency/sos-trigger", headers=H, json={"region": "india"}))
show("emergency/log", client.post("/api/v1/emergency/log", headers=H, json={"crisis_level": "high", "message": "feeling low"}))

import io
tiny_png = b"\x89PNG\r\n\x1a\n" + b"\x00" * 64
show("chat/image", client.post("/api/v1/chat/image", headers=H,
     files={"image": ("p.png", io.BytesIO(tiny_png), "image/png")},
     data={"message": "rate my photo"}))
show("chat/voice", client.post("/api/v1/chat/voice", headers=H,
     files={"audio": ("v.webm", io.BytesIO(b"\x1a\x45\xdf\xa3\x00"*8), "audio/webm")}))
show("stage2/red-green-flags(POST)", client.post("/api/v1/stage2/red-green-flags", headers=H, json={}))
print("DONE")
