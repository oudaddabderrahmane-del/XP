'use client'
import { useState, useEffect, useRef } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { fetchAPI } from '@/lib/api'
import { useStore } from '@/store/useStore'
import {
  MessageCircle, Hash, Plus, Settings, LogOut, Search, Send,
  ChevronDown, ChevronRight,
  Users, Phone, HelpCircle, Bell, Mic, Headphones,
} from 'lucide-react'

interface User { id: string; username: string; email: string; avatar?: string; bio?: string; xp: number; level: number; role: string; is_verified: boolean; location?: string }
interface Message { id: string; sender_id: string; receiver_id: string; content: string; is_read: boolean; created_at: string }
interface Community { id: string; name: string; description: string; icon: string; owner_id: string; member_count: number; is_private: boolean; created_at: string }

const SERVER_COLORS = ['#5865F2', '#57F287', '#FEE75C', '#EB459E', '#ED4245', '#FF73FA', '#00B0F4', '#95E5FF', '#BFC3C7', '#1ABC9C']

export default function ChatPage() {
  const { user, logout } = useStore()
  const [messages, setMessages] = useState<Message[]>([])
  const [users, setUsers] = useState<User[]>([])
  const [communities, setCommunities] = useState<Community[]>([])
  const [selectedServer, setSelectedServer] = useState<string>('dms')
  const [selectedDM, setSelectedDM] = useState<User | null>(null)
  const [searchQuery, setSearchQuery] = useState('')
  const [input, setInput] = useState('')
  const [ws, setWs] = useState<WebSocket | null>(null)
  const [showUserPopover, setShowUserPopover] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    fetchAPI('/api/users').then(d => setUsers(d.users || [])).catch(() => {})
    fetchAPI('/api/communities').then(d => setCommunities(d.communities || [])).catch(() => {})
    if (user) {
      fetchAPI('/api/messages').then(d => setMessages(d.messages || [])).catch(() => {})
      const socket = new WebSocket(`ws://127.0.0.1:8000/ws/${user.id}`)
      socket.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data)
          setMessages(prev => [...prev, {
            id: Date.now().toString(),
            sender_id: data.from,
            receiver_id: data.to || user.id,
            content: data.content,
            is_read: false,
            created_at: data.timestamp,
          }])
        } catch {}
      }
      setWs(socket)
      return () => socket.close()
    }
  }, [user])

  useEffect(() => { messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' }) }, [messages, selectedDM])

  function sendMessage() {
    if (!input.trim() || !selectedDM || !ws) return
    ws.send(JSON.stringify({ to: selectedDM.id, content: input, type: 'message' }))
    setMessages(prev => [...prev, {
      id: Date.now().toString(),
      sender_id: user?.id || '',
      receiver_id: selectedDM.id,
      content: input,
      is_read: false,
      created_at: new Date().toISOString(),
    }])
    setInput('')
  }

  const dmUsers = users.filter(u => u.id !== user?.id)
  const filteredDMUsers = dmUsers.filter(u =>
    u.username.toLowerCase().includes(searchQuery.toLowerCase())
  )

  const selectedMessages = messages.filter(m =>
    selectedDM && (
      (m.sender_id === user?.id && m.receiver_id === selectedDM.id) ||
      (m.receiver_id === user?.id && m.sender_id === selectedDM.id)
    )
  )

  function groupMessages(msgList: Message[]) {
    const groups: { sender: User | undefined; messages: Message[] }[] = []
    for (const m of msgList) {
      const last = groups[groups.length - 1]
      if (last && last.sender?.id === m.sender_id) {
        last.messages.push(m)
      } else {
        const sender = users.find(u => u.id === m.sender_id)
        groups.push({ sender, messages: [m] })
      }
    }
    return groups
  }

  const groupedMessages = groupMessages(selectedMessages)
  const serverList = [
    { id: 'dms', name: 'Direct Messages', icon: MessageCircle },
    ...communities.map((c, i) => ({ id: c.id, name: c.name, color: SERVER_COLORS[i % SERVER_COLORS.length] })),
  ]

  const lastMessageTime = (userId: string) => {
    const userMsgs = messages.filter(
      m => (m.sender_id === userId && m.receiver_id === user?.id) || (m.receiver_id === userId && m.sender_id === user?.id)
    )
    if (userMsgs.length === 0) return ''
    const last = userMsgs[userMsgs.length - 1]
    const d = new Date(last.created_at)
    const now = new Date()
    const diffMs = now.getTime() - d.getTime()
    const diffMin = Math.floor(diffMs / 60000)
    if (diffMin < 1) return 'now'
    if (diffMin < 60) return `${diffMin}m`
    const diffHr = Math.floor(diffMin / 60)
    if (diffHr < 24) return `${diffHr}h`
    return d.toLocaleDateString()
  }

  const formatTime = (iso: string) => {
    const d = new Date(iso)
    return d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  }

  return (
    <div className="h-[calc(100vh-4rem)] pt-16 flex">
      {/* Server Bar */}
      <div className="w-[68px] bg-black flex flex-col items-center py-3 space-y-2 border-r border-white/[0.06] flex-shrink-0">
        <button
          onClick={() => { setSelectedServer('dms'); setSelectedDM(null) }}
          className={`w-11 h-11 rounded-2xl flex items-center justify-center transition-all duration-200 group relative ${
            selectedServer === 'dms' ? 'bg-[#BFC3C7] rounded-xl' : 'bg-[#1A1A1A] hover:rounded-xl hover:bg-[#BFC3C7]'
          }`}
        >
          <MessageCircle className={`w-5 h-5 ${selectedServer === 'dms' ? 'text-black' : 'text-[#BFC3C7] group-hover:text-black'}`} />
          <span className="absolute left-full ml-3 px-2.5 py-1 bg-[#1A1A1A] text-white text-xs font-medium rounded-md whitespace-nowrap opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 shadow-xl z-50">Direct Messages</span>
          {selectedServer === 'dms' && <div className="absolute -left-3 w-[3px] h-[20px] bg-white rounded-r-full" />}
        </button>

        <div className="w-8 h-px bg-white/[0.08]" />

        <div className="flex-1 overflow-y-auto no-scrollbar space-y-2 px-1">
          <AnimatePresence>
            {communities.map((c, i) => (
              <motion.button
                key={c.id}
                initial={{ opacity: 0, scale: 0.8 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ delay: i * 0.03 }}
                onClick={() => setSelectedServer(c.id)}
                className={`w-11 h-11 rounded-2xl flex items-center justify-center transition-all duration-200 relative group font-display font-bold text-sm ${
                  selectedServer === c.id ? 'rounded-xl text-white' : 'text-white/70 hover:rounded-xl'
                }`}
                style={{ backgroundColor: selectedServer === c.id ? SERVER_COLORS[i % SERVER_COLORS.length] : '#1A1A1A' }}
              >
                {c.icon ? c.icon[0].toUpperCase() : c.name[0].toUpperCase()}
                <span className="absolute left-full ml-3 px-2.5 py-1 bg-[#1A1A1A] text-white text-xs font-medium rounded-md whitespace-nowrap opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 shadow-xl z-50">{c.name}</span>
                {selectedServer === c.id && <div className="absolute -left-3 w-[3px] h-[20px] bg-white rounded-r-full" />}
              </motion.button>
            ))}
          </AnimatePresence>
        </div>

        <button className="w-11 h-11 rounded-2xl bg-[#1A1A1A] hover:bg-green-500/20 hover:rounded-xl transition-all duration-200 flex items-center justify-center group relative border border-dashed border-white/[0.08]">
          <Plus className="w-5 h-5 text-green-500" />
          <span className="absolute left-full ml-3 px-2.5 py-1 bg-[#1A1A1A] text-white text-xs font-medium rounded-md whitespace-nowrap opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 shadow-xl z-50">Add Server</span>
        </button>
      </div>

      {/* Channel/DM Sidebar */}
      <div className="w-60 bg-[#1A1A1A] flex flex-col border-r border-white/[0.06] flex-shrink-0">
        {/* Server header */}
        <div className="h-12 flex items-center px-4 border-b border-white/[0.06] flex-shrink-0 group cursor-pointer">
          <div className="flex-1 font-semibold text-sm text-white/90 truncate">
            {selectedServer === 'dms' ? 'Direct Messages' : communities.find(c => c.id === selectedServer)?.name || 'Chat'}
          </div>
          <ChevronDown className="w-4 h-4 text-white/40 group-hover:text-white/70 transition" />
        </div>

        {selectedServer === 'dms' ? (
          <div className="flex-1 flex flex-col min-h-0">
            {/* Search */}
            <div className="px-3 pt-3 pb-2">
              <div className="relative">
                <Search className="absolute left-2.5 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-white/30" />
                <input
                  type="text" placeholder="Find or start a conversation"
                  value={searchQuery} onChange={e => setSearchQuery(e.target.value)}
                  className="w-full pl-8 pr-3 py-1.5 bg-black/40 border border-white/[0.06] rounded-md text-xs text-white/80 placeholder-white/30 focus:outline-none focus:border-white/20 transition"
                />
              </div>
            </div>

            {/* DM Users */}
            <div className="flex-1 overflow-y-auto px-2 pb-2 space-y-0.5">
              {filteredDMUsers.map(u => {
                const lastMsg = lastMessageTime(u.id)
                const isActive = selectedDM?.id === u.id
                return (
                  <button
                    key={u.id}
                    onClick={() => setSelectedDM(u)}
                    className={`w-full flex items-center space-x-2.5 px-2.5 py-2 rounded-md transition group ${
                      isActive ? 'bg-white/10' : 'hover:bg-white/[0.04]'
                    }`}
                  >
                    <div className="relative flex-shrink-0">
                      <div className="w-8 h-8 rounded-full bg-gradient-to-br from-[#BFC3C7] to-white/30 flex items-center justify-center text-xs font-bold text-black">
                        {u.username[0].toUpperCase()}
                      </div>
                      <div className="absolute -bottom-0.5 -right-0.5 w-3 h-3 bg-green-500 border-2 border-[#1A1A1A] rounded-full" />
                    </div>
                    <div className="flex-1 min-w-0 text-left">
                      <div className="flex items-center space-x-1.5">
                        <span className={`text-sm truncate ${isActive ? 'text-white' : 'text-white/70'}`}>{u.username}</span>
                      </div>
                      <p className="text-[10px] text-white/30 truncate">{u.bio || 'No bio'}</p>
                    </div>
                    {lastMsg && <span className="text-[10px] text-white/30 flex-shrink-0">{lastMsg}</span>}
                  </button>
                )
              })}
            </div>
          </div>
        ) : (
          <div className="flex-1 overflow-y-auto px-2 py-2 space-y-1">
            <div className="flex items-center justify-between px-2 py-1 text-[11px] font-semibold text-white/30 tracking-wider uppercase cursor-pointer hover:text-white/50">
              <span>Text Channels</span>
              <ChevronRight className="w-3 h-3" />
            </div>
            <button className="w-full flex items-center space-x-2 px-2.5 py-2 rounded-md bg-white/10 text-white/80 text-sm">
              <Hash className="w-4 h-4 text-white/40" />
              <span>general</span>
            </button>
            <button className="w-full flex items-center space-x-2 px-2.5 py-2 rounded-md hover:bg-white/[0.04] text-white/50 hover:text-white/70 text-sm transition">
              <Hash className="w-4 h-4" />
              <span>chat</span>
            </button>
            <button className="w-full flex items-center space-x-2 px-2.5 py-2 rounded-md hover:bg-white/[0.04] text-white/50 hover:text-white/70 text-sm transition">
              <Hash className="w-4 h-4" />
              <span>announcements</span>
            </button>
          </div>
        )}

        {/* User Panel */}
        <div className="h-14 bg-black/40 border-t border-white/[0.06] px-3 flex items-center flex-shrink-0 relative">
          <button
            onClick={() => setShowUserPopover(!showUserPopover)}
            className="flex items-center space-x-2.5 flex-1 min-w-0 group"
          >
            <div className="relative flex-shrink-0">
              <div className="w-8 h-8 rounded-full bg-gradient-to-br from-[#BFC3C7] to-white/30 flex items-center justify-center text-xs font-bold text-black">
                {user?.username?.[0]?.toUpperCase() || '?'}
              </div>
              <div className="absolute -bottom-0.5 -right-0.5 w-3 h-3 bg-green-500 border-2 border-black/40 rounded-full" />
            </div>
            <div className="flex-1 min-w-0 text-left">
              <p className="text-sm font-medium text-white/90 truncate">{user?.username || 'Guest'}</p>
              <p className="text-[10px] text-white/40 truncate">#{user?.id?.slice(0, 4) || '0000'}</p>
            </div>
            <div className="flex items-center space-x-1 opacity-0 group-hover:opacity-100 transition">
              <button className="p-1 rounded hover:bg-white/10 text-white/40 hover:text-white/70"><Mic className="w-3.5 h-3.5" /></button>
              <button className="p-1 rounded hover:bg-white/10 text-white/40 hover:text-white/70"><Headphones className="w-3.5 h-3.5" /></button>
              <button className="p-1 rounded hover:bg-white/10 text-white/40 hover:text-white/70"><Settings className="w-3.5 h-3.5" /></button>
            </div>
          </button>

          <AnimatePresence>
            {showUserPopover && (
              <motion.div
                initial={{ opacity: 0, y: -10, scale: 0.95 }}
                animate={{ opacity: 1, y: 0, scale: 1 }}
                exit={{ opacity: 0, y: -10, scale: 0.95 }}
                className="absolute bottom-full left-2 right-2 mb-1 bg-[#1A1A1A] border border-white/[0.08] rounded-lg shadow-2xl overflow-hidden z-50"
              >
                <div className="p-3">
                  <p className="text-sm font-semibold text-white/90">{user?.username}</p>
                  <p className="text-[11px] text-white/40">Level {user?.level} &middot; {user?.xp} XP</p>
                </div>
                <div className="border-t border-white/[0.06]">
                  <button onClick={() => { logout(); setShowUserPopover(false) }}
                    className="w-full flex items-center space-x-2 px-3 py-2.5 text-sm text-red-400 hover:bg-white/[0.04] transition">
                    <LogOut className="w-4 h-4" /><span>Log Out</span>
                  </button>
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      </div>

      {/* Chat Area */}
      <div className="flex-1 flex flex-col bg-[#111111] min-w-0">
        {selectedServer === 'dms' && selectedDM ? (
          <>
            {/* Chat Header */}
            <div className="h-12 flex items-center px-4 border-b border-white/[0.06] bg-[#111111] flex-shrink-0">
              <div className="flex items-center space-x-2.5">
                <div className="w-8 h-8 rounded-full bg-gradient-to-br from-[#BFC3C7] to-white/30 flex items-center justify-center text-xs font-bold text-black">
                  {selectedDM.username[0].toUpperCase()}
                </div>
                <div>
                  <div className="flex items-center space-x-1.5">
                    <span className="text-sm font-semibold text-white/90">{selectedDM.username}</span>
                    <div className="w-2 h-2 bg-green-500 rounded-full" />
                  </div>
                </div>
              </div>
              <div className="flex-1" />
              <div className="flex items-center space-x-1">
                <button className="p-2 rounded-md hover:bg-white/[0.06] text-white/30 hover:text-white/60 transition"><Phone className="w-4 h-4" /></button>
                <button className="p-2 rounded-md hover:bg-white/[0.06] text-white/30 hover:text-white/60 transition"><Search className="w-4 h-4" /></button>
                <button className="p-2 rounded-md hover:bg-white/[0.06] text-white/30 hover:text-white/60 transition"><HelpCircle className="w-4 h-4" /></button>
              </div>
            </div>

            {/* Messages */}
            <div className="flex-1 overflow-y-auto px-4 py-2">
              {groupedMessages.length === 0 ? (
                <div className="flex items-center justify-center h-full">
                  <div className="text-center max-w-sm">
                    <div className="w-16 h-16 rounded-full bg-white/[0.03] border border-white/[0.06] flex items-center justify-center mx-auto mb-4">
                      <MessageCircle className="w-7 h-7 text-white/20" />
                    </div>
                    <h3 className="text-lg font-semibold text-white/60 mb-1">{selectedDM.username}</h3>
                    <p className="text-sm text-white/30">This is the beginning of your direct message history with <strong className="text-white/50">{selectedDM.username}</strong>.</p>
                  </div>
                </div>
              ) : (
                <div className="space-y-0">
                  <AnimatePresence initial={false}>
                    {groupedMessages.map((group, gi) => (
                      <motion.div
                        key={group.messages[0].id}
                        initial={{ opacity: 0, y: 8 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: gi * 0.01 }}
                        className="flex space-x-3 px-4 py-0.5 hover:bg-white/[0.01] rounded group -mx-4"
                      >
                        <div className="w-10 h-10 rounded-full bg-gradient-to-br from-[#BFC3C7] to-white/30 flex items-center justify-center text-xs font-bold text-black flex-shrink-0 mt-0.5">
                          {group.sender?.username?.[0]?.toUpperCase() || '?'}
                        </div>
                        <div className="flex-1 min-w-0">
                          <div className="flex items-baseline space-x-2">
                            <span className="text-sm font-semibold text-white/90 hover:underline cursor-pointer">
                              {group.sender?.username || 'Unknown'}
                            </span>
                            <span className="text-[10px] text-white/30">{formatTime(group.messages[0].created_at)}</span>
                          </div>
                          <div className="space-y-0.5">
                            {group.messages.map(m => (
                              <p key={m.id} className="text-sm text-white/70 leading-relaxed">{m.content}</p>
                            ))}
                          </div>
                        </div>
                      </motion.div>
                    ))}
                  </AnimatePresence>
                  <div ref={messagesEndRef} />
                </div>
              )}
            </div>

            {/* Input */}
            <div className="px-4 pb-4 pt-2 bg-[#111111]">
              <div className="flex items-end space-x-2 bg-[#1A1A1A] border border-white/[0.06] rounded-lg px-3 py-2 focus-within:border-white/20 transition">
                <input
                  type="text" value={input} onChange={e => setInput(e.target.value)}
                  onKeyDown={e => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage() } }}
                  placeholder={`Message @${selectedDM.username}`}
                  className="flex-1 bg-transparent text-sm text-white/80 placeholder-white/30 focus:outline-none py-1"
                />
                <div className="flex items-center space-x-1">
                  <button className="p-1.5 rounded hover:bg-white/[0.06] text-white/30 hover:text-white/60 transition">
                    <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 9l5 5 5-5M12 4v10"/></svg>
                  </button>
                  <button onClick={sendMessage} disabled={!input.trim()}
                    className="p-1.5 rounded hover:bg-white/[0.06] text-white/30 hover:text-white/60 transition disabled:opacity-30">
                    <Send className="w-4 h-4" />
                  </button>
                </div>
              </div>
            </div>
          </>
        ) : selectedServer !== 'dms' ? (
          /* Community Chat Placeholder */
          <div className="flex flex-col h-full">
            <div className="h-12 flex items-center px-4 border-b border-white/[0.06] bg-[#111111] flex-shrink-0">
              <Hash className="w-5 h-5 text-white/40 mr-2" />
              <span className="text-sm font-semibold text-white/90">general</span>
              <div className="flex-1" />
              <div className="flex items-center space-x-1">
                <button className="p-2 rounded-md hover:bg-white/[0.06] text-white/30 hover:text-white/60 transition"><Bell className="w-4 h-4" /></button>
                <button className="p-2 rounded-md hover:bg-white/[0.06] text-white/30 hover:text-white/60 transition"><Users className="w-4 h-4" /></button>
                <button className="p-2 rounded-md hover:bg-white/[0.06] text-white/30 hover:text-white/60 transition"><Search className="w-4 h-4" /></button>
              </div>
            </div>
            <div className="flex-1 flex items-center justify-center">
              <div className="text-center max-w-md">
                <div className="w-20 h-20 rounded-full bg-white/[0.02] border border-white/[0.06] flex items-center justify-center mx-auto mb-5">
                  <Hash className="w-9 h-9 text-white/20" />
                </div>
                <h3 className="text-xl font-display font-bold text-white/50 mb-2">
                  #{'general'}
                </h3>
                <p className="text-sm text-white/30 leading-relaxed">
                  Welcome to the <strong className="text-white/50">{communities.find(c => c.id === selectedServer)?.name || 'Server'}</strong> community!<br />
                  This is the start of the <strong className="text-white/50">#general</strong> channel.
                </p>
              </div>
            </div>
            <div className="px-4 pb-4 pt-2 bg-[#111111]">
              <div className="flex items-center space-x-2 bg-[#1A1A1A] border border-white/[0.06] rounded-lg px-3 py-2.5 text-white/30 text-sm">
                <Hash className="w-4 h-4 flex-shrink-0" />
                <span>Channel chat coming soon...</span>
              </div>
            </div>
          </div>
        ) : (
          /* No DM Selected */
          <div className="flex-1 flex items-center justify-center">
            <div className="text-center">
              <div className="w-20 h-20 rounded-2xl bg-[#1A1A1A] border border-white/[0.06] flex items-center justify-center mx-auto mb-5">
                <MessageCircle className="w-9 h-9 text-white/20" />
              </div>
              <h3 className="text-xl font-display font-bold text-white/50 mb-2">Select a conversation</h3>
              <p className="text-sm text-white/30">Choose a user from the sidebar to start chatting</p>
            </div>
          </div>
        )}
      </div>

      {/* Member List (shown for community server) */}
      {selectedServer !== 'dms' && (
        <div className="w-56 bg-[#1A1A1A] border-l border-white/[0.06] hidden lg:flex flex-col flex-shrink-0">
          <div className="h-12 flex items-center px-4 border-b border-white/[0.06]">
            <span className="text-[11px] font-semibold text-white/30 tracking-wider uppercase">Members</span>
          </div>
          <div className="flex-1 overflow-y-auto px-2 py-2 space-y-1">
            {users.filter(u => u.id !== user?.id).slice(0, 10).map(u => (
              <button key={u.id} onClick={() => { setSelectedServer('dms'); setSelectedDM(u) }}
                className="w-full flex items-center space-x-2.5 px-2 py-1.5 rounded-md hover:bg-white/[0.04] transition group">
                <div className="relative flex-shrink-0">
                  <div className="w-7 h-7 rounded-full bg-gradient-to-br from-[#BFC3C7] to-white/30 flex items-center justify-center text-[10px] font-bold text-black">
                    {u.username[0].toUpperCase()}
                  </div>
                  <div className="absolute -bottom-0.5 -right-0.5 w-2.5 h-2.5 bg-green-500 border-2 border-[#1A1A1A] rounded-full" />
                </div>
                <span className="text-sm text-white/60 group-hover:text-white/80 truncate transition">{u.username}</span>
              </button>
            ))}
          </div>
        </div>
      )}

      <style jsx global>{`
        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
      `}</style>
    </div>
  )
}
