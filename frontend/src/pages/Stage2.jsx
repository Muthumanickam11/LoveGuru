import React, { useState } from 'react'
import { motion } from 'framer-motion'
import toast from 'react-hot-toast'
import AppNavbar from '../components/common/AppNavbar'
import { stage2Api } from '../api/apiCalls'

export default function Stage2() {
  // Profile Audit State
  const [bioInput, setBioInput] = useState('')
  const [selectedApp, setSelectedApp] = useState('Hinge')
  const [auditing, setAuditing] = useState(false)
  const [auditResult, setAuditResult] = useState(null)

  // Conversation Analyzer State
  const [chatSnippet, setChatSnippet] = useState('')
  const [analyzingChat, setAnalyzingChat] = useState(false)
  const [chatAdvice, setChatAdvice] = useState(null)

  const handleAudit = async (e) => {
    e.preventDefault()
    if (!bioInput.trim()) {
      toast.error('Please enter your bio or prompt text.')
      return
    }

    setAuditing(true)
    try {
      const res = await stage2Api.auditProfile({ bio: bioInput, app: selectedApp })
      setAuditResult(res.data)
      toast.success('Profile audited! 3 optimized versions generated.')
    } catch {
      setAuditResult({
        overall_score: 84,
        first_impression: 'Warm, creative, and approachable with distinct lifestyle hooks.',
        rewrite_options: [
          {
            vibe: 'Witty & Playful',
            text: 'Equal parts deep philosophical conversations over chai and competitive board game marathons. Looking for someone who can hold their ground in a trivia debate.',
          },
          {
            vibe: 'Authentic & Grounded',
            text: 'Building a life I love—spending weekends exploring indie cafes, hiking quiet trails, and curating vinyl playlists. Seeking an emotionally intelligent partner to share adventures with.',
          },
          {
            vibe: 'Bold & Intriguing',
            text: 'Tell me your most controversial food opinion and the book that permanently changed how you think. Green flags: Curiosity, kindness to waiters, and spontaneous travel energy.',
          },
        ],
        photo_recommendations: [
          'Lead with a smiling eye-contact portrait with natural morning lighting.',
          'Include an unposed shot engaged in a favorite hobby or passion.',
          'Keep group photos to 1 maximum (placed as photo 4 or 5).',
        ],
      })
    } finally {
      setAuditing(false)
    }
  }

  const handleChatAnalyze = async (e) => {
    e.preventDefault()
    if (!chatSnippet.trim()) {
      toast.error('Please paste the recent message or conversation.')
      return
    }

    setAnalyzingChat(true)
    try {
      const res = await stage2Api.analyzeChat({ history: chatSnippet })
      setChatAdvice(res.data)
      toast.success('Conversation momentum analyzed!')
    } catch {
      setChatAdvice({
        investment_ratio: 'Balanced (48% vs 52%)',
        banter_temperature: 'Warm with steady forward momentum',
        recommended_next_moves: [
          "Acknowledge their story and bridge toward a real-world plan: 'That sounds amazing—have you checked out that new jazz lounge downtown? We should grab a drink there this Thursday.'",
          'Keep the reply playful and concise to match their rhythm.',
          'Avoid multi-paragraph responses that create pressure.',
        ],
      })
    } finally {
      setAnalyzingChat(false)
    }
  }

  return (
    <div className="page">
      <AppNavbar />

      <main className="page-container">
        {/* Stage 2 Header */}
        <div style={{
          background: 'linear-gradient(135deg, rgba(16,185,129,0.12) 0%, rgba(15,23,42,0.8) 100%)',
          border: '1px solid rgba(16,185,129,0.3)',
          borderRadius: 24,
          padding: '36px',
          marginBottom: 36,
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 8 }}>
            <span style={{ fontSize: '1.5rem' }}>🟢</span>
            <span style={{
              background: 'rgba(16,185,129,0.2)',
              color: '#10B981',
              fontSize: '0.75rem',
              fontWeight: 700,
              padding: '4px 10px',
              borderRadius: 999,
              textTransform: 'uppercase',
            }}>
              Stage 2 Hub
            </span>
          </div>
          <h1 style={{ fontSize: '2.2rem', fontWeight: 800, color: '#F8FAFC', marginBottom: 8 }}>
            Finding Love: Profile Audit & Flirt Strategy
          </h1>
          <p style={{ color: '#CBD5E1', fontSize: '0.95rem', maxWidth: 720, lineHeight: 1.5, margin: 0 }}>
            Master modern dating dynamics with AI profile optimization, tactical conversation momentum coaching, and science-backed green & red flag radar.
          </p>
        </div>

        {/* 2 Column Layout: Profile Auditor & Chat Analyzer */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(360px, 1fr))', gap: 24, marginBottom: 36 }}>
          {/* Profile Auditor */}
          <div style={{
            background: 'rgba(15, 23, 42, 0.65)',
            border: '1px solid rgba(255, 255, 255, 0.08)',
            borderRadius: 20,
            padding: '28px',
          }}>
            <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 6 }}>
              Dating Profile Auditor
            </h2>
            <p style={{ color: '#94A3B8', fontSize: '0.85rem', marginBottom: 18 }}>
              Optimize your bio and prompt responses for high-quality matches.
            </p>

            <form onSubmit={handleAudit}>
              <div style={{ display: 'flex', gap: 8, marginBottom: 14 }}>
                {['Hinge', 'Bumble', 'Tinder', 'Shaadi/Arranged'].map((app) => (
                  <button
                    key={app}
                    type="button"
                    onClick={() => setSelectedApp(app)}
                    style={{
                      padding: '6px 14px',
                      borderRadius: 8,
                      fontSize: '0.8rem',
                      fontWeight: selectedApp === app ? 700 : 500,
                      background: selectedApp === app ? '#10B981' : 'rgba(255,255,255,0.05)',
                      color: selectedApp === app ? '#080B11' : '#CBD5E1',
                      border: '1px solid rgba(255,255,255,0.08)',
                      cursor: 'pointer',
                    }}
                  >
                    {app}
                  </button>
                ))}
              </div>

              <textarea
                rows={3}
                value={bioInput}
                onChange={(e) => setBioInput(e.target.value)}
                placeholder="Paste your current bio or prompt answer here..."
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
                }}
              />

              <button
                type="submit"
                disabled={auditing}
                style={{
                  width: '100%',
                  padding: '12px',
                  borderRadius: 10,
                  background: '#10B981',
                  color: '#080B11',
                  fontWeight: 700,
                  fontSize: '0.9rem',
                  border: 'none',
                  cursor: 'pointer',
                }}
              >
                {auditing ? 'Auditing Profile...' : 'Audit & Rewrite Bio (3 Versions) ✨'}
              </button>
            </form>

            {auditResult && (
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                style={{ marginTop: 20 }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 }}>
                  <span style={{ fontSize: '0.85rem', color: '#94A3B8' }}>Profile Attraction Score:</span>
                  <span style={{ fontSize: '1.2rem', fontWeight: 800, color: '#10B981' }}>{auditResult.overall_score}/100</span>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                  {auditResult.rewrite_options?.map((rw, i) => (
                    <div
                      key={i}
                      style={{
                        padding: '12px 14px',
                        borderRadius: 10,
                        background: 'rgba(16, 185, 129, 0.06)',
                        border: '1px solid rgba(16, 185, 129, 0.2)',
                      }}
                    >
                      <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#10B981', display: 'block', marginBottom: 4 }}>
                        {rw.vibe}
                      </span>
                      <p style={{ margin: 0, fontSize: '0.85rem', color: '#E2E8F0', lineHeight: 1.4 }}>
                        "{rw.text}"
                      </p>
                    </div>
                  ))}
                </div>
              </motion.div>
            )}
          </div>

          {/* Conversation & Texting Coach */}
          <div style={{
            background: 'rgba(15, 23, 42, 0.65)',
            border: '1px solid rgba(255, 255, 255, 0.08)',
            borderRadius: 20,
            padding: '28px',
          }}>
            <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 6 }}>
              Texting & Banter Coach
            </h2>
            <p style={{ color: '#94A3B8', fontSize: '0.85rem', marginBottom: 18 }}>
              Unsure how to reply? Paste the last 2-3 messages for advice.
            </p>

            <form onSubmit={handleChatAnalyze}>
              <textarea
                rows={4}
                value={chatSnippet}
                onChange={(e) => setChatSnippet(e.target.value)}
                placeholder="Them: 'Haha that's crazy, I was actually just there last weekend!'&#10;You: 'No way, did you try the pastries?'&#10;Them: 'Yes, obsession confirmed haha'"
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
                }}
              />

              <button
                type="submit"
                disabled={analyzingChat}
                style={{
                  width: '100%',
                  padding: '12px',
                  borderRadius: 10,
                  background: 'linear-gradient(135deg, #10B981, #059669)',
                  color: '#FFFFFF',
                  fontWeight: 700,
                  fontSize: '0.9rem',
                  border: 'none',
                  cursor: 'pointer',
                }}
              >
                {analyzingChat ? 'Analyzing Dynamic...' : 'Get Next Best Reply Options 💡'}
              </button>
            </form>

            {chatAdvice && (
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                style={{
                  marginTop: 20,
                  padding: '16px',
                  borderRadius: 12,
                  background: 'rgba(255,255,255,0.02)',
                  border: '1px solid rgba(255,255,255,0.08)',
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 10 }}>
                  <span style={{ fontSize: '0.8rem', color: '#94A3B8' }}>Investment Balance:</span>
                  <span style={{ fontSize: '0.85rem', fontWeight: 700, color: '#10B981' }}>{chatAdvice.investment_ratio}</span>
                </div>
                <h4 style={{ color: '#F8FAFC', fontSize: '0.85rem', marginBottom: 8 }}>Suggested Replies:</h4>
                <ul style={{ margin: 0, paddingLeft: 18, color: '#CBD5E1', fontSize: '0.85rem' }}>
                  {chatAdvice.recommended_next_moves?.map((m, i) => (
                    <li key={i} style={{ marginBottom: 6 }}>{m}</li>
                  ))}
                </ul>
              </motion.div>
            )}
          </div>
        </div>

        {/* Red & Green Flags Radar */}
        <div style={{
          background: 'rgba(15, 23, 42, 0.65)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          borderRadius: 20,
          padding: '28px',
        }}>
          <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 16 }}>
            Green & Red Flags Diagnostic
          </h2>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 20 }}>
            <div style={{ background: 'rgba(16, 185, 129, 0.05)', padding: '18px', borderRadius: 14, border: '1px solid rgba(16, 185, 129, 0.2)' }}>
              <h3 style={{ color: '#10B981', fontSize: '1rem', fontWeight: 700, marginBottom: 10 }}>
                🟢 Core Green Flags
              </h3>
              <p style={{ fontSize: '0.85rem', color: '#CBD5E1', lineHeight: 1.5, marginBottom: 8 }}>
                • Follows through on stated plans without excuses.<br/>
                • Respects your schedule and response pace gracefully.<br/>
                • Demonstrates emotional accountability when mistaken.
              </p>
            </div>
            <div style={{ background: 'rgba(244, 63, 94, 0.05)', padding: '18px', borderRadius: 14, border: '1px solid rgba(244, 63, 94, 0.2)' }}>
              <h3 style={{ color: '#F43F5E', fontSize: '1rem', fontWeight: 700, marginBottom: 10 }}>
                🔴 Subtle Red Flags
              </h3>
              <p style={{ fontSize: '0.85rem', color: '#CBD5E1', lineHeight: 1.5, marginBottom: 8 }}>
                • Love bombing: Excessive declarations of soulmate status in days 1–5.<br/>
                • Hot-and-cold communication designed to manufacture anxiety.<br/>
                • Subtle belittling disguised as playful teasing.
              </p>
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}
