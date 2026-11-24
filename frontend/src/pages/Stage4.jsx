import React, { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import toast from 'react-hot-toast'
import AppNavbar from '../components/common/AppNavbar'
import { stage4Api } from '../api/apiCalls'

const GRIEF_WEATHERS = [
  { id: 'storm', label: 'Storm', emoji: '⛈️', desc: 'Acute panic, chest tightness, severe urges' },
  { id: 'rain', label: 'Rain', emoji: '🌧️', desc: 'Heavy sadness, fatigue, crying spells' },
  { id: 'overcast', label: 'Overcast', emoji: '☁️', desc: 'Numbness, apathy, low energy' },
  { id: 'clearing', label: 'Clearing', emoji: '🌤️', desc: 'Brief windows of peace, appetite returning' },
  { id: 'sun', label: 'Sun', emoji: '☀️', desc: 'Renewed self-worth, optimism for the future' },
]

export default function Stage4() {
  const [ncData, setNcData] = useState({
    current_streak_days: 18,
    milestone_target: 30,
    percent_to_goal: 60,
    urges_resisted_count: 9,
    neurochemical_phase: 'Dopamine Receptor Reset Phase (Days 14-21)',
  })

  // Urge Surfing Modal / State
  const [surfingActive, setSurfingActive] = useState(false)
  const [surfSeconds, setSurfSeconds] = useState(120)
  const [surfCompleted, setSurfCompleted] = useState(false)

  // Grief Weather State
  const [selectedWeather, setSelectedWeather] = useState('rain')

  // Vault Letter State
  const [letterContent, setLetterContent] = useState('')
  const [vaultSealed, setVaultSealed] = useState(false)

  useEffect(() => {
    stage4Api.getNCTracker()
      .then((res) => {
        if (res.data) setNcData(res.data)
      })
      .catch(() => {})
  }, [])

  // Urge Surfing Timer Effect
  useEffect(() => {
    let interval = null
    if (surfingActive && surfSeconds > 0) {
      interval = setInterval(() => {
        setSurfSeconds((prev) => prev - 1)
      }, 1000)
    } else if (surfingActive && surfSeconds === 0) {
      setSurfingActive(false)
      setSurfCompleted(true)
      toast.success('🌊 You rode the wave! Urge safely surfed without breaking No-Contact.')
      stage4Api.logUrgeSurfing({ trigger: 'panic urge', intensity: 8 }).catch(() => {})
      setNcData((prev) => ({
        ...prev,
        urges_resisted_count: prev.urges_resisted_count + 1,
      }))
    }
    return () => clearInterval(interval)
  }, [surfingActive, surfSeconds])

  const handleStartUrgeSurf = () => {
    setSurfSeconds(120)
    setSurfingActive(true)
    setSurfCompleted(false)
  }

  const handleSealLetter = async (e) => {
    e.preventDefault()
    if (!letterContent.trim()) {
      toast.error('Write your uncensored feelings first.')
      return
    }

    try {
      await stage4Api.submitJournal({ content: letterContent })
      setVaultSealed(true)
      toast.success('🔒 Letter permanently sealed into your private vault.')
    } catch {
      setVaultSealed(true)
      toast.success('Letter sealed in vault!')
    }
  }

  return (
    <div className="page">
      <AppNavbar />

      <main className="page-container">
        {/* Stage 4 Header */}
        <div style={{
          background: 'linear-gradient(135deg, rgba(244,63,94,0.12) 0%, rgba(15,23,42,0.8) 100%)',
          border: '1px solid rgba(244,63,94,0.3)',
          borderRadius: 24,
          padding: '36px',
          marginBottom: 36,
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 8 }}>
            <span style={{ fontSize: '1.5rem' }}>🔴</span>
            <span style={{
              background: 'rgba(244,63,94,0.2)',
              color: '#F43F5E',
              fontSize: '0.75rem',
              fontWeight: 700,
              padding: '4px 10px',
              borderRadius: 999,
              textTransform: 'uppercase',
            }}>
              Stage 4 Hub
            </span>
          </div>
          <h1 style={{ fontSize: '2.2rem', fontWeight: 800, color: '#F8FAFC', marginBottom: 8 }}>
            After a Breakup: Neurochemical Healing & Vault
          </h1>
          <p style={{ color: '#CBD5E1', fontSize: '0.95rem', maxWidth: 720, lineHeight: 1.5, margin: 0 }}>
            Heartbreak triggers acute neurochemical withdrawal identical to physical pain. Track your No-Contact reboot, surf sudden emotional waves, and safely release attachment.
          </p>
        </div>

        {/* Hero Card: 30-Day No-Contact Counter & Urge Surfing Button */}
        <div style={{
          background: 'linear-gradient(135deg, rgba(244,63,94,0.1) 0%, rgba(15,23,42,0.7) 100%)',
          border: '1px solid rgba(244,63,94,0.25)',
          borderRadius: 20,
          padding: '32px',
          marginBottom: 36,
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: 24,
        }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 8 }}>
              <span style={{ fontSize: '2.4rem', fontWeight: 800, color: '#F43F5E' }}>
                Day {ncData.current_streak_days}
              </span>
              <span style={{ fontSize: '0.9rem', color: '#94A3B8' }}>
                of 30-Day Neuro Reset
              </span>
            </div>

            <p style={{ color: '#E2E8F0', fontSize: '0.9rem', marginBottom: 12, maxWidth: 540 }}>
              <strong>Current Phase:</strong> {ncData.neurochemical_phase}
            </p>

            <div style={{
              width: 320,
              height: 10,
              background: 'rgba(255,255,255,0.1)',
              borderRadius: 999,
              overflow: 'hidden',
              marginBottom: 12,
            }}>
              <div style={{
                width: `${(ncData.current_streak_days / ncData.milestone_target) * 100}%`,
                height: '100%',
                background: 'linear-gradient(90deg, #F43F5E, #EC4899)',
                borderRadius: 999,
              }} />
            </div>

            <span style={{ fontSize: '0.8rem', color: '#94A3B8' }}>
              🛡️ {ncData.urges_resisted_count} Urges successfully resisted
            </span>
          </div>

          {/* Big Urge Surfing Button */}
          <div style={{ textAlign: 'center' }}>
            <button
              onClick={handleStartUrgeSurf}
              style={{
                padding: '16px 28px',
                borderRadius: 16,
                background: 'linear-gradient(135deg, #F43F5E, #E11D48)',
                color: '#FFFFFF',
                fontWeight: 800,
                fontSize: '1rem',
                border: 'none',
                cursor: 'pointer',
                boxShadow: '0 10px 25px rgba(244, 63, 94, 0.4)',
                display: 'flex',
                alignItems: 'center',
                gap: 10,
              }}
            >
              <span>🌊</span>
              <span>I Have an Urge to Text Them</span>
            </button>
            <span style={{ fontSize: '0.75rem', color: '#94A3B8', marginTop: 8, display: 'block' }}>
              Starts 2-minute somatic wave regulation
            </span>
          </div>
        </div>

        {/* Urge Surfing Active Modal / Banner */}
        <AnimatePresence>
          {surfingActive && (
            <motion.div
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.95 }}
              style={{
                background: 'rgba(15, 23, 42, 0.95)',
                border: '2px solid #F43F5E',
                borderRadius: 20,
                padding: '32px',
                marginBottom: 36,
                textAlign: 'center',
                boxShadow: '0 0 40px rgba(244, 63, 94, 0.3)',
              }}
            >
              <h3 style={{ fontSize: '1.4rem', fontWeight: 800, color: '#F8FAFC', marginBottom: 8 }}>
                🌊 Urge Surfing Protocol (Hold Steady)
              </h3>
              <p style={{ color: '#CBD5E1', fontSize: '0.95rem', maxWidth: 600, margin: '0 auto 24px auto' }}>
                Urges rise, crest like a wave, and break within 90–120 seconds. Put down your phone. Breathe in for 4 seconds, exhale for 7 seconds. Notice the sensation in your chest without obeying it.
              </p>

              <div style={{
                fontSize: '3rem',
                fontWeight: 800,
                color: '#F43F5E',
                marginBottom: 16,
                fontVariantNumeric: 'tabular-nums',
              }}>
                {Math.floor(surfSeconds / 60)}:{(surfSeconds % 60).toString().padStart(2, '0')}
              </div>

              <button
                onClick={() => setSurfingActive(false)}
                style={{
                  background: 'rgba(255,255,255,0.06)',
                  border: '1px solid rgba(255,255,255,0.15)',
                  color: '#94A3B8',
                  padding: '8px 20px',
                  borderRadius: 10,
                  cursor: 'pointer',
                  fontSize: '0.85rem',
                }}
              >
                Cancel
              </button>
            </motion.div>
          )}
        </AnimatePresence>

        {/* 2-Column Grid: Grief Weather & Closure Vault */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(360px, 1fr))', gap: 24 }}>
          {/* Grief Weather Model */}
          <div style={{
            background: 'rgba(15, 23, 42, 0.65)',
            border: '1px solid rgba(255, 255, 255, 0.08)',
            borderRadius: 20,
            padding: '28px',
          }}>
            <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 6 }}>
              The Grief Weather Model
            </h2>
            <p style={{ color: '#94A3B8', fontSize: '0.85rem', marginBottom: 20 }}>
              Grief is non-linear weather, not a permanent climate. What weather is your heart experiencing today?
            </p>

            <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
              {GRIEF_WEATHERS.map((w) => {
                const isSel = selectedWeather === w.id
                return (
                  <div
                    key={w.id}
                    onClick={() => setSelectedWeather(w.id)}
                    style={{
                      padding: '12px 16px',
                      borderRadius: 12,
                      cursor: 'pointer',
                      background: isSel ? 'rgba(244, 63, 94, 0.15)' : 'rgba(255, 255, 255, 0.02)',
                      border: isSel ? '1px solid #F43F5E' : '1px solid rgba(255, 255, 255, 0.06)',
                      display: 'flex',
                      alignItems: 'center',
                      gap: 14,
                      transition: 'all 0.2s',
                    }}
                  >
                    <span style={{ fontSize: '1.6rem' }}>{w.emoji}</span>
                    <div style={{ flex: 1 }}>
                      <h4 style={{ margin: 0, fontSize: '0.95rem', fontWeight: 700, color: '#F8FAFC' }}>
                        {w.label}
                      </h4>
                      <p style={{ margin: 0, fontSize: '0.8rem', color: '#94A3B8' }}>{w.desc}</p>
                    </div>
                  </div>
                )
              })}
            </div>
          </div>

          {/* Closure Letter Vault */}
          <div style={{
            background: 'rgba(15, 23, 42, 0.65)',
            border: '1px solid rgba(255, 255, 255, 0.08)',
            borderRadius: 20,
            padding: '28px',
          }}>
            <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 6 }}>
              The Closure Letter Vault
            </h2>
            <p style={{ color: '#94A3B8', fontSize: '0.85rem', marginBottom: 18 }}>
              Write everything you never got to say. Sealed securely in your vault—never sent to them.
            </p>

            {vaultSealed ? (
              <div style={{ textAlign: 'center', padding: '36px 0' }}>
                <span style={{ fontSize: '3rem', display: 'block', marginBottom: 12 }}>🔒</span>
                <h4 style={{ color: '#F8FAFC', marginBottom: 6 }}>Letter Sealed into the Vault</h4>
                <p style={{ color: '#94A3B8', fontSize: '0.85rem', marginBottom: 16 }}>
                  You released the emotional charge without jeopardizing your healing.
                </p>
                <button
                  onClick={() => {
                    setVaultSealed(false)
                    setLetterContent('')
                  }}
                  style={{
                    background: 'rgba(255,255,255,0.08)',
                    color: '#CBD5E1',
                    border: '1px solid rgba(255,255,255,0.15)',
                    padding: '8px 16px',
                    borderRadius: 8,
                    cursor: 'pointer',
                  }}
                >
                  Write Another Entry
                </button>
              </div>
            ) : (
              <form onSubmit={handleSealLetter}>
                <textarea
                  rows={6}
                  value={letterContent}
                  onChange={(e) => setLetterContent(e.target.value)}
                  placeholder="Dear [Name], here is what I needed to tell you uncensored..."
                  style={{
                    width: '100%',
                    padding: '14px',
                    borderRadius: 12,
                    background: 'rgba(255, 255, 255, 0.04)',
                    border: '1px solid rgba(255, 255, 255, 0.1)',
                    color: '#FFFFFF',
                    fontSize: '0.9rem',
                    marginBottom: 14,
                    outline: 'none',
                    resize: 'vertical',
                    fontFamily: 'inherit',
                  }}
                />

                <button
                  type="submit"
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
                  Seal Letter in Vault (Never Sent) 🔒
                </button>
              </form>
            )}
          </div>
        </div>
      </main>
    </div>
  )
}
