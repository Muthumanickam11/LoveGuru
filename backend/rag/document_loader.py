"""
╔══════════════════════════════════════════════════════════════╗
║         LOVEGURU AI — Seed Knowledge & Document Loader       ║
║         Research corpus covering all 4 love journey stages   ║
╚══════════════════════════════════════════════════════════════╝
"""

import logging
from typing import List, Dict, Any
from rag.text_splitter import split_text_into_chunks
from rag.vector_store import add_documents_to_collection

logger = logging.getLogger(__name__)

SEED_DOCUMENTS = [
    # ── Stage 1: Single & Searching ──────────────────────────
    {
        "stage": "single",
        "source": "Attachment Theory in Adult Relationships (Bowlby & Hazan)",
        "content": """Attachment styles shape how we seek and maintain romantic bonds. 
Anxious attachment manifests as hyper-vigilance towards rejection, constant need for reassurance, and urgency in texting. 
Avoidant attachment manifests as emotional distancing when intimacy increases, valuing hyper-independence over connection.
Secure attachment allows comfortable emotional vulnerability, direct expression of needs, and high conflict resilience.
To attract a secure partner, one must first cultivate secure internal self-soothing and realistic partner criteria."""
    },
    {
        "stage": "single",
        "source": "The Psychology of Partner Selection & Reality Checks",
        "content": """Unrealistic romantic checklists often focus heavily on external variables (income percentiles, height, glamorous lifestyles) while under-weighting core psychological compatibilities: emotional regulation, curiosity, shared conflict resolution styles, and mutual respect.
A successful reality check separates non-negotiable ethical values from superficial aesthetic preferences, allowing singles to recognize genuine compatibility."""
    },

    # ── Stage 2: Finding Love ────────────────────────────────
    {
        "stage": "finding",
        "source": "The Neuroscience of Romance (Dr. Helen Fisher)",
        "content": """Romantic attraction activates the brain's ventral tegmental area (VTA), flooding pathways with dopamine, creating focused attention, heightened energy, and obsessive craving.
In the early dating stage, pace yourself to allow the prefrontal cortex to assess genuine character rather than projecting fantasy onto the dopamine rush.
Conversational bids: Responding warmly to small daily observations builds conversational trust 5x faster than interrogative questions."""
    },
    {
        "stage": "finding",
        "source": "Modern Dating Green & Red Flags Framework",
        "content": """Green flags in early dating: Consistency between words and actions, respecting stated boundaries without pushback, curiosity about your inner world, open communication when plans change, and gracious treatment of service staff.
Red flags: Love bombing (excessive intensity in week 1), contemptuous remarks about previous partners, hot-and-cold communication cycles designed to induce anxiety, and defensiveness against mild feedback."""
    },

    # ── Stage 3: In a Relationship ───────────────────────────
    {
        "stage": "relationship",
        "source": "The Gottman Method & Four Horsemen (Dr. John Gottman)",
        "content": """Dr. John Gottman's research identifies the Four Horsemen of relationship breakdown:
1. Criticism: Attacking partner's personality ('You always forget'). Antidote: Gentle Start-Up using 'I feel... about... and I need...'.
2. Contempt: Sneering, sarcasm, eye-rolling, name-calling. Number 1 predictor of divorce. Antidote: Build a culture of daily appreciation.
3. Defensiveness: Deflecting blame ('It's not my fault, you did it too'). Antidote: Take responsibility for even 5% of the issue.
4. Stonewalling: Shutting down, physiological flooding (>100 bpm). Antidote: Physiological self-soothing (take a 20-minute break before resuming)."""
    },
    {
        "stage": "relationship",
        "source": "The 5 Love Languages (Dr. Gary Chapman)",
        "content": """The Five Love Languages are:
1. Words of Affirmation: Verbal compliments and appreciation.
2. Quality Time: Undivided attention without screen distractions.
3. Receiving Gifts: Thoughtfulness embodied in symbolic tokens.
4. Acts of Service: Easing partner's burden through helpful actions.
5. Physical Touch: Non-sexual and sexual affectionate touch.
Misunderstandings arise when partners project their own language rather than speaking their partner's primary language."""
    },

    # ── Stage 4: Heartbreak Recovery ─────────────────────────
    {
        "stage": "heartbreak",
        "source": "Neurochemistry of Heartbreak & No-Contact Protocol",
        "content": """A romantic breakup induces acute neurochemical withdrawal akin to substance detox: dopamine drops drastically while cortisol rises.
Checking an ex's social media or texting creates intermittent reinforcement spikes that prolong addiction cycles.
The 30-Day No-Contact protocol allows neuroreceptors to down-regulate, breaking the neurochemical panic loop.
Grief is non-linear; feeling sudden grief on day 20 after feeling peaceful on day 15 is standard neurological re-calibration."""
    },
    {
        "stage": "heartbreak",
        "source": "Somatic Emotional Regulation & Grief Weather Model",
        "content": """Emotional pain registers in the anterior cingulate cortex—the same brain region that processes physical injury.
The Grief Weather model categorizes recovery states:
Storm: Acute panic, urge to text, chest tightness. (Use 4-7-8 breathing and physiological sighs).
Rain: Heavy sadness, fatigue, crying. (Allow full expression without self-judgment).
Overcast: Numbness, low energy. (Engage in gentle sensory routines).
Clearing: Moments of clarity, appetite returning.
Sun: Renewed excitement for individual growth and future possibilities."""
    },

    # ── Indian Context ───────────────────────────────────────
    {
        "stage": "indian_context",
        "source": "Cultural Dynamics in Indian Relationships & Family Systems",
        "content": """Navigating romantic relationships in Indian family contexts often requires balancing autonomy with filial respect.
Key strategies:
1. United Front: Both partners must align privately before communicating with parents or in-laws.
2. Differentiation: Setting healthy boundaries is an act of preserving family relationships, not disrespect.
3. Arranged vs Love Marriage synthesis: Evaluating shared financial values, family expectations, and emotional maturity early prevents long-term friction."""
    },

    # ── Stage 1: Additional ──────────────────────────────────
    {
        "stage": "single",
        "source": "Self-Worth & Dating Standards (Dr. Brené Brown)",
        "content": """Vulnerability is not weakness; it is the birthplace of connection. Singles who struggle with perfectionism in partner selection often do so from a place of shame — believing they are not enough unless their partner proves it by being exceptional. 
Healthy standards come from a place of self-worth: 'I deserve kindness, so I will only date kind people.' Fear-based standards come from wounds: 'They must be very successful so I can feel proud to introduce them.' 
Self-compassion practice: treat yourself with the same kindness you would offer a good friend who was struggling in dating."""
    },
    {
        "stage": "single",
        "source": "Readiness Indicators for Healthy Partnership",
        "content": """Signs you are emotionally ready to date:
1. You enjoy your own company and can sit with solitude without anxiety.
2. You have processed (not just buried) major past relationship wounds.
3. You have clear non-negotiable values — not just a wishlist of traits.
4. You can communicate a need directly without fear of immediate abandonment.
5. You have interests, friendships, and purpose that exist independently of a romantic partner.
6. You can handle rejection without it confirming a core belief that you are unlovable.
Signs you need more time: dating from fear of being alone, still checking ex's social media obsessively, unable to trust anyone new."""
    },

    # ── Stage 2: Additional ──────────────────────────────────
    {
        "stage": "finding",
        "source": "The Art of Asking Questions on Dates",
        "content": """The best dates are conversations, not interrogations. Research shows that mutual self-disclosure, in a gradually deepening sequence, creates faster emotional closeness than either humor alone or information exchange.
The 36 Questions protocol (Arthur Aron, 1997): progressively more intimate questions create closeness in strangers within 45 minutes.
Practical dating conversation levels:
Level 1 (Warmth): 'What's something you've been genuinely excited about lately?'
Level 2 (Values): 'What does a really good day look like for you?'
Level 3 (Depth): 'What's something you've changed your mind about in the last five years?'
Avoid: interrogative rapid-fire questions, oversharing trauma on first dates, resume listing."""
    },
    {
        "stage": "finding",
        "source": "Texting Psychology in Early Dating",
        "content": """Texting anxiety is epidemic in early dating. Key principles:
1. Response time anxiety: checking for responses within minutes is a trauma response, not love. It correlates with anxious attachment.
2. Mirroring message length is more effective than calculated delay games.
3. Ambiguous texts feel negative 70% of the time due to negativity bias — when unsure, assume neutral.
4. After 3 exchanges on one topic, suggest moving to voice/video call.
5. Never have a serious conversation over text — tonal misreading creates unnecessary conflict.
6. Breadcrumbing pattern: responding just enough to keep someone engaged without real investment. Exit this dynamic immediately."""
    },

    # ── Stage 3: Additional ──────────────────────────────────
    {
        "stage": "relationship",
        "source": "Emotional Bids & Relationship Bank Account (Gottman)",
        "content": """Dr. Gottman's research identifies 'emotional bids' — small moments where one partner reaches toward the other for connection, attention, or support. 
Examples of bids: 'Look at that interesting bird' (pointing out window), 'I had a rough day,' sharing a funny meme.
Three responses to bids:
1. Turning toward: 'Oh wow, what kind of bird?' — deposits into emotional bank account.
2. Turning away: ignoring or not responding — neutral withdrawal.
3. Turning against: 'I'm busy, don't bother me with birds' — withdraws from account.
Couples who divorce turn toward each other 33% of the time. Couples who stay married turn toward each other 86% of the time.
Small daily bids matter more than grand romantic gestures."""
    },
    {
        "stage": "relationship",
        "source": "Sexual Intimacy & Desire in Long-Term Relationships",
        "content": """Desire in long-term relationships requires three elements: safety (emotional security), novelty (surprise and growth), and autonomy (maintaining individual identity).
Esther Perel's research: desire needs mystery and distance to thrive — overfamiliarization reduces attraction. 
Maintaining desire: pursue individual interests your partner does not share, maintain a degree of personal mystery, approach your partner with fresh curiosity periodically.
Desire discrepancy (one partner wanting more than other) is normal. Solution: scheduled intimacy (removes pressure), sensate focus exercises, non-sexual affection baseline building."""
    },

    # ── Stage 4: Additional ──────────────────────────────────
    {
        "stage": "heartbreak",
        "source": "The No-Contact Rule — Science and Practice",
        "content": """The 30-Day No-Contact rule is not punishment — it is neurochemical recovery. 
What happens in the brain during no-contact:
- Days 1-7: Acute withdrawal. Dopamine crashes. Cortisol peaks. Physical chest pain is real (anterior cingulate cortex activation).
- Days 8-15: Anger phase often emerges (healthy — signals self-protection returning).
- Days 16-21: Grief deepens then begins lifting. Sleep patterns normalize slightly.
- Days 22-30: Cognitive clarity returns. Rumination decreases.
No-contact rules: Block on all platforms. Remove physical reminders from view (not destroy — store). Tell 2 trusted friends about the commitment for accountability.
Breaking no-contact resets the neurochemical clock to Day 1."""
    },
    {
        "stage": "heartbreak",
        "source": "Identity Rebuilding After a Long Relationship",
        "content": """In relationships longer than 1 year, partners often develop 'enmeshed identity' — losing track of who they are outside the relationship. This is why breakups feel like losing part of the self.
Identity rebuilding protocol:
1. List 10 things you loved before this relationship that got neglected.
2. Reconnect with 3 friends who knew you before this relationship.
3. Try 1 new activity per week — the brain forms new neural associations with novelty.
4. Journaling prompt: 'Who was I at my best before this relationship? What did I stand for?'
5. Physical reclamation: change something about your physical environment (rearrange furniture, new haircut, new route to work).
Identity is not found — it is actively constructed, one small choice at a time."""
    },
    {
        "stage": "heartbreak",
        "source": "When to Seek Professional Help After Heartbreak",
        "content": """Normal grief vs. clinical concern:
Normal (seek AI + community support): sadness, crying, difficulty concentrating, disrupted sleep and appetite for 2-6 weeks.
Seek professional help when:
- Suicidal ideation or self-harm thoughts persist beyond brief moments.
- Unable to function at work/school for more than 3 consecutive weeks.
- Alcohol or substance use increasing significantly.
- Complete social isolation for more than 2 weeks.
- Symptoms worsening rather than gradually improving after 6 weeks.
Therapy modalities that help: EMDR for relationship trauma, CBT for rumination, ACT for acceptance, group therapy for connection.
Reaching out for professional help is strength, not failure."""
    },
]


def load_seed_corpus() -> None:
    """Loads and indexes the core relationship science documents."""
    logger.info("Indexing relationship research corpus into RAG vector store...")
    for item in SEED_DOCUMENTS:
        stage = item["stage"]
        chunks = split_text_into_chunks(
            text=item["content"],
            chunk_size=200,
            chunk_overlap=30,
            metadata={"source": item["source"], "stage": stage}
        )
        add_documents_to_collection(collection_name=stage, documents=chunks)
    logger.info(f"✅ Successfully indexed {len(SEED_DOCUMENTS)} seed research documents")
