import type { Config } from 'tailwindcss'

const config: Config = {
  content: ['./app/**/*.{ts,tsx}', './components/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        bg: '#05070f',
        card: '#0d1325',
        accent: '#1d4ed8',
        neon: '#22d3ee'
      }
    }
  },
  plugins: []
}

export default config
