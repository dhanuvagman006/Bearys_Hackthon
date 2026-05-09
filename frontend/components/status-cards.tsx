const cards = [
  { label: 'Recovery Readiness', value: '91.6%', color: 'text-emerald-400' },
  { label: 'Immutable Vault Objects', value: '4,821', color: 'text-cyan-400' },
  { label: 'Active Incidents', value: '1', color: 'text-amber-300' },
  { label: 'MTTR (30d)', value: '38 min', color: 'text-blue-300' }
]

export function StatusCards() {
  return (
    <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
      {cards.map((card) => (
        <div key={card.label} className="card transition hover:-translate-y-0.5 hover:border-blue-500">
          <p className="text-xs uppercase text-slate-400">{card.label}</p>
          <p className={`mt-2 text-2xl font-semibold ${card.color}`}>{card.value}</p>
        </div>
      ))}
    </div>
  )
}
