import { create } from 'zustand'

interface User {
  id: string; username: string; email: string; avatar?: string; bio?: string; location?: string
  xp: number; level: number; role: string; is_verified: boolean
}

interface FirebaseUser {
  uid: string
  displayName: string
  email: string
  photoURL: string | null
}

interface AppState {
  user: User | null
  token: string | null
  firebaseUser: FirebaseUser | null
  setAuth: (user: User, token: string) => void
  setFirebaseUser: (fbUser: FirebaseUser | null) => void
  logout: () => Promise<void>
}

export const useStore = create<AppState>((set) => ({
  user: null,
  token: null,
  firebaseUser: null,
  setAuth: (user, token) => {
    localStorage.setItem('xp_token', token)
    set({ user, token })
  },
  setFirebaseUser: (firebaseUser) => {
    if (firebaseUser) {
      localStorage.setItem('xp_firebase_user', JSON.stringify(firebaseUser))
    } else {
      localStorage.removeItem('xp_firebase_user')
    }
    set({ firebaseUser })
  },
  logout: async () => {
    const { signOutGoogle } = await import('@/lib/firebase')
    await signOutGoogle()
    localStorage.removeItem('xp_token')
    localStorage.removeItem('xp_firebase_user')
    set({ user: null, token: null, firebaseUser: null })
  },
}))

try {
  const saved = localStorage.getItem('xp_firebase_user')
  if (saved) {
    useStore.getState().setFirebaseUser(JSON.parse(saved))
  }
} catch {}
