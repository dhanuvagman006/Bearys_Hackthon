import Link from 'next/link'

const links = [
  ['Overview', '/'],
  ['Backup Health', '/backup-health'],
  ['Recovery Center', '/recovery-center'],
  ['Attack Simulation', '/attack-simulation'],
  ['Infrastructure Graph', '/infrastructure-graph'],
  ['Incident Timeline', '/incident-timeline'],
  ['Reports', '/reports'],
  ['Settings', '/settings']
]

export function Nav() {
  return (
    <aside className="card h-fit w-full lg:w-64">
      <h2 className="mb-4 text-lg font-semibold text-neon">Resilience SOC</h2>
      <nav className="space-y-2">
        {links.map(([name, path]) => (
          <Link key={path} href={path} className="block rounded-md px-3 py-2 text-sm text-slate-200 hover:bg-slate-800">
            {name}
          </Link>
        ))}
      </nav>
    </aside>
  )
}
