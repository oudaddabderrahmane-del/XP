import { useCallback, useState, useEffect } from 'react'
import { api } from '@/lib/api'

export interface User {
  id: string
  username: string
  email: string
  avatar?: string
  bio?: string
  xp: number
  level: number
  badges: string[]
  followers: number
  following: number
  role: 'user' | 'seller' | 'moderator' | 'admin' | 'developer'
  createdAt: string
}

export interface AuthState {
  user: User | null
  token: string | null
  isLoading: boolean
  error: string | null
}

export const useAuth = () => {
  const [auth, setAuth] = useState<AuthState>({
    user: null,
    token: null,
    isLoading: true,
    error: null,
  })

  // Load auth from localStorage on mount
  useEffect(() => {
    const token = localStorage.getItem('accessToken')
    const user = localStorage.getItem('user')
    if (token && user) {
      setAuth({
        user: JSON.parse(user),
        token,
        isLoading: false,
        error: null,
      })
    } else {
      setAuth((prev) => ({ ...prev, isLoading: false }))
    }
  }, [])

  const login = useCallback(async (email: string, password: string) => {
    setAuth((prev) => ({ ...prev, isLoading: true, error: null }))
    try {
      const response = await api.post('/auth/login', { email, password })
      const { access_token, user } = response.data

      localStorage.setItem('accessToken', access_token)
      localStorage.setItem('user', JSON.stringify(user))

      setAuth({
        user,
        token: access_token,
        isLoading: false,
        error: null,
      })

      return { success: true }
    } catch (error: any) {
      const errorMsg = error.response?.data?.detail || 'Login failed'
      setAuth((prev) => ({ ...prev, isLoading: false, error: errorMsg }))
      return { success: false, error: errorMsg }
    }
  }, [])

  const register = useCallback(async (email: string, username: string, password: string) => {
    setAuth((prev) => ({ ...prev, isLoading: true, error: null }))
    try {
      const response = await api.post('/auth/register', { email, username, password })
      const { access_token, user } = response.data

      localStorage.setItem('accessToken', access_token)
      localStorage.setItem('user', JSON.stringify(user))

      setAuth({
        user,
        token: access_token,
        isLoading: false,
        error: null,
      })

      return { success: true }
    } catch (error: any) {
      const errorMsg = error.response?.data?.detail || 'Registration failed'
      setAuth((prev) => ({ ...prev, isLoading: false, error: errorMsg }))
      return { success: false, error: errorMsg }
    }
  }, [])

  const logout = useCallback(() => {
    localStorage.removeItem('accessToken')
    localStorage.removeItem('user')
    setAuth({
      user: null,
      token: null,
      isLoading: false,
      error: null,
    })
  }, [])

  return {
    ...auth,
    login,
    register,
    logout,
    isAuthenticated: !!auth.user,
  }
}
