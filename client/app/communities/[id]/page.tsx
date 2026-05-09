'use client'
import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { useParams } from 'next/navigation'
import { MessageSquare, Users, ArrowUp, ArrowDown, Plus, UserPlus } from 'lucide-react'
import { fetchAPI } from '@/lib/api'

export default function CommunityDetailPage() {
  const { id } = useParams()
  const [community, setCommunity] = useState<any>(null)
  const [posts, setPosts] = useState<any[]>([])
  const [loading, setLoading] = useState(true)
  const [showNewPost, setShowNewPost] = useState(false)
  const [title, setTitle] = useState('')
  const [content, setContent] = useState('')

  useEffect(() => {
    if (id) {
      Promise.all([
        fetchAPI(`/api/communities/${id}`).then(setCommunity).catch(() => {}),
        fetchAPI(`/api/posts?community_id=${id}`).then(d => setPosts(d.posts || [])).catch(() => {}),
      ]).finally(() => setLoading(false))
    }
  }, [id])

  async function createPost() {
    if (!title.trim()) return
    try {
      await fetchAPI('/api/posts', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, content, community_id: id }),
      })
      setTitle(''); setContent(''); setShowNewPost(false)
      const data = await fetchAPI(`/api/posts?community_id=${id}`)
      setPosts(data.posts || [])
    } catch (e) { console.error(e) }
  }

  async function vote(postId: string, type: string) {
    try {
      await fetchAPI(`/api/posts/${postId}/vote?vote_type=${type}`, { method: 'POST' })
      setPosts(prev => prev.map(p => p.id === postId ? { ...p, upvotes: (p.upvotes || 0) + (type === 'up' ? 1 : 0), downvotes: (p.downvotes || 0) + (type === 'down' ? 1 : 0) } : p))
    } catch (e) { console.error(e) }
  }

  if (loading) return <div className="max-w-7xl mx-auto px-4 py-8"><div className="h-64 bg-white/5 rounded-2xl animate-pulse" /></div>
  if (!community) return <div className="max-w-7xl mx-auto px-4 py-8 text-center"><p className="text-gray-400">Community not found</p></div>

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Community Header */}
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}
        className="bg-gradient-to-r from-purple-600/20 via-pink-600/20 to-blue-600/20 border border-white/10 rounded-2xl p-8 mb-8">
        <div className="flex items-center space-x-4">
          <div className="w-20 h-20 rounded-2xl bg-gradient-to-br from-purple-500 to-pink-600 flex items-center justify-center text-3xl font-bold">{community.name[0]}</div>
          <div className="flex-1">
            <h1 className="text-3xl font-display font-bold">{community.name}</h1>
            <p className="text-gray-400 mt-1">{community.description || 'No description'}</p>
            <div className="flex items-center space-x-4 mt-3 text-sm text-gray-400">
              <span className="flex items-center"><Users className="w-4 h-4 mr-1" />{community.member_count || 0} members</span>
              <span className="flex items-center"><MessageSquare className="w-4 h-4 mr-1" />{posts.length} posts</span>
            </div>
            <button className="mt-3 px-4 py-2 bg-purple-600 hover:bg-purple-700 rounded-lg text-sm font-semibold transition flex items-center space-x-2">
              <UserPlus className="w-4 h-4" /><span>Join Community</span>
            </button>
          </div>
        </div>
      </motion.div>

      {/* New Post */}
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-xl font-display font-bold">Posts</h2>
        <button onClick={() => setShowNewPost(!showNewPost)} className="flex items-center space-x-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 rounded-lg text-sm font-semibold transition">
          <Plus className="w-4 h-4" /><span>New Post</span>
        </button>
      </div>

      {showNewPost && (
        <motion.div initial={{ opacity: 0, y: -10 }} animate={{ opacity: 1, y: 0 }} className="bg-white/5 border border-white/10 rounded-xl p-6 mb-6">
          <input type="text" placeholder="Post title" value={title} onChange={(e) => setTitle(e.target.value)} className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl mb-3" />
          <textarea placeholder="Content" value={content} onChange={(e) => setContent(e.target.value)} rows={4} className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl mb-3" />
          <button onClick={createPost} className="px-6 py-2 bg-blue-600 hover:bg-blue-700 rounded-lg font-semibold">Publish</button>
        </motion.div>
      )}

      {/* Posts */}
      {posts.length === 0 ? (
        <div className="text-center py-12"><MessageSquare className="w-12 h-12 text-gray-600 mx-auto mb-3" /><p className="text-gray-400">No posts yet. Be the first to share!</p></div>
      ) : (
        <div className="space-y-4">
          {posts.map((post, i) => (
            <motion.div key={post.id} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.05 }}
              className="bg-white/5 border border-white/10 rounded-xl p-6 hover:border-purple-500/30 transition group">
              <div className="flex space-x-4">
                <div className="flex flex-col items-center space-y-1">
                  <button onClick={() => vote(post.id, 'up')} className="p-1 rounded hover:bg-white/10"><ArrowUp className="w-5 h-5 text-gray-400 hover:text-green-400" /></button>
                  <span className="text-sm font-bold">{(post.upvotes || 0) - (post.downvotes || 0)}</span>
                  <button onClick={() => vote(post.id, 'down')} className="p-1 rounded hover:bg-white/10"><ArrowDown className="w-5 h-5 text-gray-400 hover:text-red-400" /></button>
                </div>
                <div className="flex-1">
                  <h3 className="font-semibold text-lg group-hover:text-purple-400 transition">{post.title}</h3>
                  <p className="text-gray-400 text-sm mt-1">{post.content}</p>
                  <div className="flex items-center space-x-4 mt-3 text-xs text-gray-500">
                    <span>{post.comments_count || 0} comments</span>
                    <span>{new Date(post.created_at).toLocaleDateString()}</span>
                  </div>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      )}
    </div>
  )
}
