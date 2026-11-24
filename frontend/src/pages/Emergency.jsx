import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import { emergencyApi } from '../api/apiCalls'

const REGIONAL_HELPLINES = {
  india: [
    { name: 'KIRAN Mental Health Helpline', number: '1800-599-0019', desc: 'Free, 24/7, 13 Regional Languages', type: 'call' },
    { name: 'Tele-MANAS', number: '14416', desc: 'National Tele-Mental Health Programme (24/7)', type: 'call' },
    { name: 'Vandrevala Foundation', number: '+91 9999 666 555', desc: '24/7 Crisis Counseling & Mental Support', type: 'call' },
    { name: 'AASRA Suicide Prevention', number: '+91 9820 466 726', desc: '24/7 Free & Confidential Helpline', type: 'call' },
  ],
  us: [
    { name: 'Suicide & Crisis Lifeline', number: '988', desc: 'Call or Text 24/7 (Free, Confidential)', type: 'call' },
    { name: 'Crisis Text Line', number: '741741', desc: 'Text HOME to 741741 (24/7 SMS Support)', type: 'text' },
    { name: 'National Domestic Violence Hotline', number: '1-800-799-7233', desc: '24/7 Call or Text LOVEIS to 22522', type: 'call' },
  ],
  international: [
    { name: 'Befrienders Worldwide', number: 'https://www.befrienders.org', desc: 'Global directory of emotional crisis centers', type: 'link' },
    { name: 'Find A Helpline', number: 'https://findahelpline.com', desc: 'Free, confidential support in 130+ countries', type: 'link' },
  ],
}

export default function Emergency() {
  const [region, setRegion] = useState('india')
  const [breathingPhase, setBreathingPhase] = useState('Inhale')
  const [breathCount, setBreathCount] = useState(4)

  // 4-7-8 Breathing Cycle Loop
  useEffect(() => {
    let timer
    if (breathingPhase === 'Inhale') {
      timer = setTimeout(() => {
        setBreathingPhase('Hold')
      }, 4000)
    } else if (breathingPhase === 'Hold') {
      timer = setTimeout(() => {
        setBreathingPhase('Exhale')
      }, 7000)
    } else if (breathingPhase === 'Exhale') {
      timer = setTimeout(() => {
        setBreathingPhase('Inhale')
      }, 8000)
    }
    return () => clearTimeout(timer)
  }, [breathingPhase])

  const helplines = REGIONAL_HELPLINES[region] || REGIONAL_HELPLINES.india

  return (
    <div style={{
      minHeight: '100vh',
      background: 'radial-gradient(circle at 50% 10%, #200E15 0%, #080B11 80%)',
      fontFamily: "'Plus Jakarta Sans', sans-serif",
      padding: '24px',
      color: '#F8FAFC',
    }}>
      {/* Top Banner */}
      <div style={{
        maxWidth: 920,
        margin: '0 auto 32px auto',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        flexWrap: 'wrap',
        gap: 16,
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
          <div style={{
            width: 44,
            height: 44,
            borderRadius: 12,
            background: '#DC2626',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: '1.4rem',
            boxShadow: '0 0 20px rgba(220, 38, 38, 0.6)',
          }}>
            🚨
          </div>
          <div>
            <h1 style={{ fontSize: '1.6rem', fontWeight: 800, margin: 0, color: '#F8FAFC' }}>
              LoveGuru SOS Crisis Sanctuary
            </h1>
            <span style={{ fontSize: '0.85rem', color: '#FCA5A5' }}>
              You are safe here. Help is available immediately.
            </span>
          </div>
        </div>

        <Link
          to="/home"
          style={{
            textDecoration: 'none',
            padding: '8px 16px',
            borderRadius: 10,
            background: 'rgba(255, 255, 255, 0.08)',
            border: '1px solid rgba(255, 255, 255, 0.15)',
            color: '#CBD5E1',
            fontSize: '0.85rem',
            fontWeight: 600,
          }}
        >
          ← Return to Dashboard
        </Link>
      </div>

      <main style={{ maxWidth: 920, margin: '0 auto' }}>
        {/* Somatic Breathing Pacer Card */}
        <div style={{
          background: 'rgba(15, 23, 42, 0.75)',
          border: '1px solid rgba(244, 63, 94, 0.3)',
          borderRadius: 24,
          padding: '40px 24px',
          textAlign: 'center',
          marginBottom: 36,
          boxShadow: '0 20px 40px rgba(0,0,0,0.5)',
        }}>
          <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 6 }}>
            Somatic 4-7-8 Breathing Pacer
          </h2>
          <p style={{ color: '#94A3B8', fontSize: '0.85rem', maxWidth: 480, margin: '0 auto 32px auto' }}>
            Synchronize your breath with the glowing orb. This physically slows your heart rate and signals safety to your nervous system.
          </p>

          {/* Animated Glowing Orb */}
          <div style={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            height: 220,
            marginBottom: 24,
          }}>
            <motion.div
              animate={{
                scale: breathingPhase === 'Inhale' ? 1.5 : breathingPhase === 'Hold' ? 1.5 : 1.0,
                opacity: breathingPhase === 'Hold' ? 0.9 : 0.7,
              }}
              transition={{
                duration: breathingPhase === 'Inhale' ? 4 : breathingPhase === 'Hold' ? 7 : 8,
                ease: 'easeInOut',
              }}
              style={{
                width: 120,
                height: 120,
                borderRadius: '50%',
                background: 'radial-gradient(circle, #F43F5E 0%, #8B5CF6 80%)',
                boxShadow: '0 0 50px rgba(244, 63, 94, 0.6), 0 0 100px rgba(139, 92, 246, 0.3)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                flexDirection: 'column',
              }}
            >
              <span style={{ fontSize: '1.2rem', fontWeight: 800, color: '#FFFFFF', textShadow: '0 2px 8px rgba(0,0,0,0.6)' }}>
                {breathingPhase}
              </span>
            </motion.div>
          </div>

          <div style={{ fontSize: '0.9rem', color: '#CBD5E1', fontWeight: 600 }}>
            {breathingPhase === 'Inhale' && 'Breathe in slowly through your nose (4s)...'}
            {breathingPhase === 'Hold' && 'Hold gently. Your nervous system is safe (7s)...'}
            {breathingPhase === 'Exhale' && 'Slow whoosh exhale through mouth (8s)...'}
          </div>
        </div>

        {/* Crisis Helplines Section */}
        <div style={{
          background: 'rgba(15, 23, 42, 0.75)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          borderRadius: 24,
          padding: '32px',
          marginBottom: 36,
        }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20, flexWrap: 'wrap', gap: 12 }}>
            <div>
              <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#F8FAFC', margin: 0 }}>
                Instant Crisis & Support Hotlines
              </h2>
              <span style={{ fontSize: '0.8rem', color: '#94A3B8' }}>
                Free, confidential, and available 24 hours a day
              </span>
            </div>

            {/* Region Toggle */}
            <div style={{ display: 'flex', gap: 6, background: 'rgba(255,255,255,0.05)', padding: 4, borderRadius: 10 }}>
              {[
                { id: 'india', label: '🇮🇳 India' },
                { id: 'us', label: '🇺🇸 US & Canada' },
                { id: 'international', label: '🌍 Worldwide' },
              ].map((r) => (
                <button
                  key={r.id}
                  onClick={() => setRegion(r.id)}
                  style={{
                    padding: '6px 14px',
                    borderRadius: 8,
                    fontSize: '0.8rem',
                    fontWeight: region === r.id ? 700 : 500,
                    background: region === r.id ? '#DC2626' : 'transparent',
                    color: region === r.id ? '#FFFFFF' : '#94A3B8',
                    border: 'none',
                    cursor: 'pointer',
                  }}
                >
                  {r.label}
                </button>
              ))}
            </div>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
            {helplines.map((h) => (
              <div
                key={h.name}
                style={{
                  background: 'rgba(255, 255, 255, 0.03)',
                  border: '1px solid rgba(255, 255, 255, 0.08)',
                  borderRadius: 16,
                  padding: '18px 22px',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  flexWrap: 'wrap',
                  gap: 12,
                }}
              >
                <div>
                  <h4 style={{ margin: 0, fontSize: '1rem', fontWeight: 700, color: '#F8FAFC' }}>
                    {h.name}
                  </h4>
                  <span style={{ fontSize: '0.8rem', color: '#94A3B8' }}>{h.desc}</span>
                </div>

                {h.type === 'link' ? (
                  <a
                    href={h.number}
                    target="_blank"
                    rel="noopener noreferrer"
                    style={{
                      textDecoration: 'none',
                      background: 'rgba(255, 255, 255, 0.1)',
                      color: '#FFFFFF',
                      padding: '10px 18px',
                      borderRadius: 10,
                      fontWeight: 700,
                      fontSize: '0.85rem',
                    }}
                  >
                    Open Directory ↗
                  </a>
                ) : (
                  <a
                    href={`tel:${h.number.replace(/\s+/g, '')}`}
                    style={{
                      textDecoration: 'none',
                      background: '#DC2626',
                      color: '#FFFFFF',
                      padding: '10px 20px',
                      borderRadius: 10,
                      fontWeight: 800,
                      fontSize: '0.9rem',
                      display: 'flex',
                      alignItems: 'center',
                      gap: 8,
                      boxShadow: '0 6px 16px rgba(220, 38, 38, 0.4)',
                    }}
                  >
                    <span>📞</span>
                    <span>{h.number}</span>
                  </a>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* 5-4-3-2-1 Sensory Grounding */}
        <div style={{
          background: 'rgba(15, 23, 42, 0.75)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          borderRadius: 24,
          padding: '32px',
        }}>
          <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 6 }}>
            5-4-3-2-1 Sensory Grounding Exercise
          </h2>
          <p style={{ color: '#94A3B8', fontSize: '0.85rem', marginBottom: 20 }}>
            If your thoughts feel flooded or out of control, anchor into your immediate physical surroundings:
          </p>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(160px, 1fr))', gap: 12 }}>
            {[
              { num: '5', label: 'SEE', text: '5 objects you can clearly see right now' },
              { num: '4', label: 'FEEL', text: '4 physical textures (chair, fabric, table)' },
              { num: '3', label: 'HEAR', text: '3 distinct sounds in your environment' },
              { num: '2', label: 'SMELL', text: '2 scents or fresh room air' },
              { num: '1', label: 'TASTE', text: '1 taste or take a sip of cold water' },
            ].map((g) => (
              <div key={g.num} style={{
                background: 'rgba(255,255,255,0.02)',
                border: '1px solid rgba(255,255,255,0.06)',
                borderRadius: 14,
                padding: '16px',
                textAlign: 'center',
              }}>
                <span style={{ fontSize: '1.6rem', fontWeight: 800, color: '#F43F5E', display: 'block' }}>
                  {g.num}
                </span>
                <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#F8FAFC', display: 'block', marginBottom: 4 }}>
                  {g.label}
                </span>
                <p style={{ fontSize: '0.75rem', color: '#94A3B8', margin: 0, lineHeight: 1.3 }}>
                  {g.text}
                </p>
              </div>
            ))}
          </div>
        </div>
      </main>
    </div>
  )
}
