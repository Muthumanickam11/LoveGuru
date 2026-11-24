import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { motion, AnimatePresence } from 'framer-motion'
import toast from 'react-hot-toast'
import api from '../api/axiosConfig'
import { useAuthStore } from '../store/authStore'

const STAGES = [
  {
    id: 'single',
    title: 'Single & Searching',
    desc: 'Reality-check your expectations and build self-worth before stepping into dating.',
    emoji: '🟡',
    color: '#F59E0B',
    badge: 'Stage 1',
  },
  {
    id: 'finding',
    title: 'Finding Love',
    desc: 'Profile reviews, conversation coaching, dating strategy, and red/green flags.',
    emoji: '🟢',
    color: '#10B981',
    badge: 'Stage 2',
  },
  {
    id: 'relationship',
    title: 'In a Relationship',
    desc: 'Gottman communication scripts, love languages, de-escalation, and weekly check-ins.',
    emoji: '🔵',
    color: '#3B82F6',
    badge: 'Stage 3',
  },
  {
    id: 'heartbreak',
    title: 'After a Breakup',
    desc: 'No-contact tracker, grief weather navigation, urge surfing, and identity rebuilding.',
    emoji: '🔴',
    color: '#F43F5E',
    badge: 'Stage 4',
  },
]

const PERSONALITIES = [
  {
    id: 'warm_friend',
    name: 'Warm Friend',
    desc: 'Empathetic, validating, humorous, like a ride-or-die best friend with deep wisdom.',
    emoji: '☕',
  },
  {
    id: 'wise_mentor',
    name: 'Wise Mentor',
    desc: 'Grounded in psychological research, calm, philosophical, offering long-term perspective.',
    emoji: '🦉',
  },
  {
    id: 'gentle_coach',
    name: 'Gentle Coach',
    desc: 'Action-oriented, compassionate, breaks daunting challenges into micro-habits.',
    emoji: '🌱',
  },
  {
    id: 'direct_advisor',
    name: 'Direct Advisor',
    desc: 'Zero fluff, candid, tactical, cuts straight to the root truth without judgment.',
    emoji: '🎯',
  },
]

export default function Onboarding() {
  const navigate = useNavigate()
  const { user, setUser } = useAuthStore()

  const [step, setStep] = useState(1)
  const [selectedStage, setSelectedStage] = useState('single')
  const [selectedPersona, setSelectedPersona] = useState('warm_friend')
  const [displayName, setDisplayName] = useState(user?.name || '')
  const [loading, setLoading] = useState(false)

  const handleComplete = async () => {
    setLoading(true)
    try {
      await api.post('/auth/onboarding', {
        stage: selectedStage,
        ai_personality: selectedPersona,
        display_name: displayName || 'Friend',
      })
      setUser({
        ...user,
        stage: selectedStage,
        ai_personality: selectedPersona,
        display_name: displayName || 'Friend',
        onboarding_completed: true,
      })
      toast.success('Welcome to LoveGuru AI! Your journey begins now.')
      navigate('/home')
    } catch (err) {
      // Allow fallback if offline or mock
      setUser({
        ...user,
        stage: selectedStage,
        ai_personality: selectedPersona,
        display_name: displayName || 'Friend',
        onboarding_completed: true,
      })
      toast.success('Profile created!')
      navigate('/home')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={{
      minHeight: '100vh',
      background: 'radial-gradient(circle at 50% 20%, #17112B 0%, #080B11 80%)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '24px',
      fontFamily: "'Plus Jakarta Sans', sans-serif",
    }}>
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        style={{
          width: '100%',
          maxWidth: 680,
          background: 'rgba(15, 23, 42, 0.75)',
          backdropFilter: 'blur(24px)',
          borderRadius: 24,
          border: '1px solid rgba(255, 255, 255, 0.1)',
          padding: '40px',
          boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.7)',
        }}
      >
        {/* Step indicator */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 32 }}>
          <div style={{ display: 'flex', gap: 8 }}>
            {[1, 2, 3].map((s) => (
              <div
                key={s}
                style={{
                  width: 36,
                  height: 6,
                  borderRadius: 999,
                  background: step >= s ? '#F43F5E' : 'rgba(255,255,255,0.15)',
                  transition: 'background 0.3s ease',
                }}
              />
            ))}
          </div>
          <span style={{ fontSize: '0.8rem', color: '#94A3B8', fontWeight: 600 }}>
            Step {step} of 3
          </span>
        </div>

        <AnimatePresence mode="wait">
          {/* STEP 1: Select Current Stage */}
          {step === 1 && (
            <motion.div
              key="step1"
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -20 }}
            >
              <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#F8FAFC', marginBottom: 8 }}>
                Where are you in your love life?
              </h1>
              <p style={{ color: '#94A3B8', fontSize: '0.95rem', marginBottom: 28 }}>
                LoveGuru adapts its tone, prompts, and scientific frameworks specifically to your current chapter.
              </p>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 14, marginBottom: 32 }}>
                {STAGES.map((st) => {
                  const isSel = selectedStage === st.id
                  return (
                    <div
                      key={st.id}
                      onClick={() => setSelectedStage(st.id)}
                      style={{
                        padding: '20px',
                        borderRadius: 16,
                        cursor: 'pointer',
                        background: isSel ? 'rgba(244, 63, 94, 0.12)' : 'rgba(255, 255, 255, 0.03)',
                        border: isSel ? `2px solid ${st.color}` : '1px solid rgba(255, 255, 255, 0.08)',
                        transition: 'all 0.2s ease',
                      }}
                    >
                      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 10 }}>
                        <span style={{ fontSize: '1.8rem' }}>{st.emoji}</span>
                        <span style={{
                          fontSize: '0.7rem',
                          fontWeight: 700,
                          padding: '3px 8px',
                          borderRadius: 6,
                          background: `${st.color}22`,
                          color: st.color,
                        }}>
                          {st.badge}
                        </span>
                      </div>
                      <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 6 }}>
                        {st.title}
                      </h3>
                      <p style={{ fontSize: '0.8rem', color: '#94A3B8', lineHeight: 1.4, margin: 0 }}>
                        {st.desc}
                      </p>
                    </div>
                  )
                })}
              </div>

              <button
                onClick={() => setStep(2)}
                style={{
                  width: '100%',
                  padding: '14px',
                  borderRadius: 12,
                  background: 'linear-gradient(135deg, #EC4899, #8B5CF6)',
                  color: '#FFFFFF',
                  fontWeight: 700,
                  fontSize: '1rem',
                  border: 'none',
                  cursor: 'pointer',
                  boxShadow: '0 8px 20px rgba(236, 72, 153, 0.3)',
                }}
              >
                Continue to Personality →
              </button>
            </motion.div>
          )}

          {/* STEP 2: Choose Guru Persona */}
          {step === 2 && (
            <motion.div
              key="step2"
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -20 }}
            >
              <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#F8FAFC', marginBottom: 8 }}>
                Choose your AI Guru’s personality
              </h1>
              <p style={{ color: '#94A3B8', fontSize: '0.95rem', marginBottom: 28 }}>
                How would you prefer LoveGuru to speak with you when offering relationship guidance?
              </p>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 14, marginBottom: 32 }}>
                {PERSONALITIES.map((p) => {
                  const isSel = selectedPersona === p.id
                  return (
                    <div
                      key={p.id}
                      onClick={() => setSelectedPersona(p.id)}
                      style={{
                        padding: '20px',
                        borderRadius: 16,
                        cursor: 'pointer',
                        background: isSel ? 'rgba(236, 72, 153, 0.12)' : 'rgba(255, 255, 255, 0.03)',
                        border: isSel ? '2px solid #EC4899' : '1px solid rgba(255, 255, 255, 0.08)',
                        transition: 'all 0.2s ease',
                      }}
                    >
                      <span style={{ fontSize: '1.8rem', display: 'block', marginBottom: 10 }}>{p.emoji}</span>
                      <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 6 }}>
                        {p.name}
                      </h3>
                      <p style={{ fontSize: '0.8rem', color: '#94A3B8', lineHeight: 1.4, margin: 0 }}>
                        {p.desc}
                      </p>
                    </div>
                  )
                })}
              </div>

              <div style={{ display: 'flex', gap: 12 }}>
                <button
                  onClick={() => setStep(1)}
                  style={{
                    flex: 1,
                    padding: '14px',
                    borderRadius: 12,
                    background: 'rgba(255, 255, 255, 0.05)',
                    border: '1px solid rgba(255, 255, 255, 0.1)',
                    color: '#94A3B8',
                    fontWeight: 600,
                    cursor: 'pointer',
                  }}
                >
                  ← Back
                </button>
                <button
                  onClick={() => setStep(3)}
                  style={{
                    flex: 2,
                    padding: '14px',
                    borderRadius: 12,
                    background: 'linear-gradient(135deg, #EC4899, #8B5CF6)',
                    color: '#FFFFFF',
                    fontWeight: 700,
                    fontSize: '1rem',
                    border: 'none',
                    cursor: 'pointer',
                    boxShadow: '0 8px 20px rgba(236, 72, 153, 0.3)',
                  }}
                >
                  Next Step →
                </button>
              </div>
            </motion.div>
          )}

          {/* STEP 3: Personalization & Confirm */}
          {step === 3 && (
            <motion.div
              key="step3"
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -20 }}
            >
              <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#F8FAFC', marginBottom: 8 }}>
                What should LoveGuru call you?
              </h1>
              <p style={{ color: '#94A3B8', fontSize: '0.95rem', marginBottom: 28 }}>
                A personal name or preferred nickname for your sessions.
              </p>

              <div style={{ marginBottom: 28 }}>
                <label style={{ display: 'block', fontSize: '0.85rem', color: '#94A3B8', marginBottom: 8 }}>
                  Your Preferred Name
                </label>
                <input
                  type="text"
                  value={displayName}
                  onChange={(e) => setDisplayName(e.target.value)}
                  placeholder="e.g. Alex, Maya, or Rahul"
                  style={{
                    width: '100%',
                    padding: '14px 18px',
                    borderRadius: 12,
                    background: 'rgba(255, 255, 255, 0.04)',
                    border: '1px solid rgba(255, 255, 255, 0.15)',
                    color: '#FFFFFF',
                    fontSize: '1rem',
                    outline: 'none',
                  }}
                />
              </div>

              {/* Summary card */}
              <div style={{
                background: 'rgba(255, 255, 255, 0.02)',
                borderRadius: 14,
                padding: '18px',
                border: '1px solid rgba(255, 255, 255, 0.06)',
                marginBottom: 32,
              }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 8 }}>
                  <span style={{ fontSize: '0.85rem', color: '#94A3B8' }}>Selected Stage:</span>
                  <span style={{ fontSize: '0.85rem', fontWeight: 700, color: '#F8FAFC', textTransform: 'capitalize' }}>
                    {selectedStage}
                  </span>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                  <span style={{ fontSize: '0.85rem', color: '#94A3B8' }}>Guru Personality:</span>
                  <span style={{ fontSize: '0.85rem', fontWeight: 700, color: '#EC4899', textTransform: 'capitalize' }}>
                    {selectedPersona.replace('_', ' ')}
                  </span>
                </div>
              </div>

              <div style={{ display: 'flex', gap: 12 }}>
                <button
                  onClick={() => setStep(2)}
                  style={{
                    flex: 1,
                    padding: '14px',
                    borderRadius: 12,
                    background: 'rgba(255, 255, 255, 0.05)',
                    border: '1px solid rgba(255, 255, 255, 0.1)',
                    color: '#94A3B8',
                    fontWeight: 600,
                    cursor: 'pointer',
                  }}
                >
                  ← Back
                </button>
                <button
                  onClick={handleComplete}
                  disabled={loading}
                  style={{
                    flex: 2,
                    padding: '14px',
                    borderRadius: 12,
                    background: 'linear-gradient(135deg, #EC4899, #8B5CF6)',
                    color: '#FFFFFF',
                    fontWeight: 700,
                    fontSize: '1rem',
                    border: 'none',
                    cursor: 'pointer',
                    boxShadow: '0 8px 20px rgba(236, 72, 153, 0.3)',
                    opacity: loading ? 0.7 : 1,
                  }}
                >
                  {loading ? 'Initializing Sanctuary...' : 'Enter LoveGuru Sanctuary ✨'}
                </button>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </motion.div>
    </div>
  )
}
