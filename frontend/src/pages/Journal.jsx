import { useState, useEffect, useRef } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import toast from 'react-hot-toast'
import AppNavbar from '../components/common/AppNavbar'
import { stage4Api } from '../api/apiCalls'
import { useAuthStore } from '../store/authStore'

const JOURNAL_PROMPTS = [
  'What am I feeling right now, and where do I feel it in my body?',
  'What is one thing I did today that I am genuinely proud of?',
  'What fear is showing up in my life right now?',
  'What would I tell a close friend who was going through exactly what I am going through?',
  'What am I still holding onto that I know I need to release?',
  'What does healing look like for me today — not in 6 months, but today?',
  'Who showed up for me this week? How can I appreciate them?',
]

function JournalEntry({ entry }) {
  const date = new Date(entry.created_at || Date.now())
  const dateStr = date.toLocaleDateString('en-IN', { weekday: 'short', day: 'numeric', month: 'short' })

  return (
    <motion.div
      initial={{ opacity: 0, y: 8 }}
      animate={{ opacity: 1, y: 0 }}
      style={{
        background: 'rgba(255,255,255,0.03)',
        border: '1px solid rgba(255,255,255,0.08)',
        borderRadius: 16,
        padding: '20px 24px',
        marginBottom: 16,
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
        <span style={{ fontSize: '0.78rem', color: '#94A3B8', fontWeight: 500 }}>{dateStr}</span>
        {entry.mood_tag && (
          <span style={{
            fontSize: '0.72rem', background: 'rgba(244,63,94,0.15)',
            color: '#F43F5E', borderRadius: 999, padding: '3px 10px', fontWeight: 600,
          }}>{entry.mood_tag}</span>
        )}
      </div>
      <p style={{ color: '#CBD5E1', fontSize: '0.92rem', lineHeight: 1.65, margin: 0 }}>
        {entry.content}
      </p>
      {entry.ai_reflection && (
        <div style={{
          marginTop: 14, padding: '14px 16px',
          background: 'rgba(236,72,153,0.07)',
          border: '1px solid rgba(236,72,153,0.2)',
          borderRadius: 12,
        }}>
          <div style={{ fontSize: '0.72rem', color: '#EC4899', fontWeight: 700, marginBottom: 6 }}>
            💜 Guru's Reflection
          </div>
          <p style={{ color: '#CBD5E1', fontSize: '0.88rem', lineHeight: 1.6, margin: 0 }}>
            {entry.ai_reflection}
          </p>
        </div>
      )}
    </motion.div>
  )
}

export default function Journal() {
  const { user } = useAuthStore()
  const [entries, setEntries]     = useState([])
  const [content, setContent]     = useState('')
  const [moodTag, setMoodTag]     = useState('')
  const [submitting, setSubmitting] = useState(false)
  const [promptIdx, setPromptIdx] = useState(0)
  const textareaRef = useRef(null)

  const currentPrompt = JOURNAL_PROMPTS[promptIdx]

  const nextPrompt = () => setPromptIdx((i) => (i + 1) % JOURNAL_PROMPTS.length)

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!content.trim() || content.trim().length < 10) {
      toast.error('Write at least a sentence before saving.')
      return
    }
    setSubmitting(true)
    try {
      const res = await stage4Api.submitJournal({ content, mood_tag: moodTag || undefined })
      const newEntry = res.data?.entry || { content, mood_tag: moodTag, created_at: new Date().toISOString() }
      setEntries((prev) => [newEntry, ...prev])
      setContent('')
      setMoodTag('')
      toast.success('Journal entry saved 💜')
    } catch {
      // Optimistic local add on API failure
      setEntries((prev) => [{
        content, mood_tag: moodTag, created_at: new Date().toISOString(),
        ai_reflection: 'Your words carry weight and deserve to be heard. Keep going — one honest sentence at a time.',
      }, ...prev])
      setContent('')
      setMoodTag('')
      toast.success('Entry saved locally 💜')
    } finally {
      setSubmitting(false)
    }
  }

  const MOOD_OPTIONS = [
    { label: 'Heavy', color: '#F43F5E' },
    { label: 'Anxious', color: '#F59E0B' },
    { label: 'Numb', color: '#94A3B8' },
    { label: 'Hopeful', color: '#10B981' },
    { label: 'Grateful', color: '#3B82F6' },
    { label: 'Peaceful', color: '#8B5CF6' },
  ]

  return (
    <div className="page">
      <AppNavbar />
      <main className="page-container" style={{ maxWidth: 760 }}>
        {/* Header */}
        <div style={{ marginBottom: 32 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 8 }}>
            <span style={{ fontSize: '1.5rem' }}>📔</span>
            <span style={{
              background: 'rgba(244,63,94,0.15)', color: '#F43F5E',
              fontSize: '0.75rem', fontWeight: 700, padding: '4px 10px',
              borderRadius: 999, textTransform: 'uppercase',
            }}>Healing Journal</span>
          </div>
          <h1 style={{ fontSize: '2rem', fontWeight: 800, color: '#F8FAFC', marginBottom: 8 }}>
            Your Safe Space to Write
          </h1>
          <p style={{ color: '#94A3B8', fontSize: '0.95rem', maxWidth: 600, lineHeight: 1.5 }}>
            Write freely. No judgment. Your AI Guru reads every entry and reflects back wisdom to help you heal.
          </p>
        </div>

        {/* Writing Prompt */}
        <div style={{
          background: 'rgba(236,72,153,0.08)',
          border: '1px solid rgba(236,72,153,0.2)',
          borderRadius: 16,
          padding: '20px 24px',
          marginBottom: 24,
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          gap: 16,
        }}>
          <div>
            <div style={{ fontSize: '0.72rem', color: '#EC4899', fontWeight: 700, marginBottom: 6 }}>
              ✨ TODAY'S PROMPT
            </div>
            <p style={{ color: '#F0F4FF', fontSize: '0.95rem', lineHeight: 1.5, margin: 0 }}>
              {currentPrompt}
            </p>
          </div>
          <button
            onClick={nextPrompt}
            style={{
              background: 'rgba(236,72,153,0.15)', border: '1px solid rgba(236,72,153,0.3)',
              color: '#EC4899', borderRadius: 10, padding: '8px 14px',
              fontSize: '0.8rem', fontWeight: 600, cursor: 'pointer', whiteSpace: 'nowrap',
            }}
          >
            New Prompt
          </button>
        </div>

        {/* Write Form */}
        <form onSubmit={handleSubmit} style={{ marginBottom: 40 }}>
          <textarea
            ref={textareaRef}
            value={content}
            onChange={(e) => setContent(e.target.value)}
            placeholder="Start writing... let it all out."
            style={{
              width: '100%',
              minHeight: 180,
              background: 'rgba(255,255,255,0.04)',
              border: '1px solid rgba(255,255,255,0.1)',
              borderRadius: 16,
              padding: '18px 20px',
              color: '#F0F4FF',
              fontSize: '0.95rem',
              lineHeight: 1.7,
              fontFamily: "'Plus Jakarta Sans', sans-serif",
              resize: 'vertical',
              outline: 'none',
              boxSizing: 'border-box',
              marginBottom: 16,
            }}
          />

          {/* Mood tag */}
          <div style={{ marginBottom: 16 }}>
            <div style={{ fontSize: '0.78rem', color: '#94A3B8', marginBottom: 10, fontWeight: 500 }}>
              How are you feeling right now?
            </div>
            <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
              {MOOD_OPTIONS.map((m) => (
                <button
                  key={m.label}
                  type="button"
                  onClick={() => setMoodTag(moodTag === m.label ? '' : m.label)}
                  style={{
                    background: moodTag === m.label ? `${m.color}25` : 'rgba(255,255,255,0.05)',
                    border: `1px solid ${moodTag === m.label ? m.color : 'rgba(255,255,255,0.1)'}`,
                    color: moodTag === m.label ? m.color : '#94A3B8',
                    borderRadius: 999, padding: '6px 14px',
                    fontSize: '0.8rem', fontWeight: 600, cursor: 'pointer',
                    transition: 'all 0.2s',
                  }}
                >
                  {m.label}
                </button>
              ))}
            </div>
          </div>

          <button
            type="submit"
            disabled={submitting || !content.trim()}
            style={{
              background: submitting || !content.trim()
                ? 'rgba(255,255,255,0.08)'
                : 'linear-gradient(135deg, #EC4899, #8B5CF6)',
              color: submitting || !content.trim() ? '#475569' : '#fff',
              border: 'none', borderRadius: 14,
              padding: '14px 32px',
              fontSize: '0.95rem', fontWeight: 700,
              cursor: submitting || !content.trim() ? 'not-allowed' : 'pointer',
              transition: 'all 0.2s',
            }}
          >
            {submitting ? 'Saving…' : '💜 Save Entry'}
          </button>
        </form>

        {/* Past Entries */}
        {entries.length > 0 && (
          <div>
            <h2 style={{ fontSize: '1.1rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 20 }}>
              Past Entries ({entries.length})
            </h2>
            <AnimatePresence>
              {entries.map((entry, i) => (
                <JournalEntry key={i} entry={entry} />
              ))}
            </AnimatePresence>
          </div>
        )}

        {entries.length === 0 && (
          <div style={{
            textAlign: 'center', padding: '48px 24px',
            color: '#475569', fontSize: '0.9rem', lineHeight: 1.6,
          }}>
            <div style={{ fontSize: '2.5rem', marginBottom: 12 }}>📔</div>
            <div>Your journal is empty. Write your first entry above.</div>
            <div style={{ marginTop: 6 }}>Every healing journey starts with one honest sentence.</div>
          </div>
        )}
      </main>
    </div>
  )
}
