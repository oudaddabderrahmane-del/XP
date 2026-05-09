'use client'
import { useState } from 'react'
import { motion } from 'framer-motion'
import { Code2, Key, BookOpen, Terminal, Globe, Shield, Cpu, Database, Cloud, GitBranch, ChevronRight, Copy, Check } from 'lucide-react'

export default function DeveloperHubPage() {
  const [apiKey, setApiKey] = useState('xp_api_live_sk_8x$mK#2pL9qR...')
  const [copied, setCopied] = useState(false)
  const tab = 'overview'

  const features = [
    { icon: Key, title: 'API Keys', desc: 'Manage your API access keys', color: 'from-blue-500 to-cyan-500' },
    { icon: BookOpen, title: 'Documentation', desc: 'Complete API reference and guides', color: 'from-green-500 to-emerald-500' },
    { icon: Terminal, title: 'CLI Tools', desc: 'Command-line tools for automation', color: 'from-purple-500 to-pink-500' },
    { icon: Globe, title: 'Webhooks', desc: 'Real-time event notifications', color: 'from-yellow-500 to-amber-500' },
    { icon: Shield, title: 'Auth', desc: 'OAuth 2.0 & JWT authentication', color: 'from-orange-500 to-red-500' },
    { icon: Code2, title: 'SDKs', desc: 'Client libraries for Python, JS, Go', color: 'from-indigo-500 to-violet-500' },
  ]

  const endpoints = [
    { method: 'GET', path: '/api/products', desc: 'List all products' },
    { method: 'POST', path: '/api/products', desc: 'Create a product listing' },
    { method: 'GET', path: '/api/parts', desc: 'List PC parts' },
    { method: 'POST', path: '/api/ai/recommend', desc: 'Get build recommendations' },
    { method: 'GET', path: '/api/communities', desc: 'List communities' },
    { method: 'POST', path: '/api/auth/login', desc: 'Authenticate user' },
  ]

  function copyKey() {
    navigator.clipboard.writeText(apiKey)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="mb-8">
        <div className="flex items-center space-x-3">
          <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-green-500 to-teal-600 flex items-center justify-center"><Code2 className="w-6 h-6" /></div>
          <div><h1 className="text-3xl sm:text-4xl font-display font-bold">Developer Hub</h1><p className="text-gray-400">Build on top of XP with our APIs and tools</p></div>
        </div>
      </motion.div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 space-y-8">
          {/* API Key Section */}
          <div className="bg-white/5 border border-white/10 rounded-xl p-6">
            <h2 className="text-xl font-display font-bold mb-4 flex items-center"><Key className="w-5 h-5 mr-2 text-blue-400" />Your API Key</h2>
            <div className="flex items-center space-x-3">
              <code className="flex-1 px-4 py-3 bg-black/50 border border-white/10 rounded-lg text-sm font-mono text-green-400 truncate">{apiKey}</code>
              <button onClick={copyKey} className="p-3 bg-blue-600 hover:bg-blue-700 rounded-lg transition">
                {copied ? <Check className="w-4 h-4 text-green-400" /> : <Copy className="w-4 h-4" />}
              </button>
              <button className="px-4 py-3 bg-white/10 hover:bg-white/20 rounded-lg text-sm font-semibold transition">Rotate</button>
            </div>
            <p className="text-xs text-gray-400 mt-3">Last used: 2 minutes ago · Created: Jan 15, 2026</p>
          </div>

          {/* Quick Start */}
          <div className="bg-white/5 border border-white/10 rounded-xl p-6">
            <h2 className="text-xl font-display font-bold mb-4 flex items-center"><Terminal className="w-5 h-5 mr-2 text-purple-400" />Quick Start</h2>
            <div className="space-y-4">
              <div>
                <p className="text-sm text-gray-300 mb-2">Install the XP SDK:</p>
                <div className="bg-black/50 border border-white/10 rounded-lg p-4 font-mono text-sm">
                  <p className="text-green-400">pip install xp-sdk</p>
                  <p className="text-gray-400 mt-1"># or</p>
                  <p className="text-blue-400">npm install @xp/sdk</p>
                </div>
              </div>
              <div>
                <p className="text-sm text-gray-300 mb-2">Authenticate and fetch products:</p>
                <div className="bg-black/50 border border-white/10 rounded-lg p-4 font-mono text-sm">
                  <p className="text-purple-400">from xp import XP</p>
                  <p className="text-gray-400">client = XP(api_key="your_key")</p>
                  <p className="text-blue-400">products = client.products.list()</p>
                  <p className="text-green-400">print(products)</p>
                </div>
              </div>
            </div>
          </div>

          {/* API Endpoints Reference */}
          <div className="bg-white/5 border border-white/10 rounded-xl p-6">
            <h2 className="text-xl font-display font-bold mb-4 flex items-center"><BookOpen className="w-5 h-5 mr-2 text-green-400" />API Endpoints</h2>
            <div className="space-y-2">
              {endpoints.map((ep, i) => (
                <div key={i} className="flex items-center justify-between py-3 px-4 rounded-lg hover:bg-white/5 transition">
                  <div className="flex items-center space-x-4">
                    <span className={`px-2.5 py-1 rounded text-xs font-bold font-mono ${
                      ep.method === 'GET' ? 'bg-green-500/20 text-green-300' :
                      ep.method === 'POST' ? 'bg-blue-500/20 text-blue-300' :
                      'bg-yellow-500/20 text-yellow-300'
                    }`}>{ep.method}</span>
                    <code className="text-sm font-mono text-gray-300">{ep.path}</code>
                  </div>
                  <span className="text-sm text-gray-400">{ep.desc}</span>
                </div>
              ))}
            </div>
            <button className="mt-4 text-sm text-blue-400 hover:text-blue-300 transition flex items-center">
              View full docs <ChevronRight className="w-4 h-4 ml-1" />
            </button>
          </div>
        </div>

        {/* Sidebar */}
        <div className="space-y-6">
          <div className="grid grid-cols-1 gap-4">
            {features.map((feat, i) => (
              <motion.div key={i} initial={{ opacity: 0, x: 20 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: i * 0.05 }}
                className={`bg-gradient-to-br ${feat.color} p-[1px] rounded-xl group`}>
                <div className="bg-black rounded-xl p-4 h-full group-hover:bg-gray-900 transition">
                  <feat.icon className="w-5 h-5 mb-2" />
                  <h3 className="font-semibold text-sm">{feat.title}</h3>
                  <p className="text-xs text-gray-400 mt-0.5">{feat.desc}</p>
                </div>
              </motion.div>
            ))}
          </div>

          <div className="bg-white/5 border border-white/10 rounded-xl p-4">
            <h3 className="font-semibold mb-3 flex items-center"><Shield className="w-4 h-4 mr-2 text-blue-400" />Rate Limits</h3>
            <div className="space-y-2 text-sm">
              <div className="flex justify-between"><span className="text-gray-400">RPM</span><span className="font-mono">60</span></div>
              <div className="flex justify-between"><span className="text-gray-400">RPH</span><span className="font-mono">3,000</span></div>
              <div className="flex justify-between"><span className="text-gray-400">Auth</span><span className="font-mono">JWT / OAuth</span></div>
              <div className="flex justify-between"><span className="text-gray-400">Format</span><span className="font-mono">JSON</span></div>
            </div>
          </div>

          <div className="bg-gradient-to-br from-blue-600/20 to-purple-600/20 border border-white/10 rounded-xl p-4">
            <h3 className="font-semibold mb-2">Join the Developer Program</h3>
            <p className="text-xs text-gray-400 mb-3">Get early access to new features, SDKs, and support.</p>
            <button className="w-full py-2 bg-blue-600 hover:bg-blue-700 rounded-lg text-sm font-semibold transition">Apply Now</button>
          </div>
        </div>
      </div>
    </div>
  )
}
