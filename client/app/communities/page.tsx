'use client'
import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { Users, MessageSquare, Plus, Search, ArrowUp, ArrowDown } from 'lucide-react'
import { fetchAPI } from '@/lib/api'

export default function CommunitiesPage() {
  const [tab, setTab] = useState<'communities' | 'posts'>('posts')
  const [communities, setCommunities] = useState<any[]>([])
  const [posts, setPosts] = useState<any[]>([])
  const [showNewPost, setShowNewPost] = useState(false)
  const [postTitle, setPostTitle] = useState('')
  const [postContent, setPostContent] = useState('')
  const [selectedCommunity, setSelectedCommunity] = useState('')
  const [search, setSearch] = useState('')
  const [newCommunityName, setNewCommunityName] = useState('')
  const [newCommunityDesc, setNewCommunityDesc] = useState('')

  useEffect(() => {
    fetchAPI('/api/communities').then(d => setCommunities(d.communities || [])).catch(console.error)
    fetchAPI('/api/posts').then(d => setPosts(d.posts || [])).catch(console.error)
  }, [])

  async function createPost() {
    if (!postTitle.trim()) return
    try {
      await fetchAPI('/api/posts', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: postTitle, content: postContent, community_id: selectedCommunity }),
      })
      setPostTitle(''); setPostContent(''); setShowNewPost(false)
      const data = await fetchAPI('/api/posts')
      setPosts(data.posts || [])
    } catch (e) { console.error(e) }
  }

  async function vote(postId: string, type: string) {
    try {
      await fetchAPI(`/api/posts/${postId}/vote?vote_type=${type}`, { method: 'POST' })
      setPosts(prev => prev.map(p => p.id === postId ? { ...p, upvotes: p.upvotes + (type === 'up' ? 1 : 0), downvotes: p.downvotes + (type === 'down' ? 1 : 0) } : p))
    } catch (e) { console.error(e) }
  }

  async function createCommunity() {
    if (!newCommunityName.trim()) return
    try {
      await fetchAPI('/api/communities', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: newCommunityName, description: newCommunityDesc }),
      })
      setNewCommunityName(''); setNewCommunityDesc('')
      const data = await fetchAPI('/api/communities')
      setCommunities(data.communities || [])
    } catch (e) { console.error(e) }
  }

  const filteredPosts = posts.filter(p =>
    !search || p.title?.toLowerCase().includes(search.toLowerCase()) || p.content?.toLowerCase().includes(search.toLowerCase())
  )

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="mb-8">
        <h1 className="text-3xl sm:text-4xl font-display font-bold mb-2">Communities</h1>
        <p className="text-gray-400">Connect with gamers, builders, and developers</p>
      </motion.div>

      {/* Tabs */}
      <div className="flex space-x-2 mb-8">
        <button onClick={() => setTab('posts')} className={`px-6 py-3 rounded-xl font-semibold transition ${tab === 'posts' ? 'bg-blue-600' : 'bg-white/5 hover:bg-white/10'}`}>
          <MessageSquare className="w-4 h-4 inline mr-2" />Posts
        </button>
        <button onClick={() => setTab('communities')} className={`px-6 py-3 rounded-xl font-semibold transition ${tab === 'communities' ? 'bg-blue-600' : 'bg-white/5 hover:bg-white/10'}`}>
          <Users className="w-4 h-4 inline mr-2" />Communities
        </button>
      </div>

      {/* Search */}
      <div className="relative mb-6">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
        <input type="text" placeholder="Search posts..." value={search} onChange={(e) => setSearch(e.target.value)}
          className="w-full pl-10 pr-4 py-3 bg-white/5 border border-white/10 rounded-xl text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500" />
      </div>

      {tab === 'posts' ? (
        <>
          <button onClick={() => setShowNewPost(!showNewPost)}
            className="mb-6 flex items-center space-x-2 px-6 py-3 bg-blue-600 hover:bg-blue-700 rounded-xl font-semibold transition">
            <Plus className="w-5 h-5" /><span>New Post</span>
          </button>

          {showNewPost && (
            <motion.div initial={{ opacity: 0, y: -10 }} animate={{ opacity: 1, y: 0 }} className="bg-white/5 border border-white/10 rounded-xl p-6 mb-6">
              <h3 className="font-semibold mb-4">Create Post</h3>
              <input type="text" placeholder="Title" value={postTitle} onChange={(e) => setPostTitle(e.target.value)}
                className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl text-white mb-3" />
              <textarea placeholder="Content" value={postContent} onChange={(e) => setPostContent(e.target.value)} rows={4}
                className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl text-white mb-3" />
              <select value={selectedCommunity} onChange={(e) => setSelectedCommunity(e.target.value)}
                className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl text-white mb-3">
                <option value="">General</option>
                {communities.map(c => <option key={c.id} value={c.id}>{c.name}</option>)}
              </select>
              <button onClick={createPost} className="px-6 py-2 bg-blue-600 hover:bg-blue-700 rounded-lg font-semibold">Publish</button>
            </motion.div>
          )}

          <div className="space-y-4">
            {filteredPosts.map((post, i) => (
              <motion.div key={post.id} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.05 }}
                className="bg-white/5 border border-white/10 rounded-xl p-6 hover:border-blue-500/30 transition group">
                <div className="flex space-x-4">
                  <div className="flex flex-col items-center space-y-1">
                    <button onClick={() => vote(post.id, 'up')} className="p-1 rounded hover:bg-white/10 transition"><ArrowUp className="w-5 h-5 text-gray-400 hover:text-green-400" /></button>
                    <span className="text-sm font-bold">{post.upvotes - post.downvotes}</span>
                    <button onClick={() => vote(post.id, 'down')} className="p-1 rounded hover:bg-white/10 transition"><ArrowDown className="w-5 h-5 text-gray-400 hover:text-red-400" /></button>
                  </div>
                  <div className="flex-1 min-w-0">
                    <h3 className="font-semibold text-lg group-hover:text-blue-400 transition mb-1">{post.title}</h3>
                    <p className="text-gray-400 text-sm line-clamp-2 mb-3">{post.content}</p>
                    <div className="flex items-center space-x-4 text-xs text-gray-500">
                      <span>{post.comments_count || 0} comments</span>
                      <span>{new Date(post.created_at).toLocaleDateString()}</span>
                    </div>
                  </div>
                </div>
              </motion.div>
            ))}
          </div>
        </>
      ) : (
        <>
          <button onClick={() => createCommunity()}
            className="mb-6 flex items-center space-x-2 px-6 py-3 bg-purple-600 hover:bg-purple-700 rounded-xl font-semibold transition">
            <Plus className="w-5 h-5" /><span>New Community</span>
          </button>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {communities.map((community, i) => (
              <motion.div key={community.id} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.05 }}
                className="bg-white/5 border border-white/10 rounded-xl p-6 hover:border-purple-500/50 transition group">
                <div className="flex items-center space-x-3 mb-4">
                  <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center font-bold text-lg">
                    {community.name[0]}
                  </div>
                  <div>
                    <h3 className="font-semibold group-hover:text-purple-400 transition">{community.name}</h3>
                    <p className="text-xs text-gray-400">{community.member_count || 0} members</p>
                  </div>
                </div>
                <p className="text-sm text-gray-400 line-clamp-2">{community.description}</p>
              </motion.div>
            ))}
          </div>
        </>
      )}
    </div>
  )
}
