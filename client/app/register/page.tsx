'use client'
import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { UserPlus, Mail, Lock, User, Eye, EyeOff, Chrome, LogOut, ArrowRight } from 'lucide-react'
import { fetchAPI } from '@/lib/api'
import { useStore } from '@/store/useStore'
import { useRouter } from 'next/navigation'
import Link from 'next/link'
import { signInWithGoogle, signOutGoogle, mapFirebaseUser, onAuthChange } from '@/lib/firebase'

export default function RegisterPage() {
  const [username, setUsername] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [showPw, setShowPw] = useState(false)
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const [googleLoading, setGoogleLoading] = useState(false)
  const { setAuth, setFirebaseUser, firebaseUser, logout } = useStore()
  const router = useRouter()

  useEffect(() => {
    const unsub = onAuthChange((fireUser) => {
      if (fireUser) {
        setFirebaseUser(mapFirebaseUser(fireUser))
      }
    })
    return unsub
  }, []) // eslint-disable-line

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    if (password.length < 6) { setError('Password must be at least 6 characters'); return }
    setLoading(true)
    setError('')
    try {
      const data = await fetchAPI('/api/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, email, password }),
      })
      setAuth(data.user, data.access_token)
      router.push('/dashboard')
    } catch (e: any) {
      setError(e.message || 'Registration failed')
    }
    setLoading(false)
  }

  async function handleGoogleSignUp() {
    setGoogleLoading(true)
    setError('')
    try {
      const user = await signInWithGoogle()
      setFirebaseUser(mapFirebaseUser(user))
      router.push('/dashboard')
    } catch (e: any) {
      if (e.code !== 'auth/popup-closed-by-user') {
        setError(e.message || 'Google sign-up failed')
      }
    }
    setGoogleLoading(false)
  }

  async function handleGoogleLogout() {
    await signOutGoogle()
    logout()
  }

  if (firebaseUser) {
    return (
      <div className="min-h-[80vh] flex items-center justify-center px-4">
        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="w-full max-w-md">
          <div className="bg-white/5 border border-white/10 rounded-2xl p-8 text-center">
            <div className="w-20 h-20 mx-auto rounded-full overflow-hidden border-2 border-white/20 mb-4">
              {firebaseUser.photoURL ? (
                <img src={firebaseUser.photoURL} alt="" className="w-full h-full object-cover" />
              ) : (
                <div className="w-full h-full bg-gradient-to-br from-blue-400 to-purple-500 flex items-center justify-center text-2xl font-bold text-white">
                  {firebaseUser.displayName?.[0] || firebaseUser.email[0].toUpperCase()}
                </div>
              )}
            </div>
            <h2 className="text-xl font-bold">{firebaseUser.displayName || 'User'}</h2>
            <p className="text-gray-400 text-sm mt-1">{firebaseUser.email}</p>
            <div className="mt-6 space-y-3">
              <button onClick={() => router.push('/dashboard')}
                className="w-full flex items-center justify-center space-x-2 py-3 bg-white hover:bg-[#BFC3C7] text-black rounded-xl font-semibold transition">
                <span>Go to Dashboard</span>
                <ArrowRight className="w-4 h-4" />
              </button>
              <button onClick={handleGoogleLogout}
                className="w-full flex items-center justify-center space-x-2 py-3 border border-white/10 hover:bg-white/5 rounded-xl text-sm text-gray-300 transition">
                <LogOut className="w-4 h-4" />
                <span>Sign Out</span>
              </button>
            </div>
          </div>
        </motion.div>
      </div>
    )
  }

  return (
    <div className="min-h-[80vh] flex items-center justify-center px-4">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="w-full max-w-md">
        <div className="bg-white/5 border border-white/10 rounded-2xl p-8">
          <div className="text-center mb-8">
            <div className="w-16 h-16 mx-auto bg-gradient-to-br from-purple-500 to-pink-600 rounded-2xl flex items-center justify-center mb-4">
              <UserPlus className="w-8 h-8 text-white" />
            </div>
            <h1 className="text-2xl font-display font-bold">Create Account</h1>
            <p className="text-gray-400 text-sm mt-1">Join the XP ecosystem</p>
          </div>

          <button onClick={handleGoogleSignUp} disabled={googleLoading}
            className="w-full flex items-center justify-center space-x-3 py-3 border border-white/10 hover:bg-white/5 rounded-xl transition disabled:opacity-50 mb-6">
            <Chrome className="w-5 h-5 text-red-400" />
            <span className="text-sm font-medium">
              {googleLoading ? 'Signing up...' : 'Continue with Google'}
            </span>
          </button>

          <div className="relative mb-6">
            <div className="absolute inset-0 flex items-center"><div className="w-full border-t border-white/10" /></div>
            <div className="relative flex justify-center text-xs"><span className="bg-[#1A1A1A] px-3 text-gray-500">or sign up with email</span></div>
          </div>

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="text-sm text-gray-300 mb-1 block">Username</label>
              <div className="relative">
                <User className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                <input type="text" value={username} onChange={(e) => setUsername(e.target.value)}
                  className="w-full pl-10 pr-4 py-3 bg-white/5 border border-white/10 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500" required />
              </div>
            </div>
            <div>
              <label className="text-sm text-gray-300 mb-1 block">Email</label>
              <div className="relative">
                <Mail className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                <input type="email" value={email} onChange={(e) => setEmail(e.target.value)}
                  className="w-full pl-10 pr-4 py-3 bg-white/5 border border-white/10 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500" required />
              </div>
            </div>
            <div>
              <label className="text-sm text-gray-300 mb-1 block">Password</label>
              <div className="relative">
                <Lock className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                <input type={showPw ? 'text' : 'password'} value={password} onChange={(e) => setPassword(e.target.value)}
                  className="w-full pl-10 pr-12 py-3 bg-white/5 border border-white/10 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500" required />
                <button type="button" onClick={() => setShowPw(!showPw)} className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400">
                  {showPw ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                </button>
              </div>
            </div>

            {error && <p className="text-red-400 text-sm">{error}</p>}

            <button type="submit" disabled={loading}
              className="w-full py-3 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 rounded-xl font-semibold transition disabled:opacity-50">
              {loading ? 'Creating account...' : 'Create Account'}
            </button>
          </form>

          <p className="text-center text-sm text-gray-400 mt-6">
            Already have an account? <Link href="/login" className="text-blue-400 hover:underline">Sign in</Link>
          </p>
        </div>
      </motion.div>
    </div>
  )
}
