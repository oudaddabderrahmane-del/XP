import type { Config } from 'tailwindcss'

const config = {
  darkMode: 'class',
  content: ['./app/**/*.{js,ts,jsx,tsx}', './components/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        xp: {
          black: '#000000',
          white: '#FFFFFF',
          gray: '#7A7A7A',
          dark: '#1A1A1A',
          silver: '#BFC3C7',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        display: ['Orbitron', 'sans-serif'],
      },
      animation: {
        'pulse-neon': 'pulse-neon 2s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'glow': 'glow 2s ease-in-out infinite',
        'float': 'float 6s ease-in-out infinite',
        'rgb': 'rgb 3s linear infinite',
        'scan': 'scan 4s linear infinite',
      },
      keyframes: {
        'pulse-neon': {
          '0%, 100%': { opacity: '1', boxShadow: '0 0 20px rgba(191, 195, 199, 0.3)' },
          '50%': { opacity: '.5', boxShadow: '0 0 30px rgba(191, 195, 199, 0.6)' },
        },
        'glow': {
          '0%, 100%': { boxShadow: 'inset 0 0 20px rgba(191, 195, 199, 0.2)' },
          '50%': { boxShadow: 'inset 0 0 30px rgba(191, 195, 199, 0.4)' },
        },
        'float': {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-20px)' },
        },
        'rgb': {
          '0%': { filter: 'hue-rotate(0deg)' },
          '100%': { filter: 'hue-rotate(360deg)' },
        },
        'scan': {
          '0%': { transform: 'translateX(-100%)' },
          '100%': { transform: 'translateX(100%)' },
        },
      },
    },
  },
  plugins: [],
} satisfies Config

export default config
