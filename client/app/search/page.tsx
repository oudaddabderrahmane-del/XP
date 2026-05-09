'use client'
import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { Search, ShoppingCart, Users, MessageSquare, Cpu, Filter, X } from 'lucide-react'
import { fetchAPI } from '@/lib/api'
import Link from 'next/link'

export default function SearchPage() {
  const [query, setQuery] = useState('')
  const [activeTab, setActiveTab] = useState('all')
  const [products, setProducts] = useState<any[]>([])
  const [communities, setCommunities] = useState<any[]>([])
  const [posts, setPosts] = useState<any[]>([])
  const [users, setUsers] = useState<any[]>([])
  const [loading, setLoading] = useState(false)
  const [searched, setSearched] = useState(false)

  useEffect(() => {
    if (query.length > 1) {
      const timer = setTimeout(doSearch, 400)
      return () => clearTimeout(timer)
    }
  }, [query, activeTab])

  async function doSearch() {
    if (!query.trim()) return
    setLoading(true)
    setSearched(true)
    try {
      const [p, c, po, u] = await Promise.all([
        fetchAPI(`/api/products?search=${encodeURIComponent(query)}&limit=20`),
        fetchAPI(`/api/communities?search=${encodeURIComponent(query)}`),
        fetchAPI(`/api/posts?search=${encodeURIComponent(query)}`).catch(() => ({ posts: [] })),
        fetchAPI(`/api/users?search=${encodeURIComponent(query)}`),
      ])
      setProducts(p.products || [])
      setCommunities(c.communities || [])
      setPosts(po.posts || [])
      setUsers(u.users || [])
    } catch (e) { console.error(e) }
    setLoading(false)
  }

  const totalResults = products.length + communities.length + posts.length + users.length

  const tabs = [
    { id: 'all', label: 'All', count: totalResults },
    { id: 'products', label: 'Products', count: products.length },
    { id: 'communities', label: 'Communities', count: communities.length },
    { id: 'posts', label: 'Posts', count: posts.length },
    { id: 'users', label: 'Users', count: users.length },
  ]

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Search Bar */}
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="mb-8">
        <h1 className="text-3xl sm:text-4xl font-display font-bold mb-4">Search</h1>
        <div className="relative">
          <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-6 h-6 text-gray-400" />
          <input type="text" value={query} onChange={(e) => setQuery(e.target.value)}
            placeholder="Search products, communities, posts, users..."
            className="w-full pl-12 pr-4 py-4 bg-white/5 border border-white/10 rounded-xl text-lg focus:outline-none focus:ring-2 focus:ring-blue-500" />
          {query && <button onClick={() => setQuery('')} className="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-white"><X className="w-5 h-5" /></button>}
        </div>
      </motion.div>

      {/* Tabs */}
      {searched && (
        <div className="flex space-x-2 mb-6 overflow-x-auto">
          {tabs.map(t => (
            <button key={t.id} onClick={() => setActiveTab(t.id)}
              className={`px-4 py-2 rounded-xl text-sm font-medium whitespace-nowrap transition ${activeTab === t.id ? 'bg-blue-600' : 'bg-white/5 hover:bg-white/10'}`}>
              {t.label} <span className="text-gray-400 ml-1">({t.count})</span>
            </button>
          ))}
        </div>
      )}

      {/* Results */}
      {loading ? (
        <div className="space-y-4">
          {[...Array(5)].map((_, i) => <div key={i} className="h-20 bg-white/5 rounded-xl animate-pulse" />)}
        </div>
      ) : searched && totalResults === 0 ? (
        <div className="text-center py-20">
          <Search className="w-16 h-16 text-gray-600 mx-auto mb-4" />
          <h3 className="text-xl font-semibold mb-2">No results found</h3>
          <p className="text-gray-400">Try different keywords or browse categories</p>
        </div>
      ) : searched ? (
        <div className="space-y-6">
          {/* Products */}
          {(activeTab === 'all' || activeTab === 'products') && products.length > 0 && (
            <div>
              <h2 className="text-xl font-display font-bold mb-4 flex items-center"><ShoppingCart className="w-5 h-5 mr-2 text-blue-400" />Products</h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                {products.map((p, i) => (
                  <Link key={p.id} href={`/product/${p.id}`}>
                    <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.03 }} className="bg-white/5 border border-white/10 rounded-xl p-4 hover:border-blue-500/50 transition group">
                      <span className="text-xs text-blue-400 uppercase font-semibold">{p.category}</span>
                      <h3 className="font-semibold mt-1 group-hover:text-blue-400 transition">{p.title}</h3>
                      <p className="text-lg font-bold text-blue-400 mt-2">${p.price}</p>
                    </motion.div>
                  </Link>
                ))}
              </div>
            </div>
          )}

          {/* Communities */}
          {(activeTab === 'all' || activeTab === 'communities') && communities.length > 0 && (
            <div>
              <h2 className="text-xl font-display font-bold mb-4 flex items-center"><Users className="w-5 h-5 mr-2 text-purple-400" />Communities</h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                {communities.map((c, i) => (
                  <motion.div key={c.id} initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.03 }}
                    className="bg-white/5 border border-white/10 rounded-xl p-4 hover:border-purple-500/50 transition group">
                    <div className="flex items-center space-x-3">
                      <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center font-bold">{c.name[0]}</div>
                      <div><h3 className="font-semibold">{c.name}</h3><p className="text-xs text-gray-400">{c.member_count || 0} members</p></div>
                    </div>
                  </motion.div>
                ))}
              </div>
            </div>
          )}

          {/* Posts */}
          {(activeTab === 'all' || activeTab === 'posts') && posts.length > 0 && (
            <div>
              <h2 className="text-xl font-display font-bold mb-4 flex items-center"><MessageSquare className="w-5 h-5 mr-2 text-green-400" />Posts</h2>
              <div className="space-y-3">
                {posts.map((p, i) => (
                  <motion.div key={p.id} initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.03 }}
                    className="bg-white/5 border border-white/10 rounded-xl p-4 hover:border-green-500/30 transition">
                    <h3 className="font-semibold">{p.title}</h3>
                    <p className="text-sm text-gray-400 line-clamp-1 mt-1">{p.content}</p>
                  </motion.div>
                ))}
              </div>
            </div>
          )}

          {/* Users */}
          {(activeTab === 'all' || activeTab === 'users') && users.length > 0 && (
            <div>
              <h2 className="text-xl font-display font-bold mb-4 flex items-center"><Users className="w-5 h-5 mr-2 text-cyan-400" />Users</h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                {users.map((u, i) => (
                  <Link key={u.id} href={`/profile/${u.id}`}>
                    <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.03 }}
                      className="bg-white/5 border border-white/10 rounded-xl p-4 hover:border-cyan-500/50 transition group flex items-center space-x-3">
                      <div className="w-10 h-10 rounded-full bg-gradient-to-br from-blue-400 to-purple-500 flex items-center justify-center font-bold">{u.username[0]}</div>
                      <div><h3 className="font-semibold group-hover:text-cyan-400 transition">{u.username}</h3><p className="text-xs text-gray-400">{u.xp} XP</p></div>
                    </motion.div>
                  </Link>
                ))}
              </div>
            </div>
          )}
        </div>
      ) : (
        <div className="text-center py-20">
          <Search className="w-16 h-16 text-gray-600 mx-auto mb-4" />
          <h3 className="text-xl font-semibold mb-2">Search across all of XP</h3>
          <p className="text-gray-400">Find products, communities, posts, and people</p>
        </div>
      )}
    </div>
  )
}
