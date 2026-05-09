'use client'
import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { Plus, Package, TrendingUp, DollarSign, Star, Edit3, Trash2, BarChart3 } from 'lucide-react'
import { fetchAPI } from '@/lib/api'
import { useStore } from '@/store/useStore'
import { useRouter } from 'next/navigation'
import Link from 'next/link'

export default function SellerDashboard() {
  const { user } = useStore()
  const router = useRouter()
  const [products, setProducts] = useState<any[]>([])
  const [showAdd, setShowAdd] = useState(false)
  const [form, setForm] = useState({ title: '', description: '', price: 0, category: 'GPU', condition: 'new', location: '' })

  useEffect(() => {
    if (!user) { router.push('/login'); return }
    fetchAPI('/api/products').then(d => setProducts((d.products || []).filter((p: any) => p.seller_id === user!.id))).catch(() => {})
  }, [user])

  async function addProduct() {
    if (!form.title.trim()) return
    try {
      await fetchAPI('/api/products', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form),
      })
      setForm({ title: '', description: '', price: 0, category: 'GPU', condition: 'new', location: '' })
      setShowAdd(false)
      const data = await fetchAPI('/api/products')
      setProducts((data.products || []).filter((p: any) => p.seller_id === user!.id))
    } catch (e) { console.error(e) }
  }

  async function deleteProduct(id: string) {
    try {
      await fetchAPI(`/api/products/${id}`, { method: 'DELETE' })
      setProducts(prev => prev.filter(p => p.id !== id))
    } catch (e) { console.error(e) }
  }

  const stats = [
    { label: 'Listings', value: products.length, icon: Package, color: 'from-blue-500 to-cyan-500' },
    { label: 'Total Value', value: `$${products.reduce((s, p) => s + p.price, 0).toLocaleString()}`, icon: DollarSign, color: 'from-green-500 to-emerald-500' },
    { label: 'Total Views', value: products.reduce((s, p) => s + (p.views || 0), 0), icon: TrendingUp, color: 'from-purple-500 to-pink-500' },
    { label: 'Avg. Rating', value: products.length ? (products.reduce((s, p) => s + (p.rating || 0), 0) / products.length).toFixed(1) : '0.0', icon: Star, color: 'from-yellow-500 to-amber-500' },
  ]

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="flex items-center justify-between mb-8">
        <div><h1 className="text-3xl sm:text-4xl font-display font-bold">Seller Dashboard</h1><p className="text-gray-400">Manage your marketplace listings</p></div>
        <button onClick={() => setShowAdd(!showAdd)} className="flex items-center space-x-2 px-5 py-3 bg-blue-600 hover:bg-blue-700 rounded-xl font-semibold transition">
          <Plus className="w-5 h-5" /><span>Add Product</span>
        </button>
      </motion.div>

      {/* Stats */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        {stats.map((s, i) => (
          <motion.div key={i} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.05 }}
            className="bg-white/5 border border-white/10 rounded-xl p-5">
            <div className={`w-10 h-10 rounded-lg bg-gradient-to-br ${s.color} flex items-center justify-center mb-3`}><s.icon className="w-5 h-5" /></div>
            <p className="text-2xl font-bold">{s.value}</p><p className="text-sm text-gray-400">{s.label}</p>
          </motion.div>
        ))}
      </div>

      {/* Add Product Form */}
      {showAdd && (
        <motion.div initial={{ opacity: 0, y: -10 }} animate={{ opacity: 1, y: 0 }} className="bg-white/5 border border-white/10 rounded-xl p-6 mb-8">
          <h3 className="font-semibold mb-4">New Listing</h3>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-4">
            <input type="text" placeholder="Product title" value={form.title} onChange={(e) => setForm(f => ({ ...f, title: e.target.value }))} className="px-4 py-3 bg-white/5 border border-white/10 rounded-xl" />
            <input type="number" placeholder="Price" value={form.price || ''} onChange={(e) => setForm(f => ({ ...f, price: Number(e.target.value) }))} className="px-4 py-3 bg-white/5 border border-white/10 rounded-xl" />
            <select value={form.category} onChange={(e) => setForm(f => ({ ...f, category: e.target.value }))} className="px-4 py-3 bg-white/5 border border-white/10 rounded-xl">
              <option>GPU</option><option>CPU</option><option>RAM</option><option>Motherboard</option><option>Storage</option><option>PSU</option><option>PC</option><option>Console</option><option>Accessory</option>
            </select>
            <select value={form.condition} onChange={(e) => setForm(f => ({ ...f, condition: e.target.value }))} className="px-4 py-3 bg-white/5 border border-white/10 rounded-xl">
              <option value="new">New</option><option value="used">Used</option><option value="refurbished">Refurbished</option>
            </select>
            <input type="text" placeholder="Location (optional)" value={form.location} onChange={(e) => setForm(f => ({ ...f, location: e.target.value }))} className="px-4 py-3 bg-white/5 border border-white/10 rounded-xl" />
            <textarea placeholder="Description" value={form.description} onChange={(e) => setForm(f => ({ ...f, description: e.target.value }))} rows={3} className="px-4 py-3 bg-white/5 border border-white/10 rounded-xl sm:col-span-2" />
          </div>
          <button onClick={addProduct} className="px-6 py-3 bg-blue-600 hover:bg-blue-700 rounded-xl font-semibold">Publish Listing</button>
        </motion.div>
      )}

      {/* Products Table */}
      <div className="bg-white/5 border border-white/10 rounded-xl overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead><tr className="border-b border-white/10 text-left text-sm text-gray-400">
              <th className="p-4">Product</th><th className="p-4">Category</th><th className="p-4">Price</th><th className="p-4">Views</th><th className="p-4">Status</th><th className="p-4">Actions</th>
            </tr></thead>
            <tbody>{products.length === 0 ? (
              <tr><td colSpan={6} className="p-8 text-center text-gray-400">No listings yet. Click "Add Product" to get started.</td></tr>
            ) : products.map((p, i) => (
              <tr key={p.id} className="border-b border-white/5 hover:bg-white/5 transition text-sm">
                <td className="p-4"><Link href={`/product/${p.id}`} className="font-medium hover:text-blue-400 transition">{p.title}</Link></td>
                <td className="p-4"><span className="px-2 py-1 bg-blue-500/20 text-blue-300 rounded text-xs">{p.category}</span></td>
                <td className="p-4 text-blue-400 font-bold">${p.price}</td>
                <td className="p-4 text-gray-400">{p.views || 0}</td>
                <td className="p-4"><span className={`px-2 py-1 rounded text-xs ${p.is_available ? 'bg-green-500/20 text-green-300' : 'bg-red-500/20 text-red-300'}`}>{p.is_available ? 'Active' : 'Hidden'}</span></td>
                <td className="p-4"><div className="flex space-x-2">
                  <button className="p-1.5 rounded-lg hover:bg-white/10"><Edit3 className="w-4 h-4 text-gray-400" /></button>
                  <button onClick={() => deleteProduct(p.id)} className="p-1.5 rounded-lg hover:bg-white/10"><Trash2 className="w-4 h-4 text-red-400" /></button>
                </div></td>
              </tr>
            ))}</tbody>
          </table>
        </div>
      </div>
    </div>
  )
}
