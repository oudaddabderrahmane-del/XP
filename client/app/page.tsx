'use client'

import { motion } from 'framer-motion'
import Link from 'next/link'
import { ArrowRight, Zap, Users, Cpu, Brain, ShoppingCart, Gamepad2, MessageCircle, Trophy, Search } from 'lucide-react'
const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    transition: { staggerChildren: 0.1 }
  },
}
const itemVariants = {
  hidden: { opacity: 0, y: 30 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.6 } },
}

export default function Home() {
  return (
    <div className="w-full overflow-hidden">

      {/* Hero Section */}
      <section className="relative pt-32 pb-20 px-4 sm:px-6 lg:px-8 min-h-screen flex items-center justify-center">
        <motion.div
          initial="hidden"
          animate="visible"
          variants={containerVariants}
          className="max-w-4xl mx-auto text-center space-y-8"
        >
          {/* Animated particles background */}
          <div className="absolute inset-0 overflow-hidden -z-5">
            {[...Array(20)].map((_, i) => (
              <motion.div
                key={i}
                className="absolute w-1 h-1 bg-[#BFC3C7] rounded-full"
                animate={{
                  y: ['0%', '100%'],
                  opacity: [0, 0.8, 0],
                }}
                transition={{
                  duration: Math.random() * 3 + 2,
                  repeat: Infinity,
                  delay: Math.random() * 2,
                }}
                style={{
                  left: `${Math.random() * 100}%`,
                  top: '-10px',
                }}
              />
            ))}
          </div>
          {/* Scanning line */}
          <div className="absolute top-0 left-0 right-0 h-[1px] bg-gradient-to-r from-transparent via-[#BFC3C7]/40 to-transparent animate-scan" />

          <motion.div variants={itemVariants} className="space-y-4">
            <motion.div
              initial={{ opacity: 0, scale: 0.8 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.5 }}
              className="inline-block px-4 py-2 glass rounded-full border border-blue-400/50"
            >
              <span className="text-[#BFC3C7] font-semibold flex items-center space-x-2">
                <Zap className="w-4 h-4" />
                <span>Welcome to XP — the future of gaming</span>
              </span>
            </motion.div>

            <h1 className="text-5xl sm:text-6xl lg:text-7xl font-display font-black bg-gradient-to-r from-white via-[#BFC3C7] to-white bg-clip-text text-transparent leading-tight">
              XP — The Future Of Gaming & Tech
            </h1>

            <p className="text-xl text-gray-300 max-w-2xl mx-auto leading-relaxed">
              Build PCs, buy hardware, join communities, and connect gamers & developers in one futuristic ecosystem.
            </p>
          </motion.div>

          {/* CTA Buttons */}
          <motion.div
            variants={itemVariants}
            className="flex flex-col sm:flex-row gap-4 justify-center pt-8"
          >
            <Link href="/marketplace">
              <button className="btn-primary px-8 py-4 text-lg flex items-center space-x-2 group w-full sm:w-auto justify-center">
                <ShoppingCart className="w-5 h-5" />
                <span>Explore Marketplace</span>
                <ArrowRight className="w-5 h-5 group-hover:translate-x-2 transition" />
              </button>
            </Link>
            <Link href="/builder">
              <button className="btn-secondary px-8 py-4 text-lg flex items-center space-x-2 group w-full sm:w-auto justify-center">
                <Cpu className="w-5 h-5" />
                <span>Build Your PC</span>
              </button>
            </Link>
            <Link href="/communities">
              <button className="btn-secondary px-8 py-4 text-lg flex items-center space-x-2 group w-full sm:w-auto justify-center">
                <Users className="w-5 h-5" />
                <span>Join Community</span>
              </button>
            </Link>
          </motion.div>
        </motion.div>
      </section>

      {/* Features Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-6xl mx-auto">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="text-center mb-16"
          >
            <h2 className="text-4xl font-display font-bold mb-4">Powerful Features</h2>
            <p className="text-gray-400 text-lg">Everything you need to build, buy, and connect</p>
          </motion.div>

          <motion.div
            initial="hidden"
            whileInView="visible"
            variants={containerVariants}
            className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
          >
            {features.map((feature, idx) => (
              <motion.div
                key={idx}
                variants={itemVariants}
                className="card group"
              >
                <div                 className="mb-4 p-3 bg-white/5 rounded-lg w-fit group-hover:bg-white/10 transition group-hover:animate-rgb">
                  {feature.icon}
                </div>
                <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
                <p className="text-gray-400">{feature.description}</p>
              </motion.div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-6xl mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
            {stats.map((stat, idx) => (
              <motion.div
                key={idx}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: idx * 0.1 }}
                className="glass p-6 text-center"
              >
                <div className="text-4xl font-display font-bold text-[#BFC3C7] mb-2">{stat.value}</div>
                <div className="text-gray-300">{stat.label}</div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-4xl mx-auto">
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            whileInView={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8 }}
            className="glass-lg p-12 text-center"
          >
            <h2 className="text-4xl font-display font-bold mb-4">Ready to Join?</h2>
            <p className="text-gray-300 mb-8 text-lg">Start your journey in the gaming and tech ecosystem today</p>
            <Link href="/register">
              <button className="btn-primary px-8 py-4 text-lg">Get Started Now</button>
            </Link>
          </motion.div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-white/10 py-12 px-4 sm:px-6 lg:px-8">
        <div className="max-w-6xl mx-auto text-center text-gray-400">
          <p>&copy; 2026 XP Platform. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}

const features = [
  {
    icon: <ShoppingCart className="w-6 h-6 text-[#BFC3C7]" />,
    title: 'Marketplace',
    description: 'Buy and sell gaming hardware, PCs, and accessories in a trusted community',
  },
  {
    icon: <Users className="w-6 h-6 text-[#BFC3C7]" />,
    title: 'Communities',
    description: 'Connect with gamers, developers, and builders worldwide',
  },
  {
    icon: <Cpu className="w-6 h-6 text-[#BFC3C7]" />,
    title: 'PC Builder',
    description: 'Design your perfect build with real-time compatibility checking',
  },
  {
    icon: <MessageCircle className="w-6 h-6 text-[#BFC3C7]" />,
    title: 'Real-time Chat',
    description: 'Instant messaging with buyers, sellers, and community members',
  },
  {
    icon: <Brain className="w-6 h-6 text-[#BFC3C7]" />,
    title: 'AI Assistant',
    description: 'Smart recommendations and price estimation powered by AI',
  },
  {
    icon: <Gamepad2 className="w-6 h-6 text-[#BFC3C7]" />,
    title: 'XP System',
    description: 'Level up and earn achievements while trading and posting',
  },
  {
    icon: <Trophy className="w-6 h-6 text-[#BFC3C7]" />,
    title: 'Leaderboard',
    description: 'Compete with top contributors and earn your rank',
  },
  {
    icon: <Search className="w-6 h-6 text-[#BFC3C7]" />,
    title: 'Smart Search',
    description: 'Find products, communities, posts, and people instantly',
  },
]

const stats = [
  { value: '10K+', label: 'Active Users' },
  { value: '5K+', label: 'Products Listed' },
  { value: '500+', label: 'Communities' },
  { value: '99.9%', label: 'Uptime' },
]
