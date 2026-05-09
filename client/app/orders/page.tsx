'use client'
import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { Package, Search, ChevronDown, MapPin, CreditCard, Truck, CheckCircle, Clock, XCircle } from 'lucide-react'
import { fetchAPI } from '@/lib/api'
import { useStore } from '@/store/useStore'
import { useRouter } from 'next/navigation'
import Link from 'next/link'

const statusConfig: Record<string, { icon: any; color: string; label: string }> = {
  pending: { icon: Clock, color: 'text-yellow-400 bg-yellow-500/20', label: 'Pending' },
  confirmed: { icon: CheckCircle, color: 'text-blue-400 bg-blue-500/20', label: 'Confirmed' },
  shipped: { icon: Truck, color: 'text-purple-400 bg-purple-500/20', label: 'Shipped' },
  delivered: { icon: CheckCircle, color: 'text-green-400 bg-green-500/20', label: 'Delivered' },
  cancelled: { icon: XCircle, color: 'text-red-400 bg-red-500/20', label: 'Cancelled' },
}

export default function OrdersPage() {
  const { user } = useStore()
  const router = useRouter()
  const [orders, setOrders] = useState<any[]>([])
  const [tab, setTab] = useState('all')
  const [search, setSearch] = useState('')

  useEffect(() => {
    if (!user) { router.push('/login'); return }
    fetchAPI('/api/orders').then(d => setOrders(d.orders || [])).catch(() => {})
  }, [user])

  const filtered = orders.filter(o => {
    if (tab !== 'all' && o.status !== tab) return false
    if (search && !o.id?.toLowerCase().includes(search.toLowerCase())) return false
    return true
  })

  const tabs = ['all', 'pending', 'confirmed', 'shipped', 'delivered', 'cancelled']

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="mb-8">
        <h1 className="text-3xl sm:text-4xl font-display font-bold mb-2">Orders</h1>
        <p className="text-gray-400">Track and manage your purchases</p>
      </motion.div>

      <div className="flex flex-col sm:flex-row gap-4 mb-6">
        <div className="relative flex-1">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
          <input type="text" placeholder="Search by order ID..." value={search} onChange={(e) => setSearch(e.target.value)}
            className="w-full pl-10 pr-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500" />
        </div>
      </div>

      <div className="flex space-x-2 mb-6 overflow-x-auto">
        {tabs.map(t => (
          <button key={t} onClick={() => setTab(t)}
            className={`px-4 py-2 rounded-xl text-sm font-medium capitalize whitespace-nowrap transition ${tab === t ? 'bg-blue-600' : 'bg-white/5 hover:bg-white/10'}`}>
            {t} {t === 'all' ? `(${orders.length})` : `(${orders.filter(o => o.status === t).length})`}
          </button>
        ))}
      </div>

      {filtered.length === 0 ? (
        <div className="text-center py-20">
          <Package className="w-16 h-16 text-gray-600 mx-auto mb-4" />
          <h3 className="text-xl font-semibold mb-2">No orders found</h3>
          <p className="text-gray-400">When you purchase items, they'll appear here</p>
          <Link href="/marketplace"><button className="mt-4 px-6 py-3 bg-blue-600 hover:bg-blue-700 rounded-xl font-semibold">Browse Marketplace</button></Link>
        </div>
      ) : (
        <div className="space-y-4">
          {filtered.map((order, i) => {
            const config = statusConfig[order.status] || statusConfig.pending
            const Icon = config.icon
            return (
              <motion.div key={order.id} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.03 }}
                className="bg-white/5 border border-white/10 rounded-xl p-5 hover:border-blue-500/30 transition group">
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                  <div className="flex items-center space-x-4">
                    <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">
                      <Package className="w-6 h-6" />
                    </div>
                    <div>
                      <p className="text-xs text-gray-400">Order #{order.id?.slice(0, 8)}</p>
                      <p className="font-semibold mt-0.5">{order.product_id ? `Product ${order.product_id.slice(0, 8)}...` : 'Order'}</p>
                      <div className="flex items-center space-x-3 text-xs text-gray-400 mt-1">
                        <span>{new Date(order.created_at).toLocaleDateString()}</span>
                        <span>Qty: {order.quantity || 1}</span>
                      </div>
                    </div>
                  </div>
                  <div className="flex items-center space-x-4 sm:text-right">
                    <div>
                      <p className="text-lg font-bold text-blue-400">${(order.total_price || 0).toFixed(2)}</p>
                      <span className={`inline-flex items-center space-x-1 px-2.5 py-1 rounded-full text-xs font-semibold ${config.color}`}>
                        <Icon className="w-3 h-3" /><span>{config.label}</span>
                      </span>
                    </div>
                    <button className="p-2 rounded-lg hover:bg-white/10"><ChevronDown className="w-5 h-5" /></button>
                  </div>
                </div>
                {order.status === 'shipped' && order.tracking_number && (
                  <div className="mt-4 pt-4 border-t border-white/10 flex items-center text-sm text-gray-400">
                    <Truck className="w-4 h-4 mr-2 text-blue-400" />
                    <span>Tracking: <span className="text-blue-400">{order.tracking_number}</span></span>
                  </div>
                )}
              </motion.div>
            )
          })}
        </div>
      )}
    </div>
  )
}
