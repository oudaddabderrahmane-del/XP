'use client'
import { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { 
  Search, ShoppingCart, Heart, MapPin, ChevronDown, X, 
  ArrowUp, ArrowDown, MessageCircle, Share2, Clock, 
  TrendingUp, Flame, Plus, Zap, Eye, User, Tag,
  Filter, RefreshCw, CheckCircle
} from 'lucide-react'
import { fetchAPI } from '@/lib/api'
import Link from 'next/link'

interface Product {
  id: string; title: string; price: number; category: string; condition: string
  images: string[]; location: string; rating: number; created_at: string
  description?: string; seller_id?: string; views?: number; favorites?: number
}

const categories = ['All', 'GPU', 'CPU', 'RAM', 'Motherboard', 'Storage', 'PSU', 'Console', 'PC', 'Laptop', 'Monitor', 'Accessory']

function timeAgo(date: string) {
  const s = Math.floor((Date.now() - new Date(date).getTime()) / 1000)
  if (s < 60) return 'just now'
  if (s < 3600) return `${Math.floor(s / 60)}m ago`
  if (s < 86400) return `${Math.floor(s / 3600)}h ago`
  return `${Math.floor(s / 86400)}d ago`
}

export default function MarketplacePage() {
  const [products, setProducts] = useState<Product[]>([])
  const [loading, setLoading] = useState(true)
  const [search, setSearch] = useState('')
  const [category, setCategory] = useState('All')
  const [sort, setSort] = useState('newest')
  const [favorites, setFavorites] = useState<Set<string>>(new Set())
  const [votes, setVotes] = useState<Record<string, number>>({})
  const [showFilters, setShowFilters] = useState(false)

  useEffect(() => { loadProducts() }, [category, sort])

  async function loadProducts() {
    setLoading(true)
    try {
      const params = new URLSearchParams()
      if (category !== 'All') params.set('category', category)
      if (search) params.set('search', search)
      params.set('sort', sort)
      const data = await fetchAPI(`/api/products?${params}`)
      setProducts(data.products || [])
    } catch (e) { console.error(e) }
    setLoading(false)
  }

  useEffect(() => {
    const timer = setTimeout(loadProducts, 300)
    return () => clearTimeout(timer)
  }, [search])

  const trending = products.slice(0, 5)

  return (
    <div className="min-h-screen">
      {/* Scanning header line */}
      <div className="fixed top-16 left-0 right-0 h-[1px] bg-gradient-to-r from-transparent via-[#BFC3C7]/20 to-transparent z-40" />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        {/* Top Bar */}
        <motion.div initial={{ opacity: 0, y: -10 }} animate={{ opacity: 1, y: 0 }} className="flex items-center justify-between mb-6">
          <div>
            <h1 className="text-2xl sm:text-3xl font-display font-bold flex items-center gap-3">
              Marketplace
              <span className="text-xs font-normal text-gray-500 bg-white/5 px-2.5 py-1 rounded-full">Social Feed</span>
            </h1>
            <p className="text-gray-500 text-sm mt-0.5">Discover, vote, and chat — the social way to buy & sell</p>
          </div>
          <div className="flex items-center gap-3">
            <button onClick={() => setShowFilters(!showFilters)}
              className="p-2.5 rounded-xl bg-white/5 border border-white/10 hover:bg-white/10 transition">
              <Filter className="w-4 h-4 text-gray-400" />
            </button>
            <Link href="/seller" className="hidden sm:flex items-center gap-2 px-4 py-2.5 bg-white text-black rounded-xl text-sm font-semibold hover:bg-[#BFC3C7] transition">
              <Plus className="w-4 h-4" /> <span>Create Listing</span>
            </Link>
          </div>
        </motion.div>

        {/* Search + Filters */}
        <AnimatePresence>
          <motion.div initial={{ opacity: 0, height: 0 }} animate={{ opacity: 1, height: 'auto' }} exit={{ opacity: 0, height: 0 }}
            className="overflow-hidden mb-6">
            <div className="space-y-4">
              <div className="relative">
                <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-500" />
                <input type="text" placeholder="Search the marketplace..."
                  value={search} onChange={(e) => setSearch(e.target.value)}
                  className="w-full pl-11 pr-4 py-3 bg-[#1A1A1A] border border-white/10 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#BFC3C7]/30 focus:ring-1 focus:ring-[#BFC3C7]/20 text-sm transition" />
              </div>
              <div className="flex flex-wrap items-center gap-3">
                <div className="flex flex-wrap gap-1.5">
                  {categories.map((cat) => (
                    <button key={cat} onClick={() => setCategory(cat)}
                      className={`px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all ${
                        category === cat
                          ? 'bg-white text-black'
                          : 'bg-[#1A1A1A] text-gray-400 hover:text-white hover:bg-white/10 border border-white/5'
                      }`}>
                      {cat}
                    </button>
                  ))}
                </div>
                <select value={sort} onChange={(e) => setSort(e.target.value)}
                  className="px-3 py-1.5 bg-[#1A1A1A] border border-white/10 rounded-lg text-xs text-gray-300 focus:outline-none">
                  <option value="newest">Newest</option>
                  <option value="price_asc">Price: Low</option>
                  <option value="price_desc">Price: High</option>
                </select>
              </div>
            </div>
          </motion.div>
        </AnimatePresence>

        <div className="flex gap-8">
          {/* Main Feed - Reddit Style */}
          <div className="flex-1 min-w-0">
            {loading ? (
              <div className="space-y-4">
                {[...Array(4)].map((_, i) => (
                  <div key={i} className="flex gap-4 p-4 bg-[#1A1A1A] rounded-xl animate-pulse">
                    <div className="w-10 flex-shrink-0 space-y-2">
                      <div className="w-8 h-8 bg-white/5 rounded-full mx-auto" />
                      <div className="w-8 h-8 bg-white/5 rounded-full mx-auto" />
                      <div className="w-8 h-8 bg-white/5 rounded-full mx-auto" />
                    </div>
                    <div className="flex-1 space-y-3">
                      <div className="h-48 bg-white/5 rounded-lg" />
                      <div className="h-4 bg-white/5 rounded w-3/4" />
                      <div className="h-3 bg-white/5 rounded w-1/2" />
                    </div>
                  </div>
                ))}
              </div>
            ) : products.length === 0 ? (
              <div className="text-center py-24">
                <ShoppingCart className="w-16 h-16 text-gray-600 mx-auto mb-4" />
                <h3 className="text-xl font-semibold mb-2">No listings yet</h3>
                <p className="text-gray-500 mb-6">Be the first to create a listing</p>
                <Link href="/seller" className="inline-flex items-center gap-2 px-6 py-3 bg-white text-black rounded-xl font-semibold hover:bg-[#BFC3C7] transition">
                  <Plus className="w-4 h-4" /> Create Listing
                </Link>
              </div>
            ) : (
              <div className="space-y-4">
                <div className="flex items-center justify-between mb-2">
                  <span className="text-sm text-gray-500 flex items-center gap-2">
                    <Zap className="w-3.5 h-3.5" /> {products.length} listings
                  </span>
                  <button onClick={loadProducts} className="p-1.5 rounded-lg hover:bg-white/5 transition text-gray-500 hover:text-white">
                    <RefreshCw className="w-4 h-4" />
                  </button>
                </div>

                {products.map((product, i) => (
                  <motion.div
                    key={product.id}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: i * 0.04 }}
                    layout
                    className="group flex gap-3 sm:gap-4 p-3 sm:p-4 bg-[#1A1A1A] rounded-xl border border-white/5 hover:border-white/10 transition-all duration-300"
                  >
                    {/* Vote Column */}
                    <div className="flex flex-row sm:flex-col items-center gap-0.5 sm:gap-1 w-auto sm:w-12 flex-shrink-0">
                      <button onClick={() => setVotes(v => ({...v, [product.id]: (v[product.id]||0) + 1}))}
                        className="p-1.5 rounded-lg hover:bg-white/5 transition group/btn">
                        <ArrowUp className={`w-4 h-4 ${(votes[product.id]||0) > 0 ? 'text-[#BFC3C7]' : 'text-gray-600'} group-hover/btn:text-[#BFC3C7] transition`} />
                      </button>
                      <span className={`text-xs font-bold font-mono min-w-[1.5rem] text-center ${(votes[product.id]||0) !== 0 ? 'text-white' : 'text-gray-500'}`}>
                        {Math.abs(votes[product.id] || 0)}
                      </span>
                      <button onClick={() => setVotes(v => ({...v, [product.id]: (v[product.id]||0) - 1}))}
                        className="p-1.5 rounded-lg hover:bg-white/5 transition group/btn">
                        <ArrowDown className={`w-4 h-4 ${(votes[product.id]||0) < 0 ? 'text-red-400' : 'text-gray-600'} group-hover/btn:text-red-400 transition`} />
                      </button>
                    </div>

                    {/* Content */}
                    <div className="flex-1 min-w-0">
                      {/* Product Image */}
                      <Link href={`/product/${product.id}`} className="block mb-3">
                        <div className="relative aspect-[16/9] sm:aspect-[16/7] bg-gradient-to-br from-gray-800 to-gray-900 rounded-xl overflow-hidden group/image">
                          {product.images?.[0] ? (
                            <img src={product.images[0]} alt={product.title} className="w-full h-full object-cover group-hover/image:scale-105 transition duration-500" />
                          ) : (
                            <div className="w-full h-full flex items-center justify-center">
                              <div className="text-center">
                                <ShoppingCart className="w-10 h-10 text-gray-700 mx-auto mb-2" />
                                <p className="text-xs text-gray-600">No image</p>
                              </div>
                            </div>
                          )}
                          {/* Overlay badges */}
                          <div className="absolute top-3 left-3 flex gap-2">
                            <span className={`px-2.5 py-1 rounded-md text-[10px] font-bold uppercase tracking-wider backdrop-blur-sm ${
                              product.condition === 'new' ? 'bg-green-500/20 text-green-300' :
                              product.condition === 'used' ? 'bg-yellow-500/20 text-yellow-300' :
                              'bg-blue-500/20 text-blue-300'
                            }`}>
                              {product.condition}
                            </span>
                            <span className="px-2.5 py-1 rounded-md text-[10px] font-bold bg-blue-500/20 text-blue-300 backdrop-blur-sm uppercase tracking-wider">
                              {product.category}
                            </span>
                          </div>
                          {/* Price overlay */}
                          <div className="absolute bottom-3 right-3">
                            <span className="text-xl sm:text-2xl font-bold font-display bg-black/60 backdrop-blur-sm px-3 py-1.5 rounded-lg text-white">
                              ${product.price.toLocaleString()}
                            </span>
                          </div>
                          {/* Quick actions */}
                          <div className="absolute top-3 right-3 flex gap-1.5 opacity-0 group-hover/image:opacity-100 transition">
                            <button onClick={(e) => { e.preventDefault(); setFavorites(prev => { const n = new Set(prev); n.has(product.id) ? n.delete(product.id) : n.add(product.id); return n }) }}
                              className="p-2 rounded-lg bg-black/60 backdrop-blur-sm hover:bg-black/80 transition">
                              <Heart className={`w-4 h-4 ${favorites.has(product.id) ? 'text-red-400 fill-red-400' : 'text-white'}`} />
                            </button>
                          </div>
                          {/* Views */}
                          <div className="absolute bottom-3 left-3 flex items-center gap-1 text-[10px] text-gray-400 bg-black/40 backdrop-blur-sm px-2 py-1 rounded-md">
                            <Eye className="w-3 h-3" /> {product.views || 0}
                          </div>
                        </div>
                      </Link>

                      {/* Post Meta */}
                      <div className="flex items-center gap-2 mb-2">
                        <div className="w-6 h-6 rounded-full bg-gradient-to-br from-gray-600 to-gray-700 flex items-center justify-center text-[9px] font-bold text-gray-300">
                          {product.seller_id?.[0]?.toUpperCase() || 'U'}
                        </div>
                        <span className="text-xs text-gray-500 font-medium">{product.seller_id?.slice(0, 8) || 'anonymous'}</span>
                        <span className="text-gray-600">·</span>
                        <span className="text-xs text-gray-500 flex items-center gap-1">
                          <Clock className="w-3 h-3" /> {timeAgo(product.created_at)}
                        </span>
                        {product.location && (
                          <>
                            <span className="text-gray-600">·</span>
                            <span className="text-xs text-gray-500 flex items-center gap-1">
                              <MapPin className="w-3 h-3" /> {product.location}
                            </span>
                          </>
                        )}
                      </div>

                      {/* Title */}
                      <Link href={`/product/${product.id}`}>
                        <h2 className="text-base sm:text-lg font-semibold mb-1 hover:text-[#BFC3C7] transition line-clamp-1">{product.title}</h2>
                      </Link>

                      {product.description && (
                        <p className="text-sm text-gray-500 line-clamp-2 mb-3">{product.description}</p>
                      )}

                      {/* Action Bar */}
                      <div className="flex items-center gap-2 mt-3 pt-3 border-t border-white/5">
                        <Link href={`/product/${product.id}`}
                          className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs text-gray-400 hover:text-white hover:bg-white/5 transition">
                          <MessageCircle className="w-3.5 h-3.5" />
                          <span>{Math.floor(Math.random() * 12)} comments</span>
                        </Link>
                        <button className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs text-gray-400 hover:text-white hover:bg-white/5 transition">
                          <Share2 className="w-3.5 h-3.5" />
                          <span>Share</span>
                        </button>
                        <div className="flex-1" />
                        <button className="flex items-center gap-1.5 px-4 py-1.5 rounded-lg text-xs font-semibold bg-white/10 hover:bg-white/20 text-white transition">
                          <MessageCircle className="w-3.5 h-3.5" />
                          <span>Chat with seller</span>
                        </button>
                      </div>
                    </div>
                  </motion.div>
                ))}
              </div>
            )}
          </div>

          {/* Sidebar - Desktop only */}
          <div className="hidden lg:block w-80 flex-shrink-0">
            <div className="sticky top-24 space-y-5">
              {/* Create Listing Card */}
              <div className="bg-gradient-to-br from-[#1A1A1A] to-black border border-white/10 rounded-xl p-5">
                <h3 className="font-semibold mb-1">Sell on XP</h3>
                <p className="text-xs text-gray-500 mb-4">List your gaming gear and reach thousands of buyers</p>
                <Link href="/seller" className="flex items-center justify-center gap-2 w-full py-3 bg-white text-black rounded-xl text-sm font-semibold hover:bg-[#BFC3C7] transition">
                  <Plus className="w-4 h-4" /> Create Listing
                </Link>
              </div>

              {/* Trending */}
              <div className="bg-[#1A1A1A] border border-white/10 rounded-xl p-5">
                <h3 className="font-semibold mb-3 flex items-center gap-2">
                  <Flame className="w-4 h-4 text-orange-400" /> Trending
                </h3>
                <div className="space-y-2">
                  {trending.map((p, i) => (
                    <Link key={p.id} href={`/product/${p.id}`}
                      className="flex items-center gap-3 p-2 rounded-lg hover:bg-white/5 transition group">
                      <span className="text-xs font-bold text-gray-600 w-5 text-right">#{i + 1}</span>
                      <div className="flex-1 min-w-0">
                        <p className="text-sm truncate group-hover:text-white transition">{p.title}</p>
                        <p className="text-[10px] text-gray-500">${p.price.toLocaleString()}</p>
                      </div>
                      <span className="text-[10px] text-gray-600">{p.category}</span>
                    </Link>
                  ))}
                </div>
              </div>

              {/* Categories */}
              <div className="bg-[#1A1A1A] border border-white/10 rounded-xl p-5">
                <h3 className="font-semibold mb-3 flex items-center gap-2">
                  <Tag className="w-4 h-4 text-[#BFC3C7]" /> Categories
                </h3>
                <div className="flex flex-wrap gap-1.5">
                  {categories.filter(c => c !== 'All').map((cat) => (
                    <button key={cat} onClick={() => setCategory(cat)}
                      className={`px-3 py-1.5 rounded-lg text-xs transition ${
                        category === cat ? 'bg-white text-black' : 'bg-white/5 text-gray-400 hover:bg-white/10 hover:text-white'
                      }`}>
                      {cat}
                    </button>
                  ))}
                </div>
              </div>

              {/* Stats */}
              <div className="bg-[#1A1A1A] border border-white/10 rounded-xl p-5">
                <div className="grid grid-cols-2 gap-4">
                  <div className="text-center">
                    <div className="text-lg font-bold font-display text-[#BFC3C7]">{products.length}</div>
                    <div className="text-[10px] text-gray-500">Listings</div>
                  </div>
                  <div className="text-center">
                    <div className="text-lg font-bold font-display text-[#BFC3C7]">{Math.floor(Math.random() * 50 + 10)}</div>
                    <div className="text-[10px] text-gray-500">Active Sellers</div>
                  </div>
                  <div className="text-center">
                    <div className="text-lg font-bold font-display text-[#BFC3C7]">$2.4K</div>
                    <div className="text-[10px] text-gray-500">Avg. Price</div>
                  </div>
                  <div className="text-center">
                    <div className="text-lg font-bold font-display text-[#BFC3C7]">98%</div>
                    <div className="text-[10px] text-gray-500">Satisfaction</div>
                  </div>
                </div>
              </div>

              {/* Recent Activity */}
              <div className="bg-[#1A1A1A] border border-white/10 rounded-xl p-5">
                <h3 className="font-semibold mb-3 flex items-center gap-2">
                  <TrendingUp className="w-4 h-4 text-green-400" /> Activity
                </h3>
                <div className="space-y-3">
                  <div className="flex items-center gap-2 text-xs text-gray-500">
                    <div className="w-1.5 h-1.5 rounded-full bg-green-400 flex-shrink-0" />
                    New listing: RTX 4090
                  </div>
                  <div className="flex items-center gap-2 text-xs text-gray-500">
                    <div className="w-1.5 h-1.5 rounded-full bg-blue-400 flex-shrink-0" />
                    Sale completed: i7-13700K
                  </div>
                  <div className="flex items-center gap-2 text-xs text-gray-500">
                    <div className="w-1.5 h-1.5 rounded-full bg-purple-400 flex-shrink-0" />
                    New seller joined
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
