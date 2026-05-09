'use client'
import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { Trophy, Medal, Zap, Award, Star, TrendingUp } from 'lucide-react'
import { fetchAPI } from '@/lib/api'
import Link from 'next/link'

const rankIcons = [Trophy, Medal, Award]
const rankColors = ['from-yellow-400 to-amber-600', 'from-gray-300 to-gray-500', 'from-amber-600 to-yellow-700']

const xpRanks = [
  { name: 'Bronze Builder', minXp: 0, color: 'from-amber-700 to-amber-500' },
  { name: 'Silver Gamer', minXp: 500, color: 'from-gray-400 to-gray-300' },
  { name: 'Gold Tech', minXp: 1500, color: 'from-yellow-500 to-amber-400' },
  { name: 'Diamond Developer', minXp: 5000, color: 'from-cyan-400 to-blue-500' },
  { name: 'XP Elite', minXp: 10000, color: 'from-purple-500 to-pink-500' },
]

function getRank(xp: number) {
  let rank = xpRanks[0]
  for (const r of xpRanks) { if (xp >= r.minXp) rank = r }
  return rank
}

export default function LeaderboardPage() {
  const [users, setUsers] = useState<any[]>([])
  const [tab, setTab] = useState<'xp' | 'sellers'>('xp')

  useEffect(() => {
    fetchAPI('/api/users').then(d => setUsers((d.users || []).sort((a: any, b: any) => b.xp - a.xp))).catch(console.error)
  }, [])

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="mb-8">
        <h1 className="text-3xl sm:text-4xl font-display font-bold mb-2">Leaderboard</h1>
        <p className="text-gray-400">Top contributors and sellers on XP</p>
      </motion.div>

      {/* Tabs */}
      <div className="flex space-x-2 mb-8">
        <button onClick={() => setTab('xp')} className={`px-6 py-3 rounded-xl font-semibold transition ${tab === 'xp' ? 'bg-blue-600' : 'bg-white/5 hover:bg-white/10'}`}><Zap className="w-4 h-4 inline mr-2" />XP Rankings</button>
        <button onClick={() => setTab('sellers')} className={`px-6 py-3 rounded-xl font-semibold transition ${tab === 'sellers' ? 'bg-blue-600' : 'bg-white/5 hover:bg-white/10'}`}><TrendingUp className="w-4 h-4 inline mr-2" />Top Sellers</button>
      </div>

      {/* XP Ranks */}
      <div className="flex flex-wrap gap-3 mb-8">
        {xpRanks.map((rank, i) => (
          <div key={i} className={`px-4 py-2 rounded-full bg-gradient-to-r ${rank.color} text-xs font-semibold`}>{rank.name}</div>
        ))}
      </div>

      {tab === 'xp' && (
        <div className="space-y-3">
          {users.slice(0, 50).map((u, i) => {
            const rank = getRank(u.xp)
            const RankIcon = rankIcons[i] || Award
            const rankColor = rankColors[i] || 'from-blue-400 to-purple-500'
            return (
              <motion.div key={u.id} initial={{ opacity: 0, x: -20 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: i * 0.02 }}
                className="bg-white/5 border border-white/10 rounded-xl p-4 hover:border-blue-500/30 transition group">
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-4">
                    <div className={`w-10 h-10 rounded-full bg-gradient-to-br ${rankColor} flex items-center justify-center font-bold text-sm relative`}>
                      {i + 1}
                      {i < 3 && <RankIcon className="absolute -top-1 -right-1 w-4 h-4 text-yellow-400" />}
                    </div>
                    <div className="w-10 h-10 rounded-full bg-gradient-to-br from-blue-400 to-purple-500 flex items-center justify-center text-sm font-bold">{u.username[0]}</div>
                    <div>
                      <Link href={`/profile/${u.id}`} className="font-semibold group-hover:text-blue-400 transition">{u.username}</Link>
                      <div className="flex items-center space-x-2 text-xs text-gray-400">
                        <span className={`px-2 py-0.5 rounded-full bg-gradient-to-r ${rank.color}`}>{rank.name}</span>
                        <span>{u.role}</span>
                      </div>
                    </div>
                  </div>
                  <div className="text-right">
                    <div className="font-bold text-lg flex items-center">
                      <Zap className="w-4 h-4 text-yellow-400 mr-1" />{u.xp.toLocaleString()}
                    </div>
                    <div className="text-xs text-gray-400">Level {u.level}</div>
                  </div>
                </div>
              </motion.div>
            )
          })}
        </div>
      )}

      {tab === 'sellers' && (
        <div className="text-center py-12">
          <TrendingUp className="w-16 h-16 text-gray-600 mx-auto mb-4" />
          <h3 className="text-xl font-semibold mb-2">Seller Rankings Coming Soon</h3>
          <p className="text-gray-400">Top sellers will be ranked by sales volume, reviews, and reputation.</p>
        </div>
      )}
    </div>
  )
}
