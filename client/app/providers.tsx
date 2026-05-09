'use client'
import Sidebar from '@/components/Sidebar'
import { AuthProvider } from '@/lib/AuthContext'

export default function Providers({ children }: { children: React.ReactNode }) {
  return (
    <AuthProvider>
      <Sidebar />
      <main className="min-h-screen md:pl-[68px] pt-14 md:pt-0">
        {children}
      </main>
    </AuthProvider>
  )
}
