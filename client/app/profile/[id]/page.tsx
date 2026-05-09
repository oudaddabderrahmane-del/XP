'use client'
import { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { useParams } from 'next/navigation'
import { MapPin, Calendar, Zap, Award, Users, ShoppingCart, MessageSquare, Trophy, Star, Shield, Target, Flame, Crown, Sparkles, ChevronRight, Package, Eye, GitBranch } from 'lucide-react'
import { fetchAPI } from '@/lib/api'
import { useStore } from '@/store/useStore'
import Link from 'next/link'

const RANKS = [
  { minLevel: 0, title: 'Bronze', color: '#CD7F32', icon: Shield, gradient: 'from-amber-700/30 to-amber-600/10' },
  { minLevel: 10, title: 'Silver', color: '#BFC3C7', icon: Shield, gradient: 'from-[#BFC3C7]/30 to-gray-400/10' },
  { minLevel: 25, title: 'Gold', color: '#FFD700', icon: Trophy, gradient: 'from-yellow-500/30 to-yellow-400/10' },
  { minLevel: 50, title: 'Platinum', color: '#E5E4E2', icon: Star, gradient: 'from-white/30 to-[#BFC3C7]/10' },
  { minLevel: 75, title: 'Diamond', color: '#B9F2FF', icon: Crown, gradient: 'from-cyan-300/30 to-blue-400/10' },
  { minLevel: 100, title: 'XP God', color: '#FF6EC7', icon: Flame, gradient: 'from-pink-500/30 via-purple-500/20 to-red-500/10' },
]

const BADGE_DEFS = [
  { id: 'first_login', label: 'First Login', icon: Sparkles, desc: 'Joined XP', check: () => true },
  { id: 'veteran', label: 'Veteran', icon: Award, desc: 'Reach level 25', check: (lvl: number) => lvl >= 25 },
  { id: 'elite', label: 'Elite', icon: Crown, desc: 'Reach level 50', check: (lvl: number) => lvl >= 50 },
  { id: 'legendary', label: 'Legendary', icon: Flame, desc: 'Reach level 100', check: (lvl: number) => lvl >= 100 },
  { id: 'seller', label: 'Seller', icon: ShoppingCart, desc: 'List a product', check: (lvl: number, p: any) => p?.products > 0 },
  { id: 'builder', label: 'Builder', icon: GitBranch, desc: 'Create a PC build', check: (lvl: number, p: any) => p?.builds > 0 },
  { id: 'popular', label: 'Popular', icon: Users, desc: 'Get 10 followers', check: (lvl: number, p: any) => (p?.followers || 0) >= 10 },
  { id: 'rising', label: 'Rising Star', icon: Star, desc: 'Get 1000 XP', check: (lvl: number, p: any) => (p?.xp || 0) >= 1000 },
]

export default function ProfilePage() {
  const { id } = useParams()
  const { user: currentUser } = useStore()
  const [profile, setProfile] = useState<any>(null)
  const [products, setProducts] = useState<any[]>([])
  const [builds, setBuilds] = useState<any[]>([])
  const [tab, setTab] = useState('products')
  const [showMessage, setShowMessage] = useState(false)
  const [msg, setMsg] = useState('')
  const [badgeHover, setBadgeHover] = useState<string | null>(null)

  useEffect(() => {
    if (!id) return
    fetchAPI(`/api/users/${id}`).then(setProfile).catch(console.error)
    fetchAPI('/api/products').then(d => setProducts((d.products || []).filter((p: any) => p.seller_id === id))).catch(console.error)
    fetchAPI('/api/builds?public=true').then(d => setBuilds((d.builds || []).filter((b: any) => b.user_id === id))).catch(console.error)
  }, [id])

  async function sendMessage() {
    if (!msg.trim()) return
    try {
      await fetchAPI('/api/messages', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ receiver_id: id, content: msg }),
      })
      setMsg(''); setShowMessage(false)
    } catch (e) { console.error(e) }
  }

  if (!profile) return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <div className="rounded-2xl overflow-hidden">
        <div className="h-48 bg-[#1A1A1A] animate-pulse" />
        <div className="flex px-8 -mt-16">
          <div className="w-32 h-32 rounded-2xl bg-[#1A1A1A] animate-pulse border-4 border-black" />
        </div>
        <div className="p-8 space-y-4">
          <div className="h-8 w-48 bg-[#1A1A1A] animate-pulse rounded" />
          <div className="h-4 w-32 bg-[#1A1A1A] animate-pulse rounded" />
        </div>
      </div>
    </div>
  )

  const profileData = { products: products.length, builds: builds.length, followers: profile.followers || 0, xp: profile.xp || 0 }
  const rank = [...RANKS].reverse().find(r => (profile.level || 0) >= r.minLevel) || RANKS[0]
  const xpForCurrent = (lvl: number) => { let xp = 0, need = 100; for (let i = 1; i < lvl; i++) { xp += need; need += 50 } return xp }
  const xpForNext = (lvl: number) => 100 + (lvl - 1) * 50
  const currentLevelXp = xpForCurrent(profile.level || 1)
  const nextLevelXp = xpForNext(profile.level || 1)
  const progressInLevel = ((profile.xp || 0) - currentLevelXp) / nextLevelXp
  const progressPct = Math.min(100, Math.max(0, progressInLevel * 100))
  const earnedBadges = BADGE_DEFS.filter(b => b.check(profile.level || 0, profileData))
  const lockedBadges = BADGE_DEFS.filter(b => !b.check(profile.level || 0, profileData))

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
        {/* Cover + Banner */}
        <div className={`relative rounded-2xl overflow-hidden bg-gradient-to-br ${rank.gradient} border border-white/[0.06]`}>
          <div className="h-40 sm:h-48 bg-gradient-to-r from-black/40 via-transparent to-black/40 relative overflow-hidden">
            <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top,rgba(191,195,199,0.08),transparent_70%)]" />
            <div className="absolute bottom-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-[#BFC3C7]/30 to-transparent" />
          </div>

          {/* Avatar + Rank */}
          <div className="flex flex-col sm:flex-row items-center sm:items-end px-6 sm:px-8 -mt-16 relative z-10">
            <motion.div
              initial={{ scale: 0.8, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              transition={{ type: 'spring', stiffness: 200 }}
              className="relative"
            >
              <div className="w-28 h-28 sm:w-32 sm:h-32 rounded-2xl border-4 border-black overflow-hidden bg-gradient-to-br from-[#BFC3C7] to-white/30 flex items-center justify-center shadow-2xl"
                style={{ boxShadow: `0 0 30px ${rank.color}30` }}>
                <span className="text-5xl sm:text-6xl font-bold text-black">{profile.username[0].toUpperCase()}</span>
              </div>
              <div className="absolute -bottom-2 left-1/2 -translate-x-1/2 px-3 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider whitespace-nowrap border"
                style={{ backgroundColor: `${rank.color}20`, borderColor: `${rank.color}50`, color: rank.color }}>
                <rank.icon className="w-3 h-3 inline mr-1 -mt-0.5" />
                {rank.title}
              </div>
            </motion.div>

            <div className="flex-1 sm:ml-6 mt-4 sm:mt-0 text-center sm:text-left">
              <h1 className="text-2xl sm:text-3xl font-display font-bold text-white">{profile.username}</h1>
              <p className="text-white/50 text-sm mt-0.5">{profile.bio || 'No bio yet'}</p>
              <div className="flex flex-wrap justify-center sm:justify-start items-center gap-3 mt-2 text-xs text-white/40">
                {profile.location && <span className="flex items-center"><MapPin className="w-3 h-3 mr-1" />{profile.location}</span>}
                <span className="flex items-center"><Calendar className="w-3 h-3 mr-1" />Joined {new Date(profile.created_at).toLocaleDateString()}</span>
                <span className={`px-2 py-0.5 rounded text-[10px] font-semibold uppercase ${
                  profile.role === 'admin' ? 'bg-red-500/20 text-red-300' : profile.is_verified ? 'bg-blue-500/20 text-blue-300' : 'bg-white/5 text-white/30'
                }`}>{profile.role}</span>
              </div>
            </div>
          </div>

          {/* Stats Row */}
          <div className="grid grid-cols-3 sm:grid-cols-5 gap-px bg-white/[0.04] mt-6 border-t border-white/[0.06]">
            {[
              { label: 'XP', value: `${(profile.xp || 0).toLocaleString()}`, icon: Zap, color: 'text-[#BFC3C7]' },
              { label: 'Level', value: `${profile.level || 1}`, icon: Award, color: 'text-white' },
              { label: 'Products', value: `${products.length}`, icon: Package, color: 'text-white/70' },
              { label: 'Followers', value: `${profile.followers || 0}`, icon: Users, color: 'text-white/70' },
              { label: 'Builds', value: `${builds.length}`, icon: GitBranch, color: 'text-white/70' },
            ].map((s, i) => (
              <div key={i} className="py-3 sm:py-4 text-center">
                <div className={`${s.color} flex items-center justify-center space-x-1`}>
                  <s.icon className="w-3.5 h-3.5" />
                  <span className="text-sm sm:text-base font-bold">{s.value}</span>
                </div>
                <p className="text-[10px] text-white/30 mt-0.5">{s.label}</p>
              </div>
            ))}
          </div>
        </div>

        {/* XP Progress Bar */}
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.15 }}
          className="mt-6 glass-card p-5"
        >
          <div className="flex items-center justify-between mb-3">
            <div className="flex items-center space-x-2">
              <Zap className="w-4 h-4 text-[#BFC3C7]" />
              <span className="text-sm font-semibold text-white/80">Experience Progress</span>
            </div>
            <div className="text-xs text-white/40">
              <span className="text-[#BFC3C7] font-semibold">{Math.floor(progressPct)}%</span> to Level {profile.level + 1}
            </div>
          </div>
          <div className="h-3 bg-black/40 rounded-full overflow-hidden border border-white/[0.04]">
            <motion.div
              initial={{ width: 0 }}
              animate={{ width: `${progressPct}%` }}
              transition={{ duration: 1.2, ease: 'easeOut' }}
              className="h-full rounded-full relative"
              style={{
                background: `linear-gradient(90deg, ${rank.color}60, ${rank.color}, #BFC3C7)`,
                boxShadow: `0 0 12px ${rank.color}40`,
              }}
            >
              <div className="absolute inset-0 bg-[linear-gradient(90deg,transparent_0%,rgba(255,255,255,0.2)_50%,transparent_100%)] animate-scan" />
            </motion.div>
          </div>
          <div className="flex justify-between mt-2 text-[10px] text-white/30">
            <span>{currentLevelXp.toLocaleString()} XP</span>
            <span>Level {profile.level}</span>
            <span>{(currentLevelXp + nextLevelXp).toLocaleString()} XP</span>
          </div>
        </motion.div>

        {/* Action Buttons */}
        {currentUser && profile.id !== currentUser.id && (
          <div className="mt-4 flex space-x-3">
            <button onClick={() => setShowMessage(!showMessage)}
              className="flex items-center space-x-2 px-5 py-2.5 bg-white/5 hover:bg-white/10 border border-white/[0.08] rounded-xl text-sm font-semibold text-white/70 hover:text-white transition">
              <MessageSquare className="w-4 h-4" /><span>Message</span>
            </button>
          </div>
        )}
        {showMessage && (
          <motion.div initial={{ opacity: 0, y: -10 }} animate={{ opacity: 1, y: 0 }} className="mt-3 max-w-md">
            <div className="flex space-x-2">
              <input value={msg} onChange={e => setMsg(e.target.value)} placeholder={`Message @${profile.username}...`}
                className="flex-1 px-4 py-2.5 bg-[#1A1A1A] border border-white/[0.08] rounded-xl text-sm focus:outline-none focus:border-[#BFC3C7]/30" />
              <button onClick={sendMessage} disabled={!msg.trim()}
                className="px-4 py-2.5 bg-[#BFC3C7] text-black rounded-xl text-sm font-semibold hover:bg-white disabled:opacity-40 transition">Send</button>
            </div>
          </motion.div>
        )}

        {/* Badges Section */}
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.25 }}
          className="mt-6 glass-card p-5"
        >
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center space-x-2">
              <Trophy className="w-4 h-4 text-[#BFC3C7]" />
              <span className="text-sm font-semibold text-white/80">Badges</span>
            </div>
            <span className="text-xs text-white/40">{earnedBadges.length}/{BADGE_DEFS.length} earned</span>
          </div>

          <div className="grid grid-cols-4 sm:grid-cols-8 gap-3">
            {BADGE_DEFS.map((badge, i) => {
              const earned = earnedBadges.includes(badge)
              return (
                <motion.div
                  key={badge.id}
                  initial={{ opacity: 0, scale: 0.5 }}
                  animate={{ opacity: 1, scale: 1 }}
                  transition={{ delay: 0.3 + i * 0.05 }}
                  onMouseEnter={() => setBadgeHover(badge.id)}
                  onMouseLeave={() => setBadgeHover(null)}
                  className={`relative flex flex-col items-center p-2 rounded-xl transition-all duration-300 cursor-default ${
                    earned ? 'bg-white/[0.04] hover:bg-white/[0.08]' : 'bg-white/[0.02] opacity-40'
                  }`}
                >
                  <div className={`w-10 h-10 rounded-lg flex items-center justify-center mb-1.5 transition-all duration-300 ${
                    earned ? 'text-[#BFC3C7]' : 'text-white/20'
                  } ${badgeHover === badge.id && earned ? 'scale-110' : ''}`}
                    style={earned && badgeHover === badge.id ? { filter: 'drop-shadow(0 0 8px #BFC3C7)' } : {}}>
                    <badge.icon className="w-5 h-5" />
                  </div>
                  <span className={`text-[9px] font-medium text-center leading-tight ${earned ? 'text-white/60' : 'text-white/20'}`}>
                    {badge.label}
                  </span>
                  <AnimatePresence>
                    {badgeHover === badge.id && (
                      <motion.div
                        initial={{ opacity: 0, y: 5 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: 5 }}
                        className="absolute -top-1 left-1/2 -translate-x-1/2 -translate-y-full px-2.5 py-1 bg-[#1A1A1A] border border-white/[0.08] rounded-lg text-[10px] text-white/70 whitespace-nowrap shadow-xl z-20"
                      >
                        {badge.desc}
                      </motion.div>
                    )}
                  </AnimatePresence>
                </motion.div>
              )
            })}
          </div>
        </motion.div>

        {/* Tabs */}
        <div className="flex space-x-1 mt-6 bg-[#1A1A1A] border border-white/[0.06] rounded-xl p-1">
          {[
            { id: 'products', label: 'Products', icon: Package },
            { id: 'builds', label: 'Builds', icon: GitBranch },
          ].map(t => (
            <button key={t.id} onClick={() => setTab(t.id)}
              className={`flex items-center space-x-2 px-4 py-2.5 rounded-lg text-sm font-medium transition flex-1 justify-center ${
                tab === t.id ? 'bg-white/10 text-white' : 'text-white/40 hover:text-white/60'
              }`}>
              <t.icon className="w-4 h-4" /><span>{t.label}</span>
            </button>
          ))}
        </div>

        {/* Tab Content */}
        <div className="mt-4">
          {tab === 'products' && (
            products.length === 0 ? (
              <div className="text-center py-16 glass-card">
                <Package className="w-12 h-12 text-white/10 mx-auto mb-3" />
                <p className="text-white/30 text-sm">No products listed yet.</p>
              </div>
            ) : (
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                {products.map((p, i) => (
                  <motion.div key={p.id}
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: i * 0.04 }}>
                    <Link href={`/product/${p.id}`}
                      className="block glass-card p-4 hover:border-[#BFC3C7]/20 transition-all duration-300 group">
                      <div className="flex items-start justify-between">
                        <div className="flex-1 min-w-0">
                          <span className="text-[10px] text-[#BFC3C7]/60 uppercase tracking-wider font-semibold">{p.category}</span>
                          <h3 className="text-sm font-semibold text-white/80 mt-0.5 group-hover:text-white transition truncate">{p.title}</h3>
                          <div className="flex items-center space-x-3 mt-2 text-xs text-white/40">
                            <span className="text-[#BFC3C7] font-bold text-sm">${p.price}</span>
                            {p.condition && <span className="capitalize">{p.condition}</span>}
                            {p.location && <span className="truncate">{p.location}</span>}
                          </div>
                        </div>
                        <ChevronRight className="w-4 h-4 text-white/20 group-hover:text-white/40 transition flex-shrink-0 mt-1" />
                      </div>
                    </Link>
                  </motion.div>
                ))}
              </div>
            )
          )}

          {tab === 'builds' && (
            builds.length === 0 ? (
              <div className="text-center py-16 glass-card">
                <GitBranch className="w-12 h-12 text-white/10 mx-auto mb-3" />
                <p className="text-white/30 text-sm">No public builds yet.</p>
              </div>
            ) : (
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                {builds.map((b, i) => (
                  <motion.div key={b.id}
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: i * 0.04 }}
                    className="glass-card p-4 hover:border-[#BFC3C7]/20 transition-all duration-300">
                    <h3 className="text-sm font-semibold text-white/80">{b.name}</h3>
                    {b.description && <p className="text-xs text-white/40 mt-1 line-clamp-2">{b.description}</p>}
                    <div className="flex items-center space-x-3 mt-2 text-xs text-white/40">
                      <span className="text-[#BFC3C7] font-semibold">${b.total_price?.toLocaleString() || '0'}</span>
                      <span>{b.parts?.length || 0} parts</span>
                      {b.likes > 0 && <span>{b.likes} likes</span>}
                    </div>
                  </motion.div>
                ))}
              </div>
            )
          )}
        </div>
      </motion.div>
    </div>
  )
}
