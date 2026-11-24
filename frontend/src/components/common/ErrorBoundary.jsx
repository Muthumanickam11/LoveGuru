import React from 'react'
import { Link } from 'react-router-dom'

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props)
    this.state = { hasError: false, error: null }
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error }
  }

  componentDidCatch(error, info) {
    console.error('[LoveGuru ErrorBoundary]', error, info)
  }

  render() {
    if (this.state.hasError) {
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
          <div style={{ fontSize: '3rem', marginBottom: 16 }}>💔</div>
          <h2 style={{ fontSize: '1.5rem', fontWeight: 700, marginBottom: 8, color: '#F8FAFC' }}>
            Something went wrong
          </h2>
          <p style={{ color: '#94A3B8', marginBottom: 24, maxWidth: 400, lineHeight: 1.6 }}>
            An unexpected error occurred. Your data is safe. Try refreshing the page.
          </p>
          <div style={{ display: 'flex', gap: 12, flexWrap: 'wrap', justifyContent: 'center' }}>
            <button
              onClick={() => window.location.reload()}
              style={{
                background: 'linear-gradient(135deg, #EC4899, #8B5CF6)',
                color: '#fff',
                border: 'none',
                borderRadius: 12,
                padding: '12px 24px',
                fontWeight: 600,
                cursor: 'pointer',
                fontSize: '0.95rem',
              }}
            >
              Refresh Page
            </button>
            <Link
              to="/"
              onClick={() => this.setState({ hasError: false, error: null })}
              style={{
                background: 'rgba(255,255,255,0.08)',
                color: '#F0F4FF',
                border: '1px solid rgba(255,255,255,0.12)',
                borderRadius: 12,
                padding: '12px 24px',
                fontWeight: 600,
                textDecoration: 'none',
                fontSize: '0.95rem',
              }}
            >
              Go Home
            </Link>
          </div>
        </div>
      )
    }
    return this.props.children
  }
}

export default ErrorBoundary
