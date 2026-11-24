import React, { useState, useEffect } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { motion } from 'framer-motion'
import toast from 'react-hot-toast'
import AppNavbar from '../components/common/AppNavbar'
import { useAuthStore } from '../store/authStore'
import { progressApi } from '../api/apiCalls'

const STAGE_CONFIGS = {
  single: {
    title: 'Single & Searching',
    color: '#F59E0B',
    emoji: '🟡',
    hubLink: '/stage1',
    hubName: 'Partner & Readiness Hub',
    quote: '"You do not attract what you want; you attract what you are." — Attachment Research',
  },
  finding: {
    title: 'Finding Love',
    color: '#10B981',
    emoji: '🟢',
    hubLink: '/stage2',
    hubName: 'Dating & Flirt Hub',
    quote: '"Curiosity is the ultimate romantic aphrodisiac." — Dr. Helen Fisher',
  },
  relationship: {
    title: 'In a Relationship',
    color: '#3B82F6',
    emoji: '🔵',
    hubLink: '/stage3',
    hubName: 'Couples & Gottman Hub',
    quote: '"Small things done often create masters of relationships." — Dr. John Gottman',
  },
  heartbreak: {
    title: 'After a Breakup',
    color: '#F43F5E',
    emoji: '🔴',
    hubLink: '/stage4',
    hubName: 'Healing & Vault Hub',
    quote: '"Grief is love with nowhere to go. Give it time, grace, and steady breath."',
  },
}

const MOODS = [
  { emoji: '☀️', label: 'Radiant', score: 9 },
  { emoji: '🌸', label: 'Calm', score: 7 },
  { emoji: '☁️', label: 'Overcast', score: 5 },
  { emoji: '🌧️', label: 'Heavy', score: 3 },
  { emoji: '⚡', label: 'Anxious', score: 4 },
]

export default function Home() {
  const navigate = useNavigate()
  const { user } = useAuthStore()

  const currentStage = user?.stage || 'single'
  const config = STAGE_CONFIGS[currentStage] || STAGE_CONFIGS.single

  const [selectedMood, setSelectedMood] = useState(null)
  const [gratitudeNote, setGratitudeNote] = useState('')
  const [streakData, setStreakData] = useState({ current_streak: 7, total_xp: 480, level: 3 })
  const [checkinDone, setCheckinDone] = useState(false)

  useEffect(() => {
    progressApi.getOverview()
      .then((res) => {
        if (res.data) setStreakData(res.data)
      })
      .catch(() => {})
  }, [])

  const handleCheckin = async () => {
    if (!selectedMood) {
      toast.error('Please select your mood first.')
      return
    }
    try {
      await progressApi.logDailyCheckin({
        mood_score: selectedMood.score,
        emoji: selectedMood.emoji,
        checkin_type: 'morning',
        trigger_notes: gratitudeNote || undefined,
      })
    } catch {
      // non-blocking — still mark done locally
    }
    setCheckinDone(true)
    toast.success('Check-in saved! ✨')
  }

  return (
    <div className="page">
      <AppNavbar />

      <main className="page-container">
        {/* Welcome Header */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 32, flexWrap: 'wrap', gap: 16 }}>
          <div>
            <h1 style={{ fontSize: '2.1rem', fontWeight: 800, color: '#F8FAFC', margin: 0, letterSpacing: '-0.02em' }}>
              Welcome back, {user?.display_name || user?.name || 'Friend'} ✨
            </h1>
            <p style={{ color: '#94A3B8', fontSize: '0.95rem', marginTop: 6, margin: 0 }}>
              Your dedicated space for mindful connection, emotional clarity, and relationship growth.
            </p>
          </div>

          {/* Streak Badge */}
          <div style={{
            display: 'flex',
            alignItems: 'center',
            gap: 16,
            background: 'rgba(255, 255, 255, 0.04)',
            padding: '12px 20px',
            borderRadius: 16,
            border: '1px solid rgba(255, 255, 255, 0.08)',
          }}>
            <div style={{ textAlign: 'center' }}>
              <span style={{ fontSize: '1.4rem', display: 'block' }}>🔥</span>
              <span style={{ fontSize: '0.7rem', color: '#94A3B8', textTransform: 'uppercase' }}>Streak</span>
              <span style={{ fontSize: '1rem', fontWeight: 700, color: '#F8FAFC', display: 'block' }}>
                {streakData.current_streak} Days
              </span>
            </div>
            <div style={{ width: 1, height: 32, background: 'rgba(255,255,255,0.1)' }} />
            <div style={{ textAlign: 'center' }}>
              <span style={{ fontSize: '1.4rem', display: 'block' }}>⚡</span>
              <span style={{ fontSize: '0.7rem', color: '#94A3B8', textTransform: 'uppercase' }}>XP Points</span>
              <span style={{ fontSize: '1rem', fontWeight: 700, color: '#EC4899', display: 'block' }}>
                {streakData.total_xp}
              </span>
            </div>
          </div>
        </div>

        {/* Stage Hero Banner */}
        <motion.div
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          style={{
            borderRadius: 24,
            padding: '36px',
            marginBottom: 36,
            background: `linear-gradient(135deg, ${config.color}15 0%, rgba(15, 23, 42, 0.8) 100%)`,
            border: `1px solid ${config.color}44`,
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            flexWrap: 'wrap',
            gap: 24,
            boxShadow: `0 15px 35px -10px ${config.color}22`,
          }}
        >
          <div style={{ maxWidth: 680 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 12 }}>
              <span style={{ fontSize: '1.5rem' }}>{config.emoji}</span>
              <span style={{
                background: `${config.color}25`,
                color: config.color,
                fontSize: '0.75rem',
                fontWeight: 700,
                padding: '4px 10px',
                borderRadius: 999,
                textTransform: 'uppercase',
                letterSpacing: '0.06em',
              }}>
                Current Stage Focus
              </span>
            </div>
            <h2 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#F8FAFC', marginBottom: 10 }}>
              {config.title}
            </h2>
            <p style={{ color: '#CBD5E1', fontSize: '0.95rem', lineHeight: 1.5, marginBottom: 20 }}>
              {config.quote}
            </p>
            <div style={{ display: 'flex', gap: 12, flexWrap: 'wrap' }}>
              <Link
                to={config.hubLink}
                style={{
                  textDecoration: 'none',
                  background: config.color,
                  color: '#080B11',
                  fontWeight: 700,
                  fontSize: '0.9rem',
                  padding: '12px 24px',
                  borderRadius: 12,
                  boxShadow: `0 8px 18px ${config.color}44`,
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: 8,
                }}
              >
                Open {config.hubName} →
              </Link>
              <Link
                to="/chat"
                style={{
                  textDecoration: 'none',
                  background: 'rgba(255, 255, 255, 0.08)',
                  color: '#FFFFFF',
                  fontWeight: 600,
                  fontSize: '0.9rem',
                  padding: '12px 24px',
                  borderRadius: 12,
                  border: '1px solid rgba(255, 255, 255, 0.15)',
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: 8,
                }}
              >
                💬 Speak With LoveGuru
              </Link>
            </div>
          </div>

          <div style={{
            background: 'rgba(8, 11, 17, 0.6)',
            padding: '24px',
            borderRadius: 18,
            border: '1px solid rgba(255, 255, 255, 0.08)',
            minWidth: 260,
          }}>
            <h4 style={{ color: '#94A3B8', fontSize: '0.8rem', textTransform: 'uppercase', marginBottom: 12 }}>
              Stage Milestones
            </h4>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, fontSize: '0.85rem', color: '#F8FAFC' }}>
                <span style={{ color: '#10B981' }}>✓</span> Attachment Style Assessed
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, fontSize: '0.85rem', color: '#F8FAFC' }}>
                <span style={{ color: '#10B981' }}>✓</span> Reality Baseline Defined
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, fontSize: '0.85rem', color: '#94A3B8' }}>
                <span style={{ color: '#64748B' }}>○</span> Weekly Reflection Log
              </div>
            </div>
          </div>
        </motion.div>

        {/* 2-Column Grid: Daily Check-in & Quick Tools */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(340px, 1fr))', gap: 24, marginBottom: 36 }}>
          {/* Daily Check-in */}
          <div style={{
            background: 'rgba(15, 23, 42, 0.65)',
            border: '1px solid rgba(255, 255, 255, 0.08)',
            borderRadius: 20,
            padding: '28px',
          }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 16 }}>
              <h3 style={{ fontSize: '1.2rem', fontWeight: 700, color: '#F8FAFC', margin: 0 }}>
                Today's Mindful Check-in
              </h3>
              <span style={{ fontSize: '0.75rem', color: '#EC4899', fontWeight: 600 }}>+15 XP</span>
            </div>

            {checkinDone ? (
              <div style={{ textAlign: 'center', padding: '32px 0' }}>
                <span style={{ fontSize: '3rem', display: 'block', marginBottom: 12 }}>✨</span>
                <h4 style={{ color: '#F8FAFC', marginBottom: 6 }}>Checked in for today!</h4>
                <p style={{ color: '#94A3B8', fontSize: '0.85rem' }}>
                  Your emotional state is logged. Your streak is safe.
                </p>
              </div>
            ) : (
              <>
                <p style={{ color: '#94A3B8', fontSize: '0.85rem', marginBottom: 16 }}>
                  How does your heart feel right now?
                </p>

                <div style={{ display: 'flex', justifyContent: 'space-between', gap: 8, marginBottom: 20 }}>
                  {MOODS.map((m) => {
                    const isSel = selectedMood?.label === m.label
                    return (
                      <button
                        key={m.label}
                        onClick={() => setSelectedMood(m)}
                        style={{
                          flex: 1,
                          padding: '12px 6px',
                          borderRadius: 12,
                          background: isSel ? 'rgba(236, 72, 153, 0.2)' : 'rgba(255, 255, 255, 0.03)',
                          border: isSel ? '1px solid #EC4899' : '1px solid rgba(255, 255, 255, 0.08)',
                          color: '#F8FAFC',
                          cursor: 'pointer',
                          display: 'flex',
                          flexDirection: 'column',
                          alignItems: 'center',
                          gap: 6,
                        }}
                      >
                        <span style={{ fontSize: '1.5rem' }}>{m.emoji}</span>
                        <span style={{ fontSize: '0.75rem', fontWeight: isSel ? 700 : 500 }}>{m.label}</span>
                      </button>
                    )
                  })}
                </div>

                <input
                  type="text"
                  value={gratitudeNote}
                  onChange={(e) => setGratitudeNote(e.target.value)}
                  placeholder="One small thing you appreciate today..."
                  style={{
                    width: '100%',
                    padding: '12px 16px',
                    borderRadius: 10,
                    background: 'rgba(255, 255, 255, 0.04)',
                    border: '1px solid rgba(255, 255, 255, 0.1)',
                    color: '#FFFFFF',
                    fontSize: '0.9rem',
                    marginBottom: 16,
                    outline: 'none',
                  }}
                />

                <button
                  onClick={handleCheckin}
                  style={{
                    width: '100%',
                    padding: '12px',
                    borderRadius: 10,
                    background: 'linear-gradient(135deg, #EC4899, #8B5CF6)',
                    color: '#FFFFFF',
                    fontWeight: 700,
                    fontSize: '0.9rem',
                    border: 'none',
                    cursor: 'pointer',
                  }}
                >
                  Record Check-in & Claim XP
                </button>
              </>
            )}
          </div>

          {/* Quick Stage Hubs Navigation */}
          <div style={{
            background: 'rgba(15, 23, 42, 0.65)',
            border: '1px solid rgba(255, 255, 255, 0.08)',
            borderRadius: 20,
            padding: '28px',
          }}>
            <h3 style={{ fontSize: '1.2rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 16 }}>
              All 4 Relationship Hubs
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 12 }}>
              <Link
                to="/stage1"
                style={{
                  textDecoration: 'none',
                  padding: '16px',
                  borderRadius: 14,
                  background: 'rgba(245, 158, 11, 0.08)',
                  border: '1px solid rgba(245, 158, 11, 0.25)',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: 4,
                }}
              >
                <span style={{ fontSize: '1.4rem' }}>🟡</span>
                <span style={{ fontWeight: 700, color: '#F8FAFC', fontSize: '0.9rem' }}>Stage 1</span>
                <span style={{ fontSize: '0.75rem', color: '#94A3B8' }}>Single & Searching</span>
              </Link>

              <Link
                to="/stage2"
                style={{
                  textDecoration: 'none',
                  padding: '16px',
                  borderRadius: 14,
                  background: 'rgba(16, 185, 129, 0.08)',
                  border: '1px solid rgba(16, 185, 129, 0.25)',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: 4,
                }}
              >
                <span style={{ fontSize: '1.4rem' }}>🟢</span>
                <span style={{ fontWeight: 700, color: '#F8FAFC', fontSize: '0.9rem' }}>Stage 2</span>
                <span style={{ fontSize: '0.75rem', color: '#94A3B8' }}>Finding Love</span>
              </Link>

              <Link
                to="/stage3"
                style={{
                  textDecoration: 'none',
                  padding: '16px',
                  borderRadius: 14,
                  background: 'rgba(59, 130, 246, 0.08)',
                  border: '1px solid rgba(59, 130, 246, 0.25)',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: 4,
                }}
              >
                <span style={{ fontSize: '1.4rem' }}>🔵</span>
                <span style={{ fontWeight: 700, color: '#F8FAFC', fontSize: '0.9rem' }}>Stage 3</span>
                <span style={{ fontSize: '0.75rem', color: '#94A3B8' }}>In Relationship</span>
              </Link>

              <Link
                to="/stage4"
                style={{
                  textDecoration: 'none',
                  padding: '16px',
                  borderRadius: 14,
                  background: 'rgba(244, 63, 94, 0.08)',
                  border: '1px solid rgba(244, 63, 94, 0.25)',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: 4,
                }}
              >
                <span style={{ fontSize: '1.4rem' }}>🔴</span>
                <span style={{ fontWeight: 700, color: '#F8FAFC', fontSize: '0.9rem' }}>Stage 4</span>
                <span style={{ fontSize: '0.75rem', color: '#94A3B8' }}>Breakup Recovery</span>
              </Link>
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}
