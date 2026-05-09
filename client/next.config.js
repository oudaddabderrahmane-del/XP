const path = require('path')

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  transpilePackages: ['@firebase/auth', '@firebase/auth-compat', '@firebase/app', '@firebase/app-compat', 'undici'],
  webpack: (config) => {
    config.resolve.alias['firebase/app'] = path.resolve(__dirname, 'node_modules/firebase/app/dist/index.cjs.js')
    config.resolve.alias['firebase/auth'] = path.resolve(__dirname, 'node_modules/firebase/auth/dist/index.cjs.js')
    config.resolve.alias['firebase/compat/app'] = path.resolve(__dirname, 'node_modules/firebase/compat/app/dist/index.cjs.js')
    config.resolve.alias['firebase/compat/auth'] = path.resolve(__dirname, 'node_modules/firebase/compat/auth/dist/index.cjs.js')
    return config
  },
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'res.cloudinary.com',
      },
      {
        protocol: 'https',
        hostname: '**.supabase.co',
      },
    ],
    formats: ['image/avif', 'image/webp'],
  },
  headers: async () => {
    return [
      {
        source: '/api/:path*',
        headers: [
          { key: 'Access-Control-Allow-Credentials', value: 'true' },
          { key: 'Access-Control-Allow-Origin', value: '*' },
          { key: 'Access-Control-Allow-Methods', value: 'GET,OPTIONS,PATCH,DELETE,POST,PUT' },
          { key: 'Access-Control-Allow-Headers', value: 'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version' },
        ],
      },
    ]
  },
}

module.exports = nextConfig
