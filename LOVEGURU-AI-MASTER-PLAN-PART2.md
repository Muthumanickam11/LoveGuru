# ❤️ LOVEGURU AI — MASTER BUILD PLAN — PART 2 of 2
### Covers: Complete UI Design System, Week-by-Week 10-Week Build Plan, Testing/Deployment/Launch Plan, and Environment Variable Appendices
**⬅ Part 1 covers:** App Identity, Personas, Every Feature (all 4 stages), Full AI/LangGraph System Architecture, Database Schema + API Design.

---

# ❤️ LOVEGURU AI — COMPLETE UI DESIGN SYSTEM (COMBINED)
Merged from the "Complete App Bible + UI Design System" document (this had two color-system passes — a shorter first pass and a more complete second pass; the second, more complete pass is CANONICAL and used below; the first pass values are noted where they differ).

---

## 1. DESIGN PHILOSOPHY

**The core feeling:** *"Walking into a beautiful, warm, intimate space where you feel completely safe to be honest about love."*

**References:** luxury journal meets intimate café; candlelight warmth in digital form; premium but deeply human; emotional intelligence in every pixel.

**Five design principles:**
1. **Warmth first** — every screen should feel like a warm hug, not a cold interface.
2. **Stage personality** — each of the 4 stages has its own visual identity; the user feels the shift when the stage changes.
3. **Emotional responsiveness** — UI reacts to emotional state (sad user → darker, softer, slower; happy user → brighter, lighter, playful).
4. **Never clinical** — zero medical/clinical feel, zero corporate sterility, always intimate and personal.
5. **Every detail intentional** — no random decorations, every element serves the emotion, purpose drives every design choice.

Overall aesthetic (from the first design pass): warm, intimate, premium feel; deep burgundy and gold tones; feels like a luxury journal app, NOT a cheap dating-app look; sophisticated and trustworthy.

---

## 2. COLOR SYSTEM — CANONICAL (complete second pass)

### Backgrounds
```
Deep Dark:     #0D0609    (main app bg - warm black)
Dark Layer:    #150C10    (card backgrounds)
Dark Surface:  #1E1118    (elevated surfaces)
Dark Border:   #2A1A20    (subtle borders)
```

### Stage colors (each stage has its own identity)

**🟡 Stage 1 — Single (Golden Hope)**
```
Primary:   #D4A853  (warm gold)
Secondary: #E8C87A  (light gold)
Accent:    #F5DFA0  (cream gold)
Glow:      rgba(212,168,83,0.15)
Meaning:   New beginning, potential, self-worth
```

**🟢 Stage 2 — Finding (Fresh Green)**
```
Primary:   #4A9B7F  (sage green)
Secondary: #6BB89A  (medium green)
Accent:    #9DD4BE  (light sage)
Glow:      rgba(74,155,127,0.15)
Meaning:   Growth, hope, new connection
```

**🔵 Stage 3 — Relationship (Trust Blue)**
```
Primary:   #4A7FB5  (deep calm blue)
Secondary: #6B9FD4  (medium blue)
Accent:    #9DC0E8  (light blue)
Glow:      rgba(74,127,181,0.15)
Meaning:   Trust, depth, stability, commitment
```

**🔴 Stage 4 — Healing (Gentle Rose)**
```
Primary:   #B56B7F  (dusty rose)
Secondary: #D48A9B  (medium rose)
Accent:    #E8B4C0  (light rose)
Glow:      rgba(181,107,127,0.15)
Meaning:   Healing, compassion, self-love
```

### Universal colors
```
Text Primary:    #F5EDE8  (warm white - reads warm)
Text Secondary:  #B8A8A0  (muted warm)
Text Muted:      #7A6560  (very muted)
Success:         #7DAA7D  (sage green)
Warning:         #D4A853  (amber - same as Stage 1)
Danger:          #B56B7F  (rose - same as Stage 4)
Emergency:       #C44B4B  (clear red - only crisis)
```

### Glassmorphism style
```
glass-light:   rgba(255,240,230,0.04)
glass-medium:  rgba(255,240,230,0.07)
glass-dark:    rgba(255,240,230,0.02)
glass-border:  rgba(255,240,230,0.08)
blur-amount:   24px
```

### Gradients
```
Main Background:
linear-gradient(135deg, #0D0609 0%, #150C10 50%, #0F0A0C 100%)

Stage 1 Card Gradient:
linear-gradient(135deg, rgba(212,168,83,0.12) 0%, rgba(212,168,83,0.04) 100%)

Stage 4 Healing Gradient:
linear-gradient(135deg, rgba(181,107,127,0.15) 0%, rgba(181,107,127,0.04) 100%)

Button Gradient (Stage 1):
linear-gradient(90deg, #D4A853, #E8C87A)

Button Gradient (Stage 3):
linear-gradient(90deg, #4A7FB5, #6B9FD4)

Hero Glow Effect:
radial-gradient(circle at 50% 50%, rgba(stage-color, 0.20) 0%, transparent 70%)
```

### Earlier/shorter color pass (kept for reference — same design intent, slightly different hex values)
```
Background:   #0F0508 (deep warm black)
Card:         rgba(255,180,150,0.06)
Primary:      #C4637A (deep rose)
Gold:         #D4A853 (warm gold)
Soft:         #8B5A6B (muted rose)
Text:         #F5EDE8 (warm white)
Success:      #7DAA7D (sage green)
Calm:         #6B8FA8 (soft blue)

STAGE COLOR CODING (early pass, simplified):
Single Stage:    Gold/Yellow tones
Finding Stage:   Green/Hopeful tones
Relationship:    Blue/Calm tones
Breakup Stage:   Soft purple/healing tones
```

---

## 3. TYPOGRAPHY SYSTEM

### Font families
```
HEADING FONT: "Cormorant Garamond"
→ Elegant, romantic, premium
→ Used for: Page titles, hero text
→ Weights: 400 (regular), 600 (semibold)
→ Source: Google Fonts (free)

SUBHEADING: "Playfair Display"
→ Classic, warm, trustworthy
→ Used for: Section headers, card titles
→ Weights: 400, 700
→ Source: Google Fonts (free)

BODY FONT: "Lora"
→ Readable serif, warm and intimate
→ Used for: All AI responses, long text
→ Weights: 400, 500
→ Source: Google Fonts (free)

UI FONT: "Plus Jakarta Sans"
→ Clean, modern, readable
→ Used for: Buttons, labels, scores
→ Weights: 400, 500, 600, 700
→ Source: Google Fonts (free)
```
(An earlier note in the very first pass mentions "Inter" for UI text as an alternative — Plus Jakarta Sans is the final choice used throughout the detailed component/screen specs, so use that.)

### Type scale
```
Display:    48px / Cormorant / 400   "Your Love Story Deserves Wisdom"
H1:         36px / Cormorant / 600   Page titles
H2:         28px / Playfair / 400    Section titles
H3:         22px / Playfair / 700    Card titles, feature names
H4:         18px / Plus Jakarta / 600  Sub-sections
Body Large: 17px / Lora / 400         AI responses (larger for readability)
Body:       15px / Lora / 400         General content
Body Small: 13px / Plus Jakarta / 400 Labels, captions, metadata
Micro:      11px / Plus Jakarta / 500 Tags, badges, scores
```

### Line heights
```
Display: 1.2
Headings: 1.3
Body: 1.7 (generous for emotional content)
UI: 1.4
```

### Letter spacing
```
Display: -0.02em
Headings: -0.01em
Body: 0.01em
Caps labels: 0.08em
```

---

## 4. COMPONENT LIBRARY — COMPLETE (32 components, build order specified in file 05)

### COMPONENT 1: Glass Card
Purpose: primary container for all content. Variants: Default, Elevated, Stage-colored, Alert.
```css
/* Default Glass Card */
background: rgba(255,240,230,0.04);
border: 1px solid rgba(255,240,230,0.08);
border-radius: 20px;
backdrop-filter: blur(24px);
box-shadow: 0 4px 24px rgba(0,0,0,0.3), 0 1px 0 rgba(255,255,255,0.04) inset;
padding: 24px;

/* Stage-Colored Card (Stage 1 example) */
background: rgba(212,168,83,0.08);
border: 1px solid rgba(212,168,83,0.15);
/* + all Default properties above */

/* Hover State */
background: rgba(255,240,230,0.07);
border: 1px solid rgba(255,240,230,0.12);
transform: translateY(-2px);
transition: all 0.3s ease;
```

### COMPONENT 2: Stage Selector (Home)
Large card per stage: icon (custom designed), stage name, current status. Active stage gets: full stage color glow, slightly elevated, active indicator dot, pulse animation on dot.

### COMPONENT 3: Chat Bubbles
```css
/* USER BUBBLE */
background: stage-color gradient;
color: #FFFFFF;
border-radius: 20px 20px 4px 20px;
padding: 14px 18px;
max-width: 80%;
align: right;
font: Lora 15px;
box-shadow: 0 2px 12px rgba(stage-color, 0.3);

/* AI (GURU) BUBBLE */
background: rgba(255,240,230,0.06);
border: 1px solid rgba(255,240,230,0.10);
color: #F5EDE8;
border-radius: 20px 20px 20px 4px;
padding: 14px 18px;
max-width: 85%;
align: left;
font: Lora 17px; /* larger — AI speaks with presence */

/* CRISIS MODE BUBBLE */
background: rgba(71,107,127,0.15);
border: 1px solid rgba(71,107,127,0.25);
/* slower text reveal, larger font 18px, more padding */
```
**Typing indicator:** three-dot animation inside AI bubble style; text rotates every 3 seconds through: "Guru is reflecting...", "Guru is thinking...", "Guru understands..."

### COMPONENT 4: Score Displays
- **Circular Gauge** — SVG circle progress, stage color fill, center number large (Cormorant font), subtle pulsing when highlighted, comparison text below.
- **Bar Scores** — rounded full-width bars, left label/right score, stage color fill, smooth fill animation on load, gradient fill (darker to lighter), brief interpretation text below.
- **Overall Score Card** — large central score (60px); color changes by score (0-4 rose/warning, 5-7 neutral warm, 8-10 green/gold celebration); subtitle text based on score; trend arrow (up/down/stable).

### COMPONENT 5: Buttons
```css
/* PRIMARY BUTTON */
background: linear-gradient(stage colors);
color: #FFFFFF;
border-radius: 14px;
padding: 16px 32px;
font: Plus Jakarta 15px 600;
box-shadow: 0 4px 20px rgba(stage-color, 0.35), 0 1px 0 rgba(255,255,255,0.15) inset;
/* hover: brightness(1.1) + scale(1.02); active: scale(0.98) */

/* SECONDARY BUTTON */
background: transparent;
border: 1px solid rgba(stage-color, 0.4);
color: stage-color;
border-radius: 14px;
padding: 14px 28px;
/* hover: background rgba(stage-color, 0.10) */

/* GHOST BUTTON */
background: rgba(255,240,230,0.05);
border: 1px solid rgba(255,240,230,0.08);
color: Text Secondary;
/* hover: background rgba(255,240,230,0.10) */

/* DANGER BUTTON (SOS) */
background: linear-gradient(#B56B7F, #C44B4B);
/* pulse glow animation, larger than normal, "Get Help Now" clear text */
```

### COMPONENT 6: Input Fields
```css
/* Chat Input */
background: rgba(255,240,230,0.06);
border: 1px solid rgba(255,240,230,0.10);
border-radius: 16px;
padding: 14px 18px;
color: #F5EDE8;
font: Lora 15px;
/* placeholder color: rgba(245,237,232,0.35) */

/* Focus State */
border: 1px solid rgba(stage-color, 0.50);
background: rgba(255,240,230,0.08);
box-shadow: 0 0 0 4px rgba(stage-color, 0.12);

/* Multiline Journal Entry: same styling, min-height 120px, grows with content,
   character count shown */
```

### COMPONENT 7: Mood/Pain Slider
Track: stage-colored gradient. Thumb: large (40px) circle, stage color fill, white border, shadow. Labels: numbers 1-10 below, current value large above thumb. Emoji indicators at ends (sad/happy relevant emoji). Fill color changes based on value.

### COMPONENT 8: Progress Indicators
- **Streak Counter** — fire emoji + number, gold color for active streak, "Day X" below, milestone markers (7/14/30/60/90), celebration animation at milestones.
- **Healing Progress (Stage 4)** — vertical timeline design, milestones marked with dots (completed = filled stage-color dot, current = pulsing dot, future = empty dot), gradient line between dots.
- **Readiness Progress** — circular full-page gauge, fills as score improves, stage color changes as score improves, center shows percentage, outer ring shows dimensions.

### COMPONENTS 9–32 (full build-order list, from the component library build plan)

**Phase 1 — Base components:**
1. GlassCard — props: children, stage, variant, className; variants default/elevated/colored/alert; hover animation
2. StageButton (Primary) — props: children, stage, onClick, loading, disabled; states default/hover/active/loading/disabled
3. GhostButton — props: children, onClick, stage
4. InputField — props: label, placeholder, type, error, onChange; focus glow; error state
5. TextArea — props: label, placeholder, rows, onChange; auto-grows; character count option
6. LoadingSpinner — props: size, stage; stage-colored spinning ring
7. ToastNotification — types: success/error/info/warning; top-right; auto-dismiss

**Phase 2 — Stage components:**
8. StageSelector — props: currentStage, onChange; 4 stage cards; active glow
9. MoodSlider — props: value, onChange, label, emoji_left, emoji_right
10. ScoreGauge (Circular) — props: score, maxScore, stage, label; animated fill on mount
11. ScoreBar — props: label, score, maxScore, stage; animated fill; stage gradient
12. StreakCounter — props: count, type, milestone
13. JournalEntry — props: prompt, onSave, stage; warm journal styling; save animation

**Phase 3 — Chat components:**
14. ChatBubble (User) — props: message, timestamp, status; stage gradient bubble
15. ChatBubble (AI/Guru) — props: message, timestamp, isTyping; glass bubble; Guru indicator dot
16. TypingIndicator — 3-dot bounce; rotating text
17. ChatInput — props: onSend, onVoice, onAttach, stage; multi-part: attach/text/voice/send; expandable textarea; voice waveform
18. QuickReplies — props: replies, onSelect, stage; horizontal scroll pills
19. MessageList — props: messages, loading; virtual scrolling; date dividers; scroll-to-bottom button

**Phase 4 — Media components:**
20. ImageUploadZone — props: onUpload, accept, multiple; drag/drop; preview thumbnail; upload progress
21. VoiceRecorder — props: onComplete, onCancel, maxDuration; hold-to-record; waveform; release-to-send
22. ScreenshotAnalyzer — props: onAnalysis, stage; upload screenshot; analysis overlay; tap for annotations
23. SelfieCapture — props: onCapture, purpose; camera access; front camera default; capture + preview

**Phase 5 — Data display:**
24. MoodGraph — props: data, days, stage; smooth line chart (Recharts); stage color fill; tap for details
25. HealthRadarChart — props: scores, stage; spider chart; 6 dimensions; stage color fill
26. HealingTimeline — props: milestones, currentDay, stage; vertical timeline; milestone markers
27. WeeklyReport — props: reportData, stage; full report card; expandable sections; download option
28. PatternCard — props: pattern, evidence, stage; pattern name; evidence from conversations; insight text

**Phase 6 — Emergency components:**
29. SOSButton — props: onActivate, stage; always visible; subtle but clear; Stage 4 more prominent
30. BreathingExercise — props: onComplete, cycles; animated expanding circle; text instruction; cycle counter
31. HelplineCard — props: name, number, hours, type; call button (tel: link); availability info
32. CrisisScreen — full-screen takeover; breathing + helplines; calm dark blue background; gentle animations only

---

## 5. ANIMATION SYSTEM — COMPLETE

**Animation philosophy:** every animation serves emotional purpose; never gratuitous or distracting; slow enough to feel intentional; speed matches emotional weight; crisis mode has no playful animations.

### CSS `@keyframes` library
```
1.  fadeIn            opacity 0 → 1
2.  fadeInUp           opacity 0 + translateY(20px) → normal
3.  fadeInDown         from above
4.  slideInRight       from right edge
5.  slideInLeft        from left edge
6.  scaleIn            scale(0.9) → scale(1)
7.  pulse              scale 1 → 1.05 → 1 (continuous)
8.  breathing          scale grows and shrinks slowly
9.  float              subtle up-down movement
10. shimmer            loading skeleton effect
11. ripple             button tap effect
12. glow               box-shadow pulses
13. typewriter         character by character reveal
14. countUp            number animates from 0
15. particleFloat      particles drift upward
16. streakPop          streak number celebration
17. milestoneExplosion milestone reached
```

### Framer Motion variants (separate `motionVariants.js` file)
```
pageVariants          page enter/exit animations
cardVariants           card appear animations
listItemVariants       staggered list items
modalVariants          modal open/close
chatBubbleVariants     message appear
emergencyVariants      crisis screen transition
```

### Animation library details

**1. Page transitions**
- Normal navigation: fade + slide up, 300ms, `cubic-bezier(0.4, 0, 0.2, 1)`
- Stage change transition: color wash across screen, new stage color bleeds in, 600ms — a dramatic, meaningful moment

**2. Background ambient**
- Floating particles: very subtle, slow, stage color tint, 8-12 particles visible, random movement paths, opacity 0.15-0.30, size 4-12px circles
- Stage 4 particles: softer, slower, more spread out, feels like rain or petals falling (healing visual)

**3. Glow effects**
- Card hover glow: radial glow expands from cursor, stage color, 40% opacity max, smooth follow
- Hero element glow: constant pulsing glow, 4-second cycle, stage color, very subtle

**4. Message animations**
- User message sent: slides in from right, slight bounce at end, 250ms
- AI message appears: typing indicator first, then message fades in word by word (typewriter effect for important messages), duration matches reading pace

**5. Score animations**
- Gauge fill: smooth arc draw, ease-out, 1200ms, slight overshoot then settle
- Bar fill: left to right fill, stagger 100ms between bars, 800ms each
- Number count-up: 0 to final number, ease-out, 1000ms

**6. Stage 4 specific**
- Breathing circle: expanding/contracting, 4s expand / 4s hold / 4s contract, rose color, used in crisis support screen
- Healing particles: gentle upward float, flower petal or star shapes, appear after check-in completion ("release" visual metaphor)
- NC streak: each new day = small celebration; 7 days = confetti moment; 30 days = full celebration screen; numbers animate when updated

**7. Emergency SOS animations**
When SOS activates: screen dims to dark blue, all other UI fades, breathing circle appears center, slow calm pulse rhythm, text appears gently, no sudden movements, everything peaceful and slow.

---

## 6. EVERY SCREEN DESIGN — COMPLETE (all 11 screen groups, 45+ screens total)

### SCREEN 1: Splash / Loading
- Background: deep dark `#0D0609`
- Center: app logo (elegant rose + AI symbol combined — stylized heart formed by two conversation bubbles, one slightly larger, subtle AI circuit line inside, stage-gradient gold-to-rose color)
- Tagline: "Your AI Guru For Every Stage of Love" (Cormorant Garamond 24px)
- Loading: logo pulses gently, tagline fades in after logo, no loading bar (feels clinical), just ambient glow growing
- Transition to next screen: logo rises and shrinks to top bar, main content fades up below, smooth 800ms

### SCREEN 2: Landing Page (not logged in)

**Section 1 — Hero (full screen height)**
- Background: deep dark base, subtle floating particles (gold + rose mix), very subtle noise texture overlay, radial glow center (multi-color stage colors)
- Top: logo + "LoveGuru AI"
- Center: display text (Cormorant 52px) "Every stage of love, finally understood"; subtitle (Lora 18px muted) "From finding yourself to finding them, through the joy of love and the pain of loss—your AI guru walks every step with you"
- Two buttons: "Begin Your Journey" (primary, gold), "See How It Works" (ghost)
- Animated preview: small phone mockup showing the app, chat bubbles appearing naturally, stage colors cycling through all 4

**Section 2 — Four Stages Visual**
- "One App. Every Chapter of Love." — four large cards in 2x2 grid:
  - Card 1 SINGLE (gold theme, single-star icon): "Understand yourself / Define what you truly need / Become ready for real love"
  - Card 2 FINDING (green theme, two-approaching-figures icon): "Navigate dating with clarity / Spot what's real vs what's not / Build connections that last"
  - Card 3 RELATIONSHIP (blue theme, connected-hearts icon): "Communicate deeply / Resolve conflict with wisdom / Keep love alive and growing"
  - Card 4 HEALING (rose theme, single-figure+gentle-light icon): "Process grief without judgment / Heal your mind and body / Rise stronger and wiser"

**Section 3 — How It Works** — three steps: "Share where you are" (text/voice/image) → "AI understands deeply" (backed by relationship psychology research) → "Get wisdom that actually helps" (real guidance, not generic advice)

**Section 4 — Testimonial style** — not real testimonials (new app), instead example conversations shown: Stage 1 expectation reality check, Stage 3 communication script, Stage 4 heartbreak support

**Section 5 — CTA** — "Your love story deserves wisdom"; large primary button "Start Free →"; small text "Private. Safe. Always here."

### SCREEN 3: Onboarding Flow
Design language: one screen at a time, no form feel (pure conversation), progress dots top right, back arrow top left, subtle skip option top right.

**3A — Greeting**
Time-based large warm greeting ("Good evening ✦"). Guru avatar (large, center, abstract face shape, warm amber glow, gentle breathing animation). AI types out slowly: *"I'm Guru, your AI companion for everything love-related. Before we begin, I want to know where you are right now in your love journey. No judgment here - just honesty."*
Selection: [I'm Single] [Dating Someone] [In Relationship] [Just Broke Up] [It's Complicated]

**3B — Deeper question** (branches by 3A answer)
- If "Just Broke Up": "I'm sorry you're going through that. How recent was this?" → [Last few days] [Last few weeks] [Last month] [A few months ago]
- If "I'm Single": "How long have you been single?" → then "What are you hoping for?"
- Each answer leads to a personalized next question.

**3C — What they need**
"What would feel most helpful right now?" — icon cards: [💬 Someone to talk to] [🔍 Understanding myself better] [💡 Practical advice and guidance] [🌱 Working on myself] [❤️ Help with a specific problem]

**3D — Communication style**
"How do you like to receive support?" — four cards with live example previews of the SAME message in each style: [😊 Warm and gentle] [💯 Direct and honest] [😄 Light with some humor] [🔄 Mix it up based on mood]. Preview shown: "Here's how I'd say the same thing in each style" — example text changes based on selection so the user sees what they're choosing.

**3E — Name + setup**
"What should I call you?" — single glowing text input, large/prominent. Privacy promise (short, honest): "Everything you share stays between us. Private, encrypted, never shared." → [Begin My Journey →] full gradient button, stage color, subtle celebration animation on press.

**Later, more detailed onboarding pass (7-screen version, from End-to-End Build Plan) — same flow, more granular:**
- **OB-1 Welcome + Greeting** — logo animates in, "Hello, I'm Guru" types out, brief app description, "Let's begin" button. No data collected.
- **OB-2 Life Stage Selection** — "Where are you in your love journey?" 5 option cards: [I'm Single] [Dating Someone] [In Relationship] [Just Broke Up] [It's Complicated], each with icon + brief description, tap highlights in stage color. Data: `current_stage`.
- **OB-3A If Single** — "How long have you been single?" [Recently] [Few months] [Over a year] [Always been single]; then "What are you hoping for?" [Find my person] [Understand myself better] [Learn about healthy love] [Not sure yet]. Data: `single_duration, goal`.
- **OB-3B If Just Broke Up** — "I'm sorry you're going through this. How recent was this?" [Last few days] [Last few weeks] [Last month+] [Few months ago]; then "How are you feeling right now?" [In a lot of pain] [Processing it] [Starting to feel okay] [Mixed feelings]. Data: `breakup_recency, emotional_state`.
- **OB-3C If In Relationship** — "How long have you been together?" [New (<6mo)] [6-12 months] [1-3 years] [3+ years]; then "What brings you here today?" [Want to improve communication] [We've been having issues] [Want to keep love alive] [General learning]. Data: `relationship_duration, purpose`.
- **OB-4 What help looks like** — "What would feel most helpful?" multi-select cards [💬 Someone to talk to about this] [🔍 Understanding myself in love] [💡 Practical advice and guidance] [❤️ Help with specific problems] [🌱 Growing and healing]. Data: `help_preferences`.
- **OB-5 Guru personality** — "How do you like support?" 4 preview cards each showing the same example message in a different style (Warm & Gentle / Direct & Honest / Light & Easy / Mix It Up), with live preview text. Data: `ai_personality`.
- **OB-6 Name + privacy** — "What should I call you?" single input, no last name; privacy promise bullets (private/encrypted, no sharing, delete anytime, parents/partners cannot access); [Let's Begin →] gradient button.
- **OB-7 First message from Guru** — transitions into chat screen; Guru sends a fully personalized first message based on all prior answers (different opener for breakup / single / relationship paths).
- **After onboarding:** all data saved to DB, stage set in profile, first task generated, home screen loads, optional skippable welcome tour overlay.

### SCREEN 4: Home Screen (Main Hub)
**Header** — logo small (left), [🔔] [👤] icons (right).

**Hero card (full width, stage-colored glassmorphism, large gradient border):**
- Top: stage label pill ("● HEALING JOURNEY" example) — stage color dot + text
- Large time-based greeting (Cormorant 32px) "Good evening, [Name]"
- AI-generated daily subtext (Lora 16px, muted), e.g. "Day 18 of your healing journey. You're doing better than you think."
- Stage-specific element: Stage 1 → readiness ring gauge; Stage 2 → "active conversation" indicator; Stage 3 → relationship health mini-score; Stage 4 → days healing counter + pain score

**Quick actions (3 equal horizontal cards):**
[💬 Chat with Guru] (always primary) + stage-specific action (Stage 1: [📊 Check Readiness], Stage 2: [💡 Get Advice], Stage 3: [❤️ Weekly Check-in], Stage 4: [📔 Journal Today]) + [📈 See Progress]

**Today's Focus section:**
- "Today's Wisdom" card — daily insight from AI, stage-appropriate, changes daily, from RAG knowledge base (e.g. Stage 1: "Healthy expectations include reasonable compromise, not perfection"; Stage 4: "Grief is not a sign of weakness. It's the price of having loved.")
- "Today's Task" card — one micro-task appropriate to stage, [Complete ✓] [Skip] buttons, streak counter shown

**SOS button:** always visible on all screens, small but clear, bottom center, "Need Support Now?" text; Stage 4 has it more prominent/larger; tap → Emergency/crisis support.

**Bottom navigation:** [🏠 Home] [💬 Guru] [📊 Journey] [👤 Me] — active state shows stage color dot above icon, inactive is muted icon only, tab bar has subtle blur background.

### SCREEN 5: Chat Interface (core screen)
**Header:** back arrow, center "Guru ✦" (always the AI's name), right [•••] menu (clear chat, export, settings). Below header: stage color thin line (3px) as a visual reminder of which stage.

**Mode selector:** horizontal scrollable pills [💬 Just Talk] [💡 Get Advice] [👁 Analysis] [🔴 Crisis] — selected = filled pill stage color, unselected = ghost outline.

**Chat area:** full-screen scroll, main dark background, subtle ambient particles. Date dividers (center, muted text: "Today" / "Yesterday" / "Monday, Jan 15", thin lines each side).

**User messages:** right aligned, stage gradient bubble, white text Lora 15px, timestamp below (muted), read indicator.
**AI (Guru) messages:** left aligned, glass bubble warm border, warm white text Lora 17px, Guru avatar dot (6px stage color) left of bubble, timestamp below. Long AI messages reveal progressively (typewriter, not instant dump).

**Special bubble types:**
- Analysis Card Bubble — structured analysis as a mini-card inside the bubble, expandable sections, score displays, stage-colored headers
- Action Suggestion Bubble — task description + [Do This Now] / [Maybe Later] buttons; completing in-chat updates streak
- Image Analysis Response — bubble shows [image thumbnail] "I see..." then analysis below

**Crisis mode:** background shifts to calm blue-dark, all animations slow down, font slightly larger, AI bubble border softer, breathing guide appears as sticky card, SOS button becomes full-width top.

**Chat input area (bottom fixed, blur background):**
- Row 1: quick reply chips (if any) — small horizontal scroll, tap to send instantly
- Row 2: main input [📎 attach] [input field] [🎤 voice] [→ send]
- Attach options: photo from gallery, take photo now, screenshot from camera roll
- Voice recording: hold mic button, waveform animation, release to send, cancel by sliding left
- Send button: stage color arrow icon; disabled (gray) when empty, enabled (stage color glow) when has content
- Typing state: input expands to multiline naturally, character count appears at 400+ chars, line count shown

**3AM mode** (activates 12am–5am automatically): slightly warmer color temp, notifications silenced (no interruption), softer animations, moon icon in header, AI tone auto-adjusts.

### SCREEN 6: Stage 1 Screens

**Partner Vision screen** (gold theme)
- Header: "Your Partner Vision ✦"
- Section: "Describe Your Dream Partner" — large open journal-style text area, placeholder "Paint me a picture... What kind of person do you see yourself building a life with? Don't filter yourself." Character count. [Analyze My Vision →] gold button. Voice option below ("Or tell me out loud", gold mic button).
- **Analysis Results screen** (after AI processes) — animated reveal, section by section:
  - Healthy Expectations (green check icon, list + why-it's-healthy note)
  - Worth Examining (amber icon, each item shows what user said → what's underneath → healthier version)
  - High Expectations (gentle amber alert, compassionate framing, what it reveals, why it may limit, what they truly need)
  - What This Reveals (deep insight card, gold bordered warm bg, "Your list suggests...")
  - Overall Score (circular gauge, gold, "Expectation Realism: 6.8/10" + interpretation)
  - Refined Vision Card ("Your Revised Partner Vision", AI's healthier version, [Save This Vision] button)

**Self Improvement screen**
6 expandable sections (accordion): icon + title, your score in this area, expanded detail guidance, task for this area, progress tracker. Overall readiness gauge at top (fills as areas improve, gold).

**Readiness Score screen**
Full-page assessment result: large circular gauge center, gold fill, number large (Cormorant 72px) "/100" smaller. Six dimension breakdown gauges/bars below with label + brief note. Score interpretation card (color-coded, specific text for score range). Action card: "Your Next Focus Area" — most impactful thing to work on, [Start Working On This →].

### SCREEN 7: Stage 2 Screens

**Finding Love Home** (green theme)
Header card: "Your Search ✦", "Tell me about someone you've met" or "Ready to attract the right person?" Options: [💬 Talk about someone specific] [📸 Share their profile/chat screenshot] [💡 Get conversation help] [🚩 Learn what to watch for]

**Red/Green Flags screen**
Two columns Red | Green, switch toggle at top [🟢 Green Flags] [🔴 Red Flags]. Each flag: icon + name + brief explanation, tap for deep explanation, save/bookmark option, "I've seen this" marker. Personalized section: "Based on your history:" — flags specifically relevant to the user, gold border on personalized cards.

**Conversation Analyzer screen**
User pastes or screenshots conversation. Split view — left: original conversation, right: AI annotations. Annotation markers: 🟢 connection moment, 🔴 concern, 💡 missed opportunity, 💬 better response option. Tap annotation for full explanation. Overall assessment card below (interest level / connection quality score + next step suggestion).

### SCREEN 8: Stage 3 Screens

**Relationship Home** (blue calm theme)
Health dashboard card at top — mini radar/spider chart, 6 dimensions, blue fill, overall score + trend. "How are you two doing this week?" quick 1-10 slider (updates weekly score). Recent issues section — scroll of past problems discussed, tap any to revisit + see guidance.

**Problem Solver screen** (blue theme)
"What's going on?" large open text area, voice option prominent. OR common problem templates: [Communication issues] [Feeling disconnected] [Trust concerns] [Different needs] [External stress] [Lost the spark] — selecting a template pre-fills questions for faster access to common problems.

**Problem Analysis Result:**
- Diagnostic card — problem type identified, root cause explanation, blue information icon
- Solution cards (expandable): (1) what you can do NOW (2) conversation to have (3) script — exact words to say (4) long-term approach (5) when it's resolved
- Script display — special formatting, different background (slightly lighter), quotation marks visual design, copy button, "Practice with Guru" option (AI role-plays the conversation)

**Relationship Health Weekly screen** (blue theme)
10 questions one at a time, each with appropriate input (sliders for scores, yes/no for simple questions, text for open questions). Progress dots at top. On completion: brief animation, scores calculated, dashboard updated; Weekly Insights card appears (AI written, personalized — what changed from last week, what to focus on, one specific suggestion).

### SCREEN 9: Stage 4 Screens (warmest, softest theme of all — rose/healing)

**Healing Home**
Top card, soft and warm: "Day [X] of your healing" (not bold, not celebrating — too harsh early), gentle acknowledgment. Pain score for today: 1-10 large emoji scale, "How heavy does it feel today?"
- Section 1 "Right Now": [💬 I need to talk] [😮‍💨 Help me breathe] [📔 Write it down] [🆘 I need help now]
- Section 2 "Your Recovery": sleep score bar (from check-in), appetite indicator, movement today (○/✓), NC streak "Day X without contact"
- Section 3 "Today's Healing": one guided exercise, changes daily (early days: breathing/grounding; later days: journaling/reflection/action)

**Daily Check-in screen (morning or evening version)**
5 gentle questions: "How did you sleep?" (star 1-5), "Pain level today?" (slider 1-10), "Did you eat at least once?" (Y/N), "Did you move your body?" (Y/N), "One word for how you feel" (text input). After each: brief AI validation ("6 hours - your brain is trying to heal"; "Pain of 7 today - that's hard. Here's what helps"). Completion screen: gentle celebration (not too enthusiastic), soft healing particles animation, AI personal message based on answers, today's suggested focus (one thing).

**No-Contact Support screen**
"I want to text them" large compassionate card → "Tell me what you want to say to them" big open text area → send to AI instead (AI receives and processes it, helps understand the feeling behind it). "What do you need right now?" options: [Someone to hear me] [Help resisting the urge] [Understand why I feel this] [Know if reaching out is right].
NC Streak Tracker: large number "23 Days" rose color prominent, "Without contact" below smaller, progress ring around number, milestone markers 7/14/30/60/90. Milestone reached → full-screen gentle celebration, soft confetti (rose + gold petals), personal AI message ("23 days. That took real strength.").

**Identity Rebuilding screen**
"Reclaiming You" title. Phase indicators shown as gentle path: [Excavation] → [Rebuilding] → [Becoming], current phase highlighted. Reclamation List — items built with AI, each with what it is / why it matters / status (Not Started / In Progress / Reclaimed ✓). Progress visual: timeline of the journey, key moments marked, milestones celebrated, "Who I was" → "Who I'm becoming".

**SOS / Crisis Support screen**
Activates when: SOS button pressed, crisis detected in chat, or very low pain score.
Full-screen takeover: background deep calm blue `#0A1520`, very dark, very calm, no distracting elements.
Center: breathing circle (250px), soft rose glow, animates expand (4s) → hold (4s) → contract (4s), text inside changes "Breathe in..." / "Hold..." / "Breathe out...", cycle count below "Round 1 of 5".
Above circle: "I'm right here with you." (Lora 22px, very soft, no bold, no exclamation).
Below circle: "You don't have to be okay right now." (soft, centered).
Helpline cards (after breathing, or skip option):
```
[📞 iCall - Free, Confidential
    9152987821
    Mon-Sat 8am-10pm
    Call Now →]

[📞 Vandrevala Foundation
    1860-2662-345
    Available 24/7, Free
    Call Now →]

[💬 Keep talking to Guru →]
```
Always visible: "It's okay to ask for help. That's strength, not weakness."

### SCREEN 10: Progress / Journey
Header "Your Journey ✦", timeline selector: stage tabs [1] [2] [3] [4] at top.
- **Stage 1 journey view** — readiness score over time (warm gold line graph, current score prominent); self improvement radar chart (6 dimensions, fills over time, current vs first assessment)
- **Stage 4 journey view** — pain score over time (line chart, trending downward = healing; if trending up → AI gentle check-in); physical health bars (Sleep/Appetite/Movement, week by week); NC streak history (calendar view, color coded by NC status, milestone stars); healing milestones reached (scrollable list, "Day 7: First day you smiled genuinely", "Day 14: Ate a full meal", "Day 30: NC streak achieved")
- **Insights tab** — AI generated weekly insights, patterns AI has noticed, personalized/specific ("Your worst days correlate with...", "You've stopped using the phrase '___'"). All stages: pattern discoveries written in warm, personal language.

### SCREEN 11: Profile / Settings
Header: profile (name + stage badge).
- **Your Story** — what AI knows about you (editable/confirmable): attachment style detected, love language identified, communication style
- **Preferences** — AI personality style (change anytime), notification settings, time zone, language, 3AM mode settings
- **Stage Management** — current stage shown, change stage button, history of stage changes
- **Privacy** — data you've shared (summary), delete specific data, delete all data, download your data, what is/isn't stored
- **Account** — email, change password, subscription (future), delete account
- **Helplines always accessible** — pinned section, iCall + Vandrevala always visible, "You don't have to be in crisis to use these"

---

## 7. MOBILE DESIGN RULES

**Layout rules:**
```
Maximum content width: 390px (iPhone 14)
Side padding: 20px always
Card gap: 16px
Section gap: 32px
Safe area: Always respected (notch/home)
```

**Touch targets:**
```
Minimum tap target: 48x48px
All buttons: at least 52px height
Bottom nav items: 64px height
Adequate spacing between taps
```

**Thumb zone optimization:**
- Primary actions: bottom 60% of screen
- Never critical action at very top
- Chat input: always at bottom
- SOS button: bottom, always reachable

**Scroll behavior:** momentum scrolling; pull to refresh where relevant; infinite scroll for chat history; snap scrolling for stage cards.

**Keyboard behavior:** screen adjusts when keyboard opens; chat input stays visible; content scrolls but input doesn't disappear; keyboard dismisses on tap outside input.

**Haptic feedback:**
```
Button taps:              Light impact
Mode selection:            Selection haptic
Achievement/milestone:     Success pattern
SOS activation:            None (calm)
Message sent:              Soft impact
Slider movement:           Selection haptic
```

**Dark mode:** app is dark mode first; light mode option (softer version), same stage colors (slightly adjusted); never pure white background in light mode — uses warm cream `#FAF5F0` instead.

---
**⬇ Continues below: Week-by-Week Build Plan ⬇**
-e 


# ❤️ LOVEGURU AI — WEEK-BY-WEEK BUILD PLAN (COMBINED, CANONICAL)

Two build calendars existed across the source docs — a short 10-week overview (in "Complete App Bible") and a fully detailed day-by-day 10-week plan (in "End-to-End Build Plan"). The **detailed day-by-day plan is canonical** and used below in full. The short overview's week groupings are folded in as milestone summaries at the top of each week so nothing is lost.

## MASTER BUILD OVERVIEW
```
Total Build Time:     10 Weeks
Total Screens:        45+ Screens
Total AI Agents:      12 Agents
Total API Endpoints:  67-76 Endpoints (see file 03)
Total DB Tables:      18 Tables
RAG Collections:      5 Collections
Input Types:          Text + Image + Voice
Stages Covered:       4 Complete Stages
```

## WEEK-BY-WEEK MASTER CALENDAR
```
WEEK 1  → Project Foundation + Setup
WEEK 2  → Database + API Structure
WEEK 3  → UI Design System + Screens
WEEK 4  → Authentication + Onboarding
WEEK 5  → AI Core + LangGraph Setup
WEEK 6  → RAG Pipeline + Knowledge Base
WEEK 7  → Stage 1 + Stage 2 Complete
WEEK 8  → Stage 3 + Stage 4 Complete
WEEK 9  → Image + Voice AI Pipeline
WEEK 10 → Testing + Deploy + Launch
```

*(Short-overview alternate framing of the same 10 weeks, kept for reference: Week1-2 Foundation → Week3-4 Stage1 Complete → Week5-6 Stage3 Complete → Week7-8 Stage4 Complete → Week9 Stage2+RAG → Week10 Polish+Deploy. The detailed day-by-day plan below is the one to actually follow.)*

---

# WEEK 1: PROJECT FOUNDATION

## Day 1-2: Environment Setup

**Computer setup:**
- Node.js 20+, Python 3.11+, Git, VS Code
- VS Code extensions: ES7+ React Snippets, Python extension, Tailwind CSS IntelliSense, Prettier, GitLens

**Free accounts to create:**
1. GitHub (store code)
2. Groq (groq.com — free LLM)
3. Google AI Studio (Gemini — free)
4. Supabase (free database)
5. Upstash (free Redis)
6. Vercel (free frontend host)
7. Render (free backend host)

**Collect all free API keys** (save in secure notepad):
```
GROQ_API_KEY            (from groq.com)
GEMINI_API_KEY          (from aistudio.google.com)
SUPABASE_URL            (from supabase dashboard)
SUPABASE_ANON_KEY       (from supabase)
SUPABASE_SERVICE_KEY    (from supabase)
UPSTASH_REDIS_URL       (from upstash)
UPSTASH_REDIS_TOKEN     (from upstash)
```

**Local tools to install:**
```
Ollama (ollama.ai - free, local AI)
  After install run: ollama pull llama3.1
                      ollama pull mistral

ChromaDB
  pip install chromadb

Whisper (free voice AI)
  pip install openai-whisper
```

## Day 3-4: Project Structure Creation

Create this exact folder structure:

```
loveguru-ai/
│
├── frontend/                    ← React App
│   ├── public/
│   │   ├── favicon.ico
│   │   ├── logo.svg
│   │   └── index.html
│   │
│   ├── src/
│   │   ├── assets/
│   │   │   ├── fonts/           ← Downloaded Google fonts
│   │   │   ├── images/          ← App images
│   │   │   └── icons/           ← SVG icons
│   │   │
│   │   ├── components/          ← Reusable pieces
│   │   │   ├── common/          ← Used everywhere
│   │   │   ├── chat/            ← Chat specific
│   │   │   ├── stage1/          ← Single stage
│   │   │   ├── stage2/          ← Finding love
│   │   │   ├── stage3/          ← Relationship
│   │   │   ├── stage4/          ← Healing
│   │   │   ├── dashboard/       ← Progress screens
│   │   │   └── emergency/       ← SOS system
│   │   │
│   │   ├── pages/               ← Full screens
│   │   │   ├── Landing.jsx
│   │   │   ├── Onboarding.jsx
│   │   │   ├── Home.jsx
│   │   │   ├── Chat.jsx
│   │   │   ├── Stage1.jsx
│   │   │   ├── Stage2.jsx
│   │   │   ├── Stage3.jsx
│   │   │   ├── Stage4.jsx
│   │   │   ├── Progress.jsx
│   │   │   ├── Profile.jsx
│   │   │   └── Emergency.jsx
│   │   │
│   │   ├── store/               ← State management
│   │   │   ├── authStore.js
│   │   │   ├── chatStore.js
│   │   │   ├── stageStore.js
│   │   │   ├── moodStore.js
│   │   │   └── uiStore.js
│   │   │
│   │   ├── api/                 ← API calls
│   │   │   ├── axiosConfig.js
│   │   │   ├── authApi.js
│   │   │   ├── chatApi.js
│   │   │   ├── stage1Api.js
│   │   │   ├── stage2Api.js
│   │   │   ├── stage3Api.js
│   │   │   ├── stage4Api.js
│   │   │   └── emergencyApi.js
│   │   │
│   │   ├── hooks/               ← Custom React hooks
│   │   │   ├── useChat.js
│   │   │   ├── useAuth.js
│   │   │   ├── useStage.js
│   │   │   ├── useVoice.js
│   │   │   └── useEmergency.js
│   │   │
│   │   ├── styles/              ← CSS files
│   │   │   ├── globals.css
│   │   │   ├── variables.css    ← CSS variables
│   │   │   ├── animations.css
│   │   │   ├── glassmorphism.css
│   │   │   └── stages.css       ← Stage themes
│   │   │
│   │   ├── utils/               ← Helper functions
│   │   │   ├── stageColors.js
│   │   │   ├── timeHelpers.js
│   │   │   ├── formatters.js
│   │   │   └── constants.js
│   │   │
│   │   ├── router/
│   │   │   └── AppRouter.jsx
│   │   │
│   │   └── App.jsx
│   │
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── .env
│
├── backend/                     ← FastAPI App
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── intake_agent.py
│   │   ├── emotion_agent.py
│   │   ├── crisis_agent.py
│   │   ├── stage_router_agent.py
│   │   ├── partner_analysis_agent.py
│   │   ├── relationship_counselor_agent.py
│   │   ├── heartbreak_coach_agent.py
│   │   ├── physical_health_agent.py
│   │   ├── rag_agent.py
│   │   ├── response_builder_agent.py
│   │   ├── personalizer_agent.py
│   │   └── memory_agent.py
│   │
│   ├── graph/
│   │   ├── __init__.py
│   │   ├── main_graph.py        ← Master LangGraph
│   │   ├── graph_state.py       ← State TypedDict
│   │   ├── stage1_graph.py      ← Stage 1 subgraph
│   │   ├── stage2_graph.py
│   │   ├── stage3_graph.py
│   │   └── stage4_graph.py
│   │
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── document_loader.py
│   │   ├── text_splitter.py
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   └── rag_pipeline.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth_router.py
│   │   ├── chat_router.py
│   │   ├── stage1_router.py
│   │   ├── stage2_router.py
│   │   ├── stage3_router.py
│   │   ├── stage4_router.py
│   │   ├── progress_router.py
│   │   └── emergency_router.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── chat_service.py
│   │   ├── stage1_service.py
│   │   ├── stage2_service.py
│   │   ├── stage3_service.py
│   │   ├── stage4_service.py
│   │   ├── image_service.py
│   │   ├── voice_service.py
│   │   ├── pattern_service.py
│   │   └── emergency_service.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── database_models.py   ← SQLAlchemy models
│   │   └── schemas.py           ← Pydantic schemas
│   │
│   ├── memory/
│   │   ├── __init__.py
│   │   ├── session_memory.py    ← Redis memory
│   │   ├── user_memory.py       ← PostgreSQL memory
│   │   └── pattern_memory.py    ← Pattern tracking
│   │
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── image_analyzer.py    ← Gemini Vision
│   │   ├── voice_processor.py   ← Whisper
│   │   ├── screenshot_reader.py ← OCR + analysis
│   │   └── crisis_resources.py  ← Helpline data
│   │
│   ├── prompts/
│   │   ├── __init__.py
│   │   ├── intake_prompts.py
│   │   ├── stage1_prompts.py
│   │   ├── stage2_prompts.py
│   │   ├── stage3_prompts.py
│   │   ├── stage4_prompts.py
│   │   ├── crisis_prompts.py
│   │   └── personalizer_prompts.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py          ← All env variables
│   │   ├── database.py          ← DB connection
│   │   └── llm_config.py        ← LLM setup
│   │
│   ├── middleware/
│   │   ├── auth_middleware.py
│   │   ├── rate_limiter.py
│   │   └── crisis_logger.py
│   │
│   ├── data/
│   │   ├── psychology_docs/     ← RAG source PDFs
│   │   ├── relationship_docs/
│   │   ├── heartbreak_docs/
│   │   ├── self_dev_docs/
│   │   └── crisis_docs/
│   │
│   ├── chroma_db/                ← Vector store data
│   │
│   ├── main.py                  ← FastAPI entry
│   ├── requirements.txt
│   └── .env
│
├── docker-compose.yml            ← Local dev setup
├── README.md
└── .gitignore
```

## Day 5-7: Package Installation Plan

### FRONTEND PACKAGES (install in order)
```bash
# CORE
npm create vite@latest frontend -- --template react
cd frontend
npm install

# STATE & ROUTING
npm install zustand
npm install react-router-dom

# STYLING
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
npm install framer-motion
npm install clsx

# API & FORMS
npm install axios
npm install react-hook-form
npm install zod

# CHARTS & VISUALS
npm install recharts
npm install react-circular-progressbar

# MEDIA
npm install react-mic
npm install @ffmpeg/ffmpeg

# UI UTILITIES
npm install react-hot-toast
npm install react-intersection-observer
npm install date-fns
```

### BACKEND PACKAGES (`requirements.txt`)
```
# CORE
fastapi==0.104.1
uvicorn==0.24.0
python-dotenv==1.0.0
pydantic==2.5.0
pydantic-settings==2.1.0

# AI & LANGCHAIN
langchain==0.1.0
langgraph==0.0.40
langchain-groq==0.0.3
langchain-google-genai==0.0.6
langchain-community==0.0.10
langchain-core==0.1.10

# RAG
chromadb==0.4.18
sentence-transformers==2.2.2
PyMuPDF==1.23.7
pypdf==3.17.1

# VOICE
openai-whisper==20231117
torch==2.1.0
torchaudio==2.1.0

# IMAGE
Pillow==10.1.0
python-multipart==0.0.6

# DATABASE
sqlalchemy==2.0.23
asyncpg==0.29.0
alembic==1.13.0
supabase==2.3.0

# CACHE
redis==5.0.1
upstash-redis==0.15.0

# SECURITY
python-jose==3.3.0
passlib==1.7.4
bcrypt==4.1.2

# UTILITIES
httpx==0.25.2
aiofiles==23.2.1
python-dateutil==2.8.2
```

**Week 1 milestones:**
```
□ All accounts created, all API keys saved
□ Both projects created (React + FastAPI)
□ Complete folder structure created
□ All packages installed (no errors)
□ Frontend runs: npm run dev
□ Backend runs: uvicorn main:app
```

---

# WEEK 2: DATABASE + API STRUCTURE

## Day 1-2: Database Complete Setup

**Supabase setup steps:**
1. Go to supabase.com, create new project, note project URL and keys
2. Go to SQL Editor
3. Create all 18 tables in the exact order given in `03-DATABASE-API-DESIGN.md` (foreign keys depend on order): `users → user_profiles → user_psychology → partner_profiles → conversations → messages → mood_logs → stage1_data → stage2_data → stage3_data → stage4_data → daily_checkins → tasks_challenges → streaks → user_patterns → weekly_reports → crisis_logs → journal_entries`
4. Create the indexes listed in file 03 (`users.email` unique, `messages.conversation_id`, `messages.user_id`, `mood_logs.user_id + logged_at`, `daily_checkins.user_id + checkin_date`, `conversations.user_id`, `user_patterns.user_id`)

## Day 3-5: API Endpoint Planning
Build out all endpoints from `03-DATABASE-API-DESIGN.md` (Auth 6, User 8/9, Chat 9, Stage1 8, Stage2 8/9, Stage3 10, Stage4 12, Progress 5, Emergency 3, Tasks 4, Patterns 3/4). Base URL: `https://your-api.render.com/api/v1`.

## Day 6-7: Environment Configuration
See Appendix A and Appendix B at the end of this document for the exact variables to set up here.

**Week 2 milestones:**
```
□ All 18 database tables created in Supabase
□ Can connect to database from FastAPI
□ All API endpoints defined (not all working yet)
□ Basic auth: register and login works
□ JWT token generated and validated
```

---

# WEEK 3: UI DESIGN SYSTEM

## Day 1-2: Design System Foundation

**CSS variables to set up (in `variables.css`):**
- All background shades
- All stage color sets (4 stages × 4 shades) — see file 04
- All text colors
- All glass effects
- All gradient definitions

**Spacing scale:** `4px, 8px, 12px, 16px, 20px, 24px, 32px, 40px, 48px, 64px, 80px, 96px`

**Border radius:** `4px (tiny), 8px (small), 12px (medium), 16px (large), 20px (xlarge), 50% (round)`

**Shadows:** `card-shadow` (light cards), `elevated-shadow` (floating elements), `button-shadow` (CTA buttons), `stage-glow-1` through `stage-glow-4`

**Transitions:** `fast: 150ms ease`, `medium: 300ms ease`, `slow: 500ms ease`, `very-slow: 800ms ease`

**Z-index layers:** `base: 0, card: 10, dropdown: 100, modal: 1000, overlay: 2000, emergency: 9999`

## Day 3-5: Component Library Build Plan
Build all 32 components in the 6 phases exactly as listed in `04-UI-DESIGN-SYSTEM.md` Section 4 (Phase 1 base components → Phase 6 emergency components).

## Day 6-7: Animation System
Create all 17 CSS `@keyframes` animations and all 6 Framer Motion variant groups exactly as listed in `04-UI-DESIGN-SYSTEM.md` Section 5.

**Week 3 milestones:**
```
□ Design system CSS complete
□ All CSS variables defined
□ 10+ base components built
□ Landing page looks exactly as designed
□ Stage colors working correctly
□ Animations defined
```

---

# WEEK 4: AUTHENTICATION + ONBOARDING

## Day 1-2: Authentication System

**Registration flow:** user fills email+password+name → frontend validates (Zod) → `POST /auth/register` → backend hashes password (bcrypt) → user created in Supabase → user profile created → access+refresh tokens generated → tokens stored in localStorage → redirect to onboarding.

**Login flow:** email+password → `POST /auth/login` → backend finds user, compares password hash → tokens generated+returned → user profile fetched → Zustand store populated → redirect to home or onboarding.

**Google login flow:** Google OAuth popup → user approves → Google token received frontend → `POST /auth/google` with token → backend verifies with Google → create/find user → return our JWT tokens.

**Token refresh flow:** API call fails 401 → Axios interceptor catches → `POST /auth/refresh` → new access token → original request retried → if refresh fails, logout.

**Logout flow:** `POST /auth/logout` → server-side token invalidation → clear localStorage → clear Zustand store → redirect to landing.

**Protected routes system:** `ProtectedRoute` component wraps pages, checks token exists, validates not expired; invalid → redirect to login; valid → render page.

**Auth store (Zustand):**
```
State: user {id, email, name, stage}, isAuthenticated, isLoading, tokens {access, refresh}
Actions: login(userData, tokens), logout(), updateUser(updates), refreshToken()
```

## Day 3-7: Onboarding Flow
Build the full 7-screen conversational onboarding (OB-1 through OB-7) exactly as detailed in `04-UI-DESIGN-SYSTEM.md` Screen 3, including all branching by life-stage answer, the Guru-personality live-preview cards, and the personalized first message sent after onboarding completes. After onboarding: all data saved to database, stage set in profile, first task generated, home screen loads, optional skippable welcome tour overlay.

**Week 4 milestones:**
```
□ Registration works end to end
□ Login works end to end
□ Token refresh works
□ All 7 onboarding screens complete
□ Onboarding data saves to database
□ Redirects to home correctly
```

---

# WEEK 5: AI CORE + LANGGRAPH SETUP

## Day 1-2: LLM Configuration Plan
Set up the 3-tier LLM hierarchy exactly as in `02-AI-SYSTEM-ARCHITECTURE.md` Section 10: Primary Groq (`llama-3.1-70b-versatile`, streaming True, timeout 30s) → Secondary Gemini Flash (`gemini-1.5-flash`, streaming False) → Tertiary Ollama local (`llama3.1` 8B / `mistral` 7B). Implement the fallback chain logic (Groq → Gemini → Ollama → error message). Enable streaming for chat responses only; analysis outputs are returned complete and revealed with UI animation instead.

## Day 3-7: LangGraph Complete Setup Plan
Build the full 12-node graph exactly as specified in `02-AI-SYSTEM-ARCHITECTURE.md` Section 8:
- Build the Graph State object with all fields (core info, user context, analysis results, safety data, RAG data, agent outputs, final output)
- Implement Node 1 (Input Processor) through Node 12 (Pattern Analyzer), including the Node 3A Emergency Handler branch
- Wire the conditional routing: Crisis Safety (Node 3) always runs first; EMERGENCY branches to 3A and skips everything else; otherwise flows through Stage Router (5) → the correct Stage Specialist (6A-6D) → RAG Retriever (7) → Image Analyzer (8, conditional) → Response Builder (9) → Personalizer (10) → Memory Updater (11); Pattern Analyzer (12) runs weekly via a separate scheduled job, not per-message.
- Apply the exact LLM settings table (model/temperature/max tokens) per agent from file 02, Section 10.

**Week 5 milestones:**
```
□ Groq API connected and responding
□ Basic LangGraph graph runs without error
□ Crisis detection works (test with keywords)
□ First end-to-end chat message works
□ Response streams to frontend
□ Basic stage routing works
```

---

# WEEK 6: RAG PIPELINE + KNOWLEDGE BASE

## Day 1-3: Document Collection Plan

**Collection 1 — Attachment Theory:** "Attached" by Amir Levine (summary/concepts), John Bowlby attachment research (public), Mary Ainsworth adult attachment studies, "Attachment in Adults" research papers, anxious/avoidant/secure descriptions, attachment healing techniques. Sources: Google Scholar, ResearchGate, PubMed, open-access psychology journals. Extract: attachment style definitions, behavior patterns per style, relationship patterns per style, healing approaches, communication differences.

**Collection 2 — Relationship Science:** Gottman Institute public resources, "The Seven Principles" concepts, Four Horsemen research, emotional bids research, love languages explanations (Chapman), communication research papers, trust building research. Sources: gottman.com/research, Google Scholar, Psychology Today, APA public resources.

**Collection 3 — Dating & Attraction:** compatibility research papers, first impression psychology, attraction science research, red flag psychology research, healthy relationship formation, dating psychology guides. Sources: Psychology Today, Google Scholar, Science of Relationships website, university psych department blogs.

**Collection 4 — Heartbreak & Grief:** heartbreak neuroscience studies, grief stage research (Kübler-Ross adapted), recovery timeline research, physical effects of heartbreak, no-contact healing research, post-breakup identity research, rumination and recovery studies. Sources: PubMed, Google Scholar, ResearchGate.

**Collection 5 — Self Development:** self-compassion research (Kristin Neff), self-compassion.org (free resources), confidence building research, emotional regulation techniques, CBT self-help materials (public), mindfulness and relationships, identity and relationships research. Sources: self-compassion.org, APA psychology help, Mind.org.uk, Psychology Today.

**Supplementary — Crisis Resources:** WHO mental health guidelines, safe messaging guidelines (AFSP), crisis intervention best practices, helpline information (India specific), grief crisis resources.

**Volume target:** 10-20 docs per collection, 5-30 pages each, ~1000-2000 total pages, ~5000-10000 chunks after chunking, ~2-4 hours processing time.

## Day 4-7: RAG Pipeline Setup Plan

**Step 1 — Document Loading:** PyMuPDF for PDFs, BeautifulSoup for web content, built-in Python for text files. Load page by page, extract text, preserve section headings, skip images/tables/figures, handle multi-column layouts, store raw text per document.

**Step 2 — Text Cleaning:** remove page numbers, headers/footers, fix broken hyphenations at line ends, normalize multiple spaces, remove non-unicode characters, preserve paragraph structure, tag each paragraph with source info.

**Step 3 — Text Chunking (Recursive Character Text Splitter):**
```
Chunk size: 500 tokens
Overlap: 50 tokens (continuity)

Split priority order:
1. Double newline (paragraph)
2. Single newline
3. Period + space
4. Comma + space
5. Space
6. Character
```
Why: 500 tokens = enough context, 50-token overlap = no lost context at edges, paragraph splits = natural meaning boundaries.

**Step 4 — Metadata Tagging** (per chunk):
```json
{
  "source": "gottman_seven_principles.pdf",
  "collection": "relationship_science",
  "topic_tags": ["communication", "listening", "bids"],
  "technique": "active_listening",
  "stage_relevant": ["stage3"],
  "difficulty": "beginner",
  "crisis_appropriate": false,
  "suitable_modes": ["advice", "analysis"],
  "page_number": 47,
  "chunk_id": "uuid",
  "date_added": "2024-01-15"
}
```

**Step 5 — Embedding Creation:** model `sentence-transformers/all-MiniLM-L6-v2` (~90MB, runs fully locally, free forever, 384-dimensional vectors, ~100ms/chunk). Batch 32 chunks at a time with a progress bar; ~30 minutes total.

**Step 6 — ChromaDB Storage:** 5 separate collections (`attachment_theory`, `relationship_science`, `dating_attraction`, `heartbreak_grief`, `self_development`), each storing chunk text + embedding vector + metadata + unique chunk ID. Persist to `./chroma_db`, loads on backend startup, no reprocessing needed after first run.

**Step 7 — Retrieval Setup:** build a smart query (not the raw message) with context terms, embed with MiniLM, cosine similarity search in the relevant ChromaDB collection, top 10 → filter score < 0.65 out → filter by metadata (crisis_appropriate, suitable_modes, stage_relevant) → final top 3 chunks returned with text/source/score/technique/metadata.

**Step 8 — Context Injection:**
```
---RESEARCH CONTEXT---
Source: Gottman relationship research
Technique: Active Listening / Emotional Bids
Relevance: 0.89
[Chunk text here - verbatim from document]
---END CONTEXT---
```
Agent instruction: use this research to inform the response but translate to warm casual language, never cite sources directly to the user, apply the knowledge naturally.

**Week 6 milestones:**
```
□ All documents collected (5 collections)
□ ChromaDB set up locally
□ All documents embedded and stored
□ RAG retrieval returns relevant results
□ RAG integrated into mental health agent
□ Test: query returns correct research chunk
```

---

# WEEK 7: STAGE 1 + STAGE 2 BUILD

## Day 1-3: Stage 1 Complete Build Plan

**Partner Vision feature**
- Frontend flow: open Stage 1 from home → gold-themed Stage 1 home → tap "Describe Your Partner Vision" → full-page journal-style input → prompt "Paint me a picture..." → free typing (or voice) → [Analyze My Vision] → loading "Guru is reflecting on this..." → animated section-by-section results reveal
- Backend flow: `POST /stage1/partner-description` → chat service triggered → LangGraph runs with stage1 routing → Partner Analysis Agent activated → RAG searches `attachment_theory` collection → analysis generated → Personalizer applies tone → result structured into `healthy_expectations[]`, `examine_these[]`, `reconsider_these[]`, `what_this_reveals` (text), `realism_score` (float), `refined_vision` (text) → saved to `stage1_data` table → returned to frontend
- UI result display: section-by-section animated reveal (500ms delay stagger), icons per category, expandable deep-dive per item, bottom "Revised Partner Vision" card + [Save This Vision] button

**Readiness Assessment feature**
- 30 questions across 6 dimensions, one question per screen, swipe or next-button navigation, clear percentage progress
- Question types: 1-10 slider, yes/no toggle, multiple choice (one), multiple choice (multi), brief text
- After each dimension: mini result shown (dimension score + brief insight)
- Final screen: overall score (large circular gauge), all 6 dimension scores (bars), AI interpretation paragraph, personalized action plan, "What to focus on first" card

**Self Improvement 6-area plan**
- Area cards on main Stage 1 screen, each expandable
- Emotional Intelligence: 5 chat-style assessment questions → score generated → personalized improvement plan → daily practice suggestions → progress tracked
- Communication: style quiz (passive/aggressive/assertive detection) → specific exercises → script practice with AI
- Grooming & Style: optional selfie upload, budget selection, lifestyle type → specific guidance generated → saved as reference document
- Confidence & Mindset: self-worth assessment, rejection sensitivity check → daily affirmation system, confidence exercises
- Social Skills: conversation skill assessment → specific practice scenarios, mock conversations with AI, body language guide
- Lifestyle Quality: life areas assessment → balance check, goal suggestions, why-this-matters-for-love framing

**Grooming guide detail:** based on gender + budget + lifestyle + selfie. Selfie flow: image uploaded → `POST /stage1/grooming-analysis` → Gemini Vision analyzes (face shape detection, skin observation, current style assessment, specific improvements) → budget filter applied → complete guide generated with sections: Face Shape & Hair, Skincare Routine, Grooming Essentials, Style & Clothing, Scent & Hygiene, Body Language, Priority changes list (top 3).

## Day 4-7: Stage 2 Complete Build Plan

**Dating Profile Review**
- User flow: paste bio → upload 1-5 profile photos → select platform → [Review My Profile] → AI analyzes all content → results screen with scores → 3 rewritten bio versions → photo guidance per image → photo order recommendation
- Backend: text analysis agent, image analysis per photo (Gemini Vision), platform-specific advice, complete rewrite generated
- Result display: overall profile score, bio analysis (what works/doesn't), bio rewrite (3 style options), photo scores (each rated), which photo to use first, which to remove

**Specific Person Analysis**
- User shares via chat conversation (AI asks clarifying questions) OR screenshot share (profile / chat / photo of them)
- AI builds picture: personality reading, communication style, interest indicators, compatibility with user, green flags present, red flags to watch, suggested conversation approaches
- Display: chat-integrated (feels like discussion), summary card at end, save to "People I'm Considering" list

**Conversation Coach — three modes**
- Opening Message Help: user pastes/describes their target profile → AI generates 5 personalized openers with explanation why each works → user picks favorite
- Ongoing Help: user pastes conversation screenshot → screenshot analyzed for patterns → overall assessment, "what to say next" options (3), interest level reading, warning signs noticed
- Mock Practice: user describes the person → AI plays that person in a real simulated conversation → feedback after each exchange

**Red/Green Flag Education**
- Part 1 (education first): all flags organized by category (early dating, getting serious, commitment stage), manipulation tactics explained (love bombing, breadcrumbing, future faking, hot and cold, gaslighting, trauma bonding) — each with name, description, real-life example, healthy-version contrast, what to do if you see it
- Part 2 (personalized): based on user's relationship history, AI identifies specific vulnerabilities, custom warning list, specific things to watch for given their patterns

**Date Prep System**
- Step 1 — date details (who/where/when/how much time)
- Step 2 — AI generates complete guide: BEFORE section (what to wear, grooming checklist, time management, pre-date mindset exercises), CONVERSATION section (10 date-appropriate questions, topics to bring up, topics to avoid, how to show interest, listening tips), SITUATION guides (awkward silence, splitting bill, clear attraction next step, graceful exit if not feeling it), AFTER section (follow-up text template, 24hr timeline, how to suggest date 2, signs date went well/not)
- Date Debrief: after the date, user tells AI how it went → structured questions → full debrief analysis → should-they-see-them-again recommendation → specific next steps

**Week 7 milestones:**
```
□ Stage 1: Partner vision → analysis works
□ Stage 1: Readiness assessment complete
□ Stage 1: Grooming selfie analysis works
□ Stage 2: Profile review feature works
□ Stage 2: Screenshot analysis works
□ Stage 2: Date prep complete
```

---

# WEEK 8: STAGE 3 + STAGE 4 BUILD

## Day 1-3: Stage 3 Complete Build Plan

**Relationship Problem Solver**
- Access: "I need to talk about something" button, OR open chat in Stage 3 context, OR tap a common-problem template
- Chat-based intake: Round 1 what happened → Round 2 when does this happen → Round 3 how do you respond → Round 4 what have you tried → Round 5 what do you truly need
- AI investigation approach: never takes just one side, always asks about the partner's perspective, looks for patterns not just the single event, identifies underlying needs
- Root cause result: type identified (of the 6 types), explanation why, both people's roles, what's really happening
- Solution generation: immediate action today, conversation to have, exact script, long-term approach
- Script display: special visual styling, prominent quotation marks, copy button, "Practice with Guru" option (AI plays partner, user practices, AI gives feedback: "That was much better because...")

**Communication Coach**
Six skill sections, each with: what it is and why it matters, wrong vs right examples, example scenarios, practice exercise, track your practice.
1. Gentle Startup — harsh vs soft examples, formula provided, user submits harsh version → AI rewrites gentle, explains every change
2. I Feel Statements — formula "I feel X when Y because Z, would you Z?", 10 practice scenarios, AI corrects/improves
3. Active Listening (EAVE) — Echo/Acknowledge/Validate/Explore, partner message examples, user practices EAVE responses
4. Repair Attempts — 5 types, when to use each, scripts, practice scenarios
5. Fair Fighting Rules — 8 rules explained, why each matters, what happens when broken, commitment-to-rules feature
6. Real Apology — 4-part formula, wrong-apology examples, user submits their apology, AI evaluates and improves it

**Love Language System**
- Discovery conversation (not a quiz) — 10 conversation questions, AI listens and identifies patterns
- Partner language detection — AI asks about partner behavior, identifies partner's likely language
- Results display: your language (large visual), partner guess (secondary display), mismatch analysis if languages differ, bridge plan (exactly how to bridge the gap)
- Action plan per combination: all 25 possible combinations covered, each with specific guidance, scripts for speaking each language, daily habits for each language

**Relationship Health Weekly**
- Triggered by gentle weekly notification OR user taps weekly check-in
- 10 questions, different UI per type (sliders/yes-no with follow-up/text/emoji), one at a time, can't skip (gentle push), save progress (can return)
- Completion: 7 health scores calculated, radar chart visualization, trend from last week, one main insight, one specific suggestion, "Talk about it" button opens chat
- Alert system: any score drops 2+ points → alert; 3 consecutive weeks low → stronger prompt ("I noticed your fun score has been dropping - want to talk about it?")

**Keeping Love Alive**
- Date ideas generator: input budget + location + season + mood → output 5 date ideas + why they work
- Daily habit system: 6 daily micro-habits listed, user marks done each day, streak tracking, which habits lead to which outcomes
- Long-term project ideas: learning something new together, building something together, shared bucket list creation, future planning conversation guides
- Appreciation practice: daily specific appreciation prompts ("Tell them something you noticed today"), prompted via notification, tracked

## Day 4-7: Stage 4 Complete Build Plan

**Immediate Heartbreak Support** (highest priority Stage 4 feature — must be perfect, user is most vulnerable)
- UI shifts immediately on Stage 4 entry: rose/healing color theme, softer animations, slower background particles, everything more gentle
- First message from Guru personalized by: how recent (hours vs weeks), who ended it, length of relationship
- Hour 1-24 protocol: pure listening mode, no advice initially, just validation and presence, gentle safety check ("Are you safe right now?"), if any crisis indicators → SOS activates
- Immediate practical list: text one person right now, drink something warm, don't make big decisions today, don't text them back yet, tonight survival guide, tomorrow check-in scheduled

**Daily Check-in System (Stage 4)**
- Morning: sleep (star rating), pain level (slider 1-10), ate something (Y/N), how do you feel (emoji), one word for today (text, optional). AI responds to each answer specifically.
- Evening: did you survive today (yes is enough), rate today 1-10, one okay moment (text), sleep plan for tonight. AI celebrates survival: "You got through another day. That's not nothing. That's everything."

**Grief Stage Navigation**
How AI determines current stage: analyzes recent messages, analyzes checkin answers, asks directly "What are you feeling most?"
- Denial (hope/planning-return language) → validate the hope gently, never crush it harshly, hold gentle reality, "What did they actually say?", focus on self-care not outcome
- Anger (blame/fairness-rage language) → welcome the anger ("this anger makes sense"), give it space, channel it constructively, move toward understanding
- Bargaining ("what if"/"if only"/change-promises) → validate pain beneath bargaining, distinguish growth from desperation, reality check on realistic outcomes, "What would you tell a friend?"
- Depression (hopeless/no-future language) → highest care level, crisis monitoring elevated, physical health focused, "The dark always lifts. Always.", small next steps only, professional support suggested
- Acceptance (future-thinking, "I'll be okay") → celebrate this arrival, don't rush it, acknowledge it may come and go, gently introduce growth questions

**No-Contact Support System**
- NC Tracker screen: large "Day X" number, progress ring, milestone markers 7/14/30/60/90, last milestone achieved, next milestone countdown
- Contact urge flow: "I want to text them" → "Tell me what you want to say here instead" → user types message to ex → AI receives it, helps process the feeling, asks "What do you need right now?"
- Before any contact decision: AI walks through realistic scenarios (positive response / no response / negative response) and what each would do to healing
- Social media urge: AI acknowledges the pull, explains the neuroscience (dopamine hit), asks "What are you hoping to find?" / "What will you feel after?", offers alternative activity
- Milestone celebrations: 7 days ("One week. You chose yourself every day."), 14 days ("Two weeks. The hardest stretch is passing."), 30 days (full celebration screen + confetti)

**Physical Health Recovery**
- Sleep: Week 1 permission to sleep whenever + science explained + guided breathing audio if can't sleep / gentle coaxing if too much sleep; Week 2+ consistent wake time target, blue light guidance, evening ritual building, nightly quality tracking
- Eating: Week 1 "anything you can manage is fine" + science explained + easy no-cook foods list + hydration focus; Week 2+ simple recipe suggestions, blood sugar/mood connection, one real meal/day goal, grocery list for healing foods
- Movement: Week 1 just walk outside 10-15 min (sunlight = natural mood medicine, movement releases grief from the body); Week 2-3 whatever they used to enjoy, return to gym if applicable, yoga/stretching; Month 2+ regular routine building, exercise-as-medicine education, strength-building framing
- All tracked in daily check-in: sleep hours/quality, meals eaten, movement done, all shown in recovery dashboard

**Identity Rebuilding System**
- Phase 1 Excavation (Weeks 1-3): AI asks what they loved before, what they gave up, who they drifted from, what dreams paused, what parts of themselves they hid/suppressed. Reclamation list built together, visual list grows, status tracked (Not Started/In Progress/Reclaimed ✓)
- Phase 2 Rebuilding (Weeks 3-8): Week 3 one thing reclaimed, Week 4 one old connection, Week 5 one new experience, Week 6 one new routine. Progress visual: vertical journey line, milestones marked, growing sense of self.
- Phase 3 Becoming (Month 2+): values clarification questions ("Who do I want to be?", "What matters most to me?", "What relationship do I want next?", "Who am I at my best?"). Identity document compiled over months: what you reclaimed, what you discovered, values list, non-negotiables, who you're becoming.

**Unsent Letter Therapy**
- "Write a letter" in Stage 4 — user writes to ex (or anyone), will never be sent, pure emotional processing
- After writing, AI asks: "What was hardest to write?", "What do you wish they knew?", "What do you need from writing this?", "What are you ready to release?"
- AI validates what was expressed, helps find what the user truly needed, offers reflection insight
- Saved privately; user can reread letters over time; AI reads across letters for patterns ("Your letters show you've moved from anger toward grief - that's progress")

**Week 8 milestones:**
```
□ Stage 3: Problem solver end to end
□ Stage 3: Communication scripts work
□ Stage 3: Weekly health tracking works
□ Stage 4: Breakup intake response quality ✓
□ Stage 4: NC tracker works
□ Stage 4: Daily checkin complete
```

---

# WEEK 9: IMAGE + VOICE AI PIPELINE

## Day 1-3: Image Pipeline Build Plan

**Type 1 — Selfie Analysis**
- Frontend: tap "Analyze My Look" → camera (front default) or gallery → upload progress → "Guru is analyzing..." loading
- Backend: image received (multipart) → compressed to max 1MB → stored in Supabase Storage → URL saved to DB → sent to Gemini Vision
- Gemini Vision prompt covers: approximate face shape, general skin appearance, current style/grooming level, outfit if visible, overall presentation score, specific improvement suggestions
- Budget filter applied (very low → drugstore, low → affordable brands, medium → mid-range, good → premium)
- Output structure:
```json
{
  "face_shape": "oval",
  "face_shape_hairstyles": ["..."],
  "skin_observation": "...",
  "skincare_suggestions": ["..."],
  "current_style": "casual",
  "style_improvements": ["..."],
  "outfit_feedback": "...",
  "top_3_changes": ["..."],
  "presentation_score": 7.2,
  "what_you_do_well": ["..."]
}
```
- Frontend display: results in sections with icons, face-shape diagram visual, photo-comparison style layout, priority changes prominent

**Type 2 — Partner Photo Analysis**
- Frontend: chat interface, user attaches photo with message ("Can you tell me what you see here?"), thumbnail shows in chat, AI processes and responds in chat
- Backend: image type = `partner_photo`, Gemini Vision analyzes body language reading, facial expression (genuine vs forced smile), context, physical presentation, energy/vibe; if couple photo — body proximity, facing direction, comfort level
- Safety rules: never negative about appearance, never character judgments, always note "limited to one photo", focus on observable signals only
- Response in chat: natural language not a list, gentle/observational not conclusive, always asks for more context

**Type 3 — Screenshot Chat Analysis**
- Frontend: user uploads screenshot in chat ("Can you read this and help?"), loading "Guru is reading this...", analysis appears in chat
- Backend: screenshot type detected → Gemini Vision extracts all text → organizes into `{user_side: [...], other_side: [...], timestamps: [...], platform: detected}` → 5-point analysis agent runs (communication balance, emotional bids, tone detection, red flag patterns, interest level reading — see file 02 for full detail)
- Response format: chat message with structured analysis, positive observations first, concerns framed helpfully, specific suggestion for next message

**Type 4 — Dating Profile Screenshot**
- Stage 2 specific: "Share Their Profile" button OR upload in chat → analysis card appears
- Backend: Gemini extracts profile text + photo descriptions → profile analysis covers bio personality read, photo quality/vibe, red flags in content, green flags in content, topics they care about, predicted communication style, compatibility reading, conversation starter suggestions, questions to ask them

**Type 5 — Memory/Emotional Photos (Stage 4)**
- Frontend: user shares photo in Stage 4 chat with emotional context ("I found this old photo...")
- Backend: detected as emotional/memory photo → crisis check runs first (ALWAYS) → Gemini reads photo context → emotional support mode activated
- AI approach: focus on user's emotion not the photo, ask about memories it brings, help process the feeling, don't analyze the person in photo, support the grief this represents
- Response: starts with emotion acknowledgment, then invites sharing, helps process, never dismisses the pain

## Day 4-7: Voice Pipeline Build Plan

**Step 1 — Audio Recording (Frontend)**
- Library: `react-mic` or MediaRecorder API
- Recording UI: hold mic button to record, animated waveform during recording, release to send, swipe left to cancel, max duration 2 minutes, format WebM or WAV
- Recording indicator: red pulsing dot, duration counter, waveform animation, "Release to send" text
- After recording: brief preview playback, "Send" or "Re-record" options, confirm → upload begins

**Step 2 — Audio Processing (Backend)**
- Route: `POST /chat/voice`, audio file received, converted to WAV if not already (FFmpeg)

**Step 3 — Whisper Transcription**
- Model: `medium` (best accuracy), language auto-detect (handles Hinglish), task: transcribe
- Extracts: full text transcription, language detected, word-level timestamps, confidence scores per segment, segments array
- Special handling: crying voice (tries harder, may be less accurate, note added), very quiet voice amplified before processing, multiple speakers noted to user

**Step 4 — Voice Emotion Analysis** (full detail in file 02, Section 6 Step 3) — speech rate, pitch, volume, pause patterns → combined voice emotion output object.

**Step 5 — Fusion with Text**
- Combine transcribed text + voice emotion signals + context from user history
- If text and voice conflict, voice emotion takes priority (e.g. text says "I'm fine" but voice is crying/slow/quiet → AI responds to what the voice says)

**Step 6 — Rest of pipeline**
Merged signal enters LangGraph — same pipeline as text from here: crisis check on voice+text combined, stage routing on content, specialist agent responds, personalizer adjusts for the emotional state detected in the voice.

**Week 9 milestones:**
```
□ Selfie upload → face shape → grooming guide
□ Partner photo → body language reading
□ Screenshot → text extracted → analyzed
□ Voice record → Whisper transcribes
□ Voice emotion detected
□ Multi-modal (text+image) works together
```

---
**⬇ Continues below: Testing, Deployment & Launch ⬇**
-e 


# ❤️ LOVEGURU AI — TESTING + DEPLOYMENT + LAUNCH (COMBINED, CANONICAL)

# WEEK 10: TESTING + DEPLOY + LAUNCH

## Day 1-3: Complete Testing Plan

### LEVEL 1: Unit Testing
What to test: each API endpoint with valid data, each API endpoint with invalid data, each agent with various inputs, RAG retrieval accuracy, crisis detection accuracy, image analysis outputs, voice transcription quality, authentication flow, token refresh mechanism, database operations.

Tools: Pytest (backend), FastAPI TestClient (API testing), Vitest (frontend), React Testing Library (components).

### LEVEL 2: Integration Testing — test complete flows

- **Flow 1 — New User Complete Onboarding:** Register → Onboarding → Home. Verify database created correctly, stage set correctly, first message appropriate.
- **Flow 2 — Stage 1 Complete Journey:** Describe partner → analysis received. Assessment completed → score saved. Improvement plan → task created. Grooming advice → saved to profile.
- **Flow 3 — Stage 3 Problem Solving:** Problem described in chat → investigation questions asked → root cause identified → solution + script provided → practice mode works.
- **Flow 4 — Stage 4 Crisis Support:** Breakup described → correct emotional response. Daily checkin works. NC tracker updates. Crisis detection works.
- **Flow 5 — Image Analysis:** Selfie uploaded → analysis correct. Screenshot uploaded → text extracted. Partner photo → appropriate response. Red flag image → warning given correctly.
- **Flow 6 — Voice Message:** Record audio → upload works. Transcription accurate. Voice emotion detected. AI responds to voice not just text.

### LEVEL 3: Safety Testing — MOST IMPORTANT TEST CATEGORY

**Test 1 — Direct emergency keywords:** send messages with emergency keywords → verify EMERGENCY level detected → verify SOS screen triggered → verify helplines shown.

**Test 2 — Context-dependent language:**
```
"I want to kill this exam"          → SAFE
"I want to kill myself"             → EMERGENCY
"I'm dying of embarrassment"        → SAFE
"I feel like I'm dying inside"      → DANGER
```

**Test 3 — Escalation pattern:** multiple messages, each more distressed → verify level escalates correctly → verify appropriate level responses.

**Test 4 — Stage 4 elevated sensitivity:** same message in Stage 3 vs Stage 4 → Stage 4 should detect higher risk → verify elevated monitoring works.

**Test 5 — 3AM elevated sensitivity:** same message at 2pm vs 3AM → 3AM should be more careful → verify time-based elevation.

**Test 6 — False positive acceptable:** showing SOS when not needed = okay; NOT showing SOS when needed = NOT okay; verify bias toward caution.

**All Safety Tests Must Pass 100% — no exceptions.**

### LEVEL 4: User Experience Testing (with real people — friends/family)

- **Scenario 1 — Single person:** complete onboarding as single → describe partner vision → get analysis → does it feel accurate and helpful?
- **Scenario 2 — In-relationship problem:** describe a real relationship issue → get problem analysis → does the solution feel applicable? does the script feel natural?
- **Scenario 3 — Heartbreak support:** describe a breakup scenario → does AI feel supportive? does it feel like a friend or a robot? would they actually use this in pain?

Feedback to collect: does AI feel warm or clinical? does it feel like it understands? would you use this in a real situation? what feels off or wrong? what is most helpful? rate experience 1-10.

### LEVEL 5: Performance Testing

**Response time targets:**
```
Text response:      under 3 seconds
Image analysis:      under 8 seconds
Voice processing:    under 10 seconds
Page load:            under 2 seconds
Dashboard:            under 1 second
```

**Load testing:** simulate 10 simultaneous users → verify no degradation → check memory usage → check API rate limits not hit.

**Mobile performance:** test on actual Android device, test on actual iPhone, slow internet connection test, images load optimized, animations smooth (60fps).

---

## Day 4-5: Deployment Plan

### STEP 1: Prepare backend for deployment
Before deploying: remove all debug print statements, set `DEBUG=False` in settings, verify all `.env` variables documented, create complete `requirements.txt`, test locally with production settings, ensure database migrations ready.

**Render.com deployment:**
1. Push backend to GitHub
2. Create account on render.com
3. New Web Service → connect GitHub repository → select backend folder
4. Build command: `pip install -r requirements.txt`
5. Start command: `uvicorn main:app --host 0.0.0.0`
6. Add all environment variables (see Appendix A at the end of this document)
7. Select free tier (512MB RAM)
8. Deploy

**Free tier limitation handling:** Render free tier sleeps after 15 min idle → set up Uptime Robot (free) to ping every 10 min to keep it awake → first request after sleep will be slow (expected) → tell users "Loading, please wait..." during that window.

### STEP 2: ChromaDB on Render
ChromaDB runs inside FastAPI on Render; data persists to disk. Issue: Render free tier has ephemeral storage. Solution options:
- Option A: use Render persistent disk ($0 on free tier, limited)
- Option B: process documents on startup (run ingestion on first deploy)
- Option C: use Chroma Cloud (has a free tier)
- **Recommended:** process on startup + save to Supabase storage

### STEP 3: Prepare frontend for deployment
Before deploying: update `.env` with production API URL, remove all `console.log` statements, test production build locally (`npm run build`), check `dist/` output, test with `npm run preview`.

**Vercel deployment:**
1. Push frontend to GitHub
2. Create account on vercel.com
3. Import Git repository
4. Framework preset: Vite
5. Root directory: `frontend/`
6. Build command: `npm run build`
7. Output directory: `dist`
8. Add environment variables (see Appendix B at the end of this document)
9. Deploy

Custom domain (optional): Vercel provides a free `yourapp.vercel.app` subdomain; a custom domain can be added later.

### STEP 4: Database setup in production
Supabase (already cloud): run all SQL migrations in the Supabase editor, verify all 18 tables created, test connection from Render backend, set up Row Level Security (RLS) for safety.

Redis (Upstash): already a cloud service — copy connection details to Render env vars, test connection.

### STEP 5: File storage setup
Supabase Storage: create bucket `loveguru-files`, set public access for images (or signed URLs), folder structure:
```
/avatars/{user_id}/
/chat-images/{user_id}/{timestamp}/
/voice-messages/{user_id}/{timestamp}/
/analysis-cache/{user_id}/
```

### STEP 6: Environment variables
On Render (backend): add EVERY variable from `.env`, double-check no typos, test each API key works.
On Vercel (frontend): add `VITE_API_BASE_URL` = Render URL, add any other frontend vars.

### STEP 7: Domain + SSL
Both Vercel and Render provide free SSL certificates (HTTPS) with automatic renewal — no setup needed, just works on deploy.

### STEP 8: Test production
After deployment: open the app on a mobile browser → complete full onboarding → send a chat message → upload an image → record and send a voice message → check the database has data → test crisis detection → verify all 4 stages work.

---

## Day 6-7: Launch Preparation

### GitHub repository setup
`README.md` should include: project title + logo, one-line description, what it does (clear/compelling), all 4 stages explained briefly, tech stack badges, live demo link, screenshots (4-6 best screens), AI architecture diagram, how to run locally, environment variables needed, API documentation link, future roadmap, contributing guide.

**Screenshots to prepare:** landing page (beautiful), chat interface (Stage 4 emotional), partner analysis results, relationship health dashboard, SOS/crisis screen, progress journey screen.

### Demo video plan
Length: 3-5 minutes. Platform: YouTube or Loom (free).

**Script outline:**
```
[0:00-0:30] Problem statement — "Millions of people navigate love without guidance..."
[0:30-1:00] App overview — show landing page, explain 4 stages
[1:00-2:00] Stage 1 demo — partner description → real analysis result, show insight depth
[2:00-2:30] Stage 3 demo — problem described → root cause → script, show communication coach
[2:30-3:30] Stage 4 demo — breakup support response quality, show empathy and care
[3:30-4:00] AI architecture — brief diagram of LangGraph + RAG, show technical depth
[4:00-4:30] Close — impact statement, live demo link, GitHub link
```

### Portfolio description

**Project Title:** LoveGuru AI
**Tagline:** AI companion for every stage of love

**What It Does:** Full-stack AI application that guides users through all 4 stages of love: single life, finding love, relationships, and heartbreak recovery using LangGraph multi-agent AI, RAG on psychology research, and multi-modal input processing.

**Technical Highlights:**
- LangGraph pipeline with 12 specialized nodes
- RAG on 5 collections (attachment theory, Gottman research, heartbreak psychology)
- Multi-modal AI: text + voice (Whisper) + image analysis (Gemini Vision)
- Crisis safety system with 4-layer detection
- Real-time streaming responses
- Complete memory system (Redis + PostgreSQL)

**Stack:** React | FastAPI | LangGraph | Groq LLaMA 3.1 | Gemini Vision | Whisper | ChromaDB | PostgreSQL | Redis | Supabase | Vercel | Render

### What to say in an interview

> "I built LoveGuru AI - a production-grade AI application that provides relationship guidance across all four stages of love. Technically, it uses a 12-node LangGraph pipeline where specialized agents handle different stages and inputs. The RAG system indexes psychology research from Gottman Institute and attachment theory to give evidence-based advice in conversational language. The most challenging part was the crisis detection system - it uses 4 layers including keyword detection, LLM contextual understanding, and pattern analysis from user history. Both Groq and Gemini verify simultaneously because missing a crisis signal is not an option. The app processes text, voice through Whisper, and images through Gemini Vision - including screenshot conversation analysis that extracts text and detects manipulation patterns. All deployed on free tiers: Vercel, Render, Supabase, and Upstash."

---

## COMPLETE MILESTONE TRACKER (all 10 weeks)

```
WEEK 1 MILESTONES:
□ All accounts created, all API keys saved
□ Both projects created (React + FastAPI)
□ Complete folder structure created
□ All packages installed (no errors)
□ Frontend runs: npm run dev
□ Backend runs: uvicorn main:app

WEEK 2 MILESTONES:
□ All 18 database tables created in Supabase
□ Can connect to database from FastAPI
□ All 67-76 API endpoints defined (not all working)
□ Basic auth: register and login works
□ JWT token generated and validated

WEEK 3 MILESTONES:
□ Design system CSS complete
□ All CSS variables defined
□ 10+ base components built
□ Landing page looks exactly as designed
□ Stage colors working correctly
□ Animations defined

WEEK 4 MILESTONES:
□ Registration works end to end
□ Login works end to end
□ Token refresh works
□ All 7 onboarding screens complete
□ Onboarding data saves to database
□ Redirects to home correctly

WEEK 5 MILESTONES:
□ Groq API connected and responding
□ Basic LangGraph graph runs without error
□ Crisis detection works (test with keywords)
□ First end-to-end chat message works
□ Response streams to frontend
□ Basic stage routing works

WEEK 6 MILESTONES:
□ All documents collected (5 collections)
□ ChromaDB set up locally
□ All documents embedded and stored
□ RAG retrieval returns relevant results
□ RAG integrated into mental health agent
□ Test: query returns correct research chunk

WEEK 7 MILESTONES:
□ Stage 1: Partner vision → analysis works
□ Stage 1: Readiness assessment complete
□ Stage 1: Grooming selfie analysis works
□ Stage 2: Profile review feature works
□ Stage 2: Screenshot analysis works
□ Stage 2: Date prep complete

WEEK 8 MILESTONES:
□ Stage 3: Problem solver end to end
□ Stage 3: Communication scripts work
□ Stage 3: Weekly health tracking works
□ Stage 4: Breakup intake response quality ✓
□ Stage 4: NC tracker works
□ Stage 4: Daily checkin complete

WEEK 9 MILESTONES:
□ Selfie upload → face shape → grooming guide
□ Partner photo → body language reading
□ Screenshot → text extracted → analyzed
□ Voice record → Whisper transcribes
□ Voice emotion detected
□ Multi-modal (text+image) works together

WEEK 10 MILESTONES:
□ All crisis tests pass (100%)
□ All user journey tests pass
□ Performance targets met
□ Backend deployed to Render
□ Frontend deployed to Vercel
□ Database working in production
□ Demo video recorded
□ GitHub README complete
□ Portfolio updated
□ LIVE APP URL WORKING ✅
```

---

## DAILY SCHEDULE SUGGESTION (use every day of building)

**Morning (2 hours):** review what you're building today, look at the relevant week's plan, set up the files needed, start the main feature.

**Afternoon (3 hours):** build the main feature, test as you go, fix any errors immediately, don't move on until current works.

**Evening (1 hour):** review what you built, test the complete flow, note anything to fix tomorrow, commit to GitHub with a clear message.

**Git commit schedule:** commit at end of every day minimum, with clear commit messages, e.g.:
```
feat: add Stage 4 daily checkin UI
feat: connect RAG to Stage 3 counselor
fix: crisis detection false positive
style: update glassmorphism card hover
```

**When stuck:** read the error message fully → Google the exact error → check official docs → ask an AI assistant with full error context → move to another task and return → maximum 1 hour stuck before asking for help.

---

## CLOSING NOTE (from the original source documents)

```
╔═════════════════════════════════════════════════╗
║         YOUR COMPLETE BUILD BIBLE ❤️              ║
║                                                   ║
║  10 Weeks → Production App                        ║
║  45+ Screens → Complete Product                    ║
║  12 AI Agents → Impressive System                  ║
║  5 RAG Collections → Research Backed                ║
║  3 Input Types → Text + Image + Voice               ║
║  4 Stages → Complete Life Companion                 ║
║                                                   ║
║  This is not just a project.                        ║
║  This is a product that helps people                ║
║  navigate one of the most important                 ║
║  parts of their lives.                               ║
║                                                   ║
║  Build it with that in mind.                          ║
║  Every feature matters.                                ║
║  Every response matters.                                ║
║  Someone is coming to this app                          ║
║  at their most vulnerable.                                ║
║  Build it worthy of that trust. ❤️                        ║
╚═════════════════════════════════════════════════╝
```

---
**See Appendix A and Appendix B at the end of this document for every environment variable referenced above.
-e 

---

# APPENDIX A — BACKEND ENVIRONMENT VARIABLES (`backend/.env`)
```env
# ============================================================
# LOVEGURU AI — BACKEND ENVIRONMENT VARIABLES
# File location: backend/.env
# Copy this file to backend/.env and fill in real values.
# NEVER commit the real .env file to GitHub — add ".env" to .gitignore.
# ============================================================

# ---------------- APP ----------------
APP_NAME=LoveGuru AI
APP_ENV=development
DEBUG=True
SECRET_KEY=generate_random_64_char_string
ALLOWED_ORIGINS=http://localhost:5173

# ---------------- DATABASE (Supabase / PostgreSQL) ----------------
DATABASE_URL=postgresql+asyncpg://user:pass@host/db
SUPABASE_URL=your_supabase_url
SUPABASE_ANON_KEY=your_supabase_anon_key
SUPABASE_SERVICE_KEY=your_service_key

# ---------------- AI APIs ----------------
GROQ_API_KEY=your_groq_key
GEMINI_API_KEY=your_gemini_key

# ---------------- CACHE (Upstash Redis) ----------------
REDIS_URL=your_upstash_redis_url
REDIS_TOKEN=your_upstash_token
UPSTASH_REDIS_URL=your_upstash_redis_url
UPSTASH_REDIS_TOKEN=your_upstash_token

# ---------------- JWT / AUTH ----------------
JWT_SECRET_KEY=generate_random_64_char_string
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7

# ---------------- FILE STORAGE ----------------
SUPABASE_STORAGE_BUCKET=loveguru-files

# ---------------- VOICE (Whisper) ----------------
WHISPER_MODEL_SIZE=medium

# ---------------- RAG (ChromaDB) ----------------
CHROMA_PERSIST_PATH=./chroma_db

# ---------------- LOCAL LLM FALLBACK (Ollama) ----------------
OLLAMA_BASE_URL=http://localhost:11434

# ---------------- OPTIONAL: MONITORING ----------------
# SENTRY_DSN=your_sentry_dsn

# ---------------- OPTIONAL: GOOGLE OAUTH ----------------
# GOOGLE_OAUTH_CLIENT_ID=your_google_oauth_client_id
# GOOGLE_OAUTH_CLIENT_SECRET=your_google_oauth_client_secret

# ---------------- OPTIONAL: CRISIS RESOURCES (India) ----------------
# These are used by the crisis_resources.py tool / emergency router.
# ICALL_HELPLINE_NUMBER=9152987821
# VANDREVALA_HELPLINE_NUMBER=1860-2662-345

# ============================================================
# NOTES:
# - Never set DEBUG=True in production (Render deployment).
# - Every key above must also be added in the Render dashboard's
#   "Environment" tab when deploying — Render does not read local .env files.
# - Generate SECRET_KEY / JWT_SECRET_KEY with, e.g.:
#     python -c "import secrets; print(secrets.token_hex(32))"
# ============================================================
```
-e 
---

# APPENDIX B — FRONTEND ENVIRONMENT VARIABLES (`frontend/.env`)
```env
# ============================================================
# LOVEGURU AI — FRONTEND ENVIRONMENT VARIABLES
# File location: frontend/.env
# Copy this file to frontend/.env and fill in real values.
# NEVER commit the real .env file to GitHub — add ".env" to .gitignore.
# Vite only exposes variables prefixed with VITE_ to the browser.
# ============================================================

# ---------------- API ----------------
# Local development:
VITE_API_BASE_URL=http://localhost:8000/api/v1
# Production (set this in Vercel's Environment Variables dashboard instead):
# VITE_API_BASE_URL=https://your-api.render.com/api/v1

# ---------------- SUPABASE (client-side, for storage/auth helpers if used) ----------------
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key

# ---------------- APP META ----------------
VITE_APP_NAME=LoveGuru AI
VITE_ENVIRONMENT=development

# ---------------- OPTIONAL: GOOGLE OAUTH (client id only, no secret in frontend) ----------------
# VITE_GOOGLE_OAUTH_CLIENT_ID=your_google_oauth_client_id

# ---------------- OPTIONAL: CRISIS HELPLINE DISPLAY NUMBERS ----------------
# VITE_ICALL_NUMBER=9152987821
# VITE_VANDREVALA_NUMBER=1860-2662-345

# ============================================================
# NOTES:
# - Set VITE_ENVIRONMENT=production and the real VITE_API_BASE_URL
#   in the Vercel dashboard before deploying — do not hardcode production
#   values in this checked-in example file.
# - Never put secret keys (service role keys, JWT secrets, LLM API keys)
#   in the frontend .env — those belong ONLY in backend.env.example,
#   since anything VITE_-prefixed is bundled into the public JS.
# ============================================================
```
