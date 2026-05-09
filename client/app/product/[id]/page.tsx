'use client'
import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { useParams, useRouter } from 'next/navigation'
import { Heart, Share2, MessageCircle, ShoppingCart, Star, MapPin, ChevronLeft, ChevronRight, Eye, Calendar } from 'lucide-react'
import { fetchAPI } from '@/lib/api'
import { useStore } from '@/store/useStore'

export default function ProductDetailPage() {
  const { id } = useParams()
  const router = useRouter()
  const { user } = useStore()
  const [product, setProduct] = useState<any>(null)
  const [loading, setLoading] = useState(true)
  const [currentImage, setCurrentImage] = useState(0)
  const [showContact, setShowContact] = useState(false)
  const [message, setMessage] = useState('')

  useEffect(() => {
    if (id) loadProduct()
  }, [id])

  async function loadProduct() {
    try {
      const data = await fetchAPI(`/api/products/${id}`)
      setProduct(data)
    } catch (e) { console.error(e) }
    setLoading(false)
  }

  async function toggleFav() {
    try {
      await fetchAPI(`/api/favorites/${id}`, { method: 'POST' })
      loadProduct()
    } catch (e) { console.error(e) }
  }

  async function sendMessage() {
    if (!message.trim()) return
    try {
      await fetchAPI('/api/messages', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ receiver_id: product.seller_id, content: message }),
      })
      setMessage('')
      setShowContact(false)
    } catch (e) { console.error(e) }
  }

  if (loading) return <div className="max-w-7xl mx-auto px-4 py-8"><div className="h-96 bg-white/5 rounded-2xl animate-pulse" /></div>
  if (!product) return <div className="max-w-7xl mx-auto px-4 py-8 text-center"><p className="text-gray-400">Product not found</p></div>

  const images = product.images?.length ? product.images : []

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Image Gallery */}
        <div className="space-y-4">
          <div className="relative bg-white/5 border border-white/10 rounded-2xl overflow-hidden h-96 flex items-center justify-center">
            {images.length > 0 ? (
              <img src={images[currentImage]} alt={product.title} className="w-full h-full object-contain p-4" />
            ) : (
              <ShoppingCart className="w-24 h-24 text-gray-600" />
            )}
            {images.length > 1 && (
              <>
                <button onClick={() => setCurrentImage(i => Math.max(0, i - 1))} className="absolute left-4 top-1/2 -translate-y-1/2 p-2 rounded-full bg-black/50 hover:bg-black/70"><ChevronLeft className="w-5 h-5" /></button>
                <button onClick={() => setCurrentImage(i => Math.min(images.length - 1, i + 1))} className="absolute right-4 top-1/2 -translate-y-1/2 p-2 rounded-full bg-black/50 hover:bg-black/70"><ChevronRight className="w-5 h-5" /></button>
              </>
            )}
            <div className="absolute top-4 right-4 flex space-x-2">
              <button onClick={toggleFav} className="p-2 rounded-full bg-black/50 hover:bg-black/70"><Heart className="w-5 h-5 text-gray-300 hover:text-red-400" /></button>
              <button onClick={() => {}} className="p-2 rounded-full bg-black/50 hover:bg-black/70"><Share2 className="w-5 h-5 text-gray-300" /></button>
            </div>
          </div>
          {images.length > 1 && (
            <div className="flex space-x-2 overflow-x-auto">
              {images.map((img: string, i: number) => (
                <button key={i} onClick={() => setCurrentImage(i)} className={`flex-shrink-0 w-20 h-20 rounded-xl overflow-hidden border-2 transition ${i === currentImage ? 'border-blue-500' : 'border-transparent'}`}>
                  <img src={img} alt="" className="w-full h-full object-cover" />
                </button>
              ))}
            </div>
          )}
        </div>

        {/* Product Info */}
        <div className="space-y-6">
          <div>
            <div className="flex items-center space-x-3 text-sm text-gray-400 mb-2">
              <span className="px-3 py-1 bg-blue-600/20 text-blue-400 rounded-full text-xs font-semibold uppercase">{product.category}</span>
              <span className={`px-3 py-1 rounded-full text-xs font-semibold ${product.condition === 'new' ? 'bg-green-600/20 text-green-400' : 'bg-yellow-600/20 text-yellow-400'}`}>{product.condition}</span>
            </div>
            <h1 className="text-3xl font-display font-bold">{product.title}</h1>
            <div className="flex items-center space-x-4 mt-2 text-sm text-gray-400">
              <span className="flex items-center"><Star className="w-4 h-4 text-yellow-400 mr-1" />{product.rating || 'No ratings'}</span>
              <span className="flex items-center"><Eye className="w-4 h-4 mr-1" />{product.views || 0} views</span>
              <span className="flex items-center"><Calendar className="w-4 h-4 mr-1" />{new Date(product.created_at).toLocaleDateString()}</span>
            </div>
          </div>

          <div className="text-4xl font-bold text-blue-400">${product.price?.toLocaleString()}</div>

          {product.location && (
            <div className="flex items-center text-gray-400 text-sm"><MapPin className="w-4 h-4 mr-1" />{product.location}</div>
          )}

          <p className="text-gray-300 leading-relaxed">{product.description || 'No description provided.'}</p>

          {/* Specs */}
          {product.specs && Object.keys(product.specs).length > 0 && (
            <div className="bg-white/5 border border-white/10 rounded-xl p-4">
              <h3 className="font-semibold mb-3">Specifications</h3>
              <div className="grid grid-cols-2 gap-2">
                {Object.entries(product.specs).map(([key, val]) => (
                  <div key={key} className="flex justify-between py-1 border-b border-white/5 text-sm">
                    <span className="text-gray-400">{key}</span>
                    <span>{val as string}</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Actions */}
          <div className="flex flex-col sm:flex-row gap-3">
            <button onClick={() => {}} className="flex-1 flex items-center justify-center space-x-2 px-6 py-3 bg-blue-600 hover:bg-blue-700 rounded-xl font-semibold transition">
              <ShoppingCart className="w-5 h-5" /><span>Buy Now</span>
            </button>
            <button onClick={() => setShowContact(!showContact)} className="flex-1 flex items-center justify-center space-x-2 px-6 py-3 bg-white/10 hover:bg-white/20 rounded-xl font-semibold transition">
              <MessageCircle className="w-5 h-5" /><span>Contact Seller</span>
            </button>
          </div>

          {showContact && (
            <motion.div initial={{ opacity: 0, y: -10 }} animate={{ opacity: 1, y: 0 }} className="bg-white/5 border border-white/10 rounded-xl p-4">
              <textarea value={message} onChange={(e) => setMessage(e.target.value)} rows={3} placeholder="Write your message..." className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl text-white mb-3" />
              <button onClick={sendMessage} className="px-6 py-2 bg-blue-600 hover:bg-blue-700 rounded-lg font-semibold">Send Message</button>
            </motion.div>
          )}
        </div>
      </motion.div>
    </div>
  )
}
