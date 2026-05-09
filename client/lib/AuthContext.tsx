'use client'

import { createContext, useContext, useEffect, useState, ReactNode } from 'react'
import { User } from 'firebase/auth'
import { onAuthChange, mapFirebaseUser, FirebaseUserData } from '@/lib/firebase'
import { useStore } from '@/store/useStore'

interface AuthContextValue {
  firebaseUser: FirebaseUserData | null
  firebaseLoading: boolean
  firebaseError: string | null
}

const AuthContext = createContext<AuthContextValue>({
  firebaseUser: null,
  firebaseLoading: true,
  firebaseError: null,
})

export function AuthProvider({ children }: { children: ReactNode }) {
  const [firebaseLoading, setFirebaseLoading] = useState(true)
  const [firebaseError, setFirebaseError] = useState<string | null>(null)
  const { firebaseUser, setFirebaseUser: setStoreUser } = useStore()

  useEffect(() => {
    let cancelled = false
    setFirebaseLoading(true)
    setFirebaseError(null)

    const unsub = onAuthChange((user: User | null) => {
      if (cancelled) return
      if (user) {
        try {
          setStoreUser(mapFirebaseUser(user))
        } catch (e) {
          setFirebaseError('Failed to map Firebase user')
        }
      } else {
        setStoreUser(null)
      }
      setFirebaseLoading(false)
    })

    const timeout = setTimeout(() => {
      if (!cancelled) setFirebaseLoading(false)
    }, 8000)

    return () => {
      cancelled = true
      clearTimeout(timeout)
      unsub()
    }
  }, []) // eslint-disable-line

  return (
    <AuthContext.Provider value={{ firebaseUser, firebaseLoading, firebaseError }}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => useContext(AuthContext)
