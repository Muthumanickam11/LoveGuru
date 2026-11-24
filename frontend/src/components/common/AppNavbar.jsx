import React, { useState, useRef, useEffect } from 'react'
import { Link, NavLink, useNavigate } from 'react-router-dom'
import { useAuthStore } from '../../store/authStore'

const STAGES = [
  { path: '/stage1', num: '1', label: 'Stage 1 · Single & Searching', color: '#F59E0B' },
  { path: '/stage2', num: '2', label: 'Stage 2 · Finding Love', color: '#10B981' },
  { path: '/stage3', num: '3', label: 'Stage 3 · In a Relationship', color: '#3B82F6' },
  { path: '/stage4', num: '4', label: 'Stage 4 · After a Breakup', color: '#F43F5E' },
]

const MOBILE_LINKS = [
  { path: '/home', label: 'Dashboard', icon: '🏠' },
  { path: '/chat', label: 'AI Guru Chat', icon: '💬' },
  { path: '/stage1', label: 'Stage 1 · Single & Searching', icon: '🟡' },
  { path: '/stage2', label: 'Stage 2 · Finding Love', icon: '🟢' },
  { path: '/stage3', label: 'Stage 3 · In a Relationship', icon: '🔵' },
  { path: '/stage4', label: 'Stage 4 · After a Breakup', icon: '🔴' },
  { path: '/progress', label: 'Progress', icon: '📈' },
  { path: '/profile', label: 'Profile', icon: '👤' },
]

export default function AppNavbar() {
  const navigate = useNavigate()
  const { user, logout } = useAuthStore()
  const [menuOpen, setMenuOpen] = useState(false)
  const [mobileOpen, setMobileOpen] = useState(false)
  const menuRef = useRef(null)

  useEffect(() => {
    function handleClickOutside(e) {
      if (menuRef.current && !menuRef.current.contains(e.target)) {
        setMenuOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  const name = user?.display_name || user?.name || 'Friend'
  const initials = name
    .trim()
    .split(/\s+/)
    .map((w) => w[0])
    .slice(0, 2)
    .join('')
    .toUpperCase() || '❤'

  const handleLogout = () => {
    setMenuOpen(false)
    setMobileOpen(false)
    logout()
    navigate('/')
  }

  const linkClass = ({ isActive }) => 'nav-link' + (isActive ? ' active' : '')

  return (
    <header className="navbar">
      <div className="navbar-inner">
        {/* Brand */}
        <Link to="/home" className="navbar-brand">
          <div className="navbar-logo">❤️</div>
          <div className="navbar-brand-text">
            <span className="navbar-brand-name">
              LOVEGURU <span style={{ color: '#F43F5E' }}>AI</span>
            </span>
            <span className="navbar-brand-sub">Relationship Companion</span>
          </div>
        </Link>

        {/* Desktop navigation */}
        <nav className="navbar-nav">
          <NavLink to="/home" className={linkClass}>
            <span>🏠</span>
            <span>Dashboard</span>
          </NavLink>
          <NavLink to="/chat" className={linkClass}>
            <span>💬</span>
            <span>AI Guru</span>
          </NavLink>

          <span className="navbar-divider" />
          <span className="navbar-label">Stages</span>
          {STAGES.map((s) => (
            <NavLink
              key={s.path}
              to={s.path}
              title={s.label}
              className={({ isActive }) => 'nav-stage' + (isActive ? ' active' : '')}
              style={({ isActive }) =>
                isActive
                  ? { background: `${s.color}22`, borderColor: s.color, color: s.color }
                  : undefined
              }
            >
              {s.num}
            </NavLink>
          ))}

          <span className="navbar-divider" />
          <NavLink to="/progress" className={linkClass}>
            <span>📈</span>
            <span>Progress</span>
          </NavLink>
          <NavLink to="/profile" className={linkClass}>
            <span>👤</span>
            <span>Profile</span>
          </NavLink>
        </nav>

        <span className="navbar-spacer" />

        {/* Actions */}
        <div className="navbar-actions">
          <Link to="/emergency" className="nav-sos" title="Crisis Support">
            <span>🚨</span>
            <span className="label">SOS</span>
          </Link>

          <div className="nav-user" ref={menuRef}>
            <button
              type="button"
              className="nav-user-btn"
              onClick={() => setMenuOpen((o) => !o)}
              aria-haspopup="menu"
              aria-expanded={menuOpen}
            >
              <span className="nav-avatar">{initials}</span>
              <span className="nav-user-name">{name}</span>
              <span className="nav-caret">▾</span>
            </button>

            {menuOpen && (
              <div className="nav-dropdown" role="menu">
                <Link to="/profile" className="nav-dropdown-item" onClick={() => setMenuOpen(false)}>
                  👤 Profile &amp; Settings
                </Link>
                <Link to="/emergency" className="nav-dropdown-item" onClick={() => setMenuOpen(false)}>
                  🆘 Crisis Support
                </Link>
                <button type="button" className="nav-dropdown-item" onClick={handleLogout}>
                  ↩ Sign Out
                </button>
              </div>
            )}
          </div>

          <button
            type="button"
            className="nav-hamburger"
            onClick={() => setMobileOpen((o) => !o)}
            aria-label="Toggle navigation"
          >
            {mobileOpen ? '✕' : '☰'}
          </button>
        </div>
      </div>

      {/* Mobile panel */}
      {mobileOpen && (
        <div className="navbar-mobile open">
          {MOBILE_LINKS.map((item) => (
            <NavLink
              key={item.path}
              to={item.path}
              className={linkClass}
              onClick={() => setMobileOpen(false)}
            >
              <span>{item.icon}</span>
              <span>{item.label}</span>
            </NavLink>
          ))}
          <Link to="/emergency" className="nav-sos" onClick={() => setMobileOpen(false)}>
            <span>🚨</span>
            <span className="label">SOS Crisis Support</span>
          </Link>
          <button type="button" className="nav-dropdown-item" onClick={handleLogout}>
            ↩ Sign Out
          </button>
        </div>
      )}
    </header>
  )
}
