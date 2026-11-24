"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Crisis Safety & Helpline Directory      ║
║         Zero-fail emergency support & grounding tools        ║
╚══════════════════════════════════════════════════════════════╝
"""

from typing import Dict, List, Any

# Canonical crisis hotlines by region
CRISIS_HELPLINES = {
    "india": [
        {
            "name": "KIRAN Mental Health Helpline",
            "number": "1800-599-0019",
            "hours": "24/7",
            "languages": "Hindi, English, 13 Regional Languages",
            "type": "Government Mental Health Support",
        },
        {
            "name": "Tele-MANAS",
            "number": "14416",
            "hours": "24/7",
            "languages": "Multilingual",
            "type": "National Tele-Mental Health Programme",
        },
        {
            "name": "Vandrevala Foundation",
            "number": "+91 9999 666 555",
            "hours": "24/7",
            "languages": "English, Hindi",
            "type": "Crisis Intervention & Counseling",
        },
        {
            "name": "AASRA Helpline",
            "number": "+91 9820 466 726",
            "hours": "24/7",
            "languages": "English, Hindi",
            "type": "Suicide Prevention",
        },
    ],
    "us": [
        {
            "name": "Suicide & Crisis Lifeline",
            "number": "988",
            "hours": "24/7",
            "languages": "English, Spanish",
            "type": "Call or Text",
        },
        {
            "name": "Crisis Text Line",
            "number": "Text HOME to 741741",
            "hours": "24/7",
            "languages": "English",
            "type": "Text Support",
        },
        {
            "name": "National Domestic Violence Hotline",
            "number": "1-800-799-SAFE (7233)",
            "hours": "24/7",
            "languages": "Multilingual",
            "type": "Relationship Violence & Safety",
        },
    ],
    "international": [
        {
            "name": "Befrienders Worldwide",
            "number": "https://www.befrienders.org",
            "hours": "24/7",
            "type": "Global Directory of Crisis Centers",
        },
        {
            "name": "Find A Helpline",
            "number": "https://findahelpline.com",
            "hours": "24/7",
            "type": "Free, Confidential Support Worldwide",
        },
    ],
}

GROUNDING_EXERCISES = [
    {
        "id": "54321_method",
        "title": "5-4-3-2-1 Sensory Grounding",
        "description": "Engage your senses to bring your nervous system back to the present moment.",
        "steps": [
            "Acknowledge 5 things you can SEE around you right now.",
            "Touch 4 things you can physically FEEL (your clothes, the chair, cold water).",
            "Listen for 3 distinct sounds you can HEAR in this room.",
            "Identify 2 things you can SMELL.",
            "Notice 1 thing you can TASTE.",
        ],
    },
    {
        "id": "box_breathing",
        "title": "Box Breathing (4-4-4-4)",
        "description": "Slow down your heart rate and regulate your vagus nerve.",
        "steps": [
            "Inhale slowly through your nose for 4 seconds.",
            "Hold your breath gently for 4 seconds.",
            "Exhale smoothly through your mouth for 4 seconds.",
            "Hold empty lungs for 4 seconds.",
            "Repeat for 4 complete cycles.",
        ],
    },
    {
        "id": "478_breathing",
        "title": "4-7-8 Relaxing Breath",
        "description": "Natural tranquilizer for acute emotional panic.",
        "steps": [
            "Inhale silently through the nose for 4 counts.",
            "Hold your breath gently for 7 counts.",
            "Exhale completely through your mouth with a whoosh sound for 8 counts.",
            "Repeat 4 times.",
        ],
    },
]


def get_crisis_resources(region: str = "india") -> Dict[str, Any]:
    """Returns emergency contacts and grounding exercises."""
    helplines = CRISIS_HELPLINES.get(region.lower(), CRISIS_HELPLINES["india"])
    return {
        "region": region,
        "helplines": helplines,
        "backup_international": CRISIS_HELPLINES["international"],
        "grounding_exercises": GROUNDING_EXERCISES,
        "safe_exit_message": "If you are in immediate physical danger, please dial local emergency services (112 in India, 911 in US) immediately.",
    }
