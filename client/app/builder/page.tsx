'use client'
import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { Cpu, CpuIcon, HardDrive, Zap, Monitor, Save, Share2, CheckCircle, AlertTriangle, Thermometer } from 'lucide-react'
import { fetchAPI } from '@/lib/api'

interface PCPart {
  id: string; name: string; category: string; manufacturer: string; price: number; power_consumption?: number; specs: any
}

interface BuildPart {
  part: PCPart
  slot: string
}

const slots = [
  { key: 'CPU', label: 'CPU', icon: Cpu, color: 'from-blue-500 to-cyan-500' },
  { key: 'GPU', label: 'GPU', icon: CpuIcon, color: 'from-green-500 to-emerald-500' },
  { key: 'RAM', label: 'RAM', icon: Monitor, color: 'from-purple-500 to-pink-500' },
  { key: 'Motherboard', label: 'Motherboard', icon: Monitor, color: 'from-orange-500 to-red-500' },
  { key: 'Storage', label: 'Storage', icon: HardDrive, color: 'from-indigo-500 to-violet-500' },
  { key: 'PSU', label: 'PSU', icon: Zap, color: 'from-yellow-500 to-amber-500' },
  { key: 'Case', label: 'Case', icon: Monitor, color: 'from-teal-500 to-cyan-500' },
]

export default function BuilderPage() {
  const [parts, setParts] = useState<Record<string, PCPart | null>>({})
  const [availableParts, setAvailableParts] = useState<PCPart[]>([])
  const [selectedSlot, setSelectedSlot] = useState<string>('CPU')
  const [buildName, setBuildName] = useState('')
  const [compatResult, setCompatResult] = useState<any>(null)
  const [buildEstimate, setBuildEstimate] = useState<any>(null)
  const [savedBuilds, setSavedBuilds] = useState<any[]>([])
  const [tab, setTab] = useState<'build' | 'saved'>('build')

  useEffect(() => {
    fetchAPI('/api/parts').then(d => setAvailableParts(d.parts || [])).catch(console.error)
    loadBuilds()
  }, [])

  async function loadBuilds() {
    try {
      const data = await fetchAPI('/api/builds?public=true')
      setSavedBuilds(data.builds || [])
    } catch (e) { console.error(e) }
  }

  function selectPart(part: PCPart) {
    setParts(prev => ({ ...prev, [part.category]: part }))
  }

  function removePart(slot: string) {
    setParts(prev => ({ ...prev, [slot]: null }))
  }

  const totalPrice = Object.values(parts).filter(Boolean).reduce((sum, p) => sum + (p?.price || 0), 0)

  async function checkCompatibility() {
    const partList = Object.values(parts).filter(Boolean).map(p => ({
      name: p!.name, category: p!.category, power_consumption: p!.power_consumption || 0, price: p!.price
    }))
    try {
      const [compatRes, estimateRes] = await Promise.all([
        fetchAPI('/api/ai/compatibility', {
          method: 'POST', headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ parts: partList }),
        }),
        fetchAPI('/api/ai/build-estimate', {
          method: 'POST', headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ parts: partList }),
        }),
      ])
      setCompatResult(compatRes)
      setBuildEstimate(estimateRes)
    } catch (e) { console.error(e) }
  }

  async function saveBuild() {
    if (!buildName.trim()) return
    const buildParts = Object.entries(parts).filter(([_, p]) => p).map(([slot, p]) => ({ slot, part_id: p!.id, name: p!.name, price: p!.price }))
    try {
      await fetchAPI('/api/builds', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: buildName, parts: buildParts, total_price: totalPrice, is_public: true }),
      })
      setBuildName('')
      loadBuilds()
    } catch (e) { console.error(e) }
  }

  const filteredParts = availableParts.filter(p => p.category === selectedSlot)

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="mb-8">
        <h1 className="text-3xl sm:text-4xl font-display font-bold mb-2">PC Builder</h1>
        <p className="text-gray-400">Select and configure your dream PC build</p>
      </motion.div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Parts Selection */}
        <div className="lg:col-span-2 space-y-6">
          {/* Slot Selector */}
          <div className="flex flex-wrap gap-2">
            {slots.map(slot => (
              <button
                key={slot.key}
                onClick={() => setSelectedSlot(slot.key)}
                className={`flex items-center space-x-2 px-4 py-3 rounded-xl text-sm font-medium transition ${
                  selectedSlot === slot.key
                    ? 'bg-gradient-to-r ' + slot.color + ' text-white'
                    : 'bg-white/5 text-gray-300 hover:bg-white/10'
                } ${parts[slot.key] ? 'ring-2 ring-blue-500' : ''}`}
              >
                <slot.icon className="w-4 h-4" />
                <span>{slot.label}</span>
                {parts[slot.key] && <CheckCircle className="w-3 h-3 ml-1 text-green-400" />}
              </button>
            ))}
          </div>

          {/* Available Parts */}
          <div className="bg-white/5 border border-white/10 rounded-xl p-4">
            <h3 className="font-semibold mb-4">{selectedSlot} Options</h3>
            <div className="space-y-2 max-h-64 overflow-y-auto">
              {filteredParts.map((part) => (
                <div
                  key={part.id}
                  onClick={() => selectPart(part)}
                  className={`flex items-center justify-between p-3 rounded-lg cursor-pointer transition ${
                    parts[selectedSlot]?.id === part.id
                      ? 'bg-blue-600/20 border border-blue-500'
                      : 'bg-white/5 hover:bg-white/10 border border-transparent'
                  }`}
                >
                  <div>
                    <div className="font-medium text-sm">{part.name}</div>
                    <div className="text-xs text-gray-400">{part.manufacturer} · {part.power_consumption ? `${part.power_consumption}W` : ''}</div>
                  </div>
                  <div className="text-right">
                    <div className="font-bold text-blue-400">${part.price}</div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Current Build Summary */}
          <div className="bg-white/5 border border-white/10 rounded-xl p-4">
            <h3 className="font-semibold mb-4">Your Build</h3>
            {slots.map(slot => (
              <div key={slot.key} className="flex items-center justify-between py-2 border-b border-white/5 last:border-0">
                <div className="flex items-center space-x-2">
                  <slot.icon className="w-4 h-4 text-gray-400" />
                  <span className="text-sm text-gray-300">{slot.label}</span>
                </div>
                {parts[slot.key] ? (
                  <div className="flex items-center space-x-2">
                    <span className="text-sm">{parts[slot.key]!.name}</span>
                    <span className="text-sm font-bold text-blue-400">${parts[slot.key]!.price}</span>
                    <button onClick={() => removePart(slot.key)} className="text-red-400 hover:text-red-300 text-xs">✕</button>
                  </div>
                ) : (
                  <span className="text-xs text-gray-500">Not selected</span>
                )}
              </div>
            ))}
            <div className="flex items-center justify-between pt-4 mt-2 border-t border-white/10">
              <span className="font-bold text-lg">Total</span>
              <span className="font-bold text-2xl text-blue-400">${totalPrice.toFixed(2)}</span>
            </div>
          </div>

          {/* Actions */}
          <div className="flex flex-wrap gap-4">
            <button onClick={checkCompatibility} className="flex items-center space-x-2 px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 rounded-xl font-semibold hover:shadow-lg hover:shadow-blue-500/30 transition">
              <Zap className="w-5 h-5" /><span>Check Compatibility</span>
            </button>
            <div className="flex-1" />
            <input
              type="text"
              placeholder="Build name..."
              value={buildName}
              onChange={(e) => setBuildName(e.target.value)}
              className="px-4 py-2 bg-white/5 border border-white/10 rounded-xl text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 w-48"
            />
            <button onClick={saveBuild} className="flex items-center space-x-2 px-6 py-3 bg-green-600 hover:bg-green-700 rounded-xl font-semibold transition" disabled={!buildName}>
              <Save className="w-5 h-5" /><span>Save Build</span>
            </button>
          </div>

          {/* Compatibility Results */}
          {compatResult && (
            <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className={`p-4 rounded-xl ${compatResult.compatible ? 'bg-green-600/20 border border-green-500' : 'bg-red-600/20 border border-red-500'}`}>
              <div className="flex items-center space-x-2 mb-2">
                {compatResult.compatible ? <CheckCircle className="w-5 h-5 text-green-400" /> : <AlertTriangle className="w-5 h-5 text-red-400" />}
                <span className="font-semibold">{compatResult.compatible ? 'All parts compatible!' : 'Compatibility issues found'}</span>
              </div>
              {compatResult.issues?.map((issue: string, i: number) => (
                <p key={i} className="text-sm text-red-300 ml-7">• {issue}</p>
              ))}
              {compatResult.warnings?.map((warn: string, i: number) => (
                <p key={i} className="text-sm text-yellow-300 ml-7">• {warn}</p>
              ))}
            </motion.div>
          )}

          {/* Build Estimates */}
          {buildEstimate && (
            <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="grid grid-cols-1 sm:grid-cols-3 gap-4">
              {/* FPS Estimate */}
              <div className="bg-white/5 border border-white/10 rounded-xl p-4">
                <h4 className="text-sm font-semibold text-gray-300 mb-3 flex items-center"><Monitor className="w-4 h-4 mr-2 text-blue-400" />FPS Estimate</h4>
                <div className="space-y-2 text-sm">
                  <div className="flex justify-between"><span>1080p</span><span className="font-bold text-green-400">{buildEstimate.fps?.["1080p"] || 'N/A'} FPS</span></div>
                  <div className="flex justify-between"><span>1440p</span><span className="font-bold text-blue-400">{buildEstimate.fps?.["1440p"] || 'N/A'} FPS</span></div>
                  <div className="flex justify-between"><span>4K</span><span className="font-bold text-purple-400">{buildEstimate.fps?.["4k"] || 'N/A'} FPS</span></div>
                </div>
              </div>

              {/* Bottleneck */}
              <div className="bg-white/5 border border-white/10 rounded-xl p-4">
                <h4 className="text-sm font-semibold text-gray-300 mb-3 flex items-center"><AlertTriangle className="w-4 h-4 mr-2 text-yellow-400" />Bottleneck</h4>
                <p className={`text-lg font-bold ${(buildEstimate.bottleneck?.percentage || 0) > 15 ? 'text-red-400' : 'text-green-400'}`}>
                  {buildEstimate.bottleneck?.percentage || 0}%
                </p>
                <p className="text-xs text-gray-400 mt-1">{buildEstimate.bottleneck?.note || 'N/A'}</p>
              </div>

              {/* Temperature + Power */}
              <div className="bg-white/5 border border-white/10 rounded-xl p-4">
                <h4 className="text-sm font-semibold text-gray-300 mb-3 flex items-center"><Zap className="w-4 h-4 mr-2 text-orange-400" />Power & Temp</h4>
                <p className="text-lg font-bold text-blue-400">{buildEstimate.total_power_draw || 'N/A'}W</p>
                <p className="text-xs text-gray-400 mt-1">{buildEstimate.temperature || 'N/A'}</p>
              </div>
            </motion.div>
          )}
        </div>

        {/* Sidebar - Saved Builds */}
        <div className="space-y-4">
          <div className="flex space-x-2 mb-4">
            <button onClick={() => setTab('build')} className={`px-4 py-2 rounded-lg text-sm font-medium transition ${tab === 'build' ? 'bg-blue-600' : 'bg-white/5'}`}>Builder</button>
            <button onClick={() => setTab('saved')} className={`px-4 py-2 rounded-lg text-sm font-medium transition ${tab === 'saved' ? 'bg-blue-600' : 'bg-white/5'}`}>Saved Builds</button>
          </div>

          {tab === 'saved' && (
            <div className="space-y-3">
              {savedBuilds.length === 0 ? (
                <p className="text-gray-400 text-sm">No saved builds yet.</p>
              ) : (
                savedBuilds.map((build) => (
                  <div key={build.id} className="bg-white/5 border border-white/10 rounded-xl p-4 hover:border-blue-500/50 transition">
                    <h4 className="font-semibold">{build.name}</h4>
                    <p className="text-xs text-gray-400 mt-1">{build.parts?.length || 0} parts</p>
                    <p className="text-lg font-bold text-blue-400 mt-2">${(build.total_price || 0).toFixed(2)}</p>
                  </div>
                ))
              )}
            </div>
          )}

          {/* AI Recommendations */}
          <div className="bg-white/5 border border-white/10 rounded-xl p-4">
            <h3 className="font-semibold mb-4">💡 AI Recommendations</h3>
            <p className="text-xs text-gray-400 mb-4">Get build suggestions based on your budget</p>
            <BuildRecommendations />
          </div>
        </div>
      </div>
    </div>
  )
}

function BuildRecommendations() {
  const [budget, setBudget] = useState(1000)
  const [useCase, setUseCase] = useState('gaming')
  const [result, setResult] = useState<any>(null)
  const [loading, setLoading] = useState(false)

  async function getRecommendations() {
    setLoading(true)
    try {
      const res = await fetchAPI('/api/ai/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ budget, use_case: useCase }),
      })
      setResult(res)
    } catch (e) { console.error(e) }
    setLoading(false)
  }

  return (
    <div>
      <input type="number" value={budget} onChange={(e) => setBudget(Number(e.target.value))}
        placeholder="Budget" className="w-full px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-sm mb-2" />
      <select value={useCase} onChange={(e) => setUseCase(e.target.value)}
        className="w-full px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-sm mb-3">
        <option value="gaming">Gaming</option>
        <option value="office">Office</option>
        <option value="streaming">Streaming</option>
      </select>
      <button onClick={getRecommendations} disabled={loading}
        className="w-full py-2 bg-blue-600 hover:bg-blue-700 rounded-lg text-sm font-semibold transition disabled:opacity-50">
        {loading ? 'Loading...' : 'Get Recommendations'}
      </button>
      {result && (
        <div className="mt-4 space-y-2">
          {result.parts?.map((part: any, i: number) => (
            <div key={i} className="flex justify-between items-center py-1.5 border-b border-white/5 text-sm">
              <span className="text-gray-300">{part.name}</span>
              <span className="font-semibold text-blue-400">${part.price}</span>
            </div>
          ))}
          <div className="flex justify-between pt-2 text-sm font-bold">
            <span>Total</span>
            <span className="text-blue-400">${result.total_price}</span>
          </div>
        </div>
      )}
    </div>
  )
}
