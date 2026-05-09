'use client'
import Link from 'next/link'
import { useStore } from '@/store/useStore'
import { ShoppingCart, Cpu, Users, LayoutDashboard, LogIn, UserPlus, LogOut, Menu, X, Brain, MessageCircle, Search, Trophy, Bell, Code2, Calendar, Monitor, Package, Settings, ChevronDown } from 'lucide-react'
import { useState, useEffect, useRef } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { fetchAPI } from '@/lib/api'

export default function Navigation() {
  const { user, firebaseUser, logout } = useStore()
  const [mobileOpen, setMobileOpen] = useState(false)
  const [notifsOpen, setNotifsOpen] = useState(false)
  const [notifs, setNotifs] = useState<any[]>([])
  const [notifCount, setNotifCount] = useState(0)
  const notifRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (user) {
      fetchAPI('/api/notifications').then(d => {
        setNotifs(d.notifications || [])
        setNotifCount((d.notifications || []).filter((n: any) => !n.is_read).length)
      }).catch(() => {})
    }
  }, [user])

  useEffect(() => {
    function handleClick(e: MouseEvent) {
      if (notifRef.current && !notifRef.current.contains(e.target as Node)) setNotifsOpen(false)
    }
    document.addEventListener('mousedown', handleClick)
    return () => document.removeEventListener('mousedown', handleClick)
  }, [])

  const links = [
    { href: '/marketplace', label: 'Marketplace', icon: ShoppingCart },
    { href: '/builder', label: 'PC Builder', icon: Cpu },
    { href: '/showcase', label: 'Showcase', icon: Monitor },
    { href: '/communities', label: 'Communities', icon: Users },
    { href: '/events', label: 'Events', icon: Calendar },
    { href: '/chat', label: 'Chat', icon: MessageCircle },
    { href: '/ai', label: 'AI', icon: Brain },
    { href: '/leaderboard', label: 'Leaderboard', icon: Trophy },
  ]

  const rightLinks = user
    ? [
        { href: '/dashboard', label: 'Dashboard', icon: LayoutDashboard },
        { href: '/orders', label: 'Orders', icon: Package },
        { href: '/seller', label: 'Sell', icon: ShoppingCart },
        { href: '/developer', label: 'Dev', icon: Code2 },
        ...(user.role === 'admin' ? [{ href: '/admin', label: 'Admin', icon: LayoutDashboard }] : []),
      ]
    : []

  return (
    <nav className="fixed top-0 left-0 right-0 z-50">
      <div className="backdrop-blur-xl bg-black/60 border-b border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            {/* Logo */}
            <Link href="/" className="flex items-center space-x-2 group">
              <div className="w-9 h-9 bg-white rounded-lg flex items-center justify-center font-bold text-black text-sm font-display group-hover:shadow-lg group-hover:shadow-white/30 transition group-hover:animate-rgb">
                XP
              </div>
              <span className="font-display text-lg font-bold hidden sm:block text-white">XP</span>
            </Link>

            {/* Desktop Nav */}
            <div className="hidden md:flex items-center space-x-1">
              {links.slice(0, 5).map((link) => (
                <Link key={link.href} href={link.href}
                  className="flex items-center space-x-1.5 px-3 py-2 rounded-lg text-sm text-gray-300 hover:text-white hover:bg-white/10 transition">
                  <link.icon className="w-4 h-4" /><span>{link.label}</span>
                </Link>
              ))}
              <div className="relative group">
                <button className="flex items-center space-x-1 px-3 py-2 rounded-lg text-sm text-gray-300 hover:text-white hover:bg-white/10 transition">
                  <span>More</span><ChevronDown className="w-3 h-3" />
                </button>
                <div className="absolute top-full right-0 mt-1 w-48 bg-black/90 backdrop-blur-xl border border-white/10 rounded-xl py-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
                  {links.slice(5).map((link) => (
                    <Link key={link.href} href={link.href}
                      className="flex items-center space-x-3 px-4 py-2.5 text-sm text-gray-300 hover:text-white hover:bg-white/10 transition">
                      <link.icon className="w-4 h-4" /><span>{link.label}</span>
                    </Link>
                  ))}
                  <div className="border-t border-white/10 my-1" />
                  {rightLinks.slice(0, 4).map((link) => (
                    <Link key={link.href} href={link.href}
                      className="flex items-center space-x-3 px-4 py-2.5 text-sm text-gray-300 hover:text-white hover:bg-white/10 transition">
                      <link.icon className="w-4 h-4" /><span>{link.label}</span>
                    </Link>
                  ))}
                </div>
              </div>
            </div>

            {/* Right Section */}
            <div className="hidden md:flex items-center space-x-2">
              <Link href="/search" className="p-2 rounded-lg text-gray-400 hover:text-white hover:bg-white/10 transition">
                <Search className="w-5 h-5" />
              </Link>

              {user && (
                <div className="relative" ref={notifRef}>
                  <button onClick={() => setNotifsOpen(!notifsOpen)} className="relative p-2 rounded-lg text-gray-400 hover:text-white hover:bg-white/10 transition">
                    <Bell className="w-5 h-5" />
                    {notifCount > 0 && <span className="absolute -top-0.5 -right-0.5 w-4.5 h-4.5 bg-red-500 rounded-full text-[10px] font-bold text-white flex items-center justify-center">{notifCount}</span>}
                  </button>
                  <AnimatePresence>
                    {notifsOpen && (
                      <motion.div initial={{ opacity: 0, y: -10, scale: 0.95 }} animate={{ opacity: 1, y: 0, scale: 1 }} exit={{ opacity: 0, y: -10, scale: 0.95 }}
                        className="absolute right-0 mt-2 w-80 bg-black/95 backdrop-blur-xl border border-white/10 rounded-xl overflow-hidden shadow-2xl">
                        <div className="p-3 border-b border-white/10 flex items-center justify-between">
                          <h3 className="font-semibold text-sm">Notifications</h3>
                          <Link href="/settings" className="text-xs text-blue-400 hover:underline">Settings</Link>
                        </div>
                        <div className="max-h-80 overflow-y-auto">
                          {notifs.length === 0 ? (
                            <div className="p-6 text-center text-sm text-gray-400">No notifications yet</div>
                          ) : notifs.slice(0, 10).map((n) => (
                            <div key={n.id} className={`px-4 py-3 border-b border-white/5 hover:bg-white/5 transition ${!n.is_read ? 'bg-blue-600/5' : ''}`}>
                              <p className="text-sm font-medium">{n.title}</p>
                              {n.content && <p className="text-xs text-gray-400 mt-0.5">{n.content}</p>}
                              <p className="text-[10px] text-gray-500 mt-1">{new Date(n.created_at).toLocaleDateString()}</p>
                            </div>
                          ))}
                        </div>
                      </motion.div>
                    )}
                  </AnimatePresence>
                </div>
              )}

              {(user || firebaseUser) ? (
                <div className="flex items-center space-x-2">
                  <Link href="/settings" className="p-2 rounded-lg text-gray-400 hover:text-white hover:bg-white/10 transition">
                    <Settings className="w-5 h-5" />
                  </Link>
                  <Link href="/dashboard" className="flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-white/10 hover:bg-white/20 transition">
                    <div className="w-7 h-7 rounded-full bg-gradient-to-br from-blue-400 to-purple-500 flex items-center justify-center text-xs font-bold overflow-hidden">
                      {(() => {
                        const u: any = user || firebaseUser
                        return u.photoURL ? (
                          <img src={u.photoURL} alt="" className="w-full h-full object-cover" />
                        ) : (
                          (u.displayName || u.username || 'U')[0].toUpperCase()
                        )
                      })()}
                    </div>
                    <span className="text-sm">{user?.username || (firebaseUser as any)?.displayName || 'User'}</span>
                  </Link>
                  <button onClick={logout} className="p-2 rounded-lg text-gray-400 hover:text-white hover:bg-white/10 transition">
                    <LogOut className="w-4 h-4" />
                  </button>
                </div>
              ) : (
                <>
                  <Link href="/login" className="flex items-center space-x-1.5 px-3 py-2 text-sm text-gray-300 hover:text-white transition">
                    <LogIn className="w-4 h-4" /><span>Login</span>
                  </Link>
                  <Link href="/register" className="px-4 py-2 bg-white hover:bg-[#BFC3C7] text-black rounded-lg text-sm font-semibold transition flex items-center space-x-1.5">
                    <UserPlus className="w-4 h-4" /><span>Register</span>
                  </Link>
                </>
              )}
            </div>

            {/* Mobile Toggle */}
            <button onClick={() => setMobileOpen(!mobileOpen)} className="md:hidden p-2 text-gray-300 hover:text-white">
              {mobileOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Nav */}
      <AnimatePresence>
        {mobileOpen && (
          <motion.div initial={{ opacity: 0, y: -20 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -20 }}
            className="md:hidden backdrop-blur-xl bg-black/90 border-b border-white/10 max-h-[80vh] overflow-y-auto">
            <div className="px-4 py-4 space-y-1">
              {links.map((link) => (
                <Link key={link.href} href={link.href} onClick={() => setMobileOpen(false)}
                  className="flex items-center space-x-3 px-4 py-3 rounded-lg text-gray-300 hover:text-white hover:bg-white/10 transition">
                  <link.icon className="w-5 h-5" /><span>{link.label}</span>
                </Link>
              ))}
              <div className="border-t border-white/10 my-2" />
              {rightLinks.map((link) => (
                <Link key={link.href} href={link.href} onClick={() => setMobileOpen(false)}
                  className="flex items-center space-x-3 px-4 py-3 rounded-lg text-gray-300 hover:text-white hover:bg-white/10 transition">
                  <link.icon className="w-5 h-5" /><span>{link.label}</span>
                </Link>
              ))}
              {user && (
                <Link href="/orders" onClick={() => setMobileOpen(false)}
                  className="flex items-center space-x-3 px-4 py-3 rounded-lg text-gray-300 hover:text-white hover:bg-white/10 transition">
                  <Package className="w-5 h-5" /><span>Orders</span>
                </Link>
              )}
              {user || firebaseUser ? (
                <div className="pt-2 space-y-2 border-t border-white/10 mt-2">
                  <Link href="/settings" onClick={() => setMobileOpen(false)}
                    className="flex items-center space-x-3 px-4 py-3 rounded-lg text-gray-300 hover:text-white hover:bg-white/10 transition">
                    <Settings className="w-5 h-5" /><span>Settings</span>
                  </Link>
                  <button onClick={() => { logout(); setMobileOpen(false) }}
                    className="flex items-center space-x-3 px-4 py-3 rounded-lg text-red-400 hover:bg-white/10 transition w-full">
                    <LogOut className="w-5 h-5" /><span>Logout</span>
                  </button>
                </div>
              ) : (
                <div className="pt-2 space-y-2">
                  <Link href="/login" onClick={() => setMobileOpen(false)}
                    className="flex items-center space-x-3 px-4 py-3 rounded-lg text-gray-300 hover:text-white hover:bg-white/10 transition">
                    <LogIn className="w-5 h-5" /><span>Login</span>
                  </Link>
                  <Link href="/register" onClick={() => setMobileOpen(false)}
                    className="flex items-center space-x-3 px-4 py-3 rounded-lg bg-white text-black">
                    <UserPlus className="w-5 h-5" /><span>Register</span>
                  </Link>
                </div>
              )}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </nav>
  )
}
