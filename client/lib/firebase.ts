import { initializeApp, getApps, FirebaseOptions } from 'firebase/app'
import {
  getAuth,
  GoogleAuthProvider,
  Auth,
  signInWithPopup,
  signOut,
  onAuthStateChanged,
  User,
} from 'firebase/auth'

const firebaseConfig: FirebaseOptions = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY || 'AIzaSyDqmZsQng8fLOEePO9ybbqEqv1PbdIqIdw',
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN || 'xp-xp-c485d.firebaseapp.com',
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'xp-xp-c485d',
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET || 'xp-xp-c485d.firebasestorage.app',
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID || '256122079136',
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID || '1:256122079136:web:75e44239f40c022721c6c5',
  measurementId: process.env.NEXT_PUBLIC_FIREBASE_MEASUREMENT_ID || 'G-KE06T4JJF3',
}

let appInstance: ReturnType<typeof initializeApp> | null = null
let authInstance: Auth | null = null
let providerInstance: GoogleAuthProvider | null = null

function initFirebase() {
  if (typeof window === 'undefined') return
  if (!authInstance) {
    appInstance = getApps().length === 0 ? initializeApp(firebaseConfig) : getApps()[0]
    authInstance = getAuth(appInstance)
    providerInstance = new GoogleAuthProvider()
    // Optional: add scopes if needed
    // providerInstance.addScope('profile')
    // providerInstance.addScope('email')
  }
}

initFirebase()

export function getFirebaseAuth() {
  return { auth: authInstance, googleProvider: providerInstance }
}

export async function signInWithGoogle(): Promise<User> {
  const { auth, googleProvider } = getFirebaseAuth()
  if (!auth || !googleProvider) throw new Error('Firebase not initialized on server')
  const result = await signInWithPopup(auth, googleProvider)
  return result.user
}

export async function signOutGoogle(): Promise<void> {
  const { auth } = getFirebaseAuth()
  if (!auth) return
  await signOut(auth)
}

export function onAuthChange(callback: (user: User | null) => void): () => void {
  const { auth } = getFirebaseAuth()
  if (!auth) {
    callback(null)
    return () => {}
  }
  const unsub = onAuthStateChanged(auth, callback)
  return unsub
}

export type FirebaseUserData = {
  uid: string
  displayName: string
  email: string
  photoURL: string | null
}

export function mapFirebaseUser(user: User): FirebaseUserData {
  return {
    uid: user.uid,
    displayName: user.displayName || '',
    email: user.email || '',
    photoURL: user.photoURL,
  }
}
