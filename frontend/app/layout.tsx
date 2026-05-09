import './globals.css'
import { Nav } from '@/components/nav'
import type { ReactNode } from 'react'

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        <main className="mx-auto flex min-h-screen max-w-7xl flex-col gap-6 p-6 lg:flex-row">
          <Nav />
          <section className="flex-1 space-y-6">{children}</section>
        </main>
      </body>
    </html>
  )
}
