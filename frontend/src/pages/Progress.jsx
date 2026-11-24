import React, { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import AppNavbar from '../components/common/AppNavbar'
import { progressApi } from '../api/apiCalls'

export default function Progress() {
  const [overview, setOverview] = useState(null)
  const [overviewLoading, setOverviewLoading] = useState(true)

  const [moodData, setMoodData] = useState([])

  const [weeklyReport, setWeeklyReport] = useState(null)

  const [milestones, setMilestones] = useState([])

  useEffect(() => {
    progressApi.getOverview()
      .then((res) => res.data && setOverview(res.data))
      .catch(() => {})
      .finally(() => setOverviewLoading(false))
    progressApi.getMoodGraph()
      .then((res) => res.data?.data && setMoodData(res.data.data))
      .catch(() => {})
    progressApi.getWeeklyReport()
      .then((res) => res.data?.report && setWeeklyReport(res.data.report))
      .catch(() => {})
  }, [])

  return (
    <div className="page">
      <AppNavbar />

      <main className="page-container">
        {/* Header */}
        <div style={{ marginBottom: 32 }}>
          <h1 style={{ fontSize: '2.1rem', fontWeight: 800, color: '#F8FAFC', marginBottom: 8 }}>
            Your Emotional Growth & Milestones 📈
          </h1>
          <p style={{ color: '#94A3B8', fontSize: '0.95rem', margin: 0 }}>
            Longitudinal synthesis of your relationship habits, emotional trajectory, and personal milestones.
          </p>
        </div>

        {/* 3 Metric Cards */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: 20, marginBottom: 36 }}>
          <div style={{
            background: 'rgba(15, 23, 42, 0.65)',
            border: '1px solid rgba(255, 255, 255, 0.08)',
            borderRadius: 18,
            padding: '24px',
          }}>
            <span style={{ fontSize: '1.8rem', display: 'block', marginBottom: 8 }}>🔥</span>
            <span style={{ fontSize: '0.8rem', color: '#94A3B8', textTransform: 'uppercase' }}>Check-in Streak</span>
            <h3 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#F8FAFC', margin: '4px 0 0 0' }}>
              {overviewLoading ? '—' : (overview?.current_streak ?? 0)} Days
            </h3>
          </div>

          <div style={{
            background: 'rgba(15, 23, 42, 0.65)',
            border: '1px solid rgba(255, 255, 255, 0.08)',
            borderRadius: 18,
            padding: '24px',
          }}>
            <span style={{ fontSize: '1.8rem', display: 'block', marginBottom: 8 }}>⚡</span>
            <span style={{ fontSize: '0.8rem', color: '#94A3B8', textTransform: 'uppercase' }}>XP & Rank</span>
            <h3 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#EC4899', margin: '4px 0 0 0' }}>
              {overview?.total_xp ?? 0} <span style={{ fontSize: '1rem', color: '#94A3B8', fontWeight: 500 }}>(Level {overview?.level ?? 1})</span>
            </h3>
          </div>

          <div style={{
            background: 'rgba(15, 23, 42, 0.65)',
            border: '1px solid rgba(255, 255, 255, 0.08)',
            borderRadius: 18,
            padding: '24px',
          }}>
            <span style={{ fontSize: '1.8rem', display: 'block', marginBottom: 8 }}>🧭</span>
            <span style={{ fontSize: '0.8rem', color: '#94A3B8', textTransform: 'uppercase' }}>Emotional Vitality</span>
            <h3 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#10B981', margin: '4px 0 0 0' }}>
              {overview?.emotional_balance_score ?? '—'}%
            </h3>
          </div>
        </div>

        {/* 7-Day Mood Graph */}
        <div style={{
          background: 'rgba(15, 23, 42, 0.65)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          borderRadius: 20,
          padding: '28px',
          marginBottom: 36,
        }}>
          <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 8 }}>
            7-Day Emotional Trajectory
          </h2>
          <p style={{ color: '#94A3B8', fontSize: '0.85rem', marginBottom: 24 }}>
            Tracks daily emotional stability and positivity on a 1-10 scale.
          </p>

          {/* Bar Chart Visualizer */}
          <div style={{
            display: 'flex',
            alignItems: 'flex-end',
            justifyContent: 'space-between',
            gap: 12,
            height: 180,
            padding: '0 10px',
            borderBottom: '1px solid rgba(255,255,255,0.1)',
          }}>
            {moodData.map((m) => {
              const heightPct = (m.score / 10) * 100
              return (
                <div key={m.day} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', flex: 1, height: '100%', justifyContent: 'flex-end' }}>
                  <span style={{ fontSize: '0.75rem', color: '#10B981', fontWeight: 700, marginBottom: 4 }}>
                    {m.score}
                  </span>
                  <motion.div
                    initial={{ height: 0 }}
                    animate={{ height: `${heightPct}%` }}
                    transition={{ duration: 0.6, ease: 'easeOut' }}
                    style={{
                      width: '80%',
                      maxWidth: 48,
                      background: 'linear-gradient(180deg, #10B981 0%, rgba(16,185,129,0.3) 100%)',
                      borderRadius: '8px 8px 0 0',
                    }}
                  />
                  <span style={{ fontSize: '0.75rem', color: '#94A3B8', marginTop: 8, fontWeight: 600 }}>
                    {m.day}
                  </span>
                </div>
              )
            })}
          </div>
        </div>

        {/* Weekly Report & Synthesis */}
        {weeklyReport && (
        <div style={{
          background: 'rgba(15, 23, 42, 0.65)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          borderRadius: 20,
          padding: '32px',
          marginBottom: 36,
        }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16, flexWrap: 'wrap', gap: 10 }}>
            <h2 style={{ fontSize: '1.4rem', fontWeight: 700, color: '#F8FAFC', margin: 0 }}>
              Weekly Relationship Report
            </h2>
            <span style={{
              background: 'rgba(236,72,153,0.15)',
              color: '#EC4899',
              padding: '4px 12px',
              borderRadius: 8,
              fontSize: '0.8rem',
              fontWeight: 700,
            }}>
              {weeklyReport.week_title}
            </span>
          </div>

          <p style={{ color: '#E2E8F0', fontSize: '0.95rem', lineHeight: 1.6, marginBottom: 20 }}>
            {weeklyReport.executive_summary}
          </p>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 18, marginBottom: 24 }}>
            <div style={{ background: 'rgba(16,185,129,0.06)', padding: '18px', borderRadius: 14, border: '1px solid rgba(16,185,129,0.2)' }}>
              <h4 style={{ color: '#10B981', fontSize: '0.9rem', marginBottom: 10 }}>
                🏆 Top Emotional Wins
              </h4>
              <ul style={{ margin: 0, paddingLeft: 18, color: '#CBD5E1', fontSize: '0.85rem' }}>
                {weeklyReport.top_wins?.map((w, i) => (
                  <li key={i} style={{ marginBottom: 6 }}>{w}</li>
                ))}
              </ul>
            </div>

            <div style={{ background: 'rgba(59,130,246,0.06)', padding: '18px', borderRadius: 14, border: '1px solid rgba(59,130,246,0.2)' }}>
              <h4 style={{ color: '#3B82F6', fontSize: '0.9rem', marginBottom: 10 }}>
                🎯 Recommended Growth Focus
              </h4>
              <p style={{ margin: 0, color: '#CBD5E1', fontSize: '0.85rem', lineHeight: 1.5 }}>
                {weeklyReport.focus_next_week}
              </p>
            </div>
          </div>

          <div style={{
            background: 'linear-gradient(135deg, rgba(236,72,153,0.1) 0%, rgba(139,92,246,0.1) 100%)',
            border: '1px solid rgba(236,72,153,0.25)',
            borderRadius: 14,
            padding: '18px 24px',
            display: 'flex',
            alignItems: 'center',
            gap: 14,
          }}>
            <span style={{ fontSize: '1.8rem' }}>✨</span>
            <p style={{ margin: 0, color: '#F8FAFC', fontSize: '0.9rem', fontStyle: 'italic' }}>
              "{weeklyReport.ai_guru_blessing}"
            </p>
          </div>
        </div>
        )}

        {/* Milestones */}
        <div style={{
          background: 'rgba(15, 23, 42, 0.65)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          borderRadius: 20,
          padding: '28px',
        }}>
          <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#F8FAFC', marginBottom: 16 }}>
            Milestones & Badges
          </h2>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 14 }}>
            {milestones.map((m) => (
              <div key={m.title} style={{
                background: m.achieved ? 'rgba(16,185,129,0.05)' : 'rgba(255,255,255,0.02)',
                border: m.achieved ? '1px solid rgba(16,185,129,0.25)' : '1px solid rgba(255,255,255,0.06)',
                borderRadius: 14,
                padding: '16px',
                display: 'flex',
                alignItems: 'center',
                gap: 12,
              }}>
                <span style={{ fontSize: '1.5rem' }}>{m.achieved ? '🎖️' : '🔒'}</span>
                <div>
                  <h4 style={{ margin: 0, fontSize: '0.85rem', fontWeight: 700, color: '#F8FAFC' }}>{m.title}</h4>
                  <span style={{ fontSize: '0.75rem', color: '#94A3B8' }}>{m.achieved ? `Unlocked: ${m.date}` : m.target}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </main>
    </div>
  )
}
