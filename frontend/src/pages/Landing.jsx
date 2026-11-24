import { useNavigate } from 'react-router-dom'
import { motion } from 'framer-motion'

const STAGES = [
  {
    id: 's1',
    emoji: '🟡',
    title: 'Single & Searching',
    desc: 'Reality-check your expectations and build yourself into the partner you want to attract.',
    color: '#F59E0B',
    glow: 'rgba(245,158,11,0.2)',
  },
  {
    id: 's2',
    emoji: '🟢',
    title: 'Finding Love',
    desc: 'AI-powered dating profile reviews, conversation coaching, and green flag/red flag education.',
    color: '#10B981',
    glow: 'rgba(16,185,129,0.2)',
  },
  {
    id: 's3',
    emoji: '🔵',
    title: 'In a Relationship',
    desc: 'Gottman Method scripts, love language discovery, and weekly relationship health tracking.',
    color: '#3B82F6',
    glow: 'rgba(59,130,246,0.2)',
  },
  {
    id: 's4',
    emoji: '🔴',
    title: 'After a Breakup',
    desc: '24/7 crisis support, grief weather guidance, no-contact tracker, and identity rebuilding.',
    color: '#F43F5E',
    glow: 'rgba(244,63,94,0.2)',
  },
]

const RESEARCHERS = [
  { name: 'Dr. John Gottman', field: '40 years of relationship research' },
  { name: 'Dr. Gary Chapman', field: 'The 5 Love Languages' },
  { name: 'Dr. John Bowlby', field: 'Attachment Theory' },
  { name: 'Dr. Helen Fisher', field: 'Neuroscience of Love' },
]

export default function Landing() {
  const navigate = useNavigate()

  return (
    <div className="page">

      {/* ── NAV ───────────────────────────────────────────── */}
      <nav className="navbar" style={{ position: 'fixed', left: 0, right: 0 }}>
        <div className="navbar-inner">
          <div className="navbar-brand">
            <div className="navbar-logo">❤️</div>
            <span className="navbar-brand-name gradient-text">LoveGuru AI</span>
          </div>
          <span className="navbar-spacer" />
          <div style={{ display: 'flex', gap: 12 }}>
          <button
            id="landing-login-btn"
            onClick={() => navigate('/home')}
            style={{
              padding: '8px 20px', background: 'transparent',
              border: '1px solid rgba(255,255,255,0.15)',
              borderRadius: 999, color: '#94A3B8', cursor: 'pointer',
              fontFamily: "'Plus Jakarta Sans', sans-serif", fontWeight: 600,
              transition: 'all 0.2s',
            }}
            onMouseEnter={e => { e.target.style.color = '#F0F4FF'; e.target.style.borderColor = 'rgba(255,255,255,0.3)' }}
            onMouseLeave={e => { e.target.style.color = '#94A3B8'; e.target.style.borderColor = 'rgba(255,255,255,0.15)' }}
          >Sign In</button>
          <button
            id="landing-start-btn"
            onClick={() => navigate('/home')}
            style={{
              padding: '8px 24px',
              background: 'linear-gradient(135deg,#EC4899,#8B5CF6)',
              border: 'none', borderRadius: 999,
              color: '#fff', cursor: 'pointer', fontWeight: 600,
              fontFamily: "'Plus Jakarta Sans', sans-serif",
              boxShadow: '0 4px 20px rgba(236,72,153,0.3)',
              transition: 'all 0.2s',
            }}
          >Start Free</button>
          </div>
        </div>
      </nav>

      {/* ── HERO ──────────────────────────────────────────── */}
      <section style={{
        minHeight: '100vh', display: 'flex', flexDirection: 'column',
        alignItems: 'center', justifyContent: 'center', textAlign: 'center',
        padding: '120px 24px 80px',
        position: 'relative', overflow: 'hidden',
      }}>
        {/* Background orbs */}
        <div style={{
          position: 'absolute', top: '20%', left: '15%',
          width: 400, height: 400, borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(139,92,246,0.12) 0%, transparent 70%)',
          pointerEvents: 'none',
        }} />
        <div style={{
          position: 'absolute', bottom: '20%', right: '15%',
          width: 350, height: 350, borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(236,72,153,0.1) 0%, transparent 70%)',
          pointerEvents: 'none',
        }} />

        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          <div style={{
            display: 'inline-flex', alignItems: 'center', gap: 8,
            padding: '6px 16px',
            background: 'rgba(236,72,153,0.1)',
            border: '1px solid rgba(236,72,153,0.25)',
            borderRadius: 999, marginBottom: 24,
            fontSize: '0.8rem', color: '#EC4899', fontWeight: 600,
          }}>
            ✨ AI-Powered Relationship Guidance
          </div>

          <h1 style={{
            fontFamily: "'Outfit', sans-serif",
            fontWeight: 800,
            fontSize: 'clamp(2.5rem, 6vw, 4rem)',
            color: '#F0F4FF',
            lineHeight: 1.15,
            marginBottom: 16,
          }}>
            Your AI Guru For<br />
            <span style={{
              background: 'linear-gradient(135deg, #EC4899, #8B5CF6)',
              WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent',
            }}>
              Every Stage of Love
            </span>
          </h1>

          <p style={{
            fontSize: 'clamp(1rem, 2vw, 1.2rem)',
            color: '#94A3B8', maxWidth: 620, margin: '0 auto 40px',
            lineHeight: 1.7,
          }}>
            From single to soulmate — LoveGuru AI walks beside you with wisdom, warmth,
            and real guidance. Backed by relationship science. Available 24/7.
          </p>

          <div style={{ display: 'flex', gap: 12, justifyContent: 'center', flexWrap: 'wrap' }}>
            <motion.button
              id="hero-start-btn"
              whileHover={{ scale: 1.04, y: -2 }}
              whileTap={{ scale: 0.98 }}
              onClick={() => navigate('/home')}
              style={{
                padding: '14px 36px',
                background: 'linear-gradient(135deg,#EC4899,#8B5CF6)',
                border: 'none', borderRadius: 999,
                color: '#fff', fontSize: '1rem', fontWeight: 700, cursor: 'pointer',
                boxShadow: '0 4px 30px rgba(236,72,153,0.4)',
                fontFamily: "'Plus Jakarta Sans', sans-serif",
              }}
            >
              Start Your Journey — Free ✨
            </motion.button>
            <motion.button
              whileHover={{ scale: 1.02 }}
              onClick={() => {
                document.getElementById('stages-section')?.scrollIntoView({ behavior: 'smooth' })
              }}
              style={{
                padding: '14px 32px',
                background: 'transparent',
                border: '1px solid rgba(255,255,255,0.12)',
                borderRadius: 999, color: '#94A3B8',
                fontSize: '1rem', fontWeight: 600, cursor: 'pointer',
                fontFamily: "'Plus Jakarta Sans', sans-serif",
              }}
            >
              See How It Works
            </motion.button>
          </div>

          {/* Trust badges */}
          <div style={{
            display: 'flex', gap: 32, justifyContent: 'center',
            marginTop: 56, flexWrap: 'wrap',
          }}>
            {['🔒 Crisis-Safe', '🧠 Research-Backed', '❤️ India-Aware', '🌙 24/7 Available'].map((badge) => (
              <div key={badge} style={{ color: '#475569', fontSize: '0.85rem', fontWeight: 500 }}>
                {badge}
              </div>
            ))}
          </div>
        </motion.div>
      </section>

      {/* ── 4 STAGES ─────────────────────────────────────── */}
      <section id="stages-section" style={{ padding: '80px 24px', maxWidth: 1200, margin: '0 auto' }}>
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          style={{ textAlign: 'center', marginBottom: 56 }}
        >
          <h2 style={{
            fontFamily: "'Outfit', sans-serif", fontSize: 'clamp(1.75rem, 4vw, 2.5rem)',
            fontWeight: 700, color: '#F0F4FF', marginBottom: 12,
          }}>
            Whatever stage you're in — <span style={{
              background: 'linear-gradient(135deg,#EC4899,#8B5CF6)',
              WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent',
            }}>we're with you</span>
          </h2>
          <p style={{ color: '#94A3B8', fontSize: '1.05rem', maxWidth: 550, margin: '0 auto' }}>
            Nobody has built all 4 stages together. This is the unique power of LoveGuru AI.
          </p>
        </motion.div>

        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))',
          gap: 20,
        }}>
          {STAGES.map((stage, i) => (
            <motion.div
              key={stage.id}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1 }}
              whileHover={{ y: -6, transition: { duration: 0.2 } }}
              onClick={() => navigate('/home')}
              style={{
                padding: 28,
                background: `linear-gradient(135deg, ${stage.glow} 0%, rgba(22,29,42,0.9) 100%)`,
                border: `1px solid ${stage.color}33`,
                borderRadius: 20,
                cursor: 'pointer',
                transition: 'box-shadow 0.3s',
              }}
              onMouseEnter={e => e.currentTarget.style.boxShadow = `0 0 40px ${stage.glow}`}
              onMouseLeave={e => e.currentTarget.style.boxShadow = 'none'}
            >
              <div style={{ fontSize: '1.5rem', marginBottom: 12 }}>{stage.emoji}</div>
              <h3 style={{
                fontFamily: "'Outfit', sans-serif",
                color: stage.color, fontWeight: 700,
                fontSize: '1.1rem', marginBottom: 10,
              }}>{stage.title}</h3>
              <p style={{ color: '#94A3B8', fontSize: '0.9rem', lineHeight: 1.6 }}>{stage.desc}</p>
            </motion.div>
          ))}
        </div>
      </section>

      {/* ── RESEARCH SECTION ─────────────────────────────── */}
      <section style={{ padding: '80px 24px', maxWidth: 900, margin: '0 auto', textAlign: 'center' }}>
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
        >
          <p style={{ color: '#EC4899', fontWeight: 600, fontSize: '0.85rem', letterSpacing: 1, marginBottom: 12 }}>
            RESEARCH-BACKED
          </p>
          <h2 style={{
            fontFamily: "'Outfit', sans-serif",
            fontSize: 'clamp(1.5rem, 3.5vw, 2rem)',
            color: '#F0F4FF', fontWeight: 700, marginBottom: 40,
          }}>
            Built on decades of relationship science
          </h2>
          <div style={{
            display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))',
            gap: 16,
          }}>
            {RESEARCHERS.map((r, i) => (
              <motion.div
                key={r.name}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.1 }}
                viewport={{ once: true }}
                style={{
                  padding: 20,
                  background: 'rgba(255,255,255,0.03)',
                  border: '1px solid rgba(255,255,255,0.07)',
                  borderRadius: 16,
                }}
              >
                <div style={{ color: '#8B5CF6', fontSize: '1.5rem', marginBottom: 8 }}>🔬</div>
                <div style={{ color: '#F0F4FF', fontWeight: 600, fontSize: '0.9rem', marginBottom: 4 }}>{r.name}</div>
                <div style={{ color: '#475569', fontSize: '0.8rem' }}>{r.field}</div>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </section>

      {/* ── CTA ──────────────────────────────────────────── */}
      <section style={{
        padding: '100px 24px', textAlign: 'center',
        background: 'linear-gradient(180deg, transparent, rgba(139,92,246,0.05))',
      }}>
        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          whileInView={{ opacity: 1, scale: 1 }}
          viewport={{ once: true }}
        >
          <h2 style={{
            fontFamily: "'Outfit', sans-serif",
            fontSize: 'clamp(1.75rem, 4vw, 2.5rem)',
            color: '#F0F4FF', fontWeight: 700, marginBottom: 16,
          }}>
            Your love story deserves real guidance
          </h2>
          <p style={{ color: '#94A3B8', fontSize: '1.05rem', marginBottom: 40 }}>
            Start free. No credit card needed. Available 24/7.
          </p>
          <motion.button
            id="cta-start-btn"
            whileHover={{ scale: 1.04, y: -2 }}
            whileTap={{ scale: 0.98 }}
            onClick={() => navigate('/home')}
            style={{
              padding: '16px 48px',
              background: 'linear-gradient(135deg,#EC4899,#8B5CF6)',
              border: 'none', borderRadius: 999,
              color: '#fff', fontSize: '1.1rem', fontWeight: 700, cursor: 'pointer',
              boxShadow: '0 4px 40px rgba(236,72,153,0.5)',
              fontFamily: "'Plus Jakarta Sans', sans-serif",
            }}
          >
            Begin Your Journey ❤️
          </motion.button>
        </motion.div>
      </section>

      {/* ── FOOTER ───────────────────────────────────────── */}
      <footer style={{ borderTop: '1px solid rgba(255,255,255,0.05)' }}>
        <div className="navbar-inner" style={{ minHeight: 0, padding: '32px 24px', flexWrap: 'wrap', gap: 16 }}>
          <div style={{
            fontFamily: "'Outfit', sans-serif", fontWeight: 700,
            background: 'linear-gradient(135deg,#EC4899,#8B5CF6)',
            WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent',
          }}>❤️ LoveGuru AI</div>
          <span className="navbar-spacer" />
          <div style={{ color: '#334155', fontSize: '0.8rem' }}>
            Not a therapy replacement. Crisis helplines: iCall 9152987821 | AASRA 9820466627
          </div>
        </div>
      </footer>
    </div>
  )
}
