import axios from 'axios'
import { useAuthStore } from '../store/authStore'

const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1'

const api = axios.create({
  baseURL: BASE_URL,
  timeout: 30000,
  headers: { 'Content-Type': 'application/json' },
})

// ── Request interceptor — attach access token ──────────────────
api.interceptors.request.use(
  (config) => {
    const token = useAuthStore.getState().getAccessToken()
    if (token) config.headers.Authorization = `Bearer ${token}`
    return config
  },
  (error) => Promise.reject(error)
)

// ── Response interceptor — handle 401, refresh token ──────────
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const original = error.config
    if (error.response?.status === 401 && !original._retry) {
      original._retry = true
      try {
        const refreshToken = useAuthStore.getState().tokens.refresh
        if (!refreshToken) throw new Error('No refresh token')
        const res = await axios.post(`${BASE_URL}/auth/refresh`, { refresh_token: refreshToken })
        const newToken = res.data.access_token
        const currentTokens = useAuthStore.getState().tokens || {}
        useAuthStore.setState({
          tokens: { ...currentTokens, access: newToken },
        })
        original.headers.Authorization = `Bearer ${newToken}`
        return api(original)
      } catch {
        // Auth disabled in dev - don't redirect
        console.warn('Token refresh failed (auth disabled in dev mode)')
      }
    }
    return Promise.reject(error)
  }
)

export default api
