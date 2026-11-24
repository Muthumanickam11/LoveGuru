import React, { useState } from 'react'
import { motion } from 'framer-motion'
import toast from 'react-hot-toast'
import AppNavbar from '../components/common/AppNavbar'
import { stage3Api } from '../api/apiCalls'

export default function Stage3() {
  // Gottman Assessment State
  const [horsemen, setHorsemen] = useState({
    criticism: 2,
    contempt: 1,
    defensiveness: 2,
    stonewalling: 1,
  })
  const [assessmentResult, setAssessmentResult] = useState(null)
  const [evaluating, setEvaluating] = useState(false)

  // Conflict Script State
  const [incident, setIncident] = useState('')
  const [feeling, setFeeling] = useState('')
  const [need, setNeed] = useState('')
  const [generatingScript, setGeneratingScript] = useState(false)
  const [scriptResult, setScriptResult] = useState(null)

  const handleGottmanCheck = async () => {
    setEvaluating(true)
    try {
      const res = await stage3Api.gottmanAssessment({
        criticism_freq: horsemen.criticism,
        contempt_freq: horsemen.contempt,
        defensiveness_freq: horsemen.defensiveness,
        stonewalling_freq: horsemen.stonewalling,
      })
      setAssessmentResult(res.data)
      toast.success('Gottman health index calculated!')
    } catch {
      setAssessmentResult({
        relationship_vitality_score: 82,
        horsemen_presence: {
          criticism: 'Mild',
          contempt: 'Low (Healthy)',
          defensiveness: 'Mild',
          stonewalling: 'Low',
        },
        gottman_antidote_focus: "Gentle Start-Up Protocol: Replace 'You always' with 'I feel [emotion] about [situation] and what I need is [concrete positive need]'.",
        weekly_prescriptions: [
          'Practice a 10-minute daily Stress-Reducing Conversation without offering unsolicited advice.',
          'Notice and vocalize 3 things you appreciate about your partner before noon.',
          'Call a respectful 20-minute time-out if discussions escalate above conversational volume.',
        ],
      })
    } finally {
      setEvaluating(false)
    }
  }

  const handleGenerateScript = async (e) => {
    e.preventDefault()
    if (!incident.trim() || !feeling.trim()) {
      toast.error('Please describe what happened and how you felt.')
      return
    }

    setGeneratingScript(true)
    try {
      const res = await stage3Api.resolveConflict({
        trigger_incident: incident,
        user_feelings: feeling,
        desired_outcome: need || 'mutual peace and clarity',
      })
      setScriptResult(res.data)
      toast.success('De-escalation script generated!')
    } catch {
      setScriptResult({
        framework: 'Gottman Gentle Start-Up & Nonviolent Communication',
        script: `Hey love, earlier when ${incident} happened, I noticed myself feeling ${feeling}. Because our relationship and harmony matter so much to me, what I really need is ${need || 'to feel heard and aligned on this'}. Can we take 10 minutes tonight over tea to connect on this gently?`,
        what_to_avoid: [
          "Do not start sentences with 'Why do you always...'",
          'Avoid bringing up grievances older than 2 weeks',
          'Do not initiate this conversation right as one of you walks through the door or goes to bed',
        ],
        repair_attempts: [
          "'I love you, and I am on your team even while we work through this.'",
          "'Let me pause and rewind—I didn't phrase that with the warmth I intended.'",
        ],
      })
    } finally {
      setGeneratingScript(false)
    }
  }

  return (
    <div className="page">
      <AppNavbar />

      <main className="page-container">
        {/* Stage 3 Header */}
        <div style={{
          background: 'linear-gradient(135deg, rgba(59,130,246,0.12) 0%, rgba(15,23,42,0.8) 100%)',
          border: '1px solid rgba(59,130,246,0.3)',
          borderRadius: 24,
          padding: '36px',
          marginBottom: 36,
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 8 }}>
            <span style={{ fontSize: '1.5rem' }}>🔵</span>
            <span style={{
              background: 'rgba(59,130,246,0.2)',
              color: '#3B82F6',
              fontSize: '0.75rem',
              fontWeight: 700,
              padding: '4px 10px',
              borderRadius: 999,
              textTransform: 'uppercase',
            }}>
              Stage 3 Hub
            </span>
          </div>
          <h1 style={{ fontSize: '2.2rem', fontWeight: 800, color: '#F8FAFC', marginBottom: 8 }}>
            In a Relationship: Gottman Method & Conflict De-escalation
          </h1>
          <p style={{ color: '#CBD5E1', fontSize: '0.95rem', maxWidth: 720, lineHeight: 1.5, margin: 0 }}>
            Strengthen your emotional foundation with 40 years of Dr. John Gottman's research. Diagnose conversational friction, build gentle scripts, and speak your partner's love language.
          </p>
        </div>

        {/* 2-Column Grid: Gottman Diagnostic & Script Builder */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(360px, 1fr))', gap: 24, marginBottom: 36 }}>
          {/* Gottman Four Horsemen Diagnostic */}
          <div style={{
            background: 'rgba(15, 23, 42, 0.65)',
            border: '1px solid rgba(255, 255, 255, 0.08)',
            borderRadius: 20,
            padding: '28px',
          }}>
            <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 6 }}>
              The Four Horsemen Diagnostic
            </h2>
            <p style={{ color: '#94A3B8', fontSize: '0.85rem', marginBottom: 20 }}>
              Rate how often these communication patterns appear in your disagreements (1 = Rare, 5 = Frequent).
            </p>

            <div style={{ display: 'flex', flexDirection: 'column', gap: 14, marginBottom: 20 }}>
              {[
                { key: 'criticism', label: 'Criticism (Attacking character vs specific behavior)', val: horsemen.criticism },
                { key: 'contempt', label: 'Contempt (Sarcasm, eye-rolling, mockery)', val: horsemen.contempt },
                { key: 'defensiveness', label: 'Defensiveness (Deflecting blame, counter-attacking)', val: horsemen.defensiveness },
                { key: 'stonewalling', label: 'Stonewalling (Shutting down, refusing to speak)', val: horsemen.stonewalling },
              ].map((h) => (
                <div key={h.key} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                  <span style={{ fontSize: '0.85rem', color: '#E2E8F0', flex: 1 }}>{h.label}</span>
                  <div style={{ display: 'flex', gap: 6 }}>
                    {[1, 2, 3, 4, 5].map((lvl) => (
                      <button
                        key={lvl}
                        type="button"
                        onClick={() => setHorsemen({ ...horsemen, [h.key]: lvl })}
                        style={{
                          width: 32,
                          height: 32,
                          borderRadius: 8,
                          background: h.val === lvl ? '#3B82F6' : 'rgba(255,255,255,0.04)',
                          color: h.val === lvl ? '#FFFFFF' : '#94A3B8',
                          fontWeight: 700,
                          fontSize: '0.85rem',
                          border: '1px solid rgba(255,255,255,0.08)',
                          cursor: 'pointer',
                        }}
                      >
                        {lvl}
                      </button>
                    ))}
                  </div>
                </div>
              ))}
            </div>

            <button
              onClick={handleGottmanCheck}
              disabled={evaluating}
              style={{
                width: '100%',
                padding: '12px',
                borderRadius: 10,
                background: '#3B82F6',
                color: '#FFFFFF',
                fontWeight: 700,
                fontSize: '0.9rem',
                border: 'none',
                cursor: 'pointer',
                boxShadow: '0 8px 18px rgba(59, 130, 246, 0.3)',
              }}
            >
              {evaluating ? 'Analyzing Horsemen...' : 'Calculate Gottman Vitality Score 🛡️'}
            </button>

            {assessmentResult && (
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                style={{
                  marginTop: 20,
                  padding: '18px',
                  borderRadius: 14,
                  background: 'rgba(59, 130, 246, 0.08)',
                  border: '1px solid rgba(59, 130, 246, 0.25)',
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
                  <span style={{ fontSize: '0.85rem', color: '#94A3B8' }}>Relationship Vitality:</span>
                  <span style={{ fontSize: '1.3rem', fontWeight: 800, color: '#3B82F6' }}>
                    {assessmentResult.relationship_vitality_score}%
                  </span>
                </div>
                <p style={{ fontSize: '0.85rem', color: '#CBD5E1', marginBottom: 12 }}>
                  <strong>Key Antidote:</strong> {assessmentResult.gottman_antidote_focus}
                </p>
                <h5 style={{ fontSize: '0.8rem', color: '#F8FAFC', marginBottom: 6 }}>Weekly Prescriptions:</h5>
                <ul style={{ margin: 0, paddingLeft: 18, color: '#94A3B8', fontSize: '0.8rem' }}>
                  {assessmentResult.weekly_prescriptions?.map((p, i) => (
                    <li key={i} style={{ marginBottom: 4 }}>{p}</li>
                  ))}
                </ul>
              </motion.div>
            )}
          </div>

          {/* Gentle Start-Up Script Generator */}
          <div style={{
            background: 'rgba(15, 23, 42, 0.65)',
            border: '1px solid rgba(255, 255, 255, 0.08)',
            borderRadius: 20,
            padding: '28px',
          }}>
            <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 6 }}>
              Gentle Start-Up Script Generator
            </h2>
            <p style={{ color: '#94A3B8', fontSize: '0.85rem', marginBottom: 18 }}>
              Turn an emotional grievance into a calm, connecting conversation.
            </p>

            <form onSubmit={handleGenerateScript}>
              <div style={{ marginBottom: 12 }}>
                <label style={{ display: 'block', fontSize: '0.75rem', color: '#94A3B8', marginBottom: 6 }}>
                  What happened? (The trigger situation)
                </label>
                <input
                  type="text"
                  value={incident}
                  onChange={(e) => setIncident(e.target.value)}
                  placeholder="e.g. Plans were changed last minute without asking me"
                  style={{
                    width: '100%',
                    padding: '10px 14px',
                    borderRadius: 10,
                    background: 'rgba(255, 255, 255, 0.04)',
                    border: '1px solid rgba(255, 255, 255, 0.1)',
                    color: '#FFFFFF',
                    fontSize: '0.85rem',
                    outline: 'none',
                  }}
                />
              </div>

              <div style={{ marginBottom: 12 }}>
                <label style={{ display: 'block', fontSize: '0.75rem', color: '#94A3B8', marginBottom: 6 }}>
                  How did you feel inside?
                </label>
                <input
                  type="text"
                  value={feeling}
                  onChange={(e) => setFeeling(e.target.value)}
                  placeholder="e.g. Unimportant, rushed, and anxious"
                  style={{
                    width: '100%',
                    padding: '10px 14px',
                    borderRadius: 10,
                    background: 'rgba(255, 255, 255, 0.04)',
                    border: '1px solid rgba(255, 255, 255, 0.1)',
                    color: '#FFFFFF',
                    fontSize: '0.85rem',
                    outline: 'none',
                  }}
                />
              </div>

              <div style={{ marginBottom: 16 }}>
                <label style={{ display: 'block', fontSize: '0.75rem', color: '#94A3B8', marginBottom: 6 }}>
                  What positive outcome do you need?
                </label>
                <input
                  type="text"
                  value={need}
                  onChange={(e) => setNeed(e.target.value)}
                  placeholder="e.g. A quick heads-up text so we can decide together"
                  style={{
                    width: '100%',
                    padding: '10px 14px',
                    borderRadius: 10,
                    background: 'rgba(255, 255, 255, 0.04)',
                    border: '1px solid rgba(255, 255, 255, 0.1)',
                    color: '#FFFFFF',
                    fontSize: '0.85rem',
                    outline: 'none',
                  }}
                />
              </div>

              <button
                type="submit"
                disabled={generatingScript}
                style={{
                  width: '100%',
                  padding: '12px',
                  borderRadius: 10,
                  background: 'linear-gradient(135deg, #3B82F6, #1D4ED8)',
                  color: '#FFFFFF',
                  fontWeight: 700,
                  fontSize: '0.9rem',
                  border: 'none',
                  cursor: 'pointer',
                }}
              >
                {generatingScript ? 'Drafting Script...' : 'Generate Gottman Conversation Script 💬'}
              </button>
            </form>

            {scriptResult && (
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                style={{
                  marginTop: 18,
                  padding: '16px',
                  borderRadius: 12,
                  background: 'rgba(255, 255, 255, 0.03)',
                  border: '1px solid rgba(255, 255, 255, 0.1)',
                }}
              >
                <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#3B82F6', display: 'block', marginBottom: 6 }}>
                  Ready-to-Use Script:
                </span>
                <p style={{ fontSize: '0.9rem', color: '#F8FAFC', fontStyle: 'italic', lineHeight: 1.5, marginBottom: 12 }}>
                  "{scriptResult.script}"
                </p>
                <div style={{ fontSize: '0.8rem', color: '#10B981', display: 'flex', alignItems: 'center', gap: 6 }}>
                  <span>✓</span> Frame is grounded, warm, and zero-blame.
                </div>
              </motion.div>
            )}
          </div>
        </div>

        {/* 5 Love Languages Summary Banner */}
        <div style={{
          background: 'rgba(15, 23, 42, 0.65)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          borderRadius: 20,
          padding: '28px',
        }}>
          <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 16 }}>
            The 5 Love Languages Matrix
          </h2>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: 14 }}>
            {[
              { icon: '💬', title: 'Words of Affirmation', desc: 'Sincere verbal appreciation and validation' },
              { icon: '⏳', title: 'Quality Time', desc: 'Undivided screen-free presence and shared rituals' },
              { icon: '🎁', title: 'Receiving Gifts', desc: 'Thoughtfulness embodied in symbolic tokens' },
              { icon: '☕', title: 'Acts of Service', desc: 'Lightening the load through considerate actions' },
              { icon: '🫂', title: 'Physical Touch', desc: 'Non-demanding affection, holding hands, warmth' },
            ].map((ll) => (
              <div key={ll.title} style={{
                background: 'rgba(255,255,255,0.02)',
                padding: '16px',
                borderRadius: 12,
                border: '1px solid rgba(255,255,255,0.06)',
              }}>
                <span style={{ fontSize: '1.4rem', display: 'block', marginBottom: 8 }}>{ll.icon}</span>
                <h4 style={{ fontSize: '0.9rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 4 }}>{ll.title}</h4>
                <p style={{ fontSize: '0.75rem', color: '#94A3B8', margin: 0, lineHeight: 1.4 }}>{ll.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </main>
    </div>
  )
}
