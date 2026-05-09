'use client'
import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { useStore } from '@/store/useStore'
import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import {
  ShoppingCart, Cpu, Monitor, Users, Calendar, MessageCircle,
  Brain, Trophy, LayoutDashboard, Package, Code2, Settings, LogOut,
  ChevronRight, Search, Store, Gamepad2
} from 'lucide-react'

const navLinks = [
  { href: '/marketplace', label: 'Marketplace', icon: ShoppingCart },
  { href: '/builder', label: 'PC Builder', icon: Cpu },
  { href: '/showcase', label: 'Showcase', icon: Monitor },
  { href: '/communities', label: 'Communities', icon: Users },
  { href: '/events', label: 'Events', icon: Calendar },
  { href: '/chat', label: 'Chat', icon: MessageCircle },
  { href: '/ai', label: 'AI Assistant', icon: Brain },
  { href: '/leaderboard', label: 'Leaderboard', icon: Trophy },
]

const userLinks = [
  { href: '/dashboard', label: 'Dashboard', icon: LayoutDashboard },
  { href: '/orders', label: 'Orders', icon: Package },
  { href: '/seller', label: 'Sell', icon: Store },
  { href: '/developer', label: 'Dev Hub', icon: Code2 },
  { href: '/settings', label: 'Settings', icon: Settings },
]

export default function Sidebar() {
  const pathname = usePathname()
  const { user, firebaseUser, logout } = useStore()
  const [expanded, setExpanded] = useState(false)
  const [mobileOpen, setMobileOpen] = useState(false)

  const sidebarW = expanded ? 240 : 68

  return (
    <>
      {/* Mobile overlay */}
      <AnimatePresence>
        {mobileOpen && (
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            onClick={() => setMobileOpen(false)}
            className="fixed inset-0 bg-black/60 z-40 md:hidden" />
        )}
      </AnimatePresence>

      {/* Mobile sidebar */}
      <AnimatePresence>
        {mobileOpen && (
          <motion.aside initial={{ x: -300 }} animate={{ x: 0 }} exit={{ x: -300 }}
            transition={{ type: 'spring', damping: 25, stiffness: 300 }}
            className="fixed left-0 top-0 bottom-0 w-[280px] z-50 md:hidden
              bg-[#1A1A1A] border-r border-white/10 overflow-y-auto">
            <SidebarContent user={user} logout={logout} pathname={pathname}
              onClose={() => setMobileOpen(false)} firebaseUser={firebaseUser} />
          </motion.aside>
        )}
      </AnimatePresence>

      {/* Desktop sidebar */}
      <aside
        onMouseEnter={() => setExpanded(true)}
        onMouseLeave={() => setExpanded(false)}
        className="hidden md:flex fixed left-0 top-0 bottom-0 z-30 flex-col
          bg-[#1A1A1A]/95 backdrop-blur-xl border-r border-white/10
          transition-[width] duration-300 ease-in-out overflow-hidden"
        style={{ width: sidebarW }}
      >
        {/* Logo */}
        <div className="flex-shrink-0 flex items-center justify-center h-16 border-b border-white/10">
          <Link href="/" className="flex items-center space-x-2.5 group">
            <div className="w-9 h-9 bg-white rounded-lg flex items-center justify-center font-bold text-black text-sm font-display group-hover:animate-rgb">
              XP
            </div>
            <AnimatePresence>
              {expanded && (
                <motion.span initial={{ opacity: 0, x: -10 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: -10 }}
                  className="font-display text-lg font-bold text-white">XP</motion.span>
              )}
            </AnimatePresence>
          </Link>
        </div>

        {/* Search shortcut */}
        <div className="flex-shrink-0 px-3 py-3">
          <Link href="/search"
            className="flex items-center space-x-3 px-3 py-2 rounded-lg text-gray-400 hover:text-white hover:bg-white/10 transition">
            <Search className="w-5 h-5 flex-shrink-0" />
            <AnimatePresence>
              {expanded && (
                <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
                  className="text-sm">Search...</motion.span>
              )}
            </AnimatePresence>
          </Link>
        </div>

        {/* Nav links */}
        <nav className="flex-1 overflow-y-auto overflow-x-hidden px-3 space-y-0.5">
          {navLinks.map((link) => {
            const active = pathname === link.href || pathname.startsWith(link.href + '/')
            return (
              <Link key={link.href} href={link.href}
                className={`flex items-center space-x-3 px-3 py-2.5 rounded-lg text-sm transition relative group ${
                  active
                    ? 'text-white bg-white/10'
                    : 'text-gray-400 hover:text-white hover:bg-white/5'
                }`}>
                <link.icon className="w-5 h-5 flex-shrink-0" />
                <AnimatePresence>
                  {expanded && (
                    <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
                      className="truncate">{link.label}</motion.span>
                  )}
                </AnimatePresence>
                {active && expanded && (
                  <motion.div layoutId="sidebar-active" className="absolute left-0 top-1 bottom-1 w-0.5 bg-white rounded-full" />
                )}
              </Link>
            )
          })}
        </nav>

        {/* User section */}
        {(user || firebaseUser) ? (
          <div className="flex-shrink-0 border-t border-white/10 px-3 py-3 space-y-1">
            <Link href="/dashboard"
              className="flex items-center space-x-3 px-3 py-2 rounded-lg text-gray-400 hover:text-white hover:bg-white/5 transition">
              <div className="w-7 h-7 rounded-full bg-gradient-to-br from-blue-400 to-purple-500 flex items-center justify-center text-xs font-bold flex-shrink-0 overflow-hidden">
                {(() => {
                  const u: any = user || firebaseUser
                  return u.photoURL ? (
                    <img src={u.photoURL} alt="" className="w-full h-full object-cover" />
                  ) : (
                    (u.displayName || u.username || 'U')[0].toUpperCase()
                  )
                })()}
              </div>
              <AnimatePresence>
                {expanded && (
                  <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
                    className="flex-1 min-w-0">
                    <p className="text-sm font-medium text-white truncate">{user?.username || (firebaseUser as any)?.displayName || 'User'}</p>
                    {user && (
                      <p className="text-[10px] text-gray-500">Lv.{user.level} &middot; {user.xp?.toLocaleString()} XP</p>
                    )}
                    {firebaseUser && !user && (
                      <p className="text-[10px] text-green-400">Google</p>
                    )}
                  </motion.div>
                )}
              </AnimatePresence>
            </Link>
            <button onClick={logout}
              className="flex items-center space-x-3 px-3 py-2 rounded-lg text-gray-500 hover:text-red-400 hover:bg-white/5 transition w-full text-sm">
              <LogOut className="w-4 h-4 flex-shrink-0" />
              <AnimatePresence>
                {expanded && (
                  <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>Logout</motion.span>
                )}
              </AnimatePresence>
            </button>
          </div>
        ) : (
          <div className="flex-shrink-0 border-t border-white/10 px-3 py-3 space-y-1">
            <Link href="/login"
              className="flex items-center space-x-3 px-3 py-2 rounded-lg text-gray-400 hover:text-white hover:bg-white/5 transition text-sm">
              <LogOut className="w-4 h-4 flex-shrink-0 rotate-180" />
              <AnimatePresence>
                {expanded && <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>Login</motion.span>}
              </AnimatePresence>
            </Link>
            <Link href="/register"
              className="flex items-center justify-center px-3 py-2 rounded-lg bg-white hover:bg-[#BFC3C7] text-black text-sm font-semibold transition">
              <AnimatePresence>
                {expanded ? (
                  <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>Register</motion.span>
                ) : (
                  <span className="text-xs">+</span>
                )}
              </AnimatePresence>
            </Link>
          </div>
        )}

        {/* Expand indicator */}
        <div className="flex-shrink-0 flex items-center justify-center h-8 border-t border-white/5">
          <ChevronRight className={`w-4 h-4 text-gray-600 transition-transform duration-300 ${expanded ? 'rotate-180' : ''}`} />
        </div>
      </aside>

      {/* Mobile top bar */}
      <div className="md:hidden fixed top-0 left-0 right-0 z-30 flex items-center justify-between h-14 px-4
        bg-[#1A1A1A]/95 backdrop-blur-xl border-b border-white/10">
        <button onClick={() => setMobileOpen(true)} className="p-1.5 text-gray-400 hover:text-white">
          <ChevronRight className="w-5 h-5" />
        </button>
        <Link href="/" className="flex items-center space-x-2">
          <div className="w-8 h-8 bg-white rounded-lg flex items-center justify-center font-bold text-black text-xs font-display">XP</div>
          <span className="font-display text-base font-bold text-white">XP</span>
        </Link>
        <Link href="/search" className="p-1.5 text-gray-400 hover:text-white">
          <Search className="w-5 h-5" />
        </Link>
      </div>
    </>
  )
}

function SidebarContent({ user, logout, pathname, onClose, firebaseUser }: {
  user: any, logout: () => void, pathname: string, onClose: () => void, firebaseUser?: any
}) {
  return (
    <div className="flex flex-col h-full">
      <div className="flex items-center justify-between px-4 h-14 border-b border-white/10">
        <Link href="/" onClick={onClose} className="flex items-center space-x-2">
          <div className="w-8 h-8 bg-white rounded-lg flex items-center justify-center font-bold text-black text-xs font-display">XP</div>
          <span className="font-display text-base font-bold text-white">XP</span>
        </Link>
        <button onClick={onClose} className="text-gray-400 hover:text-white p-1">
          <ChevronRight className="w-5 h-5" />
        </button>
      </div>
      <nav className="flex-1 px-3 py-3 space-y-0.5 overflow-y-auto">
        <Link href="/search" onClick={onClose}
          className="flex items-center space-x-3 px-3 py-2.5 rounded-lg text-sm text-gray-400 hover:text-white hover:bg-white/10 transition mb-2">
          <Search className="w-5 h-5" /><span>Search...</span>
        </Link>
        {navLinks.map((link) => {
          const active = pathname === link.href || pathname.startsWith(link.href + '/')
          return (
            <Link key={link.href} href={link.href} onClick={onClose}
              className={`flex items-center space-x-3 px-3 py-2.5 rounded-lg text-sm transition ${
                active ? 'text-white bg-white/10' : 'text-gray-400 hover:text-white hover:bg-white/5'
              }`}>
              <link.icon className="w-5 h-5" /><span>{link.label}</span>
            </Link>
          )
        })}
        <div className="border-t border-white/10 my-3" />
        <p className="px-3 text-[10px] uppercase tracking-widest text-gray-600 font-semibold mb-1">Account</p>
        {(user || firebaseUser) ? (
          <>
            {userLinks.map((link) => (
              <Link key={link.href} href={link.href} onClick={onClose}
                className="flex items-center space-x-3 px-3 py-2.5 rounded-lg text-sm text-gray-400 hover:text-white hover:bg-white/5 transition">
                <link.icon className="w-5 h-5" /><span>{link.label}</span>
              </Link>
            ))}
            <button onClick={() => { logout(); onClose(); }}
              className="flex items-center space-x-3 px-3 py-2.5 rounded-lg text-sm text-red-400 hover:bg-white/5 transition w-full mt-2">
              <LogOut className="w-5 h-5" /><span>Logout</span>
            </button>
          </>
        ) : (
          <>
            <Link href="/login" onClick={onClose}
              className="flex items-center space-x-3 px-3 py-2.5 rounded-lg text-sm text-gray-400 hover:text-white hover:bg-white/5 transition">
              <LogOut className="w-5 h-5 rotate-180" /><span>Login</span>
            </Link>
            <Link href="/register" onClick={onClose}
              className="flex items-center justify-center px-3 py-2.5 rounded-lg bg-white text-black text-sm font-semibold hover:bg-[#BFC3C7] transition mt-2">
              <span>Register</span>
            </Link>
          </>
        )}
      </nav>
    </div>
  )
}
