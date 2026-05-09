'use client'
import { useState } from 'react'
import { motion } from 'framer-motion'
import { Cpu, Heart, MessageCircle, Share2, TrendingUp, Filter, Monitor, Gamepad2, Lightbulb, Star } from 'lucide-react'
import Link from 'next/link'

const setups = [
  { id: 1, name: 'Cyberpunk RGB Dream', user: 'NeonGamer42', specs: 'RTX 4090 · i9-14900K · 64GB DDR5', likes: 342, comments: 28, rating: 4.9, image: null, category: 'gaming', color: 'from-cyan-500 to-blue-600' },
  { id: 2, name: 'Minimalist White Build', user: 'SilentTech', specs: 'RTX 4070 Ti · Ryzen 7 7800X3D · 32GB', likes: 256, comments: 19, rating: 4.8, image: null, category: 'gaming', color: 'from-gray-300 to-white' },
  { id: 3, name: 'Developer Dual Monitor', user: 'CodeMaster', specs: 'Mac Studio · LG 4K · Mechanical KB', likes: 189, comments: 15, rating: 4.7, image: null, category: 'workstation', color: 'from-green-500 to-teal-600' },
  { id: 4, name: 'Watercooled Beast', user: 'LiquidCool', specs: 'RTX 4090 · i9-13900K · Custom Loop', likes: 521, comments: 47, rating: 5.0, image: null, category: 'gaming', color: 'from-purple-500 to-pink-600' },
  { id: 5, name: 'Studio Production Rig', user: 'CreatorPro', specs: 'RTX 4080 · Ryzen 9 · 128GB RAM', likes: 167, comments: 12, rating: 4.6, image: null, category: 'workstation', color: 'from-amber-500 to-orange-600' },
  { id: 6, name: 'Retro Gaming Corner', user: 'PixelVault', specs: 'RTX 4060 · i5-14600K · Retro CRT', likes: 298, comments: 34, rating: 4.9, image: null, category: 'retro', color: 'from-red-500 to-rose-600' },
]

const categories = [
  { id: 'all', label: 'All Setups', icon: Monitor },
  { id: 'gaming', label: 'Gaming', icon: Gamepad2 },
  { id: 'workstation', label: 'Workstation', icon: Cpu },
  { id: 'retro', label: 'Retro', icon: Lightbulb },
  { id: 'trending', label: 'Trending', icon: TrendingUp },
]

export default function ShowcasePage() {
  const [activeCategory, setActiveCategory] = useState('all')
  const [sortBy, setSortBy] = useState('popular')

  const filtered = activeCategory === 'all' ? setups : setups.filter(s => s.category === activeCategory || activeCategory === 'trending')
  const sorted = [...filtered].sort((a, b) => sortBy === 'popular' ? b.likes - a.likes : b.rating - a.rating)

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="mb-8">
        <h1 className="text-3xl sm:text-4xl font-display font-bold mb-2">Setup Showcase</h1>
        <p className="text-gray-400">Discover amazing gaming rigs and workstations from the community</p>
      </motion.div>

      <div className="flex items-center justify-between mb-6">
        <div className="flex space-x-2 overflow-x-auto">
          {categories.map(cat => (
            <button key={cat.id} onClick={() => setActiveCategory(cat.id)}
              className={`flex items-center space-x-1.5 px-4 py-2.5 rounded-xl text-sm font-medium whitespace-nowrap transition ${activeCategory === cat.id ? 'bg-blue-600 text-white' : 'bg-white/5 hover:bg-white/10'}`}>
              <cat.icon className="w-4 h-4" /><span>{cat.label}</span>
            </button>
          ))}
        </div>
        <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}
          className="px-4 py-2.5 bg-white/5 border border-white/10 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
          <option value="popular">Most Popular</option>
          <option value="top">Top Rated</option>
        </select>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {sorted.map((setup, i) => (
          <motion.div key={setup.id} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.05 }}
            className="group bg-white/5 border border-white/10 rounded-xl overflow-hidden hover:border-blue-500/50 hover:shadow-lg hover:shadow-blue-500/10 transition-all duration-300">
            <div className={`h-48 bg-gradient-to-br ${setup.color} flex items-center justify-center relative`}>
              <Monitor className="w-20 h-20 opacity-30" />
              {setup.id === 4 && <Star className="absolute top-3 right-3 w-6 h-6 text-yellow-400 fill-yellow-400" />}
            </div>
            <div className="p-5">
              <div className="flex items-center justify-between mb-3">
                <h3 className="font-semibold group-hover:text-blue-400 transition">{setup.name}</h3>
                <div className="flex items-center space-x-1">
                  <Star className="w-4 h-4 text-yellow-400 fill-yellow-400" />
                  <span className="text-sm font-semibold">{setup.rating}</span>
                </div>
              </div>
              <p className="text-xs text-gray-400 mb-3">by <span className="text-blue-400">{setup.user}</span></p>
              <p className="text-sm text-gray-300 mb-4">{setup.specs}</p>
              <div className="flex items-center justify-between text-sm text-gray-400">
                <div className="flex items-center space-x-4">
                  <span className="flex items-center"><Heart className="w-4 h-4 mr-1" />{setup.likes}</span>
                  <span className="flex items-center"><MessageCircle className="w-4 h-4 mr-1" />{setup.comments}</span>
                </div>
                <button className="p-1.5 rounded-lg hover:bg-white/10"><Share2 className="w-4 h-4" /></button>
              </div>
            </div>
          </motion.div>
        ))}
      </div>

      <div className="text-center mt-12">
        <button className="px-8 py-3 bg-gradient-to-r from-blue-600 to-purple-600 rounded-xl font-semibold hover:shadow-lg hover:shadow-blue-500/30 transition">
          <Monitor className="w-5 h-5 inline mr-2" />Showcase Your Setup
        </button>
      </div>
    </div>
  )
}
