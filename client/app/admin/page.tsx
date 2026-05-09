'use client'
import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { Users, ShoppingCart, MessageSquare, TrendingUp, DollarSign, Shield, Activity, BarChart3, AlertTriangle, CheckCircle, XCircle } from 'lucide-react'
import { fetchAPI } from '@/lib/api'
import { useStore } from '@/store/useStore'
import { useRouter } from 'next/navigation'

export default function AdminDashboard() {
  const { user } = useStore()
  const router = useRouter()
  const [users, setUsers] = useState<any[]>([])
  const [products, setProducts] = useState<any[]>([])
  const [posts, setPosts] = useState<any[]>([])
  const [tab, setTab] = useState('overview')

  useEffect(() => {
    if (user && user.role !== 'admin') { router.push('/dashboard'); return }
    Promise.all([
      fetchAPI('/api/users').then(d => setUsers(d.users || [])).catch(() => {}),
      fetchAPI('/api/products').then(d => setProducts(d.products || [])).catch(() => {}),
      fetchAPI('/api/posts').then(d => setPosts(d.posts || [])).catch(() => {}),
    ])
  }, [user])

  const stats = [
    { label: 'Total Users', value: users.length, icon: Users, color: 'from-blue-500 to-cyan-500', change: '+12%' },
    { label: 'Products', value: products.length, icon: ShoppingCart, color: 'from-green-500 to-emerald-500', change: '+8%' },
    { label: 'Posts', value: posts.length, icon: MessageSquare, color: 'from-purple-500 to-pink-500', change: '+15%' },
    { label: 'Revenue', value: '$24.5K', icon: DollarSign, color: 'from-yellow-500 to-amber-500', change: '+22%' },
  ]

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="mb-8">
        <div className="flex items-center space-x-3">
          <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-red-500 to-purple-600 flex items-center justify-center"><Shield className="w-6 h-6" /></div>
          <div><h1 className="text-3xl sm:text-4xl font-display font-bold">Admin Panel</h1><p className="text-gray-400">Manage users, products, and platform health</p></div>
        </div>
      </motion.div>

      {/* Tabs */}
      <div className="flex space-x-2 mb-8 overflow-x-auto">
        {['overview', 'users', 'products', 'posts', 'analytics', 'reports'].map(t => (
          <button key={t} onClick={() => setTab(t)}
            className={`px-5 py-2.5 rounded-xl text-sm font-medium capitalize whitespace-nowrap transition ${tab === t ? 'bg-blue-600 text-white' : 'bg-white/5 hover:bg-white/10'}`}>{t}</button>
        ))}
      </div>

      {tab === 'overview' && (
        <>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
            {stats.map((s, i) => (
              <motion.div key={i} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.05 }}
                className="bg-white/5 border border-white/10 rounded-xl p-5">
                <div className="flex items-center justify-between mb-4">
                  <div className={`w-10 h-10 rounded-lg bg-gradient-to-br ${s.color} flex items-center justify-center`}><s.icon className="w-5 h-5" /></div>
                  <span className="text-xs text-green-400 bg-green-400/10 px-2 py-1 rounded-full">{s.change}</span>
                </div>
                <p className="text-2xl font-bold">{s.value}</p>
                <p className="text-sm text-gray-400">{s.label}</p>
              </motion.div>
            ))}
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div className="bg-white/5 border border-white/10 rounded-xl p-6">
              <h3 className="font-semibold mb-4 flex items-center"><Activity className="w-5 h-5 mr-2 text-blue-400" />Recent Users</h3>
              <div className="space-y-3">
                {users.slice(0, 5).map((u, i) => (
                  <div key={u.id} className="flex items-center justify-between py-2 border-b border-white/5 last:border-0">
                    <div className="flex items-center space-x-3">
                      <div className="w-8 h-8 rounded-full bg-gradient-to-br from-blue-400 to-purple-500 flex items-center justify-center text-xs font-bold">{u.username[0]}</div>
                      <div><p className="font-medium text-sm">{u.username}</p><p className="text-xs text-gray-400">{u.role} · {u.xp} XP</p></div>
                    </div>
                    <span className="text-xs text-gray-400">{new Date(u.created_at).toLocaleDateString()}</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="bg-white/5 border border-white/10 rounded-xl p-6">
              <h3 className="font-semibold mb-4 flex items-center"><BarChart3 className="w-5 h-5 mr-2 text-purple-400" />Platform Health</h3>
              <div className="space-y-4">
                {[
                  { label: 'Server Uptime', value: '99.9%', status: 'ok' },
                  { label: 'Active Users (24h)', value: '1,247', status: 'ok' },
                  { label: 'Pending Reports', value: '3', status: 'warning' },
                  { label: 'New Registrations', value: '89', status: 'ok' },
                  { label: 'Support Tickets', value: '12', status: 'warning' },
                ].map((item, i) => (
                  <div key={i} className="flex items-center justify-between py-2 border-b border-white/5 last:border-0">
                    <span className="text-sm text-gray-300">{item.label}</span>
                    <div className="flex items-center space-x-2">
                      <span className="font-semibold">{item.value}</span>
                      {item.status === 'ok' ? <CheckCircle className="w-4 h-4 text-green-400" /> : <AlertTriangle className="w-4 h-4 text-yellow-400" />}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </>
      )}

      {tab === 'users' && (
        <div className="bg-white/5 border border-white/10 rounded-xl overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead><tr className="border-b border-white/10 text-left text-sm text-gray-400">
                <th className="p-4">User</th><th className="p-4">Role</th><th className="p-4">XP</th><th className="p-4">Level</th><th className="p-4">Joined</th><th className="p-4">Actions</th>
              </tr></thead>
              <tbody>{users.map((u, i) => (
                <tr key={u.id} className="border-b border-white/5 hover:bg-white/5 transition text-sm">
                  <td className="p-4"><div className="flex items-center space-x-3"><div className="w-8 h-8 rounded-full bg-gradient-to-br from-blue-400 to-purple-500 flex items-center justify-center text-xs font-bold">{u.username[0]}</div><span>{u.username}</span></div></td>
                  <td className="p-4"><span className={`px-2 py-1 rounded text-xs font-semibold ${u.role === 'admin' ? 'bg-red-500/20 text-red-300' : u.role === 'moderator' ? 'bg-purple-500/20 text-purple-300' : 'bg-blue-500/20 text-blue-300'}`}>{u.role}</span></td>
                  <td className="p-4">{u.xp}</td><td className="p-4">{u.level}</td>
                  <td className="p-4 text-gray-400">{u.created_at ? new Date(u.created_at).toLocaleDateString() : '-'}</td>
                  <td className="p-4"><button className="text-xs text-red-400 hover:text-red-300">Suspend</button></td>
                </tr>
              ))}</tbody>
            </table>
          </div>
        </div>
      )}

      {tab === 'products' && (
        <div className="bg-white/5 border border-white/10 rounded-xl overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead><tr className="border-b border-white/10 text-left text-sm text-gray-400">
                <th className="p-4">Title</th><th className="p-4">Category</th><th className="p-4">Price</th><th className="p-4">Views</th><th className="p-4">Status</th><th className="p-4">Actions</th>
              </tr></thead>
              <tbody>{products.map((p, i) => (
                <tr key={p.id} className="border-b border-white/5 hover:bg-white/5 transition text-sm">
                  <td className="p-4 font-medium">{p.title}</td>
                  <td className="p-4"><span className="px-2 py-1 bg-blue-500/20 text-blue-300 rounded text-xs">{p.category}</span></td>
                  <td className="p-4 text-blue-400 font-bold">${p.price}</td>
                  <td className="p-4 text-gray-400">{p.views || 0}</td>
                  <td className="p-4"><span className={`px-2 py-1 rounded text-xs ${p.is_available ? 'bg-green-500/20 text-green-300' : 'bg-red-500/20 text-red-300'}`}>{p.is_available ? 'Active' : 'Hidden'}</span></td>
                  <td className="p-4"><div className="flex space-x-2"><button className="text-xs text-red-400 hover:text-red-300">Remove</button><button className="text-xs text-gray-400 hover:text-gray-300">View</button></div></td>
                </tr>
              ))}</tbody>
            </table>
          </div>
        </div>
      )}

      {tab === 'analytics' && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div className="bg-white/5 border border-white/10 rounded-xl p-6">
            <h3 className="font-semibold mb-4">Category Distribution</h3>
            {['GPU', 'CPU', 'PC', 'Console', 'RAM', 'Other'].map(cat => (
              <div key={cat} className="flex items-center justify-between py-2 border-b border-white/5 text-sm">
                <span>{cat}</span>
                <div className="flex items-center space-x-3"><div className="w-32 h-2 bg-white/10 rounded-full overflow-hidden"><div className="h-full bg-blue-500 rounded-full" style={{ width: `${Math.random() * 40 + 10}%` }} /></div><span className="text-gray-400">{Math.floor(Math.random() * 30 + 5)}</span></div>
              </div>
            ))}
          </div>
          <div className="bg-white/5 border border-white/10 rounded-xl p-6">
            <h3 className="font-semibold mb-4">Revenue Overview</h3>
            <p className="text-4xl font-bold mb-4">$24,583</p>
            <div className="space-y-3 text-sm">
              <div className="flex justify-between"><span className="text-gray-400">This Month</span><span>$12,450</span></div>
              <div className="flex justify-between"><span className="text-gray-400">Last Month</span><span>$10,230</span></div>
              <div className="flex justify-between"><span className="text-gray-400">Avg. Order Value</span><span>$342</span></div>
              <div className="flex justify-between"><span className="text-gray-400">Conversion Rate</span><span>3.2%</span></div>
            </div>
          </div>
        </div>
      )}

      {tab === 'reports' && (
        <div className="text-center py-12">
          <Shield className="w-16 h-16 text-gray-600 mx-auto mb-4" />
          <h3 className="text-xl font-semibold mb-2">No Reports</h3>
          <p className="text-gray-400">All reported content has been reviewed.</p>
        </div>
      )}
    </div>
  )
}
