import { create } from 'zustand'

export const useChatStore = create((set, get) => ({
  sessions: [],
  currentSessionId: null,
  messages: [],
  isLoading: false,
  quickReplies: [],
  lastCrisisLevel: 'safe',

  setCurrentSession: (id) => set({ currentSessionId: id }),
  setSessions: (sessions) => set({ sessions }),
  setMessages: (messages) => set({ messages }),
  setLoading: (isLoading) => set({ isLoading }),
  setQuickReplies: (quickReplies) => set({ quickReplies }),

  addMessage: (message) => set((state) => ({
    messages: [...state.messages, message],
  })),

  appendAIMessage: (content, meta = {}) => set((state) => ({
    messages: [
      ...state.messages,
      {
        id: Date.now().toString(),
        role: 'assistant',
        content,
        type: 'text',
        timestamp: new Date().toISOString(),
        ...meta,
      },
    ],
    quickReplies: meta.quickReplies || [],
    lastCrisisLevel: meta.crisisLevel || 'safe',
  })),

  addUserMessage: (content) => set((state) => ({
    messages: [
      ...state.messages,
      {
        id: Date.now().toString(),
        role: 'user',
        content,
        type: 'text',
        timestamp: new Date().toISOString(),
      },
    ],
    quickReplies: [],
  })),

  clearMessages: () => set({ messages: [], quickReplies: [] }),
}))
