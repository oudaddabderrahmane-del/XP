'use client'
import { useState } from 'react'
import { motion } from 'framer-motion'
import { Calendar, MapPin, Users, Trophy, Gamepad2, Clock, ArrowRight, Sparkles, Timer } from 'lucide-react'
import Link from 'next/link'

const events = [
  {
    id: 1, title: 'XP Build-Off Championship', type: 'tournament', status: 'live',
    date: 'May 15-20, 2026', time: '3:00 PM EST', location: 'Online',
    prize: '$10,000', participants: 1247, spots: 2000,
    desc: 'Build the ultimate gaming PC under a budget. Best build wins!',
    color: 'from-blue-500 to-cyan-500',
  },
  {
    id: 2, title: 'Speed Build Challenge', type: 'competition', status: 'upcoming',
    date: 'June 1, 2026', time: '2:00 PM EST', location: 'Online',
    prize: '$5,000', participants: 843, spots: 1500,
    desc: 'Race against time to assemble a PC. Fastest builder wins!',
    color: 'from-purple-500 to-pink-500',
  },
  {
    id: 3, title: 'AI Coding Hackathon', type: 'hackathon', status: 'upcoming',
    date: 'June 10-12, 2026', time: '9:00 AM EST', location: 'Virtual',
    prize: '$7,500', participants: 512, spots: 1000,
    desc: 'Build AI-powered tools for the gaming community.',
    color: 'from-green-500 to-emerald-500',
  },
  {
    id: 4, title: 'Community Game Night', type: 'social', status: 'live',
    date: 'Every Friday', time: '8:00 PM EST', location: 'XP Discord',
    prize: '$500 in prizes', participants: 3200, spots: 5000,
    desc: 'Weekly gaming session with the XP community.',
    color: 'from-orange-500 to-red-500',
  },
  {
    id: 5, title: 'PC Photography Contest', type: 'contest', status: 'completed',
    date: 'April 20, 2026', time: 'All day', location: 'Online',
    prize: '$1,000', participants: 891, spots: null,
    desc: 'Show off your beautiful PC builds and setups.',
    color: 'from-indigo-500 to-violet-500',
  },
  {
    id: 6, title: 'Developer Summit 2026', type: 'conference', status: 'upcoming',
    date: 'July 5-6, 2026', time: '10:00 AM EST', location: 'San Francisco, CA',
    prize: 'Networking + Swag', participants: 234, spots: 500,
    desc: 'Annual developer conference for the XP platform.',
    color: 'from-yellow-500 to-amber-500',
  },
]

const statusColors: Record<string, string> = {
  live: 'bg-green-500/20 text-green-400',
  upcoming: 'bg-blue-500/20 text-blue-400',
  completed: 'bg-gray-500/20 text-gray-400',
}

const typeIcons: Record<string, any> = {
  tournament: Trophy,
  competition: Gamepad2,
  hackathon: Terminal,
  social: Users,
  contest: Sparkles,
  conference: Calendar,
}

function Terminal() { return <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg> }

export default function EventsPage() {
  const [filter, setFilter] = useState('all')

  const filtered = filter === 'all' ? events : events.filter(e => e.status === filter)

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="mb-8">
        <h1 className="text-3xl sm:text-4xl font-display font-bold mb-2">Events & Tournaments</h1>
        <p className="text-gray-400">Compete, learn, and connect with the community</p>
      </motion.div>

      {/* Filters */}
      <div className="flex space-x-2 mb-8 overflow-x-auto">
        {['all', 'live', 'upcoming', 'completed'].map(f => (
          <button key={f} onClick={() => setFilter(f)}
            className={`px-5 py-2.5 rounded-xl text-sm font-medium capitalize whitespace-nowrap transition ${filter === f ? 'bg-blue-600 text-white' : 'bg-white/5 hover:bg-white/10'}`}
          >{f} {f === 'live' && <span className="w-2 h-2 bg-green-400 rounded-full inline-block ml-1 animate-pulse" />}</button>
        ))}
      </div>

      {/* Featured Live Event */}
      {filtered.some(e => e.status === 'live') && (
        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}
          className="bg-gradient-to-r from-green-600/20 via-blue-600/20 to-purple-600/20 border border-green-500/30 rounded-2xl p-6 mb-8">
          <div className="flex items-center space-x-3 mb-4">
            <span className="flex items-center space-x-2 px-3 py-1.5 bg-red-500/20 text-red-400 rounded-full text-xs font-semibold">
              <span className="w-2 h-2 bg-red-500 rounded-full animate-pulse" /><span>LIVE NOW</span>
            </span>
            <span className="text-sm text-gray-400 flex items-center"><Users className="w-4 h-4 mr-1" />1,247 participating</span>
          </div>
          <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between">
            <div>
              <h2 className="text-2xl font-display font-bold">XP Build-Off Championship</h2>
              <p className="text-gray-300 mt-1">Build the ultimate gaming PC under a budget. Best build wins!</p>
              <div className="flex flex-wrap items-center gap-4 mt-3 text-sm text-gray-400">
                <span className="flex items-center"><Trophy className="w-4 h-4 mr-1 text-yellow-400" />$10,000 Prize Pool</span>
                <span className="flex items-center"><Clock className="w-4 h-4 mr-1" />Ends in 5 days</span>
                <span className="flex items-center"><Users className="w-4 h-4 mr-1" />1,247 / 2,000 spots</span>
              </div>
            </div>
            <button className="mt-4 lg:mt-0 px-6 py-3 bg-green-600 hover:bg-green-700 rounded-xl font-semibold transition flex items-center space-x-2">
              <span>Join Now</span><ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </motion.div>
      )}

      {/* Events Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filtered.map((event, i) => {
          const Icon = typeIcons[event.type] || Calendar
          return (
            <motion.div key={event.id} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.05 }}
              className={`bg-gradient-to-br ${event.color} p-[1px] rounded-xl group`}>
              <div className="bg-black rounded-xl p-6 h-full group-hover:bg-gray-900 transition">
                <div className="flex items-center justify-between mb-4">
                  <div className="p-2.5 bg-white/5 rounded-lg"><Icon className="w-5 h-5" /></div>
                  <span className={`px-2.5 py-1 rounded-full text-xs font-semibold ${statusColors[event.status]}`}>{event.status}</span>
                </div>
                <h3 className="font-semibold text-lg mb-2 group-hover:text-blue-400 transition">{event.title}</h3>
                <p className="text-sm text-gray-400 mb-4 line-clamp-2">{event.desc}</p>
                <div className="space-y-2 text-sm text-gray-400">
                  <div className="flex items-center"><Calendar className="w-4 h-4 mr-2" />{event.date}</div>
                  {event.location && <div className="flex items-center"><MapPin className="w-4 h-4 mr-2" />{event.location}</div>}
                  <div className="flex items-center"><Trophy className="w-4 h-4 mr-2 text-yellow-400" />{event.prize}</div>
                  <div className="flex items-center"><Users className="w-4 h-4 mr-2" />{event.participants.toLocaleString()}{event.spots ? ` / ${event.spots.toLocaleString()}` : ''}</div>
                </div>
                <button className={`mt-4 w-full py-2.5 rounded-lg text-sm font-semibold transition ${
                  event.status === 'completed' ? 'bg-gray-500/20 text-gray-400 cursor-not-allowed' :
                  event.status === 'live' ? 'bg-green-600 hover:bg-green-700' : 'bg-blue-600 hover:bg-blue-700'
                }`}>{event.status === 'completed' ? 'Ended' : event.status === 'live' ? 'Join Now' : 'Register'}</button>
              </div>
            </motion.div>
          )
        })}
      </div>
    </div>
  )
}
