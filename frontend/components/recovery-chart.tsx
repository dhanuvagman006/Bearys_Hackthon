'use client'

import { Area, AreaChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts'

const data = [
  { day: 'Mon', rto: 48 },
  { day: 'Tue', rto: 43 },
  { day: 'Wed', rto: 36 },
  { day: 'Thu', rto: 39 },
  { day: 'Fri', rto: 33 },
  { day: 'Sat', rto: 30 },
  { day: 'Sun', rto: 34 }
]

export function RecoveryChart() {
  return (
    <div className="card h-80">
      <h3 className="mb-2 text-sm font-medium text-slate-300">Recovery Time Trend (minutes)</h3>
      <ResponsiveContainer width="100%" height="90%">
        <AreaChart data={data}>
          <CartesianGrid stroke="#1f2937" />
          <XAxis dataKey="day" stroke="#94a3b8" />
          <YAxis stroke="#94a3b8" />
          <Tooltip />
          <Area type="monotone" dataKey="rto" stroke="#22d3ee" fill="#1d4ed8" fillOpacity={0.35} />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  )
}
