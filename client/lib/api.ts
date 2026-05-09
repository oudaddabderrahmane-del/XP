import axios from 'axios'

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:8000'

export const api = axios.create({
  baseURL: API_BASE,
  headers: { 'Content-Type': 'application/json' },
})

api.interceptors.request.use((config) => {
  if (typeof window !== 'undefined') {
    const token = localStorage.getItem('xp_token')
    if (token) config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export async function fetchAPI(path: string, options?: RequestInit) {
  const token = typeof window !== 'undefined' ? localStorage.getItem('xp_token') : null
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { 'Content-Type': 'application/json', ...(token ? { Authorization: `Bearer ${token}` } : {}), ...options?.headers },
    ...options,
  })
  if (!res.ok) throw new Error(await res.text())
  return res.json()
}
