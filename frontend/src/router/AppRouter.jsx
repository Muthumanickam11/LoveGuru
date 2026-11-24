import { Suspense, lazy } from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import { useAuthStore } from '../store/authStore'

// Pages — lazy-loaded so each route ships as its own chunk.
const Landing    = lazy(() => import('../pages/Landing'))
const Onboarding = lazy(() => import('../pages/Onboarding'))
const Home       = lazy(() => import('../pages/Home'))
const Chat       = lazy(() => import('../pages/Chat'))
const Stage1     = lazy(() => import('../pages/Stage1'))
const Stage2     = lazy(() => import('../pages/Stage2'))
const Stage3     = lazy(() => import('../pages/Stage3'))
const Stage4     = lazy(() => import('../pages/Stage4'))
const Progress   = lazy(() => import('../pages/Progress'))
const Profile    = lazy(() => import('../pages/Profile'))
const Emergency  = lazy(() => import('../pages/Emergency'))
const Journal    = lazy(() => import('../pages/Journal'))
const NotFound   = lazy(() => import('../pages/NotFound'))

function PageFallback() {
  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      background: '#080B11',
      color: '#8B92A8',
      fontFamily: "'Plus Jakarta Sans', sans-serif",
      fontSize: 14,
    }}>
      Loading…
    </div>
  )
}

// Auth disabled for development - all routes are public
function ProtectedRoute({ children }) { return children }
function AppRoute({ children }) { return children }
function PublicOnlyRoute({ children }) { return children }

export default function AppRouter() {
  return (
    <Suspense fallback={<PageFallback />}>
      <Routes>
        {/* Public */}
        <Route path="/"     element={<Landing />} />

        {/* Requires auth but NOT onboarding gate (onboarding itself) */}
        <Route path="/onboarding" element={<ProtectedRoute><Onboarding /></ProtectedRoute>} />

        {/* Fully gated — requires auth + completed onboarding */}
        <Route path="/home"       element={<AppRoute><Home /></AppRoute>} />
        <Route path="/chat"       element={<AppRoute><Chat /></AppRoute>} />
        <Route path="/chat/:conversationId" element={<AppRoute><Chat /></AppRoute>} />
        <Route path="/stage1"     element={<AppRoute><Stage1 /></AppRoute>} />
        <Route path="/stage2"     element={<AppRoute><Stage2 /></AppRoute>} />
        <Route path="/stage3"     element={<AppRoute><Stage3 /></AppRoute>} />
        <Route path="/stage4"     element={<AppRoute><Stage4 /></AppRoute>} />
        <Route path="/progress"   element={<AppRoute><Progress /></AppRoute>} />
        <Route path="/profile"    element={<AppRoute><Profile /></AppRoute>} />
        <Route path="/journal"    element={<AppRoute><Journal /></AppRoute>} />

        {/* Emergency — intentionally public (crisis access without login) */}
        <Route path="/emergency"  element={<Emergency />} />

        {/* 404 */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Suspense>
  )
}
