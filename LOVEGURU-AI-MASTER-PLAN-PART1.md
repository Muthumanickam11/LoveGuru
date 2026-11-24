# ❤️ LOVEGURU AI — MASTER BUILD PLAN — PART 1 of 2
### Covers: App Identity, Personas, Every Feature (all 4 stages), Full AI/LangGraph System Architecture, Database Schema + API Design
**➡ Part 2 continues with:** UI Design System, Week-by-Week Build Plan, Testing/Deployment/Launch, and both .env files as appendices.

No details skipped from the original source documents. Where two documents described the same thing differently, both are preserved — the more complete version is marked **CANONICAL**, the earlier draft kept as **EARLIER DRAFT (for reference)**.

---

Nothing from the four source documents has been dropped. Where two documents described the same thing differently (e.g. two draft database schemas), both are preserved — the more complete/final version is marked **CANONICAL** and the earlier draft is kept underneath as **EARLIER DRAFT (for reference)** so no detail is lost.

---

## 1. APP IDENTITY & VISION

**Name:** LOVEGURU AI

**Tagline options:**
- Primary: *"Your AI Guru For Every Stage of Love"*
- Secondary: *"From Single to Soulmate - AI Guides Every Step"*
- Short: *"Love, Understood"*

**What it is:**
- AI companion for the complete love journey
- Covers all 4 stages of love life
- Text + Image + Voice understanding
- Research-backed relationship science
- Culturally aware (Indian context)
- Safe space with crisis support

**What it is NOT:**
- Not a dating app
- Not a matchmaking service
- Not a therapy replacement
- Not a generic advice website
- Not a chatbot with canned responses

**Core promise:**
> "Whatever stage of love you are in - single, searching, committed, or healing - LoveGuru AI walks beside you with wisdom, warmth, and real guidance"

**Mission:**
Help people build healthier relationships by first understanding themselves, then understanding love better, one conversation at a time.

**Impact goals:**
- Help singles find genuine compatibility
- Help couples communicate better
- Help heartbroken people heal faster
- Reduce toxic relationship patterns
- Educate on healthy love standards
- Provide safe space 24/7 availability

### App name alternatives considered
- LOVEGURU (simple, clear) ← **chosen**
- AMORE AI (elegant)
- HEARTWISE (smart love)
- SOULMATE (deep meaning)
- LUMINA (light in love)
- KINDRED (deep connection)
- VEDA (wisdom, fits guru)

---

## 2. CORE CONCEPT — WHY 4 STAGES TOGETHER IS UNIQUE

```
STAGE 1: SINGLE LIFE
→ User describes dream partner
→ AI analyzes if expectations are realistic
→ AI tells what to improve in themselves
→ Grooming, personality, lifestyle guidance

STAGE 2: FINDING LOVE
→ AI helps understand what they truly need
→ Green flags vs red flags education
→ Where to find right person
→ How to approach, talk, attract

STAGE 3: IN RELATIONSHIP
→ Discuss problems with AI
→ AI acts as relationship counselor
→ Communication guidance
→ Conflict resolution
→ Keeping love alive tips

STAGE 4: AFTER BREAKUP
→ Mental health support immediately
→ Physical health guidance
→ Healing roadmap
→ Positive rebuilding
→ When ready → back to Stage 1
```
Nobody has built ALL 4 stages together — this is the unique power of the app: a **complete love-life companion**.

---

## 3. COMPLETE APP MAP

```
LOVEGURU AI
│
├── 🟡 STAGE 1: SINGLE & SEARCHING
│   ├── Dream Partner Describer
│   ├── Reality Check Analysis
│   ├── Self Improvement Roadmap
│   ├── Grooming & Style Guide
│   ├── Personality Development
│   └── Readiness Score
│
├── 🟢 STAGE 2: FINDING LOVE
│   ├── Partner Type Matcher
│   ├── Green Flag / Red Flag Guide
│   ├── Conversation Coach
│   ├── First Date Preparation
│   ├── Attraction Building Guide
│   └── Where To Find Them Guide
│
├── 🔵 STAGE 3: IN RELATIONSHIP
│   ├── Relationship Problem Solver
│   ├── Communication Coach
│   ├── Conflict Resolution Guide
│   ├── Love Language Discovery
│   ├── Relationship Health Check
│   └── Keeping Love Alive Tips
│
└── 🔴 STAGE 4: AFTER BREAKUP
    ├── Immediate Crisis Support
    ├── Grief Stage Guidance
    ├── Mental Health Recovery
    ├── Physical Health Rebuilding
    ├── Identity Rebuilder
    ├── Lesson Extractor
    └── Ready For Love Again Check
```

---

## 4. COMPLETE USER PERSONAS

### PERSONA 1: SINGLE PRIYA
- Age 22 | College Student | Mumbai
- **Problem:** Has high expectations, keeps getting disappointed in dating
- **Needs:** Reality check on expectations, self improvement guidance, confidence building
- **How she uses app:** Describes dream partner to AI → gets honest feedback → works on self improvement plan → learns green/red flags

### PERSONA 2: SEARCHING RAHUL
- Age 26 | Working Professional | Bangalore
- **Problem:** Met someone at work, doesn't know how to proceed
- **Needs:** Conversation coaching, date preparation, confidence in approaching
- **How he uses app:** Shares screenshots of chats → AI analyzes and guides responses → practices conversation with AI → gets first date preparation guide

### PERSONA 3: RELATIONSHIP NEHA
- Age 24 | In 2yr relationship | Delhi
- **Problem:** Constant fights about small things, feeling disconnected lately
- **Needs:** Communication tools, conflict resolution guidance, reconnection strategies
- **How she uses app:** Describes fights to AI → AI finds root cause → gets scripts for conversations → weekly relationship health tracking

### PERSONA 4: HEARTBROKEN ARJUN
- Age 25 | Recently single | Hyderabad
- **Problem:** 3-year relationship just ended, can't eat, sleep, or function
- **Needs:** Immediate emotional support, healing roadmap, physical health guidance, reason to move forward
- **How he uses app:** Opens app at 3AM crying → tells AI everything → gets immediate compassionate support → daily healing check-ins → rebuilding identity slowly

---

## 5. EVERY FEATURE — ALL 4 STAGES (COMPLETE)

## 🟡 STAGE 1: SINGLE & SEARCHING — ALL FEATURES

### F1.0 Onboarding Conversation (real conversation, not a form)
AI opens naturally:
> "Hey, I'm really glad you're here. Before we dive in, I want to understand where you are right now in your love life. Are you single and looking? In something complicated? Just got out of something? Whatever it is - no judgment here, just tell me."

What AI collects through conversation:
- Current relationship status
- Past relationship count/experience
- What went wrong before (if anything)
- What they're looking for now
- Their biggest fears about love
- Their communication style
- Family/cultural expectations they face
- Their biggest strength in relationships

### F1.1 Dream Partner Describer / Dream Partner AI Analysis
**The experience:**
AI asks in conversation style: *"Tell me about the person you imagine building your life with. Don't filter yourself - just describe them freely."*

Follow-up questions AI asks:
- "What qualities matter most to you beyond appearance?"
- "Describe a perfect day with this person"
- "What does love feel like to you?"
- "What would make you feel truly safe with someone?"
- "What has hurt you in past relationships?"

**AI collects full picture across:**
- Physical expectations (height, appearance, body type, age range)
- Personality expectations (temperament, humor, emotional availability, social style)
- Lifestyle expectations (career/financial, family orientation, hobbies, religious/cultural alignment)
- Emotional expectations (communication style, conflict handling, affection style, independence vs togetherness)
- Financial expectations
- Social expectations

**What AI analyzes:**
- Are these expectations realistic?
- Which ones are healthy needs?
- Which ones are fear-based?
- Which ones come from movies/social media?
- Which ones are negotiable vs non-negotiable?
- What do these expectations say about the user themselves?

Inputs supported: free text (no form), voice description option, image of "type" (celebrity etc) optional.

### F1.2 Reality Check Analysis (CORE unique feature of Stage 1)
Example output structure:

```
YOUR PARTNER VISION ANALYSIS

HEALTHY EXPECTATIONS ✅
These are completely valid and you deserve them:
→ Emotional availability
→ Mutual respect
→ Someone who makes you feel safe
→ Shared values
→ Genuine kindness

WORTH EXAMINING 🤔
These come from a real need but expressed in an unrealistic way:
You said: "Never fights with me"
Reality: Every healthy relationship has disagreements. The goal is not zero
conflict but HOW you handle conflict together.
What you actually need: Someone who fights FAIR and wants to resolve, not win.

You said: "Understands without me saying"
Reality: Mind reading is not love - it's a fantasy.
What you actually need: Someone safe enough that you CAN say it.

HIGH EXPECTATIONS TO RECONSIDER ⚠️
These may be limiting your chances:
You said: "Must be extremely wealthy"
Consider: Financial stability matters. But "extremely wealthy" eliminates
97% of genuinely loving partners. Is security what you truly need?

WHAT YOUR EXPECTATIONS REVEAL ABOUT YOU:
Your list shows you deeply value security and fear being emotionally hurt
again. Some of your "requirements" are actually armor protecting a past wound.

COMPATIBILITY SCORE: 6.2/10  (how realistic your current list is)

REVISED PARTNER VISION
Based on your true needs, your ideal partner: [AI suggests refined,
realistic version]
```

**Five outputs generated:**
1. **Expectation Reality Score** — per-category scores (Physical/Personality/Lifestyle/Emotional) + overall realism score
2. **Category Breakdown** — Healthy Expectations ✅ / Needs Examination 🤔 / Reconsider These ⚠️ (each with explanation, real need underneath, reframed healthier version)
3. **What Expectations Reveal** — deep psychological insight: what past experiences shaped these, what fears are disguised as preferences, what genuine needs are valid
4. **Refined Partner Vision** — AI suggests healthier version, keeps valid expectations, reframes problematic ones, adds things user missed but actually needs
5. **Questions For Self** — 5 reflection questions, journaling with AI

### F1.3 Self Improvement Roadmap (6 complete areas)
Philosophy: *"Before finding the right person, become the right person"*

AI asks: "What kind of partner are YOU for someone?", "What do your exes/people say about you?", "What are your emotional strengths?", "Where do you struggle in relationships?", "What habits would a partner have to accept about you?"

**AREA 1 — Emotional Intelligence**
Assessment: express anger, handle hurt, ask for needs, handle jealousy, take responsibility.
AI scores: emotion recognition, emotion regulation, empathy level, vulnerability capacity, accountability (all X/10).
Plan: daily practices, books/resources, scripts for hard conversations, weekly check-ins.

**AREA 2 — Communication Skills**
Assessment: passive/aggressive/assertive?, avoid hard conversations?, listen without defending?, make assumptions?, express needs clearly?
Plan: assertiveness training exercises, active listening practice, "I feel" statement practice, conflict approach coaching.

**AREA 3 — Grooming & Appearance**
AI asks: current style description, body type/comfort, budget, lifestyle (office/casual/active), cultural context, desired look.

*For all genders:*
- Skincare: routine for skin type, product recs by budget, common mistakes, morning vs evening routine
- Hair: face shape analysis, hairstyle suggestions, hair care routine, grooming maintenance schedule
- Hygiene: complete checklist, often-missed areas, scent guidance, oral health

*For men specifically:* beard grooming guide, clothing basics (colors/fits), shoe importance, watch/accessory basics, gym routine for confidence.

*For women specifically:* natural makeup look guide, clothing that flatters body type, accessory coordination, confidence-based dressing.

*Body language guide:* posture, eye contact, smile authenticity, approachability signals, confidence body language.

Output: complete personal style/presentation package specific to budget, lifestyle, goals.

**AREA 4 — Confidence & Mindset**
Assessment: self-feelings, belief in deserving love, self-talk about past failures, rejection handling.
Plan: daily self-affirmations (specific not generic), confidence-building exercises, rejection reframing practice, self-compassion techniques.

**AREA 5 — Social Skills**
Assessment: conversation ease, approach struggles, eye contact, listening, making people comfortable.
Training: conversation openers guide, active listening techniques, humor development basics, body language improvement, making memorable impressions.

**AREA 6 — Lifestyle & Life Quality**
Assessment: career/financial stability, friend group health, hobbies/interests, physical fitness, mental health baseline.
Development: why life quality attracts, goal setting for life areas, balance creation, independence before partnership.

Output: **Personalized 90-Day Self Growth Plan** — week-by-week specific actions, daily small habits, books/resources recommended, progress check-ins with AI.

### F1.4 Love Readiness Score (comprehensive 30-question assessment)
Six dimensions:
1. **Past Healing** (0-20 pts) — over previous heartbreaks? forgiven past partners? learned from patterns? no revenge motivation?
2. **Self Love** (0-20 pts) — happy alone before together? strong self-worth independent of partner? no validation-need? respect yourself in relationships?
3. **Emotional Availability** (0-20 pts) — able to be vulnerable? trust reasonably? open to commitment? not just wanting attention?
4. **Life Stability** (0-15 pts) — basic financial responsibility? career/education direction? living situation stable? mental health managed?
5. **Healthy Expectations** (0-15 pts) — realistic partner expectations? understand compromise? looking for partner not perfect?
6. **Communication Ready** (0-10 pts) — can express needs? handle conflict constructively?

Score meanings:
```
0-30:   Not ready yet - focus on healing
31-50:  Getting there - specific areas to work
51-70:  Mostly ready - polish these areas
71-85:  Ready - some awareness items
86-100: Very ready - go find love!
```

For each score: exactly what to focus on, specific timeline estimate, action plan to improve, re-assess in 2 weeks, celebration when score improves.

Visual example:
```
LOVE READINESS SCORE
Healing from past        ████████░░  80%
Self love level          ██████░░░░  60%
Emotional availability   ███████░░░  70%
Life stability           █████░░░░░  50%
Communication skills     ████████░░  80%
Boundary awareness       ███░░░░░░░  30%
OVERALL READINESS: 61%
```

---

## 🟢 STAGE 2: FINDING LOVE — ALL FEATURES

### F2.0 Complete Dating Profile AI Review
User submits: profile text, photos (1-5), platform (Instagram/Bumble/Hinge).

**Bio analysis:** first impression score, personality coming through?, conversation starters created?, clichés identified/removed, authenticity score, humor appropriate?, length appropriate?

**Photo analysis (each photo):** lighting quality, expression (genuine vs forced), background appropriateness, outfit presentation, body language shown, energy conveyed.

**Photo order strategy:** which photo first, which shows personality best, which creates intrigue, which to remove entirely.

**Output:** complete bio rewrite in 3 versions (Casual, Warm, Witty), photo order recommendation, 5 conversation starter suggestions for others to use.

### F2.1 Partner Type Matcher
Based on Stage 1 data (refined partner vision, attachment style, personality type, lifestyle):
> "Based on everything we know about you, here are the types of people who would truly complement YOU"

Deep compatibility explanation (not surface-level): communication style match, attachment style compatibility, lifestyle compatibility, emotional intelligence match, ambition/growth alignment.

### F2.2 Specific Person Analysis
User can share: text description, profile screenshot, conversation screenshot, publicly shared photo, voice description.

**From profile screenshot:** what photos say about them, bio analysis for personality, what they value, compatibility indicators, initial green/red flags.

**From conversation screenshot:** communication style analysis, interest level indicators, personality traits visible, response pattern analysis, warning signs if any.

**Compatibility assessment:** communication style match, energy level match, values alignment visible, potential challenges, overall compatibility reading.

Always includes disclaimer: *"This is based on limited information. People are complex. Use this as a starting point not a final judgment."*

### F2.3 Green Flag / Red Flag Guide (personalized education)

**Universal Green Flags — early conversation:**
- Asks questions AND listens to answers
- Remembers small things shared
- Consistent — replies within reasonable time
- Respects when you're busy
- Makes you feel comfortable not anxious
- Talks about others with respect
- Has own life, friends, goals
- No pressure for too much too fast

**Universal Green Flags — first meeting:**
On time, phone away, asks about YOU, comfortable silence possible, you feel safe, accepts your "no" gracefully.

**Universal Red Flags — early:**
- Love bombing (too intense too fast)
- Talks badly about ALL exes ("everyone was crazy")
- Inconsistency (amazing then cold)
- Pushes boundaries after you set them
- Guilt-tripping over normal limits
- No friends / estranged from family
- Lies about small things
- Rushing commitment too fast
- Isolates you from friends/family

**Manipulation tactics education:**
- **Breadcrumbing** — just enough attention to keep you hooked, never enough for a real relationship
- **Future faking** — big promises early ("we should go to Europe", "I can see us married") that never materialize
- **Hot and cold** — inconsistency that creates anxiety and seeking, this is control through inconsistency
- **Trauma bonding** — intense connection from intensity; confusion between anxiety and chemistry
- **Gaslighting** — "that never happened" / "you're too sensitive" / "you're imagining things" / "you always overreact"
- **Guilt-tripping language** — "if you loved me you would..." / "I guess I'm not important to you" / "fine, don't worry about me"
- **Controlling language** — "who were you with?" (demanding not curious) / "you shouldn't wear that" / "I don't like your friends"

AI teaches core reframe: *"Attraction ≠ Compatibility. Anxiety ≠ Chemistry. Intensity ≠ Love."*

**Personalized section:** based on user's own relationship history — "You've described [specific pattern] twice", "Watch for [specific flag] for you", "Your weakness is [pattern]."

### F2.4 Conversation Coach (three modes)

**Mode 1 — First Message Help:** AI generates 5 personalized opening messages based on the other person's actual profile content/shared interests (not generic "hey what's up").
Example: profile says hiking + coffee → *"Okay I need to know - are you a sunrise hike or sunset hike person? This is important information 😄"*

**Mode 2 — Ongoing Conversation Analysis:** user pastes conversation so far; AI analyzes how it's going, interest signals, what's working, missed opportunities, what to say next, when to ask for number/date.

**Mode 3 — Response Helper:** user shares last message received; AI gives 3-5 response options (playful/serious/direct) with explanation of why each works.

**Mock conversation practice:** user says "pretend to be [type of person]"; AI plays that character; user practices; AI gives feedback after each exchange ("That was great because..." / "Next time try...").

**Texting guide:** response timing, length matching their energy, humor dos/don'ts, when to move offline, how to ask someone out smoothly.

### F2.5 First Date Complete Preparation

**Before the date:**
- What to wear (venue + style-based)
- Grooming checklist for date day
- Conversation topics to prepare
- Topics to avoid (exes, marriage/kids too directly, salary/money, family drama, past trauma detail, heavy politics/religion)
- Managing date anxiety (mindset reframe: "interviewing them too", worst-case scenario exercise, confidence anchoring)
- What time to arrive (5 min early), what to eat before

**20 great date questions** — deep but not heavy (e.g. "What's something you're really proud of that most people don't know?", "What does a perfect Sunday look like?") and light/fun (e.g. "Best meal you've ever had?", "Hidden talent no one knows about?").

**During the date:**
- Listening more than talking rule
- Body language: genuine eye contact, lean in slightly, mirror energy, smile genuinely, open posture
- Active listening: follow-up questions, remember and reference, don't rehearse next line, validate before opining
- Handling awkward silences
- Compliments that feel genuine
- When/how to pay
- How to end the date well

**After the date:**
- How soon to text (within 24hrs fine)
- What to say in follow-up
- How to ask for date 2
- How to handle no reply
- How to know if they liked you

**Date debrief with AI:** user reports how it went → AI analyzes what went well, what could improve, connection moments, red/green flags noticed, should they pursue further.

---

## 🔵 STAGE 3: IN RELATIONSHIP — ALL FEATURES

### F3.0 Relationship Problem Solver (CORE Stage 3 feature)
Real problems users bring: *"My partner never listens to me", "We fight about money all the time", "They are too close with their ex", "I feel lonely even though we are together", "They changed after 6 months", "I don't feel attractive to them anymore", "We have different future plans."*

**AI approach:**
- NOT: "Leave them" / "You're right they're wrong" / generic advice
- YES: deep analysis of the specific situation, both sides always considered, root cause identification, practical actionable solutions, exact scripts of what to say

**4-Step Problem Analysis Framework:**
1. **Understand the full situation** — multiple follow-up questions, both sides of the story, relationship history, pattern not just event
2. **Root Cause Analysis** — communication problem? expectation mismatch? fear/attachment trigger? values difference? phase or pattern?
3. **Solution Generation** — what user can do immediately, exact words to say to partner, conversation framework, specific change to request, how to approach without blame
4. **Outcome Prediction** — realistic expectations, when to give it time vs when to worry, what success looks like

**Investigation rounds (from later doc, expanded):**
- Round 1 — Understanding (5-7 Qs): what happened exactly, what did they say, what did you say, how did it end, how do you feel now, how long an issue, happened before?
- Round 2 — Context Building: what's the relationship like normally, stress in their life, stress in your life, anything changed recently?
- Round 3 — Root Cause Analysis, classified into **6 problem types**:
  1. **Communication Problem** — same thing expressed differently, neither wrong just different styles → solution: translation + bridge building
  2. **Expectation Mismatch** — different assumptions never explicitly discussed → solution: explicit conversation framework
  3. **Unmet Need** — needs going unexpressed → solution: need identification + expression
  4. **External Stress Spillover** — outside stress entering relationship, each other becoming target → solution: source ID + team approach
  5. **Values Difference** — fundamental different values, long-term compatibility question → solution: honest evaluation needed
  6. **Pattern Problem** — recurring cycle both stuck in → solution: cycle map + interruption

Solution generation per type: immediate action today, conversation to have (exact script), long-term approach, what success looks like, when to revisit with AI.

### F3.1 Communication Coach — Complete Scripts (teaches simplified Gottman Method)

**The Four Horsemen (relationship destroyers) & antidotes:**
- **Criticism vs Complaint** — Criticism: "You're so selfish." Complaint: "When you didn't call I felt alone." → Always complain, never criticize.
- **Contempt** (most dangerous) — eye rolling, mockery, dismissiveness ("You're so immature") → express needs with respect always.
- **Defensiveness** — "Well YOU did the same thing!" counter-attacking → take responsibility first.
- **Stonewalling** — shutting down, silent treatment → take breaks, but come back.

**The antidotes AI teaches:** gentle startup technique, "I feel" statement structure, active listening validation, repair attempts during conflict, physiological self-soothing, compromise vs capitulation difference.

**Six full skills taught with scripts:**

1. **The Gentle Startup**
   - Wrong: "You ALWAYS do this. You never listen. You're so selfish and I'm sick of it."
   - Right: "Hey can I share something with you? When [specific situation happened], I felt [emotion] because I need [need]. I'm not trying to attack you, I just want us to understand each other."
   - Practice: user submits harsh version → AI rewrites as gentle startup, explains every changed word.

2. **The "I Feel" Formula**
   - Formula: "I feel [emotion] when [specific situation] because I need [underlying need]. Would you be willing to [specific request]?"
   - Example: Instead of "You never make time for me" → "I feel lonely when we go more than 3 days without real conversation because connection is how I feel loved. Would you be willing to have one phone-free evening this week?"

3. **Active Listening — the EAVE method**
   - **E**cho (reflect back what you heard), **A**cknowledge (name the emotion), **V**alidate (make it make sense), **E**xplore (ask to understand more)
   - Example: Partner: "You never prioritize me over your friends." → EAVE response walks through each step rather than defending.

4. **Repair Attempts** (when fight is escalating)
   - Humor repair (lighten mood), affection repair (touch hand, soften), clarification repair ("Wait, I don't think I'm explaining this right"), responsibility repair ("I'm sorry, I said that harshly"), pause repair ("Can we take 10 minutes and come back to this?")
   - AI gives scripts for each; user practices with AI playing partner.

5. **Fight Fair Rules**
   - No "always"/"never", one issue at a time, no character attacks (behavior vs person), no bringing up old resolved issues, no silent treatment, no threatening relationship to win, breaks okay (with return time), goal is understanding not winning.

6. **Apology That Works**
   - Wrong: "I'm sorry you feel that way" / "I'm sorry but you also—" / "I'm sorry if I upset you"
   - Right (4 parts): 1) "I was wrong to [specific action]" 2) "I understand that made you feel [emotion]" 3) "That's not the partner I want to be" 4) "What I'm going to do differently is [change]"
   - AI evaluates user's draft apology and gives feedback on what's missing.

**Conversation scripts library:**
- Needing space: "I love you and I want to work this out. I need 20 minutes to calm down and then I really want to talk about this with you."
- Expressing unmet needs: "Something has been on my mind and I want to talk about it. Is now a good time? I've been feeling [emotion] when [specific situation]. What I need is [need]."
- Genuine apology: (see 4-part formula above).

### F3.2 Love Language Discovery (Five Love Languages — Gary Chapman)
Discovery is a **real conversation, not a multiple-choice test**. AI asks:
- "Think about a moment when you felt most loved by your partner. What exactly were they doing?"
- "When you feel unappreciated, what's usually missing? What would make you feel better immediately?"
- "How do you naturally show love to the people you care about?"
- "What would your ideal Saturday look like with your partner?"
- "What's something small they do that means more than they probably know?"

The five languages: **Words of Affirmation**, **Acts of Service**, **Receiving Gifts**, **Quality Time**, **Physical Touch** — each with concrete examples.

From answers, AI detects: primary love language, secondary love language, partner's likely language (from user's descriptions).

**All 25 combinations covered**, each with: understanding of the mismatch, action plan for the user, action plan framed for the partner, common conflict of that pairing, how to bridge the gap.

Example output:
> "You are Words of Affirmation person. Your partner seems to be Acts of Service. This means when they cook for you that IS them saying I love you... Here is how to bridge this gap..."

### F3.3 Relationship Health Monitor
**Weekly check-in — 10 questions:**
1. Connection score this week (1-10)
2. Any conflict? How did it resolve?
3. Felt heard and understood? (1-10)
4. Felt appreciated? (1-10)
5. Did something fun together?
6. Physical intimacy satisfaction (1-10)
7. Are you growing individually still?
8. Any resentment building?
9. Future feeling positive or anxious?
10. One thing you love about them this week

**Dashboard example:**
```
RELATIONSHIP HEALTH DASHBOARD
Connection Score    ███████░░░  7.2/10
Communication       ██████░░░░  6.0/10
Trust Level         █████████░  9.0/10
Fun & Joy           ████░░░░░░  4.5/10 ⚠️
Conflict Health     ███████░░░  7.0/10
Intimacy            ██████░░░░  6.5/10
OVERALL: 6.7/10 (↓ from 7.4 last month)
```

**Early warning system:** score drops 2+ points in any area, or over 3 consecutive weeks → AI proactively checks in ("Hey, your connection score has dropped the last two weeks. Nothing urgent but I wanted to check in - is everything okay with you two?"). Proactive, not reactive.

**Trend analysis (monthly):** improving or declining?, which areas consistently low?, seasonal patterns, correlation between events and scores.

### F3.4 Keeping Love Alive / Intimacy Guide
**Science of lasting love:** novelty keeps attraction alive, appreciation prevents contempt, individual growth keeps relationship fresh, friendship is the foundation of romance.

**Non-physical intimacy builders:**
- Emotional intimacy: 36 Questions (Arthur Aron research), weekly conversation topics, dreams sharing ritual, gratitude practice, vulnerability challenge system
- Intellectual intimacy: learning something new together, light debate topics, sharing perspectives practice
- Experiential intimacy: new experience ideas (budget-based), novelty research, shared goals creation, bucket list building

**Date night ideas by budget:**
- Free: sunrise walk + coffee, cook new recipe together, home movie marathon, star gazing, photo walk
- Low (<₹500): local café exploration, museum/gallery, cooking class, board game café
- Medium (₹500–2000): day trip nearby, activity class (pottery/dance), special dinner at meaningful place

**Daily micro-habits for love:**
- 6-second kiss (Gottman research)
- Genuine "how was your day" (no phone)
- One specific appreciation daily
- Physical touch throughout day
- Goodbye/hello rituals
- Protected phone-free time

**Special occasions:** anniversary ideas, birthday personalization, surprise gestures guide, how to make ordinary days special.

---

## 🔴 STAGE 4: AFTER BREAKUP — ALL FEATURES (highest-priority, most vulnerable stage)

### F4.0 Immediate Crisis Support (Hour 1 / first 24–48 hours)
AI detects new/recent breakup and responds:

**NOT:** "You'll be fine" / "Better without them" / generic positivity
**YES:** acknowledge the real pain, validate grief as legitimate, immediate comfort and presence, safety check

Example AI opening:
> "I can hear how much pain you're in right now. What you're feeling is real. Heartbreak is not just emotional - it creates physical pain in your body. I'm here. You don't have to be okay right now. Tell me what happened if you want to. I'm listening."

**Protocol, step by step:**
1. **Pure presence (first 5 min)** — no advice, no silver linings, just "I'm here. Tell me what happened. Take all the time you need." AI just listens; asks only "Tell me more"; validates every feeling.
2. **Validate the pain is real** — explain heartbreak activates the same brain regions as physical injury; "You are not overreacting. You are not weak. You are human, and you loved someone."
3. **Immediate practical help (Hour 1 survival guide)** — text one safe person you trust (not to talk, just so you're not alone); drink something warm; don't make major decisions today; don't text them back yet; permission to cry; safety check ("Where are you right now? Are you safe?").
4. **Tonight plan** — who can you be with tonight; if alone, what helps; sleep aid suggestions (herbal); permission to not be okay tonight; "Tomorrow we'll talk more. Tonight, just survive."

**Safety check (always):** gentle direct question "How are you really doing? Are you safe right now?"; if any concerning response → crisis detection activates; resources provided immediately (iCall, Vandrevala numbers); urge to contact someone they trust.

### F4.1 The Science of Heartbreak Explained
**Brain science:**
> "When you lose a relationship, your brain goes through withdrawal similar to addiction. This is not weakness - this is neuroscience. The same brain regions that activate for physical pain activate for heartbreak. When you feel physical chest pain right now - that pain is real, not dramatic."

**What's happening in the body:**
- Cortisol (stress hormone) spikes
- Dopamine withdrawal (they were your reward)
- Sleep disrupted (oxytocin loss)
- Appetite gone (stress hormones)
- Immune system weakened
- Energy completely depleted
- Concentration broken

**Why they keep thinking about their ex:**
> "Your brain formed neural pathways around this person over time. Every thought of them releases a tiny bit of dopamine. This is why you can't stop thinking about them even when you want to. This is not weakness. This is biology."

**Each physical symptom explained on demand:** can't eat (cortisol suppresses appetite — small snacks fine, don't force it), can't sleep (oxytocin loss disrupts sleep cycles — temporary), chest pain ("broken heart syndrome" — medically real, stress hormones affect heart muscle, will ease), can't concentrate (brain using enormous resources on the loss), keep checking their social media (each check = tiny dopamine hit, feeding the addiction, extends healing time).

**Honest timeline (no exact deadline promised):**
```
Acute pain peak:  Week 2-3 (worse before better is normal)
Active grief:     1-3 months (processing the loss)
Integration:      3-6 months (making meaning of it)
New normal:       6-12 months (life restructured)
Fully healed:     Different for everyone — "There is no deadline for your grief"
```

### F4.2 Grief Stage Navigation (presented as weather that changes, NOT linear)
> "You will not grieve in order. You might feel acceptance on Tuesday and denial on Wednesday. This is completely normal."

- **Denial** — signs: "This isn't really over", "They'll come back", "I'll just text them..." → AI validates the hope gently, never crushes it harshly, holds gentle reality: "Can I gently ask - what did they actually say to you? Let's look at what really happened."
- **Anger** — signs: "How could they do this", "They're terrible", "I hate them" → AI: "Anger is actually healthy right now. It's your emotional system protecting you... Let it out here with me... anger held too long becomes poison for YOU not them. When you're ready, we'll process this."
- **Bargaining** — signs: "What if I had done things differently", "Maybe if I change they'll come back" → AI: "What outcome are you hoping for? What is the realistic probability? What would happen to your healing if you reach out and they don't respond?"
- **Depression** (most careful stage; crisis detection heightened, warmth increased, small hope offerings, professional help suggested gently, physical health focus) — signs: "I'll never love again", "I'm not worthy of love", "What's the point" → AI: "This is the darkest part of the grief. It won't stay this dark. I need you to hear that... Can we talk about what's happening with your body right now? Are you eating? Sleeping?"
- **Acceptance** — signs: "I think I'm starting to be okay", "I actually laughed today" → AI celebrates: "This is a beautiful moment. Acceptance doesn't mean you're over it or that it didn't matter. It means you're big enough to hold the pain AND move forward."

### F4.3 Mental Health Complete Recovery
**Daily system:**
- Morning check-in: sleep quality, pain 1-10, one word for feeling, biggest fear for today → personalized morning support
- Evening check-in: "Did you survive today? (yes is enough)", one small okay moment, eating/moving, anything proud of → AI celebrates survival

**Journal prompts (rotate by phase):**
- Week 1 (acute grief): "Just write everything you feel", "What do you miss most right now?", "Write a letter you'll never send", "What does the pain feel like physically?"
- Week 2-4 (processing): "What was real vs what was idealized?", "What did you give up of yourself?", "What did you learn about what you need?", "When did you feel most yourself with them?"
- Month 2-3 (integration): "Who were you before this relationship?", "What parts of yourself do you want back?", "What would you tell someone going through this?", "What are you grateful this taught you?"

**Rumination management ("worry time" technique):** give yourself 10 full minutes with a timer to think about it completely, then gently redirect when the timer ends — this actually reduces overall rumination.

**No-contact (NC) support system:**
- Day counter, urge-to-text handling: "Before you text them, tell me what you want to say to me instead" (AI receives the text), 24-hour rule, "Unsent Letter" technique (write it, don't send it)
- Social media detox guide: why seeing their posts hurts healing, how to mute/unfollow without drama, dealing with mutual friends' content, the comparison spiral explained
- Handling urges hour-by-hour → day-by-day → week-by-week ("We're doing this one step at a time")
- NC tracker: days since last contact, gamified streak, milestone celebrations ("You made it 7 days. That took strength.")

**Professional therapy guidance:** when AI recommends therapy (specific signs), how to find a therapist (free/low-cost options), destigmatizing what therapy is, affordability (government options), what to say in the first session.

### F4.4 Physical Health Recovery System

**Sleep recovery protocol:**
- Week 1: permission to sleep whenever, guided sleep meditation, audiobook/podcast list, "Sleep is healing your brain"
- Week 2-3: consistent wake time (most important), no phone 1hr before sleep, warm tea ritual (chamomile/ashwagandha), body-scan relaxation audio
- Month 2+: full sleep hygiene protocol, track sleep quality, correlate with mood improvement

**Eating recovery protocol:**
- Days 1-7: "eat whatever you can manage", small amounts frequently, banana/peanut butter easy option, don't force — sip liquids minimum, "eating is self-care right now"
- Week 2-3: simple easy recipes, one real meal/day goal, blood sugar and mood connection taught, grocery list for healing foods
- Month 2: return to nourishing eating, cooking as self-care reframe, meal prep for stability

**Movement protocol:**
- Week 1-2 (micro-movement): walk outside 10-15 min even if it hurts to go out; sunlight is medically important; movement releases grief from the body
- Week 3-4 (gentle exercise): whatever they used to enjoy, not for body but for mind; yoga options; "Your body held this pain, let it move"
- Month 2-3 (building strength): regular exercise routine, exercise-as-mood-medicine education, group classes (social aspect), "Building your strongest self"
- Month 3+ (transformation phase): physical transformation as healing symbol — **not revenge body, reclaimed body**; strength building; energy returning

**Complete physical tracker:** daily sleep score, appetite level (1-5), movement (yes/no + type), energy level (1-10), physical pain (chest, headache etc), AI celebrates each improvement.

### F4.5 No-Contact Guide (most practical Stage 4 feature)
**Why no contact — the science analogy:**
> "Every time you check their profile, text them, or 'accidentally' run into them, you reset your brain's withdrawal. It's like trying to quit sugar while eating a cookie 'just once a day.' No contact is not cruel. It is the kindest thing you can do for your healing."

Full support system as described above under F4.3 (urge handling, social media detox, hour-by-hour plan, gamified NC tracker with milestone markers at 7/14/30/60/90 days).

### F4.6 Identity Rebuilder
> "In long relationships we lose parts of ourselves. Not because our partner was bad - but because we merged. Now is the time to rediscover and rebuild yourself as a whole person."

**Phase 1 — Excavation:** What did you stop doing when with them? What interests got pushed aside? Who are the friends you lost touch with? What dreams did you put on hold? What parts of yourself did you hide? What did you always want to try?

**Phase 2 — Rebuilding (week by week):**
- Week 1: identify one thing to reclaim
- Week 2: do one thing just for yourself
- Week 3: reconnect with one old friend
- Week 4: try one new thing
- Month 2: build new routine around YOU
- Month 3: new version of self emerging

**Phase 3 — Becoming (values clarification):** "I am someone who...", "My most important values are...", "The relationship I want to build is...", "The person I'm becoming is..."

**Identity document:** AI compiles over time — what you reclaimed, what you discovered, what you want going forward, who you are at your best, what you will not compromise on again.

**Self-love rebuilding:** self-compassion practice, daily affirmations (specific), achievements logging, treating yourself as you'd treat a friend.

### F4.7 Lesson Extractor
> "Relationships are teachers. This one taught you something. When you're ready, let's find out what."

Not: "They were terrible." Not: "It was all my fault." Yes: "What can I honestly learn from this?"

**Questions AI asks:** What did you learn about what you need? What patterns do you see in yourself? What would you do differently? What did this relationship give you? What do you want to carry forward? What do you want to leave behind?

**The honest relationship audit:** what was genuinely good, what was genuinely problematic, your own contribution to difficulties, the other person's contribution, what needs were trying to be met, whether those needs are valid.

**Pattern identification example:**
> "This is the third relationship where you've felt not heard. That pattern is telling you something important - not that you're unlovable, but that there may be a way you're choosing people or communicating needs that we can work on together."

**Wisdom document output:** personalized "Lessons Learned" — what you need in the next relationship, what you will not accept again, how you want to show up differently, updated non-negotiables, updated flexibility areas.

### F4.8 Ready For Love Again Assessment
**Emotional readiness:** think of ex without acute pain? wish them well (even a little)? excited about life without them? dating curiosity not desperation? feel whole without a partner?

**Practical readiness:** social media cleared/healed? mutual friends situation settled? shared items/places handled? finances separated? internal closure (not from them)?

**Self readiness:** identity rebuilt and strong? lessons integrated? patterns identified and worked on? physical health back? social life rebuilt?

Example dashboard:
```
LOVE READINESS ASSESSMENT
Emotional Healing     ████████░░  80%
Self Identity         ███████░░░  70%
Lessons Integrated    █████████░  90%
Physical Wellness     ████████░░  80%
Social Life Rebuilt   ██████░░░░  60%
Excitement not Fear   ███████░░░  70%
READY SCORE: 75%
"You're mostly ready. The area to focus on before jumping back in is
rebuilding your social life first. Here's why and how..."
[Begin Stage 2: Finding Love Again →]
```

**Full circle moment:** app shows who you were when you first opened the app, who you are now, what you learned, what you're bringing into the next chapter, celebration of the journey.

---

## 6. SECURITY & PRIVACY

- All data encrypted at rest (AES-256)
- All data encrypted in transit (TLS 1.3)
- User can delete ALL data anytime
- No data sold, ever
- No ads, no tracking
- GDPR compliant
- Data stays in India (Indian servers)

**Emotional data protection:**
- Conversations not stored after 90 days
- Only patterns/scores kept long term
- No human ever reads conversations
- AI cannot share your data with anyone
- Parent/partner cannot access your data

**Stored permanently:** account info (name, email), stage and progress, mood scores (not conversation content), pattern summaries (not raw conversations), assessment results.

**Deleted after 90 days:** full conversation text, uploaded images, voice recordings, screenshot analysis.

**Crisis exception:** crisis events logged for safety, never shared externally, used only to detect worsening patterns, user informed clearly.

---

## 7. HIGH-LEVEL TECH STACK (see file 05 for the week-by-week package install plan)

**Frontend:** React 18, React Router v6, Zustand (state), TailwindCSS + CSS Modules, Recharts, Framer Motion, Lucide React icons, Google Fonts, Vite (build).

**Backend:** FastAPI (Python), LangGraph (AI agents), Groq (LLaMA 3.1) primary LLM, Gemini Flash secondary LLM, Ollama local fallback, Gemini Vision (images), Whisper local (voice), sentence-transformers local (embeddings), ChromaDB local (RAG vector DB).

**Database:** PostgreSQL (Supabase free tier), Redis (Upstash free tier) for cache/session, Supabase Storage (free tier) for files.

**Deployment (all free tiers):** Frontend → Vercel, Backend → Render.com, Database → Supabase, Cache → Upstash, Monitoring → Sentry free tier.

**Free API keys needed:** Groq (groq.com), Gemini (aistudio.google.com), Supabase (supabase.com), Upstash (upstash.com).

---

## 8. WHY THIS PROJECT IS POWERFUL (portfolio framing)

✅ Solves a universal human problem
✅ Every person has been in one of 4 stages
✅ Complex multi-agent AI system
✅ RAG on psychology research
✅ LangGraph conditional routing
✅ Emotional AI (hard to build)
✅ Beautiful unique UI
✅ Social impact clear
✅ Startup potential massive

**What to say in an interview:**
> "I built an AI Love Guru that guides users through all four stages of love: single life, finding love, relationships, and heartbreak recovery. It uses a LangGraph multi-agent system with specialized agents for each stage, RAG on Gottman Institute and attachment theory research, and crisis detection for vulnerable emotional moments. The system can detect when someone is in genuine distress after a breakup and provide mental health support while routing to professional help if needed."

(See file `06-TESTING-DEPLOYMENT-LAUNCH.md` for the full expanded interview pitch, demo video script, and README plan.)

---
**⬇ Continues below: AI System Architecture ⬇**
-e 


-e 


# ❤️ LOVEGURU AI — AI SYSTEM ARCHITECTURE (COMBINED)
Merged from the "AI System Deep Dive", "Complete App Bible" AI section, and the "End-to-End Build Plan" LangGraph section. All details preserved; the 12-node LangGraph version (from the build plan) is the **CANONICAL / most detailed** pipeline description — it supersedes the earlier 9-agent / 11-node summaries, which are kept below for reference since they contain extra detail not repeated elsewhere.

---

## 1. MASTER AI OVERVIEW

**Input types AI handles:**
```
├── Text Messages        → Conversation, problems, stories
├── Images               → Partner photos, screenshots, selfies
├── Voice Messages       → Emotional tone + content
├── Screenshots          → Chat analysis, social media
└── Structured Data      → Check-ins, scores, forms
```

**AI models used (all free):**
```
├── Groq LLaMA 3.1 70B  → Main conversation AI
├── Google Gemini Flash  → Image analysis + long analysis
├── Whisper (Local)      → Voice to text
├── CLIP / LLaVA         → Image understanding (local backup)
├── MiniLM               → Embeddings for RAG
└── Ollama                → Local fallback
```

**Processing pipelines:**
```
├── Text Pipeline        → nodes/agents (see below)
├── Image Pipeline       → 6 analysis layers (5 image types)
├── Voice Pipeline       → 4-6 processing steps
├── Multi-modal          → Combines all inputs (Fusion Layer)
└── RAG Pipeline         → 5 knowledge collections
```

---

## 2. MASTER ARCHITECTURE MAP (high level)

```
USER SENDS SOMETHING (text / image / voice / screenshot)
           │
           ▼
┌──────────────────────────────────────┐
│         INPUT CLASSIFIER             │
│  → Text only / Image only / Voice    │
│    only / Text+Image / Screenshot    │
└──────────┬───────────────────────────┘
           │
    ┌──────┴──────────────────┐
    ▼                         ▼
TEXT PIPELINE           IMAGE PIPELINE
    │                         │
    ▼                         ▼
VOICE PIPELINE ──────► FUSION LAYER (combines all)
                             │
                             ▼
                    LANGGRAPH AGENTS
                             │
                             ▼
                    FINAL AI RESPONSE (text + actions)
```

---

## 3. EARLIER DRAFT — 9-AGENT SUMMARY (from "Complete App Bible") — kept for reference

State object fields tracked: `user_id, session_id, current_stage, user_profile, relationship_history, current_situation, partner_description, problem_description, emotion_detected, crisis_level, rag_context, agent_outputs, final_response, action_items, resources`.

```
AGENT 1: Stage Router          → detects life stage, routes, can switch stages mid-conversation
AGENT 2: Emotion Detector      → detects emotional state always, adjusts tone, flags crisis moments
AGENT 3: Crisis Safety Agent   → runs on EVERY message, especially active in Stage 4, provides resources
AGENT 4: Partner Analysis      → Stage 1 specific, analyzes partner descriptions, reality check generator
AGENT 5: Self Growth Agent     → Stage 1 & 4, personal development, grooming/lifestyle advice
AGENT 6: Relationship Counselor→ Stage 3, problem analysis, communication coaching, solution generation
AGENT 7: Heartbreak Coach      → Stage 4, grief guidance, recovery planning, mental+physical health
AGENT 8: RAG Research Agent    → searches knowledge base, backs advice with science
AGENT 9: Response Personalizer → warm empathetic tone, non-judgmental, culturally sensitive, age appropriate
```

**RAG knowledge base collections (5):**
1. Attachment Theory — Bowlby research, adult attachment styles, anxious/avoidant/secure patterns
2. Relationship Science — Gottman Institute (40yrs data), love languages, communication research
3. Heartbreak & Grief — grief psychology, heartbreak neuroscience, recovery timeline research
4. Self Development — self-compassion (Neff), confidence building, emotional intelligence
5. Attraction & Dating — evidence-based attraction research, compatibility research, healthy relationship formation

---

## 4. EARLIER DRAFT — 11-NODE TEXT PIPELINE (from "AI System Deep Dive") — kept for reference, richer detail on each early node

### TEXT STEP 1: Text Preprocessor
Cleans every text message before anything else runs.

**Cleaning operations example:**
```
Input: "omg idk wat 2 do my bf ignores me 😭😭"

Step 1: Normalize slang
"omg" → "oh my god" | "idk" → "I don't know" | "wat" → "what" | "bf" → "boyfriend"

Step 2: Extract emojis separately
Emojis found: 😭😭 → meaning: crying, distress

Step 3: Detect language
Language: English | Mixed language: No

Step 4: Clean output
"Oh my god I don't know what to do my boyfriend ignores me"
+ emoji_signals: [distress, crying]
```
Also detects: message length (short=emotional, long=analytical), punctuation patterns (!!!=high emotion), capitalization (CAPS=intense feeling), question vs statement vs exclamation, time sent (3AM message = special flag).

### TEXT STEP 2: Context Builder
Builds the complete picture before any agent runs.

**Fetches from database:**
- **User profile context** — name, age, current stage, relationship duration, partner name (as told to AI), past issues discussed, attachment style (detected earlier), communication preference
- **Conversation history context** — last 10 messages, previous topics, what AI previously said, user's reaction, time since last message
- **Pattern context** — recurring themes this month (e.g. "Arjun ignores me" mentioned 4 times), mood drops every Sunday evening, established patterns

All of this is injected into every agent prompt so the AI responds knowing the user and their history — not starting from zero every message.

### TEXT STEP 3: Stage Router Agent
- LLM: Groq LLaMA 3.1 70B | Temperature: 0.0 (deterministic) | Max tokens: 100
- Identifies which life stage the message belongs to, routes to correct specialist agents, can change stage mid-conversation (no manual switching needed by user).

**Routing examples:**
```
"I'm single and want to know what kind of partner to look for" → STAGE 1
"This guy I met seems nice but I'm not sure about him"          → STAGE 2
"My boyfriend and I had a huge fight"                            → STAGE 3
"We broke up last night"                                         → STAGE 4
"I'm still not over my ex but I met someone new"                 → STAGE 4 + STAGE 2 BLEND
```

### TEXT STEP 4: Emotion Detector Agent
- LLM: Groq LLaMA 3.1 70B | Temperature: 0.1 | Max tokens: 200
- **Multi-signal emotion detection:**

**Signal 1 — Word-level analysis (vocabulary mapping):**
- Hurt signals: "ignored", "invisible", "don't care", "doesn't matter to them", "gave up"
- Fear signals: "scared", "what if", "losing them", "going to leave", "maybe I should"
- Anger signals: "unfair", "always", "never", "sick of", "done with this", "can't believe"
- Love signals (Stage 2): "butterflies", "can't stop thinking", "makes me smile", "really like them"
- Grief signals (Stage 4): "miss them", "empty", "nothing matters", "how do I", "will I ever", "can't eat"

**Signal 2 — Sentence structure analysis:** short fragmented = overwhelmed; very long rambling = anxious/processing; questions only = confused/seeking clarity; statements only = processing/venting; mixed = complex emotional state.

**Signal 3 — Emoji emotional data:** 😭 crying distress, 😤 frustrated anger, 💔 heartbreak/loss, 😰 anxiety/worry, 🥺 vulnerability/sadness, 😍 excitement/attraction (Stage 2), 😶 numbness/shutdown; multiple same emoji = intensity multiplier.

**Signal 4 — Historical baseline:** compare to user's average emotional state, is this worse than normal?, new emotion or recurring?, trajectory getting better or worse?

**Final emotion output example:**
```json
{
  "primary_emotion": "hurt",
  "secondary_emotion": "fear",
  "intensity": "high",
  "emotion_score": 7.8,
  "needs": "validation_first",
  "tone_needed": "warm_and_gentle",
  "avoid": "advice_too_soon"
}
```

### TEXT STEP 5: Crisis Safety Agent ⚠️ runs on EVERY single message, cannot be skipped
- LLM: Groq + Gemini BOTH (double check) | Temperature: 0.0 (zero creativity, pure safety)

**Layer 1 — Instant keyword scan (no LLM, instant):**
- EMERGENCY (trigger immediately): "kill myself" / "end my life" / "want to die" / "hurt myself" / "self harm" / "not worth living"
- DANGER (trigger deep analysis): "can't take this anymore" / "want to disappear" / "nobody would care" / "what's the point of anything" / "better off without me"
- WATCH (monitor pattern): "so alone" / "nobody understands" / "hopeless" / "nothing will change" / "can't do this anymore"

**Layer 2 — LLM contextual understanding (context saves false positives):**
```
"I want to kill him" → SAFE (anger at partner)
"I want to kill myself" → EMERGENCY
"I'm dying of embarrassment" → SAFE
"I feel like dying" → DANGER
```
LLM reads full conversation context, understands figurative vs literal language, checks if a plan or means is mentioned.

**Layer 3 — Pattern risk score:**
```
+ Recent breakup (Stage 4 active)  +20 points
+ 3AM message time                 +10 points
+ Declining mood 5+ days           +15 points
+ Previous crisis history          +25 points
+ Social isolation mentioned       +10 points
+ Physical symptoms mentioned      +10 points
```

**Layer 4 — Final level decision:**
```
SAFE      → Normal pipeline continues
WATCH     → Extra gentle response + check-in
DANGER    → AI directly addresses concern
EMERGENCY → Full SOS screen + helplines
```

**Crisis response rules:** validate pain FIRST always, never alarm or panic, never threaten to "tell someone", always give user control.

**Helplines shown:** iCall — 9152987821 (free, India); Vandrevala Foundation — 1860-2662-345 (24/7, free).

### TEXT STEP 6: RAG Research Agent
Retrieval Augmented Generation — AI searches real psychology research, finds relevant science, adds it to response generation so the response is backed by real research.

**Step 1 — Smart query building** (not the raw user message):
```
User: "My partner never listens to me"
Smart query built: "active listening relationship communication feeling
unheard couples conflict resolution Gottman emotional bids response"
```

**Step 2 — Collection selection:**
```
Collection 1: Attachment Theory        → Stage 1 pattern analysis, Stage 4
Collection 2: Relationship Science     → Stage 3 all features
Collection 3: Dating & Attraction      → Stage 1, Stage 2
Collection 4: Heartbreak & Grief       → Stage 4 exclusively
Collection 5: Self Development         → Stage 1, Stage 4 identity rebuilding
```

**Step 3 — Vector search process:**
```
Query → MiniLM Embedding Model → 384-dimensional vector
     → ChromaDB cosine similarity search
     → Returns top 10 candidates
     → Filter by score > 0.65
     → Re-rank by relevance
     → Final top 3 chunks selected
```
Example retrieved chunk: source `Gottman_relationship_research.pdf`, score 0.87, content about emotional bids and "turning toward" vs "turning away".

**Step 4 — Context injection to agent:** research chunks are added to the agent's prompt with instructions: "Based on this research: [CHUNK 1/2/3]... now help user with their specific situation."

### TEXT STEP 7: Specialist AI Agents (stage-specific)

**Agent A — Partner Analysis Agent (Stage 1)**
- LLM: Groq LLaMA 3.1 70B | Temperature: 0.6
- Categorizes each expectation (e.g. "Tall" → personal preference/valid-but-rigid; "Rich" → investigate deeper, real need security-or-materialism?; "Never angry" → unrealistic, real need = safety from aggression, possible past wound like an angry parent; "Always happy" → unrealistic, real need = positive energy; "Totally devoted" → examine carefully, real need = security/being prioritized, risk = controlling or anxious attachment).
- Asks follow-up questions like: "When you say rich - what does that actually mean to you? Is it about lifestyle, security, or something you grew up without?"
- Generates insight: what expectations reveal, what they truly need vs think they want, what past experiences shaped these.

**Agent B — Relationship Counselor (Stage 3)**
- LLM: Groq LLaMA 3.1 70B | Temperature: 0.7
- Investigates 5 dimensions per problem: (1) what exactly happens, (2) when does it happen, (3) how do you respond, (4) what have you tried, (5) what do you truly need.
- Example: "My partner never listens when I talk" → root cause identified as partner decompressing after work (misread as rejection, timing not interest level) → solution: request 30min decompression time first, then 20min full-attention conversation, with an exact script.

**Agent C — Heartbreak Coach Agent (Stage 4)**
- LLM: Groq LLaMA 3.1 70B | Temperature: 0.5 (careful, not creative)
- Analyzes: how recent was breakup, who initiated, how long was relationship, current symptoms, safety check (always), current grief stage, what user needs RIGHT NOW.
- Response calibration by time since breakup: Day 1-3 presence/validation ONLY; Week 1-2 gentle stabilization; Week 3-4 beginning to process; Month 2-3 active healing work; Month 4+ growth and forward movement.

### TEXT STEP 8: Response Personalizer
- LLM: Groq LLaMA 3.1 70B | Temperature: 0.8 (warm, natural language)
- Transforms raw clinical-sounding advice into human warmth.

**Before:** *"The subject is experiencing anxious attachment style behaviors manifesting as hypervigilance to partner's communication patterns. Recommend self-soothing techniques and communication of needs using non-violent communication model."*

**After:** *"Okay so first - what you're feeling makes complete sense. When we really love someone, small things like a delayed reply can feel so much bigger than they are. Here's what I think is happening and what might actually help..."*

**Tone calibration by stage:** Stage 1 (Single) — encouraging, coaching; Stage 2 (Finding) — excited, supportive; Stage 3 (Relationship) — balanced, thoughtful; Stage 4 (Breakup) — tender, gentle, patient.

**Cultural sensitivity:** Indian relationship context awareness, family pressure understanding, arranged marriage context if relevant, conservative family dynamics, financial family expectations.

---

## 5. IMAGE AI PIPELINE — 5 COMPLETE IMAGE TYPES

### IMAGE TYPE 1: Partner Photo Analysis
- AI model: Google Gemini Vision (free tier, 1500 req/day) + LLaVA (local, free) as backup
- Trigger: "Let me show you who I'm talking about" → uploads photo of person they like/partner

**Layer 1 — Basic visual description:** approximate age range, general presentation/style, setting/context, body language, facial expression.

**Layer 2 — Body language reading:**
- Open (positive): arms uncrossed, genuine smile (Duchenne — eye crinkles), leaning toward people, relaxed posture, direct eye contact
- Closed (note for user): arms crossed consistently, forced/fake smile (mouth only), leaning away, tense posture, avoiding eye contact
- **Important disclaimer always shown:** "Body language in photos has limitations. This is one photo, one moment. Please don't judge someone fully by this."

**Layer 3 — Context analysis (if couple photo):** physical closeness, who initiated contact in photo, facing each other or camera?, comfort level visible, matching energy.

**Layer 4 — Photo context:** dating profile photo → profile analysis; casual selfie → authenticity indicators; group photo → social context; professional photo → self-presentation.

**Sample response:** *"From this photo I can see a few things: They have an open, relaxed smile here - the kind that reaches their eyes which generally suggests genuine comfort. Their posture looks relaxed and open. Of course, one photo only shows one moment. Tell me more about them - what drew you to them beyond this photo?"*

**What AI NEVER does with photos:** never harsh judgments about appearance, never rates attractiveness, never says "they look like a bad person", never assumes character, never stores or trains on user photos.

### IMAGE TYPE 2: Screenshot Chat Analysis (most powerful image feature)
Pipeline: Step 1 Gemini Vision extracts all text from image → Step 2 structures the conversation → Step 3 deep pattern analysis agents.

**Step 1 — Text extraction:** all message text (both sides), timestamps, who sent which message, emojis, read receipts (if visible), typing indicators (if captured).

**Step 2 — Conversation structure:** organizes into USER side / PARTNER side / timeline of exchange / response time gaps.

**Step 3 — Five analyses:**
1. **Communication Balance** — who sends more, who asks more questions, is one person doing all the work, response length comparison.
2. **Emotional Bids (Gottman)** — how many connection bids made, how many responded to, how many ignored/deflected.
   Example: User: "Had the worst day at work 😔" (a BID) → Good response: "Oh no what happened? Tell me" (turned TOWARD) vs Bad response: "Yeah same lol" (turned AWAY).
3. **Tone Detection** — warm or cold?, passive aggression?, gaslighting language?, contempt (eye-roll language)?, genuine vs performative affection?
4. **Red Flag Detection** — manipulative language, guilt-tripping phrases, love bombing vs genuine warmth, silent treatment patterns, dismissiveness patterns.
5. **Response Time Patterns (if timestamps visible)** — consistent = reliable; hours of silence then burst = avoidant?; instant to some, hours to others = selective interest.

**Sample output:** positive signs noted (follow-up questions, using your name) → worth noticing (a direct question that got dodged) → suggestion (a script to ask directly next time).

### IMAGE TYPE 3: User Selfie Analysis (for grooming & style guidance)
- AI model: Gemini Vision + LLaVA
- Trigger: "Can you help me look better?" / "What should I change about my appearance?" / "Does this outfit work?"

**Layer 1 — Face shape detection:** oval, round, square, heart, oblong, diamond → then suggests best hairstyles, beard style (men), makeup techniques (women), glasses frames.

**Layer 2 — Skin analysis (observes, doesn't diagnose):** general appearance, tone category, visible concerns → suggests basic skincare routine, products by tone, common mistakes.
**Important note always shown:** "I can see general skin health but I'm not a dermatologist. For specific skin concerns see a professional."

**Layer 3 — Style assessment (if outfit visible):** fit for body type, color coordination, occasion appropriateness, simple improvements; body type identification → flattering clothing, colors for skin tone, fit guidance.

**Layer 4 — Presentation score example:**
```
Grooming:         ████████░░  8/10
Style:             ██████░░░░  6/10
Presentation:      ███████░░░  7/10
Confidence shown:  █████░░░░░  5/10
TOP 3 CHANGES FOR BIGGEST IMPACT: [1] [2] [3]
```

**AI tone rule for selfie analysis:** always kind and constructive, never harsh or critical, frame as enhancement not fixing ("You already have great X, let's enhance Y"), body-positive framing always.

### IMAGE TYPE 4: Mood/Journal Image Analysis (Stage 4 especially)
- Trigger: "I found this old photo of us" / "This was from our last trip together"
- Approach: extremely gentle and careful, safety check runs immediately, focus on user's emotion not the photo.
- AI observes context (place, occasion), user's expression, what the memory might mean.
- **Response approach:** start with the emotion — *"Looking at old photos is one of the hardest parts of healing. What memories does this one bring up for you?"* — then help process what the memory represents, how to hold memories with compassion, the difference between missing the memory vs missing the person.

### IMAGE TYPE 5: Red Flag Evidence Analysis
- Trigger: "Is this normal? Look at what they sent me" / "Does this seem okay to you?"

**Concerning patterns detected:**
- Guilt-tripping: "If you loved me you would..." / "I guess I'm not important to you" / "Fine, don't worry about me"
- Controlling: "Who were you with?" (demanding not curious) / "You shouldn't wear that" / "I don't like your friends"
- Gaslighting: "That never happened" / "You're too sensitive" / "You're imagining things" / "You always overreact"
- Manipulation: "I'll hurt myself if you leave" / "Nobody will ever love you like I do" / "You owe me after everything I've done"

**AI response approach:** name the pattern clearly, explain WHY it's concerning, validate the user's instinct to question it, give the user agency to decide what to do, never force a conclusion, offer resources if needed.

**Example response:** *"What you've shared here is something worth paying attention to. The phrase 'if you loved me you would' is a classic guilt-tripping pattern. It puts the responsibility for their feelings onto you, which is not fair or healthy. The fact that you're questioning this suggests your instinct is already picking something up. Trust that. Would you like to talk about how this pattern has been showing up?"*

---

## 6. VOICE AI PIPELINE

### STEP 1: Audio Capture
User holds mic button and speaks. App records WAV format, 16kHz, mono. Max length: 2 minutes per message. Shows waveform animation while recording.

### STEP 2: Speech to Text
- Model: OpenAI Whisper (runs LOCAL, FREE), Medium model size (best accuracy)
- Extracts: transcribed text, language detected, confidence score per segment, timestamps for each word
- Handles: English, Hindi, mixed Hinglish, crying voice (harder to transcribe), soft quiet voice (nighttime), fast anxious speaking

### STEP 3: Voice Emotion Analysis (beyond the words — the voice itself)

**Speech rate analysis:** very fast → anxious/excited/overwhelmed; normal → calm/processing; very slow → depressed/exhausted/grieving; irregular → emotional/distressed.

**Pitch analysis:** high → anxiety/excitement/fear; low → sadness/depression/defeat; breaking voice → crying/overwhelmed; flat monotone → emotional numbness.

**Volume analysis:** very quiet → shame/exhaustion/defeat; loud bursts → anger/passion; volume drops at end → hopelessness.

**Pause pattern:** long pauses → searching for words, emotional; crying pauses → active grief; quick pauses only → anxious rushing.

**Combined voice emotion score example:**
```json
{
  "voice_emotion": "grief",
  "intensity": "high",
  "crying_detected": true,
  "energy_level": "very_low",
  "crisis_voice_flag": false
}
```

### STEP 4: Combined (Text + Voice) Analysis
Example — text says "I'm fine I guess" but voice is slow, breaking, very quiet → merged reading: text and voice contradict → priority given to voice emotion (more honest signal).
**AI responds to the voice, not just the words:** *"You said you're fine, but I can hear that things feel heavy right now. You don't have to be okay with me. What's really going on?"*

---

## 7. MULTI-MODAL FUSION LAYER

When text + image arrive together:
```
Example 1:
Text: "Is this a red flag? I'm worried"
Image: Screenshot of concerning conversation
→ Text analysis: fear/worry, needs validation + clear guidance, Stage 3
→ Image analysis: 2 red flag patterns found (guilt-tripping + dismissiveness)
→ Fusion: user's instinct is scared and correct → validate instinct + educate on pattern
→ Response: "Your instinct is right to question this. Looking at what they wrote here..."
```
When text + image + voice all arrive together:
```
Example 2:
Text: "Help me look better for our first date"
Image: Selfie of user
Voice: "I'm so nervous about meeting them" (nervous tone detected)
→ Fusion priority: address nervousness FIRST, then give specific style suggestions
  based on what AI actually saw in the selfie (face shape etc.)
```

---

## 8. COMPLETE LANGGRAPH FLOW (CANONICAL — 12-node master graph, from the End-to-End Build Plan)

### GRAPH STATE OBJECT (everything that flows through all 12 nodes)

**Core info:** `user_id, session_id, raw_input, input_type (text/voice/image/multi), timestamp, time_of_day`

**User context (loaded from DB):** `user_profile, current_stage, ai_personality, support_preference, attachment_style, partner_name, conversation_history (last 20 messages), recent_mood_scores (7 days), known_triggers, what_helps, recurring_themes`

**Analysis results (filled by agents):** `message_type (vent/question/crisis/etc), topics_detected, urgency_score, primary_emotion, secondary_emotion, emotion_intensity, mood_score`

**Safety data:** `crisis_level (safe/watch/danger/emergency), crisis_confidence, crisis_keywords_found, crisis_patterns_detected`

**RAG data:** `rag_needed, rag_query, rag_collection, retrieved_chunks, retrieval_scores`

**Agent outputs:** `intake_analysis, specialist_advice, physical_health_tip, pattern_found, action_suggested`

**Final output:** `raw_response, final_response, response_includes_sos, response_includes_breathing, quick_replies, task_suggested, error_occurred, error_message`

### THE 12 NODES

**NODE 1 — Input Processor** *(no LLM, pure logic)*
Determines input type; routes voice → Whisper, image → image processor; cleans/normalizes text; detects emojis and meaning; checks message length patterns; detects if 3AM mode needed; populates basic state fields. → Always goes to Node 2.

**NODE 2 — Context Loader** *(no LLM, database fetching)*
Fetches user profile (PostgreSQL), last 20 messages (Redis), last 7 days mood scores, current stage data, known patterns, partner profile (if exists); calculates time since last crisis; builds comprehensive context object. → Always goes to Node 3.

**NODE 3 — Crisis Safety Agent** *(LLM: Groq + Gemini, temp 0.0, ALWAYS RUNS, cannot be skipped)*
4-layer detection exactly as described in Section 4 / Text Step 5 above.
- SAFE/WATCH/DANGER → continue to Node 5
- EMERGENCY → routes to **Node 3A**

**NODE 3A — Emergency Handler** *(only for EMERGENCY level)*
Bypasses ALL other agents; generates calming response only; triggers SOS screen in frontend; logs crisis event; shows helplines; goes straight to Node 11 (memory) then END.

**NODE 4 — Intake Analyzer** *(LLM: Groq, temp 0.1, max 200 tokens)*
Classifies message type: VENT (just expressing, no advice wanted), QUESTION (wants specific information), PROBLEM (has a situation to solve), UPDATE (sharing news/progress), CRISIS (backup to Node 3), CHECKIN (responding to AI question), PHYSICAL (body/health related), SOCIAL (people/relationships).
Extracts topics: academic, career, family, friendship, romance, intimacy, finances, health, identity, loneliness, breakup, etc.
Determines routing: which specialist agent, whether to skip physical agent, whether RAG is needed. → Always goes to Node 5, sets routing flags.

**NODE 5 — Stage Router** *(LLM: Groq, temp 0.0, max 100 tokens)*
Confirms which stage the message belongs to; can override the user's saved current_stage (e.g. Stage 3 user suddenly talking about a breakup → switch to Stage 4 mode); sets `specialist_needed` flag.
Routes to: Node 6A (Stage 1) / Node 6B (Stage 2) / Node 6C (Stage 3) / Node 6D (Stage 4).

**NODE 6 — Specialist Agents (4 branches)**
- **6A Stage 1 Specialist** (temp 0.6) — partner expectation analysis, readiness assessment conversations, self-improvement guidance, grooming/style advice, attraction/confidence building, "Am I ready for love?" questions. Reads user context + RAG (attachment research); always validating, never harsh.
- **6B Stage 2 Specialist** (temp 0.65) — specific person analysis, conversation coaching, red/green flag identification, date prep/debrief, profile review, "Should I pursue this?" questions. Reads image/screenshot analysis, checks against known red flags (RAG); personalized dating strategies.
- **6C Stage 3 Specialist** (temp 0.7) — relationship problem solving, communication coaching, fight analysis/resolution, love language guidance, intimacy/connection advice, keeping-love-alive strategies. 5-dimension investigation, root cause ID, generates scripts, both-sides perspective, uses Gottman research (RAG).
- **6D Stage 4 Specialist** (temp 0.5, more careful) — acute heartbreak support, grief stage navigation, NC support, identity rebuilding, physical health in grief, readiness-for-love-again. Extra careful/gentle tone, safety check integrated, physical health addressed, grief science explained, practical survival guidance.

**NODE 7 — RAG Retriever** *(no LLM for retrieval, MiniLM for embeddings; runs only if `rag_needed = True`)*
Builds targeted smart search query (not raw message), selects the right of the 5 collections, embeds query with MiniLM, cosine similarity search in ChromaDB, top 10 → filter score > 0.65 → re-rank → final top 3 chunks.
Output: `retrieved_chunks, retrieval_scores, technique_suggested, rag_used = True`.

**NODE 8 — Image Analyzer** *(LLM: Gemini Vision, only activates if image present)*
Determines image type (SELFIE / PARTNER_PHOTO / SCREENSHOT_CHAT / SCREENSHOT_PROFILE / MEMORY_PHOTO / EVIDENCE) and runs the matching analysis from Section 5 above.
Output: `image_type, image_analysis, extracted_text (if screenshot), red_flags_in_image, image_insights`.

**NODE 9 — Response Builder** *(LLM: Groq, temp 0.7, max 700 tokens)*
Takes ALL agent outputs together, decides what to include.

*Inclusion decision rules:*
- Vent mode → validation only, NO advice
- Advice mode → include technique + action
- Crisis → ONLY comfort + resources
- 3AM → shorter + calmer everything
- Physical mentioned → include physical tip
- Image analyzed → include image insights

*Response structure built:* (1) Validation/acknowledgment (ALWAYS) → (2) Main insight or support → (3) Technique or guidance (if needed) → (4) Physical tip (if relevant) → (5) Action suggestion (if not vent) → (6) Open-ended question or space.

*Length rules:* Vent mode 2-3 sentences max; Crisis 2-3 sentences, simple; Normal 4-6 sentences; Analysis can be longer (structured).

*Also determines:* `quick_replies` (3 suggested responses), `show_sos`, `show_breathing`, `task_to_suggest`, `follow_up_needed` (flag for memory).

**NODE 10 — Response Personalizer** *(LLM: Groq, temp 0.8, max 600 tokens)*
Takes `raw_response` from Node 9, applies the user's chosen personality style, adjusts for time of day (3AM special), adjusts for detected emotional state, adds appropriate emojis (max 2), adjusts formality, removes any remaining clinical language.

*Personality transformations:*
- **Warm & Gentle** — more "I hear you" language, collaborative "we" language, softer transitions, more emotional acknowledgment
- **Direct & Honest** — gets to point faster, "Real talk:" intros, fewer softening words, still kind but efficient, clear action-oriented
- **Light & Easy** — Gen-Z casual language where appropriate, humor when not crisis, lighter framing, still substantive

*3AM override (all personalities):* softer everything, no exclamations, moon/star emoji only, focus on rest and tomorrow, "It looks different in daylight."

*Crisis override (all personalities):* removes all humor, removes all casual language, calm/present/simple, direct about resources.

**NODE 11 — Memory Updater** *(no LLM, pure logic, runs AFTER response sent)*

*Redis (session memory):* append message to session history, update session mood trajectory, track topics this session, update chat mode if changed, set 30-min TTL.

*PostgreSQL (persistent):* save message to `messages` table, update `conversations` table, log mood score to `mood_logs`, if crisis → log to `crisis_logs`, if task suggested → save to `tasks_challenges`.

*Pattern detection logic:* count topic occurrences; topic appears 3rd time → add to `recurring_themes`; technique helped (mood improved) → add to `what_helps`; topic precedes low mood → add to `known_triggers`; self-criticism pattern → flag for pattern card.

**NODE 12 — Pattern Analyzer** *(runs weekly, not per message; LLM: Gemini Flash, temp 0.3)*
Triggered every Sunday midnight, per user.

*Gathers:* all mood logs from past 7 days, all checkin data, all conversation topics, physical health data, task completion rates, crisis events if any.

*Analyzes:* day-of-week mood patterns, sleep-mood correlation, exercise-mood correlation, topic-mood correlation, improvement/decline trend, what worked this week.

*Generates:* 3 personalized insights, 1 focus area for next week, celebration of wins, weekly report saved to DB, notification queued for user.

---

## 9. FULL 12-NODE FLOW DIAGRAM

```
MESSAGE ARRIVES (any type)
         │
         ▼
   NODE 1: Input Classifier ──→ text/image/voice/multi
         │
         ▼
   NODE 2: Preprocessor (per input type) ──→ clean + structure all inputs
         │
         ▼
   NODE 3: Context Builder ──→ fetch all user history
         │
         ▼
   NODE 4: Crisis Safety Agent ──→ ALWAYS RUNS FIRST
         │
    ┌────┴──────────────────────┐
    │ SAFE/WATCH/DANGER         │ EMERGENCY
    ▼                           ▼
 NODE 5: Stage Router     NODE 4A: Emergency Handler
    │                     → SOS Screen, Helplines, Breathing
 ┌──┴────────────────┐
 ▼                    ▼
NODE 6A Stage 1   NODE 6B Stage 2
 │                    │
 ▼                    ▼
NODE 6C Stage 3   NODE 6D Stage 4
 └────────┬───────────┘
          ▼
   NODE 7: RAG Retriever ──→ search knowledge base
          ▼
   NODE 8: Emotion Detector ──→ precise emotion mapping
          ▼
   NODE 9: Response Builder ──→ combine all outputs
          ▼
   NODE 10: Personalizer ──→ warm human tone
          ▼
   NODE 11: Memory Updater ──→ save patterns + learnings
          ▼
      RESPONSE SENT TO USER
```
> Note: the node numbering above (with Image Analyzer, RAG, Emotion Detector) reflects the two source-document orderings merged — in the canonical 12-node section (Section 8) Image Analysis is Node 8 and RAG is Node 7; in this summary diagram they are shown in the linear order the original document used. Both orderings are conditional branches around the same core pipeline — build it so Crisis Safety always runs first, Stage Routing happens once, and RAG/Image Analysis run in parallel/conditionally before the Response Builder.

---

## 10. LLM SETTINGS — EVERY AGENT (complete configuration table)

```
┌────────────────────┬──────────────┬───────┬─────────────┐
│ AGENT               │ MODEL        │ TEMP  │ MAX TOKENS  │
├────────────────────┼──────────────┼───────┼─────────────┤
│ Input Classifier    │ Groq LLaMA   │ 0.0   │ 50          │
│ Stage Router         │ Groq LLaMA   │ 0.0   │ 100         │
│ Emotion Detector     │ Groq LLaMA   │ 0.1   │ 200         │
│ Crisis Safety        │ Groq+Gemini  │ 0.0   │ 150         │
│ Emergency Handler     │ Groq LLaMA   │ 0.0   │ 300         │
│ Partner Analyzer      │ Groq LLaMA   │ 0.6   │ 600         │
│ Relationship Coach    │ Groq LLaMA   │ 0.7   │ 700         │
│ Heartbreak Coach      │ Groq LLaMA   │ 0.5   │ 600         │
│ RAG Retriever         │ MiniLM embed │ N/A   │ N/A         │
│ Image Analyzer        │ Gemini Vision│ 0.3   │ 500         │
│ Voice Processor       │ Whisper Local│ 0.0   │ N/A         │
│ Response Builder       │ Groq LLaMA   │ 0.7   │ 700         │
│ Personalizer          │ Groq LLaMA   │ 0.8   │ 600         │
│ Memory Updater        │ No LLM       │ N/A   │ N/A (logic) │
│ Pattern Analyzer       │ Gemini Flash │ 0.3   │ 1000        │
└────────────────────┴──────────────┴───────┴─────────────┘

FREE API SOURCES:
Groq:    groq.com     → Free 14,400 req/day
Gemini:  aistudio.google.com → Free 1500 req/day
Whisper: Local install → Free forever
MiniLM:  Local install → Free forever
LLaVA:   Ollama local  → Free forever
```

### LLM Setup Hierarchy (from the build plan)
**Primary — Groq (LLaMA 3.1 70B):** free limit 14,400 req/day, ~500 tokens/sec, used for all real-time chat agents. Config: `model: "llama-3.1-70b-versatile"`, `streaming: True` (typewriter effect), `timeout: 30s`.

**Secondary — Gemini Flash:** free limit 1,500 req/day, used for image analysis + weekly reports. Config: `model: "gemini-1.5-flash"`, `streaming: False` (structured output).

**Tertiary — Ollama Local:** free/unlimited local compute, used for development + fallback. Models: `llama3.1` (8B, smaller/faster), `mistral` (7B, good quality).

**Fallback chain logic:** Try Groq → if error/limit → Try Gemini → if error/limit → Use Ollama local → if error → Return error message to user.

**Streaming setup:** Chat responses stream (tokens arrive one by one, typewriter effect, feels alive). Analysis (partner/conversation) is NOT streamed — complete result returned, animated section-by-section reveal in UI instead.

---

## 11. MEMORY SYSTEM COMPLETE (3 types working together)

**Memory 1 — Session Memory (Redis):** last 20 messages this conversation, current mood trajectory, topics discussed today, expires 30 minutes after last message.

**Memory 2 — User Profile (PostgreSQL):** permanent user knowledge — name, stage, attachment style, what AI has learned, past issues discussed, what advice worked/didn't, partner details (if shared). Never expires.

**Memory 3 — Pattern Memory (PostgreSQL):** detected behavioral patterns, recurring topics, emotional triggers identified, weekly mood patterns, updated after every conversation.

**How memory makes the AI smarter — example:**
```
CONVERSATION 1:
User: "My boyfriend Arjun doesn't text back"
AI learns: Partner name = Arjun; Issue = communication, texting

CONVERSATION 2 (days later):
User: "Same problem again"
AI KNOWS (from memory): "Same problem as before - Arjun not texting"
AI says: "Is this the same situation with Arjun you mentioned before?
          What's happened since we last talked?"
```
This feels like talking to someone who ACTUALLY remembers you and your story — not starting over every single time.

---

## 12. FULL END-TO-END WORKED EXAMPLE (Stage 4, multi-modal)

**Input:** User uploads a photo of their ex + sends a crying-voice message + text: *"I found this old photo and I can't stop looking at it. It's been 2 weeks and I'm not getting better."*

1. **Input Classifier** — photo + voice + text detected → multi-modal processing starts
2. **Whisper processes voice** — transcribes text; detects crying voice, very slow speech; `emotion_from_voice: grief, high intensity`
3. **Image analysis (Gemini Vision)** — detects couple photo, happy memory, context = meaningful past memory
4. **Crisis Safety Agent** — checks all content; "not getting better" flagged; crisis level: **WATCH** (elevated, not emergency, needs care)
5. **Stage Router** — Stage 4 confirmed (breakup grief) → routes to Heartbreak Coach Agent
6. **RAG Retriever** — searches grief timeline research; finds "2-3 weeks acute grief peak"; also photo-stimulus-and-grief-loop research
7. **Emotion Detector** — text + voice + image combined; primary: grief (high); secondary: despair; needs: validation + hope + gentle guide
8. **Heartbreak Coach Agent** — sees it's been 2 weeks, sees photo is triggering a loop, RAG context confirms this is a normal timeline → generates validation + explanation + gentle next step
9. **Personalizer** — makes it warm and human, not clinical/cold, gentle present energy

**Final response:**
> "Looking at old photos is one of the hardest parts of this. Two weeks in is actually right in the middle of the hardest stretch - your brain is still rewiring from someone who was a big part of your daily life. The fact that you're not okay yet doesn't mean something is wrong. It means you loved genuinely. Can I ask - is this photo somewhere you keep seeing it? Sometimes just moving it somewhere less visible (not deleting, just moving) can give your mind a tiny bit of rest. How are you sleeping and eating? I want to understand how your body is doing through this too."

**Then AI sends:** gentle check-in questions, photo management suggestion (gentle), physical health check, no SOS (WATCH level, not emergency), warm follow-up invitation.

---
**⬇ Continues below: Database + API Design ⬇**
-e 


# ❤️ LOVEGURU AI — DATABASE + API DESIGN (COMBINED)

Two draft database schemas existed across the source documents. The one from the **"End-to-End Build Plan"** (18 tables, more detailed field types and CHECK constraints) is **CANONICAL** — build this one. The earlier, simpler 12-table version from the **"Complete App Bible"** is kept below it labeled **EARLIER DRAFT** purely for reference since a couple of its tables (`partner_profiles` fields like `known_about` JSON, `readiness_assessments` as its own table) weren't merged verbatim into the canonical version, and it's useful context for anyone reading both docs.

---

## PART A — CANONICAL DATABASE SCHEMA (18 tables, from End-to-End Build Plan)

### Table creation order matters (foreign keys) — build in this order:

### ORDER 1: `users`
```
id                (uuid, primary key, auto-generated)
email             (text, unique, not null)
password_hash     (text)
created_at        (timestamptz, default now())
last_active       (timestamptz)
email_verified    (boolean, default false)
google_id         (text, nullable)
```

### ORDER 2: `user_profiles`
```
id                    (uuid, primary key)
user_id               (uuid, FK → users.id)
display_name          (text)
age                   (integer)
gender                (text)
city                  (text)
current_stage         (text) CHECK: single/finding/relationship/breakup
ai_personality        (text) CHECK: warm/direct/chill/hype
support_preference    (text) CHECK: vent/advice/mix
onboarding_complete   (boolean, default false)
language_pref         (text, default 'en')
timezone              (text, default 'Asia/Kolkata')
notification_enabled  (boolean, default true)
created_at            (timestamptz, default now())
updated_at            (timestamptz)
```

### ORDER 3: `user_psychology`
```
id                             (uuid, primary key)
user_id                        (uuid, FK → users.id)
attachment_style               (text) nullable
love_language_primary          (text) nullable
love_language_secondary        (text) nullable
communication_style            (text) nullable
readiness_score                (integer) nullable
self_improvement_scores        (jsonb) nullable
recurring_themes               (jsonb, default '[]')
known_triggers                 (jsonb, default '[]')
what_helps                     (jsonb, default '[]')
relationship_history_summary   (text) nullable
last_assessed                  (timestamptz) nullable
updated_at                     (timestamptz)
```

### ORDER 4: `partner_profiles`
```
id                        (uuid, primary key)
user_id                   (uuid, FK → users.id)
partner_name              (text)
stage_context             (text)
relationship_type         (text)
relationship_start        (date) nullable
partner_description       (text) nullable
love_language_guess       (text) nullable
communication_style_guess (text) nullable
ai_known_facts            (jsonb, default '[]')
is_active                 (boolean, default true)
created_at                (timestamptz)
updated_at                (timestamptz)
```

### ORDER 5: `conversations`
```
id                  (uuid, primary key)
user_id             (uuid, FK → users.id)
session_id          (uuid)
stage_context       (text)
chat_mode           (text)
started_at          (timestamptz, default now())
ended_at            (timestamptz) nullable
message_count       (integer, default 0)
primary_topics      (jsonb, default '[]')
crisis_occurred     (boolean, default false)
crisis_level_max    (text, default 'safe')
mood_start          (integer) nullable
mood_end            (integer) nullable
```

### ORDER 6: `messages`
```
id                  (uuid, primary key)
conversation_id     (uuid, FK → conversations.id)
user_id             (uuid, FK → users.id)
role                (text) CHECK: user/assistant
content             (text)
message_type        (text) CHECK: text/voice/image/multimodal
image_url           (text) nullable
voice_url           (text) nullable
voice_transcript    (text) nullable
emotion_detected    (text) nullable
crisis_level        (text, default 'safe')
agents_used         (jsonb, default '[]')
rag_used            (boolean, default false)
created_at          (timestamptz, default now())
```

### ORDER 7: `mood_logs`
```
id            (uuid, primary key)
user_id       (uuid, FK → users.id)
mood_score    (integer) CHECK: 1-10
pain_score    (integer) nullable CHECK: 1-10
mood_label    (text)
mood_emoji    (text)
trigger_note  (text) nullable
stage_context (text)
source        (text) CHECK: chat/checkin/manual
logged_at     (timestamptz, default now())
```

### ORDER 8: `stage1_data`
```
id                            (uuid, primary key)
user_id                       (uuid, FK → users.id)
partner_description_raw       (text) nullable
partner_analysis_result       (jsonb) nullable
expectation_realism_score     (float) nullable
refined_partner_vision        (text) nullable
readiness_assessment          (jsonb) nullable
readiness_score               (integer) nullable
improvement_plan              (jsonb) nullable
grooming_guide                (jsonb) nullable
last_updated                  (timestamptz)
```

### ORDER 9: `stage2_data`
```
id                        (uuid, primary key)
user_id                   (uuid, FK → users.id)
current_interest_name     (text) nullable
profile_review_result     (jsonb) nullable
conversation_analyses     (jsonb, default '[]')
flags_learned             (jsonb, default '[]')
date_prep_notes           (text) nullable
last_updated              (timestamptz)
```

### ORDER 10: `stage3_data`
```
id                          (uuid, primary key)
user_id                     (uuid, FK → users.id)
relationship_health_scores  (jsonb, default '[]')
problems_discussed          (jsonb, default '[]')
love_language_assessment    (jsonb) nullable
communication_issues        (jsonb, default '[]')
date_ideas_used             (jsonb, default '[]')
last_checkin                (date) nullable
last_updated                (timestamptz)
```

### ORDER 11: `stage4_data`
```
id                           (uuid, primary key)
user_id                      (uuid, FK → users.id)
breakup_date                 (date) nullable
relationship_length          (text) nullable
who_ended                    (text) nullable
current_grief_stage          (text) nullable
nc_streak_days               (integer, default 0)
nc_last_contact              (date) nullable
nc_longest_streak            (integer, default 0)
pain_score_today             (integer) nullable
sleep_score_today            (integer) nullable
appetite_score_today         (integer) nullable
movement_today                (boolean, default false)
recovery_phase                (text, default 'acute')
lessons_learned               (jsonb, default '[]')
identity_reclamations         (jsonb, default '[]')
readiness_to_love_score       (integer) nullable
last_updated                  (timestamptz)
```

### ORDER 12: `daily_checkins`
```
id                (uuid, primary key)
user_id           (uuid, FK → users.id)
checkin_date      (date)
checkin_type      (text) CHECK: morning/evening
stage_context     (text)
mood_score        (integer)
pain_score        (integer) nullable
sleep_hours       (float) nullable
sleep_quality     (integer) nullable
appetite_score    (integer) nullable
movement_done     (boolean, default false)
one_word          (text) nullable
open_text         (text) nullable
day_rating        (integer) nullable
ai_response       (text) nullable
created_at        (timestamptz, default now())
```

### ORDER 13: `tasks_challenges`
```
id                (uuid, primary key)
user_id           (uuid, FK → users.id)
task_text         (text)
task_category     (text)
task_difficulty   (text)
stage_context     (text)
assigned_date     (date)
completed         (boolean, default false)
completed_at      (timestamptz) nullable
skipped           (boolean, default false)
created_at        (timestamptz, default now())
```

### ORDER 14: `streaks`
```
id                    (uuid, primary key)
user_id               (uuid, FK → users.id)
streak_type           (text)
current_count         (integer, default 0)
longest_count         (integer, default 0)
last_activity_date    (date)
updated_at            (timestamptz)
```

### ORDER 15: `user_patterns`
```
id                  (uuid, primary key)
user_id             (uuid, FK → users.id)
pattern_type        (text)
pattern_description (text)
confidence_score    (float)
evidence_count      (integer, default 1)
first_detected      (timestamptz, default now())
last_confirmed      (timestamptz, default now())
is_active           (boolean, default true)
```

### ORDER 16: `weekly_reports`
```
id                 (uuid, primary key)
user_id            (uuid, FK → users.id)
week_start_date    (date)
week_end_date      (date)
stage_context      (text)
avg_mood_score     (float) nullable
avg_pain_score     (float) nullable
insights           (jsonb, default '[]')
patterns_found     (jsonb, default '[]')
recommendations    (jsonb, default '[]')
generated_at       (timestamptz, default now())
```

### ORDER 17: `crisis_logs`
```
id                (uuid, primary key)
user_id           (uuid, FK → users.id)
crisis_level      (text)
trigger_summary   (text)
response_type     (text)
helplines_shown   (boolean)
sos_activated     (boolean)
logged_at         (timestamptz, default now())
```

### ORDER 18: `journal_entries`
```
id                 (uuid, primary key)
user_id            (uuid, FK → users.id)
entry_date         (date)
stage_context      (text)
content            (text)
prompt_used        (text) nullable
mood_score         (integer) nullable
ai_reflection      (text) nullable
is_unsent_letter   (boolean, default false)
recipient          (text) nullable
created_at         (timestamptz, default now())
```

### Database indexes to create (speeds up queries)
```
- users.email (unique index)
- messages.conversation_id
- messages.user_id
- mood_logs.user_id + logged_at
- daily_checkins.user_id + checkin_date
- conversations.user_id
- user_patterns.user_id
```

---

## PART B — EARLIER DRAFT DATABASE SCHEMA (12 tables, from Complete App Bible) — kept for reference

```
TABLE: users
id, email, name, display_name, age, gender, location_city, current_stage
(enum: single/finding/relationship/breakup), created_at, last_active,
onboarding_complete, timezone, language_pref, notification_on

TABLE: user_profiles
id, user_id (FK), attachment_style (anxious/avoidant/secure/disorganized),
love_language (words/acts/gifts/time/touch), communication_style
(passive/aggressive/assertive), relationship_history (text summary),
known_triggers (JSON array), what_helps (JSON array),
recurring_themes (JSON array), self_described (text), readiness_score
(1-100), updated_at

TABLE: partner_profiles
id, user_id (FK), partner_name, relationship_type (dating/committed/ex),
relationship_duration, partner_description, love_language_guess,
communication_style, known_about (JSON — what AI knows about partner),
created_at, updated_at

TABLE: conversations
id, user_id, session_id, stage_context, started_at, ended_at,
message_count, primary_topic, crisis_occurred, crisis_level,
mood_at_start, mood_at_end

TABLE: messages
id, conversation_id, role (user/assistant), content, message_type
(text/voice/image/screenshot), image_url, voice_url, emotion_detected,
crisis_level, agents_used (JSON array), rag_used, created_at

TABLE: mood_logs
id, user_id, mood_score (1-10), mood_label, pain_score (Stage 4 specific),
stage_context, note (optional), logged_at, source (checkin/chat/manual)

TABLE: stage4_recovery
id, user_id, breakup_date, relationship_length, who_ended_it (me/them/mutual),
sleep_score, appetite_score, movement_done, crisis_count, nc_streak_days,
current_grief_stage, daily_pain_score, updated_at

TABLE: relationship_health
id, user_id, week_date, connection_score, communication_score, trust_score,
fun_score, appreciation_score, intimacy_score, growth_score, overall_score,
notes, ai_insights (JSON)

TABLE: challenges_tasks
id, user_id, task_text, task_category, stage_context, assigned_date,
completed, completed_at, skipped

TABLE: readiness_assessments
id, user_id, assessment_type (single/breakup), total_score,
dimension_scores (JSON), ai_feedback, recommendations (JSON), assessed_at

TABLE: patterns
id, user_id, pattern_type, pattern_detail, confidence, first_detected,
confirmed_count, active

TABLE: crisis_logs
id, user_id, crisis_level, trigger_message (encrypted), response_given,
helplines_shown, logged_at
```
*(This draft's `stage4_recovery`, `relationship_health` and `readiness_assessments` tables were folded into the canonical `stage1_data` / `stage3_data` / `stage4_data` JSON columns + `daily_checkins` + `weekly_reports` in the final schema above.)*

---

## PART C — COMPLETE API DESIGN — ALL ENDPOINTS

Two endpoint lists existed. Below is the **merged superset** — the canonical build-plan list (67 endpoints, versioned `/api/v1`) plus every endpoint unique to the earlier draft list, so nothing is missing.

### Base URL
```
https://your-api.render.com/api/v1
```
*(Earlier draft used unversioned `/api/...` — use the versioned `/api/v1/...` form when building.)*

### AUTH ENDPOINTS
```
POST   /auth/register
  Body: email, password, display_name, age
  Returns: user_id, access_token, refresh_token

POST   /auth/login
  Body: email, password
  Returns: access_token, refresh_token, user_profile

POST   /auth/google
  Body: google_token
  Returns: access_token, refresh_token, user_profile
  (earlier draft named this /auth/google-oauth)

POST   /auth/refresh
  Body: refresh_token
  Returns: new access_token

POST   /auth/logout
  Headers: Authorization Bearer token
  Returns: success message

DELETE /auth/account
  Headers: Authorization Bearer token
  Body: password (confirmation)
  Returns: success message
```

### USER ENDPOINTS
```
GET    /user/profile              → complete user profile object
PUT    /user/profile               → Body: any updatable fields → updated profile
GET    /user/stage                 → current_stage + stage_data
PUT    /user/stage                 → Body: new_stage → updated stage
GET    /user/onboarding-status     → complete/incomplete + current step
PUT    /user/onboarding             → Body: onboarding step data → next step or complete
GET    /user/psychology-profile     → attachment style, love language etc
PUT    /user/preferences            → Body: ai_personality, support_pref, notifications → updated preferences
GET    /user/onboarding             (earlier draft alias for onboarding-status)
```

### CHAT ENDPOINTS (MAIN AI)
```
POST   /chat/text
  Body: message, session_id, chat_mode
  Returns: ai_response, emotion_detected, crisis_level, quick_replies,
           action_suggested, session_id

POST   /chat/voice
  Body: audio_file (multipart), session_id
  Returns: transcript + ai_response + voice_emotion_detected

POST   /chat/image
  Body: image_file (multipart), caption, session_id, image_type
  Returns: image_analysis + ai_response

POST   /chat/screenshot
  Body: screenshot_file (multipart), context
  Returns: extracted_text + analysis + guidance

POST   /chat/multimodal   (a.k.a. /chat/multi-modal)
  Body: message + image_file, session_id
  Returns: combined_analysis + response

GET    /chat/history       Params: session_id or conversation_id → list of messages
GET    /chat/sessions      → list of all conversation sessions
DELETE /chat/session/{session_id}  → success
PUT    /chat/mode          Body: chat_mode (talk/advice/analysis) → confirmation
```

### STAGE 1 ENDPOINTS
```
POST   /stage1/partner-description
  Body: description_text or voice_url
  Returns: analysis_started, job_id

GET    /stage1/partner-analysis/{job_id}
  Returns: full analysis result (realistic/examine/reconsider + insights)

GET    /stage1/readiness-score
  Returns: current readiness score + breakdown

POST   /stage1/readiness-assessment
  Body: assessment answers (30 questions)
  Returns: score, dimension scores, guidance

GET    /stage1/improvement-plan     → full 6-area improvement plan
PUT    /stage1/improvement-progress  Body: area, progress_data → updated plan

POST   /stage1/grooming-analysis
  Body: selfie image + preferences
  Returns: face shape, style guidance

GET    /stage1/daily-task           → today's Stage 1 task
```

### STAGE 2 ENDPOINTS
```
POST   /stage2/profile-review
  Body: bio_text + profile_images[]
  Returns: score, bio rewrite, photo guidance

POST   /stage2/person-analysis
  Body: description/screenshot/photo
  Returns: personality reading, compatibility

POST   /stage2/conversation-help
  Body: conversation screenshot or text
  Returns: analysis + response suggestions

POST   /stage2/conversation-analysis  (earlier draft alias)

POST   /stage2/opening-message
  Body: their_profile_text
  Returns: 5 personalized opening messages

GET    /stage2/red-green-flags
  Params: personalized=true/false
  Returns: full flags list + user-specific

POST   /stage2/date-prep
  Body: date_details (who, where, when)
  Returns: complete date preparation guide

POST   /stage2/date-debrief
  Body: how_it_went description
  Returns: analysis + next steps

GET    /stage2/conversation-starters  Params: context, platform → personalized starters
```

### STAGE 3 ENDPOINTS
```
POST   /stage3/problem-analysis
  Body: problem description + context
  Returns: root cause + solution + scripts

POST   /stage3/communication-help
  Body: message or situation
  Returns: better version + explanation

GET    /stage3/communication-scripts   Params: situation_type → scripts for that situation

POST   /stage3/weekly-checkin
  Body: 10 question answers
  Returns: health scores + AI insights

GET    /stage3/health-dashboard    → current scores + trends
GET    /stage3/health-history      Params: weeks (4/8/12) → historical health data

POST   /stage3/love-language-assessment
  Body: assessment conversation answers
  Returns: primary + secondary languages + partner guess + action plan

GET    /stage3/date-ideas
  Params: budget, location_type, interests
  Returns: 5 personalized date ideas

GET    /stage3/communication-technique  Params: technique_name → full technique guide + examples

POST   /stage3/fight-analyzer
  Body: fight description or screenshot
  Returns: pattern + resolution guide
```

### STAGE 4 ENDPOINTS
```
POST   /stage4/breakup-intake
  Body: breakup details, how they feel
  Returns: immediate support response + first night guide

POST   /stage4/daily-checkin
  Body: sleep, pain, appetite, movement, one_word, open_text
  Returns: AI personalized response + today's healing focus

GET    /stage4/recovery-dashboard    → all recovery metrics + trends

POST   /stage4/journal-entry
  Body: content, prompt_used
  Returns: saved + AI reflection

GET    /stage4/journal-prompts       Params: recovery_week, grief_stage → 3 prompts for that stage

GET    /stage4/nc-tracker            → current streak, history, milestones

POST   /stage4/nc-checkin
  Body: urge_to_contact=true/false
  Returns: support + streak update

POST   /stage4/unsent-letter
  Body: letter content, recipient
  Returns: processing + AI response to emotion

GET    /stage4/grief-guidance        Params: current_grief_stage → what this stage is + how to move

GET    /stage4/readiness-check       → score + what still needs healing

POST   /stage4/identity-reclaim
  Body: item being reclaimed
  Returns: updated reclamation list

GET    /stage4/healing-report        Params: period (week/month) → healing progress report
```

### PROGRESS ENDPOINTS
```
GET    /progress/overview           → complete journey summary
GET    /progress/mood-graph         Params: days (7/30/90) → mood data for charting
GET    /progress/patterns           → all detected patterns
GET    /progress/weekly-report      → latest weekly report
GET    /progress/milestones         → all achieved milestones
```

### EMERGENCY ENDPOINTS
```
POST   /emergency/sos-trigger
  Body: trigger_source, current_message
  Returns: immediate response + helplines + breathing guide

GET    /emergency/resources         → all crisis resources (helplines by region + type)

POST   /emergency/log
  Body: crisis_level, what_happened
  Returns: logged + support response
```

### TASKS ENDPOINTS
```
GET    /tasks/today                 → today's tasks for current stage
POST   /tasks/complete/{task_id}    → updated streak + celebration
POST   /tasks/skip/{task_id}        → acknowledged + no penalty
GET    /tasks/history               Params: days → task completion history
```

### PATTERNS ENDPOINTS
```
GET    /patterns/mine               → all user patterns detected
GET    /patterns/weekly-insights    → AI insights from this week
GET    /patterns/report             Params: period → full pattern analysis report
GET    /patterns/user-patterns      (earlier draft alias for /patterns/mine)
```

**Endpoint totals:** Auth (6) + User (8) + Chat (9) + Stage1 (8) + Stage2 (8) + Stage3 (10) + Stage4 (12) + Progress (5) + Emergency (3) + Tasks (4) + Patterns (3) = **76 endpoints** in the fully merged list (canonical build plan's 67 plus the earlier draft's unique aliases/extras).

---

## PART D — SECURITY & PRIVACY (repeated here for the DB/API context)

- All data encrypted at rest (AES-256) and in transit (TLS 1.3)
- User can delete ALL data anytime; no data sold; no ads/tracking; GDPR compliant; data stays in India (Indian servers)
- Conversations not stored after 90 days — only patterns/scores kept long term; no human ever reads conversations; AI cannot share data with anyone; parent/partner cannot access data
- **Stored permanently:** account info, stage and progress, mood scores (not conversation content), pattern summaries (not raw conversations), assessment results
- **Deleted after 90 days:** full conversation text, uploaded images, voice recordings, screenshot analysis
- **Crisis exception:** crisis events logged for safety, never shared externally, used only to detect worsening patterns, user informed clearly

---
**⬇ Continues below: UI Design System ⬇**
-e 


