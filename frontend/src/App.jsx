import { BrowserRouter } from 'react-router-dom'
import { Toaster } from 'react-hot-toast'
import AppRouter from './router/AppRouter'
import ErrorBoundary from './components/common/ErrorBoundary'

export default function App() {
  return (
    <ErrorBoundary>
      <BrowserRouter>
        <AppRouter />
        <Toaster
          position="top-right"
          toastOptions={{
            className: 'toast',
            duration: 4000,
            style: {
              background: '#161D2A',
              border: '1px solid rgba(255,255,255,0.08)',
              color: '#F0F4FF',
              fontFamily: "'Plus Jakarta Sans', sans-serif",
            },
          }}
        />
      </BrowserRouter>
    </ErrorBoundary>
  )
}
