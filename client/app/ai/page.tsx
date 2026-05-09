'use client'
import { useState } from 'react'
import { motion } from 'framer-motion'
import { Brain, MessageSquare, Cpu, Search, Zap, TrendingUp, DollarSign, Shield } from 'lucide-react'
import { fetchAPI } from '@/lib/api'

export default function AIPage() {
  const [query, setQuery] = useState('')
  const [messages, setMessages] = useState<{role: string, content: string}[]>([
    { role: 'ai', content: 'Hello! I\'m your XP AI assistant. I can help you find parts, check compatibility, analyze prices, detect scams, and more. How can I help?' },
  ])
  const [loading, setLoading] = useState(false)
  const [budget, setBudget] = useState(1000)
  const [useCase, setUseCase] = useState('gaming')
  const [recommendations, setRecommendations] = useState<any>(null)
  const [priceUrl, setPriceUrl] = useState('')
  const [priceAnalysis, setPriceAnalysis] = useState<any>(null)

  async function handleQuery() {
    if (!query.trim()) return
    setMessages(prev => [...prev, { role: 'user', content: query }])
    setLoading(true)
    try {
      const res = await fetchAPI('/api/ai/smart-search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query }),
      })
      const resultText = res.results?.length > 0
        ? `Found ${res.count} results for "${query}". Top match: ${res.results[0].title} - $${res.results[0].price}`
        : `No products found for "${query}". Try different keywords.`
      setMessages(prev => [...prev, { role: 'ai', content: resultText }])
    } catch (e) {
      setMessages(prev => [...prev, { role: 'ai', content: 'Sorry, I encountered an error.' }])
    }
    setLoading(false)
    setQuery('')
  }

  async function getRecommendations() {
    try {
      const res = await fetchAPI('/api/ai/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ budget, use_case: useCase }),
      })
      setRecommendations(res)
    } catch (e) { console.error(e) }
  }

  async function analyzePrice() {
    if (!priceUrl.trim()) return
    try {
      const res = await fetchAPI(`/api/ai/price-analysis/${priceUrl}`)
      setPriceAnalysis(res)
    } catch (e) {
      setPriceAnalysis({ status: 'error', analysis: 'Could not analyze. Check the product ID.' })
    }
  }

  const features = [
    { icon: Search, title: 'Smart Search', desc: 'AI-powered product search across the marketplace', color: 'from-blue-500 to-cyan-500' },
    { icon: Cpu, title: 'Build Optimizer', desc: 'Get optimal PC build recommendations for your budget', color: 'from-green-500 to-emerald-500' },
    { icon: TrendingUp, title: 'Price Analysis', desc: 'AI analyzes if a product is fairly priced', color: 'from-purple-500 to-pink-500' },
    { icon: Zap, title: 'Compatibility Check', desc: 'Check if your PC parts work together', color: 'from-yellow-500 to-amber-500' },
    { icon: DollarSign, title: 'Market Trends', desc: 'Track hardware pricing trends over time', color: 'from-orange-500 to-red-500' },
    { icon: Shield, title: 'Scam Detection', desc: 'AI-powered fraud detection for listings', color: 'from-indigo-500 to-violet-500' },
  ]

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="mb-8">
        <h1 className="text-3xl sm:text-4xl font-display font-bold mb-2">AI Assistant</h1>
        <p className="text-gray-400">Smart tools to help you build, buy, and sell smarter</p>
      </motion.div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Chat / Main */}
        <div className="lg:col-span-2 space-y-6">
          {/* Chat Messages */}
          <div className="bg-white/5 border border-white/10 rounded-2xl p-6 h-80 overflow-y-auto space-y-4">
            {messages.map((m, i) => (
              <div key={i} className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                <div className={`max-w-[80%] p-4 rounded-2xl ${m.role === 'user' ? 'bg-blue-600' : 'bg-white/10'}`}>
                  <p className="text-sm">{m.content}</p>
                </div>
              </div>
            ))}
            {loading && <div className="flex items-center space-x-2 text-gray-400"><Brain className="w-4 h-4 animate-pulse" /><span className="text-sm">Thinking...</span></div>}
          </div>

          {/* Chat Input */}
          <div className="flex space-x-3">
            <input type="text" value={query} onChange={(e) => setQuery(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleQuery()}
              placeholder="Search products or ask AI..." className="flex-1 px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500" />
            <button onClick={handleQuery} disabled={loading} className="px-6 py-3 bg-blue-600 hover:bg-blue-700 rounded-xl font-semibold disabled:opacity-50"><MessageSquare className="w-5 h-5" /></button>
          </div>

          {/* Features Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {features.map((feat, i) => (
              <motion.div key={i} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.05 }}
                className={`bg-gradient-to-br ${feat.color} p-[1px] rounded-xl group`}>
                <div className="bg-black rounded-xl p-4 h-full group-hover:bg-gray-900 transition">
                  <feat.icon className="w-6 h-6 mb-2" />
                  <h3 className="font-semibold text-sm">{feat.title}</h3>
                  <p className="text-xs text-gray-400 mt-1">{feat.desc}</p>
                </div>
              </motion.div>
            ))}
          </div>
        </div>

        {/* Sidebar Tools */}
        <div className="space-y-6">
          {/* Build Recommendations */}
          <div className="bg-white/5 border border-white/10 rounded-xl p-4">
            <h3 className="font-semibold mb-4 flex items-center"><Cpu className="w-5 h-5 mr-2 text-blue-400" />Build Recommendations</h3>
            <input type="number" value={budget} onChange={(e) => setBudget(Number(e.target.value))}
              className="w-full px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-sm mb-2" placeholder="Budget" />
            <select value={useCase} onChange={(e) => setUseCase(e.target.value)}
              className="w-full px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-sm mb-3">
              <option value="gaming">Gaming</option><option value="office">Office</option><option value="streaming">Streaming</option>
            </select>
            <button onClick={getRecommendations} className="w-full py-2 bg-blue-600 hover:bg-blue-700 rounded-lg text-sm font-semibold">Get Recommendations</button>
            {recommendations && (
              <div className="mt-4 space-y-2">
                {recommendations.parts?.map((part: any, i: number) => (
                  <div key={i} className="flex justify-between text-sm py-1 border-b border-white/5">
                    <span className="text-gray-300">{part.name}</span><span className="font-bold text-blue-400">${part.price}</span>
                  </div>
                ))}
                <div className="flex justify-between pt-2 font-bold"><span>Total</span><span className="text-blue-400">${recommendations.total_price}</span></div>
              </div>
            )}
          </div>

          {/* Price Analysis */}
          <div className="bg-white/5 border border-white/10 rounded-xl p-4">
            <h3 className="font-semibold mb-4 flex items-center"><DollarSign className="w-5 h-5 mr-2 text-green-400" />Price Analysis</h3>
            <input type="text" value={priceUrl} onChange={(e) => setPriceUrl(e.target.value)}
              placeholder="Product ID" className="w-full px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-sm mb-3" />
            <button onClick={analyzePrice} className="w-full py-2 bg-green-600 hover:bg-green-700 rounded-lg text-sm font-semibold">Analyze</button>
            {priceAnalysis && (
              <div className="mt-4 p-3 bg-white/5 rounded-lg">
                <div className="flex items-center space-x-2 mb-2">
                  <Shield className={`w-4 h-4 ${priceAnalysis.status === 'great_deal' ? 'text-green-400' : priceAnalysis.status === 'overpriced' ? 'text-red-400' : 'text-yellow-400'}`} />
                  <span className="text-sm font-semibold capitalize">{priceAnalysis.status?.replace('_', ' ')}</span>
                </div>
                <p className="text-xs text-gray-400">{priceAnalysis.analysis}</p>
              </div>
            )}
          </div>

          {/* Quick Stats */}
          <div className="bg-white/5 border border-white/10 rounded-xl p-4">
            <h3 className="font-semibold mb-4 flex items-center"><TrendingUp className="w-5 h-5 mr-2 text-purple-400" />Market Stats</h3>
            <div className="space-y-3 text-sm">
              <div className="flex justify-between"><span className="text-gray-400">Avg. GPU Price</span><span className="font-semibold">$549</span></div>
              <div className="flex justify-between"><span className="text-gray-400">Avg. CPU Price</span><span className="font-semibold">$299</span></div>
              <div className="flex justify-between"><span className="text-gray-400">Hot Category</span><span className="font-semibold text-blue-400">GPU</span></div>
              <div className="flex justify-between"><span className="text-gray-400">Listings Today</span><span className="font-semibold">247</span></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
