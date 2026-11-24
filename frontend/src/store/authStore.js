import { create } from 'zustand'
import { persist } from 'zustand/middleware'

export const useAuthStore = create(
  persist(
    (set, get) => ({
      user: null,
      isAuthenticated: false,
      isLoading: false,
      tokens: { access: null, refresh: null },

      login: (userData, tokens) => set({
        user: userData,
        isAuthenticated: true,
        tokens,
      }),

      logout: () => set({
        user: null,
        isAuthenticated: false,
        tokens: { access: null, refresh: null },
      }),

      updateUser: (updates) => set((state) => ({
        user: { ...state.user, ...updates },
      })),

      updateStage: (stage) => set((state) => ({
        user: { ...state.user, stage },
      })),

      setLoading: (isLoading) => set({ isLoading }),

      getAccessToken: () => get().tokens.access,
    }),
    {
      name: 'loveguru-auth',
      partialize: (state) => ({
        user: state.user,
        isAuthenticated: state.isAuthenticated,
        tokens: state.tokens,
      }),
    }
  )
)
