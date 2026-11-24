import api from './axiosConfig'
import { useAuthStore } from '../store/authStore'

export const authApi = {
  register: (data) => api.post('/auth/register', data),
  login: (data) => api.post('/auth/login', data),
  logout: () => api.post('/auth/logout'),
  refresh: (token) => api.post('/auth/refresh', { refresh_token: token }),
  me: () => api.get('/auth/me'),
}

export const chatApi = {
  sendText: (data) => api.post('/chat/text', data),
  sendTextStream: async (data, onToken, onDone) => {
    const token = useAuthStore.getState().getAccessToken()
    const res = await fetch(`${api.defaults.baseURL}/chat/text/stream`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...(token ? { Authorization: `Bearer ${token}` } : {}),
      },
      body: JSON.stringify(data),
    })
    if (!res.ok) throw new Error('Stream request failed')
    const reader = res.body.getReader()
    const decoder = new TextDecoder()
    let buffer = ''
    while (true) {
      const { done, value } = await reader.read()
      if (done) break
      buffer += decoder.decode(value, { stream: true })
      const lines = buffer.split('\n')
      buffer = lines.pop() || ''
      for (const line of lines) {
        if (line.startsWith('data: ')) {
          try {
            const payload = JSON.parse(line.slice(6))
            if (payload.token) onToken(payload.token)
            if (payload.done) onDone(payload)
            if (payload.error) throw new Error(payload.error)
          } catch (e) {
            if (e.message !== 'Stream request failed') console.warn('SSE parse error', e)
          }
        }
      }
    }
  },
  getHistory: (conversationId, limit = 50) =>
    api.get('/chat/history', { params: { conversation_id: conversationId, limit } }),
  getSessions: () => api.get('/chat/sessions'),
  deleteSession: (id) => api.delete(`/chat/session/${id}`),
}

export const stage1Api = {
  submitPartnerDescription: (data) => api.post('/stage1/partner-description', data),
  getReadinessScore: () => api.get('/stage1/readiness-score'),
  getImprovementPlan: () => api.get('/stage1/improvement-plan'),
  getDailyTask: () => api.get('/stage1/daily-task'),
  analyzeGrooming: (data) => api.post('/stage1/grooming-analysis', data),
}

export const stage2Api = {
  auditProfile: (data) => api.post('/stage2/profile-review', data),
  analyzeChat: (data) => api.post('/stage2/conversation-analysis', data),
  getFlirtCoaching: (data) => api.post('/stage2/flirt-coaching', data),
  checkFlags: (data) => api.post('/stage2/red-green-flags', data),
}

export const stage3Api = {
  gottmanAssessment: (data) => api.post('/stage3/gottman-check', data),
  resolveConflict: (data) => api.post('/stage3/conflict-script', data),
  getLoveLanguage: () => api.get('/stage3/love-language'),
  submitLoveLanguage: (data) => api.post('/stage3/love-language', data),
  getDateIdeas: () => api.get('/stage3/date-night-ideas'),
}

export const stage4Api = {
  getNCTracker: () => api.get('/stage4/nc-tracker'),
  logUrgeSurfing: (data) => api.post('/stage4/urge-surfing', data),
  submitJournal: (data) => api.post('/stage4/journal-entry', data),
  getGriefGuidance: () => api.get('/stage4/grief-guidance'),
  logGriefWeather: (data) => api.post('/stage4/grief-weather', data),
}

export const progressApi = {
  getOverview: () => api.get('/progress/overview'),
  getMoodGraph: () => api.get('/progress/mood-graph'),
  getWeeklyReport: () => api.get('/progress/weekly-report'),
  logDailyCheckin: (data) => api.post('/progress/checkin', data),
}

export const emergencyApi = {
  triggerSOS: (data) => api.post('/emergency/sos-trigger', data),
  getResources: () => api.get('/emergency/resources'),
}

export const profileApi = {
  getProfile: () => api.get('/auth/me'),
  updateProfile: (data) => api.put('/auth/profile', data),
}
