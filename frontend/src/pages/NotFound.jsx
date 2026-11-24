import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'

export default function NotFound() {
  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      background: '#080B11',
      color: '#F0F4FF',
      fontFamily: "'Plus Jakarta Sans', sans-serif",
      padding: 32,
      textAlign: 'center',
    }}>
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <div style={{ fontSize: '4rem', marginBottom: 16 }}>🗺️</div>
        <h1 style={{ fontSize: '1.8rem', fontWeight: 800, marginBottom: 8, color: '#F8FAFC' }}>
          Page Not Found
        </h1>
        <p style={{ color: '#94A3B8', marginBottom: 32, maxWidth: 400, lineHeight: 1.6 }}>
          Looks like you wandered off the path. Even in love, it's okay to get lost — but let's guide you back.
        </p>
        <div style={{ display: 'flex', gap: 12, justifyContent: 'center', flexWrap: 'wrap' }}>
          <Link
            to="/home"
            style={{
              background: 'linear-gradient(135deg, #EC4899, #8B5CF6)',
              color: '#fff',
              borderRadius: 14,
              padding: '12px 28px',
              fontWeight: 700,
              textDecoration: 'none',
              fontSize: '0.95rem',
            }}
          >
            Go to Dashboard
          </Link>
          <Link
            to="/"
            style={{
              background: 'rgba(255,255,255,0.08)',
              color: '#F0F4FF',
              border: '1px solid rgba(255,255,255,0.12)',
              borderRadius: 14,
              padding: '12px 28px',
              fontWeight: 600,
              textDecoration: 'none',
              fontSize: '0.95rem',
            }}
          >
            Back to Landing
          </Link>
        </div>
      </motion.div>
    </div>
  )
}
