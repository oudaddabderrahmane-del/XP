import type { Metadata } from 'next'
import '../styles/globals.css'
import Providers from './providers'

export const metadata: Metadata = {
  title: 'XP — The Future of Gaming & Tech',
  description: 'Build PCs, buy hardware, join communities, and connect gamers & developers in one futuristic ecosystem.',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className="dark scroll-smooth">
      <head>
        <meta name="theme-color" content="#000000" />
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Orbitron:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
      </head>
      <body className="font-sans bg-black text-white antialiased">
        <div className="fixed inset-0 -z-10">
          <div className="absolute inset-0 bg-black" />
          <div className="absolute top-0 left-1/4 w-px h-full bg-gradient-to-b from-transparent via-[#BFC3C7]/10 to-transparent" />
          <div className="absolute top-0 right-1/4 w-px h-full bg-gradient-to-b from-transparent via-[#BFC3C7]/5 to-transparent" />
          <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-[#BFC3C7]/20 to-transparent" />
          <div className="absolute top-1/4 -right-40 w-96 h-96 bg-[#BFC3C7]/[0.03] rounded-full blur-3xl" />
          <div className="absolute bottom-1/4 -left-40 w-96 h-96 bg-white/[0.02] rounded-full blur-3xl" />
        </div>
        <Providers>
          {children}
        </Providers>
      </body>
    </html>
  )
}
