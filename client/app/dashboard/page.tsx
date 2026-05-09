'use client'

import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { Zap, ShoppingCart, Users, Activity, Award, LogOut, Chrome, Loader2 } from 'lucide-react'
import { fetchAPI } from '@/lib/api'
import { useStore } from '@/store/useStore'
import { useAuth } from '@/lib/AuthContext'
import { useRouter } from 'next/navigation'
import Link from 'next/link'

export default function DashboardPage() {
  const [stats, setStats] = useState({ products: 0, builds: 0, communities: 0 })
  const [backendUser, setBackendUser] = useState<any>(null)
  const { firebaseUser, firebaseLoading } = useAuth()
  const { logout } = useStore()
  const router = useRouter()

  useEffect(() => {
    const token = localStorage.getItem('xp_token')
    if (token) {
      fetchAPI('/api/auth/me').then(setBackendUser).catch(() => {})
    }
    Promise.all([
      fetchAPI('/api/products').then(d => setStats(s => ({ ...s, products: d.total || 0 }))).catch(() => {}),
      fetchAPI('/api/builds?public=true').then(d => setStats(s => ({ ...s, builds: d.builds?.length || 0 }))).catch(() => {}),
    ])
  }, [])

  const displayUser = backendUser || firebaseUser

  async function handleLogout() {
    await logout()
    router.push('/')
  }

  if (firebaseLoading) {
    return (
      <div className="min-h-[80vh] flex items-center justify-center">
        <div className="text-center">
          <Loader2 className="w-8 h-8 animate-spin text-gray-400 mx-auto mb-3" />
          <p className="text-gray-500 text-sm">Loading dashboard...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
        <h1 className="text-3xl sm:text-4xl font-display font-bold mb-2">Dashboard</h1>
        <p className="text-gray-400">Your platform overview and activity</p>
      </motion.div>

      {displayUser ? (
        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.1 }}
          className="mt-8 bg-gradient-to-r from-blue-600/20 via-purple-600/20 to-pink-600/20 border border-white/10 rounded-2xl p-6">
          <div className="flex items-center justify-between flex-wrap gap-4">
            <div className="flex items-center space-x-4">
              <div className="w-16 h-16 rounded-2xl overflow-hidden bg-gradient-to-br from-blue-400 to-purple-600 flex items-center justify-center text-2xl font-bold flex-shrink-0">
                {displayUser.photoURL ? (
                  <img src={displayUser.photoURL} alt="" className="w-full h-full object-cover" />
                ) : (
                  <span>{(displayUser.displayName || displayUser.username || displayUser.email)?.[0]?.toUpperCase() || 'U'}</span>
                )}
              </div>
              <div>
                <h2 className="text-2xl font-bold">{displayUser.displayName || displayUser.username || 'User'}</h2>
                <p className="text-gray-400">{displayUser.email}</p>
                {backendUser && (
                  <div className="flex items-center space-x-4 mt-2">
                    <span className="flex items-center space-x-1 text-sm">
                      <Zap className="w-4 h-4 text-yellow-400" />
                      <span className="text-yellow-400">{backendUser.xp} XP</span>
                    </span>
                    <span className="flex items-center space-x-1 text-sm">
                      <Award className="w-4 h-4 text-blue-400" />
                      <span>Level {backendUser.level}</span>
                    </span>
                  </div>
                )}
                {firebaseUser && !backendUser && (
                  <div className="flex items-center space-x-1 mt-2">
                    <Chrome className="w-4 h-4 text-green-400" />
                    <span className="text-xs text-green-400">Connected with Google</span>
                  </div>
                )}
              </div>
            </div>
            <button onClick={handleLogout}
              className="flex items-center space-x-2 px-4 py-2 border border-white/10 hover:bg-white/5 rounded-xl text-sm text-gray-300 transition">
              <LogOut className="w-4 h-4" />
              <span>Logout</span>
            </button>
          </div>
        </motion.div>
      ) : (
        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.1 }}
          className="mt-8 bg-white/5 border border-white/10 rounded-2xl p-12 text-center">
          <p className="text-gray-400 mb-4">You are not signed in.</p>
          <Link href="/login"
            className="inline-flex items-center space-x-2 px-6 py-3 bg-white hover:bg-[#BFC3C7] text-black rounded-xl font-semibold transition">
            <span>Sign In with Google</span>
          </Link>
        </motion.div>
      )}

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 mt-8">
        {[
          { label: 'Products', value: stats.products, icon: ShoppingCart, color: 'from-blue-500 to-cyan-500' },
          { label: 'Builds', value: stats.builds, icon: Activity, color: 'from-green-500 to-emerald-500' },
          { label: 'Communities', value: stats.communities, icon: Users, color: 'from-purple-500 to-pink-500' },
        ].map((stat, i) => (
          <motion.div key={i} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.2 + i * 0.1 }}
            className="bg-white/5 border border-white/10 rounded-xl p-6 hover:border-blue-500/50 transition group">
            <div className={`w-12 h-12 rounded-xl bg-gradient-to-br ${stat.color} flex items-center justify-center mb-4`}>
              <stat.icon className="w-6 h-6" />
            </div>
            <p className="text-3xl font-bold">{stat.value}</p>
            <p className="text-gray-400 text-sm">{stat.label}</p>
          </motion.div>
        ))}
      </div>

      <div className="mt-12">
        <h2 className="text-2xl font-display font-bold mb-6">Quick Actions</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {[
            { href: '/marketplace', label: 'Browse Marketplace', desc: 'Find the best deals', color: 'from-blue-500 to-cyan-500' },
            { href: '/builder', label: 'Build a PC', desc: 'Design your dream rig', color: 'from-green-500 to-emerald-500' },
            { href: '/communities', label: 'Join Discussion', desc: 'Connect with others', color: 'from-purple-500 to-pink-500' },
            { href: '/register', label: 'Create Account', desc: 'Start your journey', color: 'from-orange-500 to-red-500' },
          ].map((action, i) => (
            <Link key={i} href={action.href}>
              <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.3 + i * 0.1 }}
                className={`bg-gradient-to-br ${action.color} p-[1px] rounded-xl group`}>
                <div className="bg-black rounded-xl p-5 h-full group-hover:bg-gray-900 transition">
                  <h3 className="font-semibold mb-1">{action.label}</h3>
                  <p className="text-sm text-gray-400">{action.desc}</p>
                </div>
              </motion.div>
            </Link>
          ))}
        </div>
      </div>
    </div>
  )
}
