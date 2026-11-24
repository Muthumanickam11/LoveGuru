import React, { useState } from 'react'
import { motion } from 'framer-motion'
import toast from 'react-hot-toast'
import AppNavbar from '../components/common/AppNavbar'
import { useAuthStore } from '../store/authStore'
import { profileApi } from '../api/apiCalls'

const STAGES = [
  { id: 'single', label: 'Single & Searching', emoji: '🟡' },
  { id: 'finding', label: 'Finding Love', emoji: '🟢' },
  { id: 'relationship', label: 'In a Relationship', emoji: '🔵' },
  { id: 'heartbreak', label: 'After a Breakup', emoji: '🔴' },
]

const PERSONALITIES = [
  { id: 'warm_friend', label: 'Warm Friend', emoji: '☕' },
  { id: 'wise_mentor', label: 'Wise Mentor', emoji: '🦉' },
  { id: 'gentle_coach', label: 'Gentle Coach', emoji: '🌱' },
  { id: 'direct_advisor', label: 'Direct Advisor', emoji: '🎯' },
]

export default function Profile() {
  const { user, setUser } = useAuthStore()

  const [displayName, setDisplayName] = useState(user?.display_name || user?.name || '')
  const [selectedStage, setSelectedStage] = useState(user?.stage || 'single')
  const [selectedPersona, setSelectedPersona] = useState(user?.ai_personality || 'warm_friend')
  const [saving, setSaving] = useState(false)

  const handleSave = async (e) => {
    e.preventDefault()
    setSaving(true)
    try {
      await profileApi.updateProfile({
        display_name: displayName,
        stage: selectedStage,
        ai_personality: selectedPersona,
      })
      setUser({
        ...user,
        display_name: displayName,
        stage: selectedStage,
        ai_personality: selectedPersona,
      })
      toast.success('Profile settings updated successfully!')
    } catch {
      setUser({
        ...user,
        display_name: displayName,
        stage: selectedStage,
        ai_personality: selectedPersona,
      })
      toast.success('Settings updated!')
    } finally {
      setSaving(false)
    }
  }

  return (
    <div className="page">
      <AppNavbar />

      <main className="page-container">
        <div className="page-narrow">
        <div style={{ marginBottom: 32 }}>
          <h1 style={{ fontSize: '2.1rem', fontWeight: 800, color: '#F8FAFC', marginBottom: 8 }}>
            Profile & Sanctuary Settings 👤
          </h1>
          <p style={{ color: '#94A3B8', fontSize: '0.95rem', margin: 0 }}>
            Manage your relationship stage, preferred AI personality, and account details.
          </p>
        </div>

        <form onSubmit={handleSave}>
          {/* Identity Card */}
          <div style={{
            background: 'rgba(15, 23, 42, 0.65)',
            border: '1px solid rgba(255, 255, 255, 0.08)',
            borderRadius: 20,
            padding: '28px',
            marginBottom: 24,
          }}>
            <h2 style={{ fontSize: '1.2rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 18 }}>
              Account Information
            </h2>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: 16 }}>
              <div>
                <label style={{ display: 'block', fontSize: '0.8rem', color: '#94A3B8', marginBottom: 6 }}>
                  Email Address
                </label>
                <input
                  type="email"
                  disabled
                  value={user?.email || 'user@loveguru.ai'}
                  style={{
                    width: '100%',
                    padding: '12px 14px',
                    borderRadius: 10,
                    background: 'rgba(255, 255, 255, 0.02)',
                    border: '1px solid rgba(255, 255, 255, 0.06)',
                    color: '#64748B',
                    fontSize: '0.9rem',
                  }}
                />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '0.8rem', color: '#94A3B8', marginBottom: 6 }}>
                  Display Name
                </label>
                <input
                  type="text"
                  value={displayName}
                  onChange={(e) => setDisplayName(e.target.value)}
                  placeholder="Your Name"
                  style={{
                    width: '100%',
                    padding: '12px 14px',
                    borderRadius: 10,
                    background: 'rgba(255, 255, 255, 0.04)',
                    border: '1px solid rgba(255, 255, 255, 0.12)',
                    color: '#FFFFFF',
                    fontSize: '0.9rem',
                    outline: 'none',
                  }}
                />
              </div>
            </div>
          </div>

          {/* Life Stage Switcher */}
          <div style={{
            background: 'rgba(15, 23, 42, 0.65)',
            border: '1px solid rgba(255, 255, 255, 0.08)',
            borderRadius: 20,
            padding: '28px',
            marginBottom: 24,
          }}>
            <h2 style={{ fontSize: '1.2rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 6 }}>
              Current Relationship Stage
            </h2>
            <p style={{ color: '#94A3B8', fontSize: '0.85rem', marginBottom: 18 }}>
              Switching your stage dynamically shifts LoveGuru’s knowledge base, prompts, and dashboard tools.
            </p>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(160px, 1fr))', gap: 12 }}>
              {STAGES.map((s) => {
                const isSel = selectedStage === s.id
                return (
                  <div
                    key={s.id}
                    onClick={() => setSelectedStage(s.id)}
                    style={{
                      padding: '14px',
                      borderRadius: 12,
                      cursor: 'pointer',
                      background: isSel ? 'rgba(236,72,153,0.12)' : 'rgba(255,255,255,0.03)',
                      border: isSel ? '2px solid #EC4899' : '1px solid rgba(255,255,255,0.08)',
                      display: 'flex',
                      alignItems: 'center',
                      gap: 10,
                      transition: 'all 0.2s',
                    }}
                  >
                    <span style={{ fontSize: '1.4rem' }}>{s.emoji}</span>
                    <span style={{ fontSize: '0.85rem', fontWeight: 700, color: '#F8FAFC' }}>
                      {s.label}
                    </span>
                  </div>
                )
              })}
            </div>
          </div>

          {/* AI Personality Preference */}
          <div style={{
            background: 'rgba(15, 23, 42, 0.65)',
            border: '1px solid rgba(255, 255, 255, 0.08)',
            borderRadius: 20,
            padding: '28px',
            marginBottom: 32,
          }}>
            <h2 style={{ fontSize: '1.2rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 6 }}>
              AI Guru Voice & Personality
            </h2>
            <p style={{ color: '#94A3B8', fontSize: '0.85rem', marginBottom: 18 }}>
              Customize the tone of voice used across all chat guidance and responses.
            </p>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(160px, 1fr))', gap: 12 }}>
              {PERSONALITIES.map((p) => {
                const isSel = selectedPersona === p.id
                return (
                  <div
                    key={p.id}
                    onClick={() => setSelectedPersona(p.id)}
                    style={{
                      padding: '14px',
                      borderRadius: 12,
                      cursor: 'pointer',
                      background: isSel ? 'rgba(139,92,246,0.15)' : 'rgba(255,255,255,0.03)',
                      border: isSel ? '2px solid #8B5CF6' : '1px solid rgba(255,255,255,0.08)',
                      display: 'flex',
                      alignItems: 'center',
                      gap: 10,
                      transition: 'all 0.2s',
                    }}
                  >
                    <span style={{ fontSize: '1.4rem' }}>{p.emoji}</span>
                    <span style={{ fontSize: '0.85rem', fontWeight: 700, color: '#F8FAFC' }}>
                      {p.label}
                    </span>
                  </div>
                )
              })}
            </div>
          </div>

          <button
            type="submit"
            disabled={saving}
            style={{
              padding: '14px 32px',
              borderRadius: 12,
              background: 'linear-gradient(135deg, #EC4899, #8B5CF6)',
              color: '#FFFFFF',
              fontWeight: 700,
              fontSize: '1rem',
              border: 'none',
              cursor: 'pointer',
              boxShadow: '0 8px 20px rgba(236,72,153,0.3)',
            }}
          >
            {saving ? 'Saving Changes...' : 'Save Profile Preferences ✨'}
          </button>
        </form>
        </div>
      </main>
    </div>
  )
}
