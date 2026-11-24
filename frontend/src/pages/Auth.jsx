import { useState } from 'react'
import { useNavigate, useSearchParams } from 'react-router-dom'
import { motion, AnimatePresence } from 'framer-motion'
import toast from 'react-hot-toast'
import { authApi } from '../api/apiCalls'
import { useAuthStore } from '../store/authStore'

export default function Auth() {
  const navigate = useNavigate()
  const [searchParams] = useSearchParams()
  const { login } = useAuthStore()

  const [mode, setMode] = useState(searchParams.get('mode') === 'register' ? 'register' : 'login')
  const [isLoading, setIsLoading] = useState(false)
  const [form, setForm] = useState({ email: '', password: '', display_name: '' })

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value })

  const handleSubmit = async (e) => {
    e.preventDefault()
    setIsLoading(true)
    try {
      let res
      if (mode === 'register') {
        res = await authApi.register({
          email: form.email,
          password: form.password,
          display_name: form.display_name,
        })
      } else {
        res = await authApi.login({ email: form.email, password: form.password })
      }

      const { user, access_token, refresh_token } = res.data
      login(user, { access: access_token, refresh: refresh_token })
      toast.success(`Welcome${user.display_name ? ', ' + user.display_name : ''}! ❤️`)

      if (mode === 'register' || !user.onboarding_completed) {
        navigate('/onboarding')
      } else {
        navigate('/home')
      }
    } catch (err) {
      const msg = err.response?.data?.detail || 'Something went wrong. Please try again.'
      toast.error(msg)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div style={{
      minHeight: '100vh', background: '#080B11',
      display: 'flex', alignItems: 'center', justifyContent: 'center',
      padding: 24, fontFamily: "'Plus Jakarta Sans', sans-serif",
      position: 'relative',
    }}>
      {/* Background orbs */}
      <div style={{
        position: 'fixed', top: '10%', right: '10%',
        width: 400, height: 400, borderRadius: '50%', pointerEvents: 'none',
        background: 'radial-gradient(circle, rgba(139,92,246,0.1) 0%, transparent 70%)',
      }} />
      <div style={{
        position: 'fixed', bottom: '10%', left: '10%',
        width: 300, height: 300, borderRadius: '50%', pointerEvents: 'none',
        background: 'radial-gradient(circle, rgba(236,72,153,0.08) 0%, transparent 70%)',
      }} />

      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        style={{ width: '100%', maxWidth: 420 }}
      >
        {/* Logo */}
        <div style={{ textAlign: 'center', marginBottom: 32 }}>
          <div style={{ fontSize: '2.5rem', marginBottom: 8 }}>❤️</div>
          <h1 style={{
            fontFamily: "'Outfit', sans-serif", fontWeight: 800,
            fontSize: '1.75rem',
            background: 'linear-gradient(135deg,#EC4899,#8B5CF6)',
            WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent',
          }}>LoveGuru AI</h1>
          <p style={{ color: '#94A3B8', fontSize: '0.9rem', marginTop: 4 }}>
            Your AI Guru For Every Stage of Love
          </p>
        </div>

        {/* Card */}
        <div style={{
          background: 'rgba(22,29,42,0.9)',
          border: '1px solid rgba(255,255,255,0.08)',
          borderRadius: 24,
          padding: '36px 32px',
          backdropFilter: 'blur(20px)',
          boxShadow: '0 8px 48px rgba(0,0,0,0.5)',
        }}>
          {/* Tab switcher */}
          <div style={{
            display: 'flex', background: 'rgba(255,255,255,0.04)',
            borderRadius: 12, padding: 4, marginBottom: 28,
          }}>
            {['login', 'register'].map((m) => (
              <button
                key={m}
                id={`auth-tab-${m}`}
                onClick={() => setMode(m)}
                style={{
                  flex: 1, padding: '8px 0',
                  background: mode === m ? 'linear-gradient(135deg,#EC4899,#8B5CF6)' : 'transparent',
                  border: 'none', borderRadius: 10,
                  color: mode === m ? '#fff' : '#94A3B8',
                  fontWeight: 600, fontSize: '0.9rem',
                  cursor: 'pointer', transition: 'all 0.2s',
                  fontFamily: "'Plus Jakarta Sans', sans-serif",
                }}
              >
                {m === 'login' ? 'Sign In' : 'Create Account'}
              </button>
            ))}
          </div>

          <form onSubmit={handleSubmit}>
            <AnimatePresence mode="wait">
              {mode === 'register' && (
                <motion.div
                  key="name"
                  initial={{ opacity: 0, height: 0 }}
                  animate={{ opacity: 1, height: 'auto' }}
                  exit={{ opacity: 0, height: 0 }}
                  style={{ overflow: 'hidden', marginBottom: 16 }}
                >
                  <label style={{ display: 'block', color: '#94A3B8', fontSize: '0.85rem', marginBottom: 6, fontWeight: 500 }}>
                    Your Name
                  </label>
                  <input
                    id="auth-name-input"
                    name="display_name"
                    value={form.display_name}
                    onChange={handleChange}
                    placeholder="What should I call you?"
                    required={mode === 'register'}
                    style={{
                      width: '100%', padding: '12px 16px',
                      background: 'rgba(255,255,255,0.05)',
                      border: '1px solid rgba(255,255,255,0.08)',
                      borderRadius: 12, color: '#F0F4FF',
                      fontSize: '0.95rem', outline: 'none',
                      fontFamily: "'Plus Jakarta Sans', sans-serif",
                      transition: 'border-color 0.2s',
                      boxSizing: 'border-box',
                    }}
                    onFocus={e => e.target.style.borderColor = '#EC4899'}
                    onBlur={e => e.target.style.borderColor = 'rgba(255,255,255,0.08)'}
                  />
                </motion.div>
              )}
            </AnimatePresence>

            {/* Email */}
            <div style={{ marginBottom: 16 }}>
              <label style={{ display: 'block', color: '#94A3B8', fontSize: '0.85rem', marginBottom: 6, fontWeight: 500 }}>
                Email
              </label>
              <input
                id="auth-email-input"
                type="email"
                name="email"
                value={form.email}
                onChange={handleChange}
                placeholder="your@email.com"
                required
                style={{
                  width: '100%', padding: '12px 16px',
                  background: 'rgba(255,255,255,0.05)',
                  border: '1px solid rgba(255,255,255,0.08)',
                  borderRadius: 12, color: '#F0F4FF',
                  fontSize: '0.95rem', outline: 'none',
                  fontFamily: "'Plus Jakarta Sans', sans-serif",
                  transition: 'border-color 0.2s',
                  boxSizing: 'border-box',
                }}
                onFocus={e => e.target.style.borderColor = '#EC4899'}
                onBlur={e => e.target.style.borderColor = 'rgba(255,255,255,0.08)'}
              />
            </div>

            {/* Password */}
            <div style={{ marginBottom: 24 }}>
              <label style={{ display: 'block', color: '#94A3B8', fontSize: '0.85rem', marginBottom: 6, fontWeight: 500 }}>
                Password
              </label>
              <input
                id="auth-password-input"
                type="password"
                name="password"
                value={form.password}
                onChange={handleChange}
                placeholder={mode === 'register' ? 'Min. 8 characters' : 'Your password'}
                required
                style={{
                  width: '100%', padding: '12px 16px',
                  background: 'rgba(255,255,255,0.05)',
                  border: '1px solid rgba(255,255,255,0.08)',
                  borderRadius: 12, color: '#F0F4FF',
                  fontSize: '0.95rem', outline: 'none',
                  fontFamily: "'Plus Jakarta Sans', sans-serif",
                  transition: 'border-color 0.2s',
                  boxSizing: 'border-box',
                }}
                onFocus={e => e.target.style.borderColor = '#EC4899'}
                onBlur={e => e.target.style.borderColor = 'rgba(255,255,255,0.08)'}
              />
            </div>

            {/* Submit */}
            <motion.button
              id="auth-submit-btn"
              type="submit"
              disabled={isLoading}
              whileHover={{ scale: isLoading ? 1 : 1.02 }}
              whileTap={{ scale: 0.98 }}
              style={{
                width: '100%', padding: '13px',
                background: isLoading
                  ? 'rgba(255,255,255,0.1)'
                  : 'linear-gradient(135deg,#EC4899,#8B5CF6)',
                border: 'none', borderRadius: 12,
                color: isLoading ? '#475569' : '#fff',
                fontSize: '1rem', fontWeight: 700, cursor: isLoading ? 'not-allowed' : 'pointer',
                fontFamily: "'Plus Jakarta Sans', sans-serif",
                boxShadow: isLoading ? 'none' : '0 4px 20px rgba(236,72,153,0.4)',
                transition: 'all 0.2s',
                display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8,
              }}
            >
              {isLoading ? (
                <>
                  <div style={{
                    width: 16, height: 16, border: '2px solid #475569',
                    borderTopColor: 'transparent', borderRadius: '50%',
                    animation: 'spin 1s linear infinite',
                  }} />
                  {mode === 'register' ? 'Creating...' : 'Signing in...'}
                </>
              ) : (
                mode === 'register' ? 'Create My Account ❤️' : 'Sign In'
              )}
            </motion.button>
          </form>

          {/* Footer note */}
          {mode === 'register' && (
            <p style={{ color: '#334155', fontSize: '0.75rem', textAlign: 'center', marginTop: 16, lineHeight: 1.5 }}>
              By creating an account, you agree to our Terms of Service.
              Crisis helplines are always available — no login required.
            </p>
          )}
        </div>

        <button
          onClick={() => navigate('/')}
          style={{
            width: '100%', marginTop: 16, padding: '8px',
            background: 'transparent', border: 'none',
            color: '#475569', fontSize: '0.85rem', cursor: 'pointer',
            fontFamily: "'Plus Jakarta Sans', sans-serif",
          }}
        >
          ← Back to home
        </button>
      </motion.div>
    </div>
  )
}
