export function DependencyGraph() {
  const nodes = [
    { id: 'api-gateway', x: 25, y: 15 },
    { id: 'auth', x: 60, y: 10 },
    { id: 'backup-engine', x: 45, y: 40 },
    { id: 'vault', x: 75, y: 45 },
    { id: 'recovery', x: 35, y: 70 }
  ]

  return (
    <div className="card h-96">
      <h3 className="mb-4 text-sm font-medium text-slate-300">Infrastructure Dependency Map</h3>
      <div className="relative h-80 rounded-lg border border-slate-800 bg-slate-950">
        {nodes.map((n) => (
          <div key={n.id} className="absolute -translate-x-1/2 -translate-y-1/2 rounded bg-blue-900/50 px-2 py-1 text-xs"
               style={{ left: `${n.x}%`, top: `${n.y}%` }}>
            {n.id}
          </div>
        ))}
      </div>
    </div>
  )
}
