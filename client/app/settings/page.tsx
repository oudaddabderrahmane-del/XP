'use client'
import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { User, Bell, Shield, Palette, Globe, CreditCard, Smartphone, Eye, EyeOff, Save, CheckCircle } from 'lucide-react'
import { fetchAPI } from '@/lib/api'
import { useStore } from '@/store/useStore'
import { useRouter } from 'next/navigation'

const tabs = [
  { id: 'profile', label: 'Profile', icon: User },
  { id: 'notifications', label: 'Notifications', icon: Bell },
  { id: 'security', label: 'Security', icon: Shield },
  { id: 'appearance', label: 'Appearance', icon: Palette },
  { id: 'payments', label: 'Payments', icon: CreditCard },
]

export default function SettingsPage() {
  const { user } = useStore()
  const router = useRouter()
  const [tab, setTab] = useState('profile')
  const [saved, setSaved] = useState(false)
  const [form, setForm] = useState({ username: '', bio: '', location: '', email: '' })

  useEffect(() => {
    if (!user) { router.push('/login'); return }
    setForm({ username: user.username || '', bio: user.bio || '', location: user.location || '', email: user.email || '' })
  }, [user])

  function handleSave() {
    setSaved(true)
    setTimeout(() => setSaved(false), 2000)
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="mb-8">
        <h1 className="text-3xl sm:text-4xl font-display font-bold">Settings</h1>
        <p className="text-gray-400">Manage your account preferences</p>
      </motion.div>

      <div className="flex flex-col lg:flex-row gap-8">
        {/* Sidebar Tabs */}
        <div className="lg:w-64 flex-shrink-0">
          <div className="flex lg:flex-col space-x-2 lg:space-x-0 lg:space-y-1 overflow-x-auto">
            {tabs.map(t => (
              <button key={t.id} onClick={() => setTab(t.id)}
                className={`flex items-center space-x-2 px-4 py-3 rounded-xl text-sm font-medium whitespace-nowrap transition ${tab === t.id ? 'bg-blue-600 text-white' : 'text-gray-300 hover:bg-white/10'}`}>
                <t.icon className="w-4 h-4" /><span>{t.label}</span>
              </button>
            ))}
          </div>
        </div>

        {/* Content */}
        <div className="flex-1">
          {tab === 'profile' && (
            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="bg-white/5 border border-white/10 rounded-xl p-6 space-y-5">
              <h2 className="text-xl font-display font-bold">Profile Information</h2>
              <div className="flex items-center space-x-4 pb-5 border-b border-white/10">
                <div className="w-20 h-20 rounded-2xl bg-gradient-to-br from-blue-400 to-purple-600 flex items-center justify-center text-3xl font-bold">{user?.username?.[0] || '?'}</div>
                <div><button className="px-4 py-2 bg-white/10 hover:bg-white/20 rounded-lg text-sm font-semibold">Change Avatar</button><p className="text-xs text-gray-400 mt-1">JPG, PNG, GIF. Max 5MB.</p></div>
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div><label className="text-sm text-gray-300 block mb-1">Username</label><input type="text" value={form.username} onChange={(e) => setForm(f => ({ ...f, username: e.target.value }))} className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500" /></div>
                <div><label className="text-sm text-gray-300 block mb-1">Email</label><input type="email" value={form.email} onChange={(e) => setForm(f => ({ ...f, email: e.target.value }))} className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500" /></div>
                <div><label className="text-sm text-gray-300 block mb-1">Location</label><input type="text" value={form.location} onChange={(e) => setForm(f => ({ ...f, location: e.target.value }))} className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500" /></div>
                <div className="sm:col-span-2"><label className="text-sm text-gray-300 block mb-1">Bio</label><textarea value={form.bio} onChange={(e) => setForm(f => ({ ...f, bio: e.target.value }))} rows={3} className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500" /></div>
              </div>
              <button onClick={handleSave} className="flex items-center space-x-2 px-6 py-3 bg-blue-600 hover:bg-blue-700 rounded-xl font-semibold transition">
                {saved ? <><CheckCircle className="w-5 h-5 text-green-400" /><span>Saved!</span></> : <><Save className="w-5 h-5" /><span>Save Changes</span></>}
              </button>
            </motion.div>
          )}

          {tab === 'notifications' && (
            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="bg-white/5 border border-white/10 rounded-xl p-6 space-y-5">
              <h2 className="text-xl font-display font-bold">Notification Preferences</h2>
              {[
                { label: 'Messages', desc: 'When someone sends you a message' },
                { label: 'Comments', desc: 'When someone comments on your post' },
                { label: 'Orders', desc: 'Order confirmations and updates' },
                { label: 'Marketplace', desc: 'Price drops and new listings' },
                { label: 'Community', desc: 'Community announcements' },
                { label: 'Promotions', desc: 'Special offers and promotions' },
              ].map((item, i) => (
                <div key={i} className="flex items-center justify-between py-3 border-b border-white/10 last:border-0">
                  <div><p className="font-medium text-sm">{item.label}</p><p className="text-xs text-gray-400">{item.desc}</p></div>
                  <label className="relative inline-flex items-center cursor-pointer"><input type="checkbox" defaultChecked className="sr-only peer" /><div className="w-11 h-6 bg-white/10 rounded-full peer peer-checked:bg-blue-600 after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:after:translate-x-full" /></label>
                </div>
              ))}
              <button onClick={handleSave} className="px-6 py-3 bg-blue-600 hover:bg-blue-700 rounded-xl font-semibold">Save Preferences</button>
            </motion.div>
          )}

          {tab === 'security' && (
            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="bg-white/5 border border-white/10 rounded-xl p-6 space-y-5">
              <h2 className="text-xl font-display font-bold">Security Settings</h2>
              <div><label className="text-sm text-gray-300 block mb-1">Current Password</label><input type="password" className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl" /></div>
              <div><label className="text-sm text-gray-300 block mb-1">New Password</label><input type="password" className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl" /></div>
              <div><label className="text-sm text-gray-300 block mb-1">Confirm Password</label><input type="password" className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl" /></div>
              <button className="px-6 py-3 bg-blue-600 hover:bg-blue-700 rounded-xl font-semibold">Update Password</button>
              <div className="border-t border-white/10 pt-5 space-y-3">
                <h3 className="font-semibold">Two-Factor Authentication</h3>
                <div className="flex items-center justify-between"><span className="text-sm text-gray-300">Authenticator App</span><label className="relative inline-flex items-center cursor-pointer"><input type="checkbox" className="sr-only peer" /><div className="w-11 h-6 bg-white/10 rounded-full peer peer-checked:bg-blue-600 after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:after:translate-x-full" /></label></div>
                <div className="flex items-center justify-between"><span className="text-sm text-gray-300">SMS Authentication</span><label className="relative inline-flex items-center cursor-pointer"><input type="checkbox" className="sr-only peer" /><div className="w-11 h-6 bg-white/10 rounded-full peer peer-checked:bg-blue-600 after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:after:translate-x-full" /></label></div>
              </div>
            </motion.div>
          )}

          {tab === 'appearance' && (
            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="bg-white/5 border border-white/10 rounded-xl p-6 space-y-5">
              <h2 className="text-xl font-display font-bold">Appearance</h2>
              <div><label className="text-sm text-gray-300 block mb-3">Theme</label><div className="flex space-x-3">
                {['Dark', 'Light', 'System'].map(theme => (<button key={theme} className={`flex-1 px-4 py-3 rounded-xl text-sm font-medium border transition ${theme === 'Dark' ? 'bg-blue-600/20 border-blue-500 text-white' : 'bg-white/5 border-white/10 text-gray-300 hover:bg-white/10'}`}>{theme}</button>))}
              </div></div>
              <div><label className="text-sm text-gray-300 block mb-3">Accent Color</label><div className="flex space-x-3">
                {['#3B82F6', '#8B5CF6', '#10B981', '#F59E0B', '#EF4444', '#EC4899'].map(color => (<button key={color} className={`w-10 h-10 rounded-xl transition ${color === '#3B82F6' ? 'ring-2 ring-white ring-offset-2 ring-offset-black' : ''}`} style={{ backgroundColor: color }} />))}
              </div></div>
              <div><label className="text-sm text-gray-300 block mb-3">Card Style</label><div className="flex space-x-3">
                {['Glassmorphism', 'Minimal', 'Bordered'].map(style => (<button key={style} className={`flex-1 px-4 py-3 rounded-xl text-sm font-medium border transition ${style === 'Glassmorphism' ? 'bg-blue-600/20 border-blue-500 text-white' : 'bg-white/5 border-white/10 text-gray-300 hover:bg-white/10'}`}>{style}</button>))}
              </div></div>
            </motion.div>
          )}

          {tab === 'payments' && (
            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="bg-white/5 border border-white/10 rounded-xl p-6 space-y-5">
              <h2 className="text-xl font-display font-bold">Payment Methods</h2>
              <div className="p-4 bg-white/5 rounded-xl flex items-center justify-between">
                <div className="flex items-center space-x-3"><CreditCard className="w-8 h-8 text-blue-400" /><div><p className="font-medium">•••• 4242</p><p className="text-xs text-gray-400">Expires 12/28</p></div></div>
                <span className="px-2 py-1 bg-green-500/20 text-green-400 text-xs rounded-full font-semibold">Default</span>
              </div>
              <button className="w-full py-3 border-2 border-dashed border-white/20 rounded-xl text-sm text-gray-400 hover:text-white hover:border-white/40 transition">+ Add Payment Method</button>
              <div className="border-t border-white/10 pt-5 space-y-3">
                <h3 className="font-semibold">Crypto Payments</h3>
                <div className="flex items-center justify-between"><span className="text-sm text-gray-300">Accept crypto payments</span><label className="relative inline-flex items-center cursor-pointer"><input type="checkbox" className="sr-only peer" /><div className="w-11 h-6 bg-white/10 rounded-full peer peer-checked:bg-blue-600 after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:after:translate-x-full" /></label></div>
                <p className="text-xs text-gray-400">Support BTC, ETH, USDT, and more</p>
              </div>
            </motion.div>
          )}
        </div>
      </div>
    </div>
  )
}
