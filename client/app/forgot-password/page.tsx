'use client'
import { useState } from 'react'
import { motion } from 'framer-motion'
import { Mail, ArrowLeft, CheckCircle, AlertCircle } from 'lucide-react'
import Link from 'next/link'
import { fetchAPI } from '@/lib/api'

export default function ForgotPasswordPage() {
  const [email, setEmail] = useState('')
  const [step, setStep] = useState<'email' | 'code' | 'reset' | 'done'>('email')
  const [code, setCode] = useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  async function handleSendCode(e: React.FormEvent) {
    e.preventDefault()
    setLoading(true)
    setError('')
    await new Promise(r => setTimeout(r, 1000))
    setStep('code')
    setLoading(false)
  }

  async function handleReset(e: React.FormEvent) {
    e.preventDefault()
    if (password.length < 6) { setError('Password must be at least 6 characters'); return }
    if (password !== confirmPassword) { setError('Passwords do not match'); return }
    setLoading(true)
    setError('')
    await new Promise(r => setTimeout(r, 1500))
    setStep('done')
    setLoading(false)
  }

  return (
    <div className="min-h-[80vh] flex items-center justify-center px-4">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="w-full max-w-md">
        <div className="bg-white/5 border border-white/10 rounded-2xl p-8">
          <div className="text-center mb-8">
            <div className="w-16 h-16 mx-auto bg-gradient-to-br from-blue-500 to-purple-600 rounded-2xl flex items-center justify-center mb-4">
              {step === 'done' ? <CheckCircle className="w-8 h-8 text-white" /> : <Mail className="w-8 h-8 text-white" />}
            </div>
            <h1 className="text-2xl font-display font-bold">
              {step === 'email' && 'Reset Password'}
              {step === 'code' && 'Check Your Email'}
              {step === 'reset' && 'New Password'}
              {step === 'done' && 'Password Reset!'}
            </h1>
            <p className="text-gray-400 text-sm mt-1">
              {step === 'email' && 'Enter your email to receive a reset code'}
              {step === 'code' && `We sent a code to ${email}`}
              {step === 'reset' && 'Choose a new password for your account'}
              {step === 'done' && 'Your password has been reset successfully'}
            </p>
          </div>

          {step === 'email' && (
            <form onSubmit={handleSendCode} className="space-y-4">
              <div>
                <label className="text-sm text-gray-300 mb-1 block">Email</label>
                <div className="relative">
                  <Mail className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                  <input type="email" value={email} onChange={(e) => setEmail(e.target.value)}
                    className="w-full pl-10 pr-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500" required />
                </div>
              </div>
              {error && <p className="text-red-400 text-sm flex items-center"><AlertCircle className="w-4 h-4 mr-1" />{error}</p>}
              <button type="submit" disabled={loading} className="w-full py-3 bg-blue-600 hover:bg-blue-700 rounded-xl font-semibold transition disabled:opacity-50">
                {loading ? 'Sending...' : 'Send Reset Code'}
              </button>
            </form>
          )}

          {step === 'code' && (
            <div className="space-y-4">
              <input type="text" placeholder="Enter 6-digit code" value={code} onChange={(e) => {
                setCode(e.target.value)
                if (e.target.value.length === 6) setTimeout(() => setStep('reset'), 500)
              }} maxLength={6} className="w-full text-center text-2xl tracking-[0.5em] px-4 py-4 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500" />
              <p className="text-xs text-gray-400 text-center">Didn't receive it? <button className="text-blue-400 hover:underline">Resend code</button></p>
            </div>
          )}

          {step === 'reset' && (
            <form onSubmit={handleReset} className="space-y-4">
              <div>
                <label className="text-sm text-gray-300 mb-1 block">New Password</label>
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)}
                  className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500" required />
              </div>
              <div>
                <label className="text-sm text-gray-300 mb-1 block">Confirm Password</label>
                <input type="password" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)}
                  className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500" required />
              </div>
              {error && <p className="text-red-400 text-sm">{error}</p>}
              <button type="submit" disabled={loading} className="w-full py-3 bg-blue-600 hover:bg-blue-700 rounded-xl font-semibold transition disabled:opacity-50">
                {loading ? 'Resetting...' : 'Reset Password'}
              </button>
            </form>
          )}

          {step === 'done' && (
            <div className="text-center space-y-4">
              <div className="w-20 h-20 mx-auto rounded-full bg-green-500/20 flex items-center justify-center">
                <CheckCircle className="w-10 h-10 text-green-400" />
              </div>
              <Link href="/login"><button className="w-full py-3 bg-blue-600 hover:bg-blue-700 rounded-xl font-semibold">Back to Login</button></Link>
            </div>
          )}

          <div className="text-center mt-6">
            <Link href="/login" className="text-sm text-gray-400 hover:text-blue-400 transition flex items-center justify-center space-x-1">
              <ArrowLeft className="w-4 h-4" /><span>Back to login</span>
            </Link>
          </div>
        </div>
      </motion.div>
    </div>
  )
}
