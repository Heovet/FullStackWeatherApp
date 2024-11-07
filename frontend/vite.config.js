import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  root: './',  // Ensure this points to the correct directory
  build: {
    outDir: 'build',  // Output directory for production build
  }
})
