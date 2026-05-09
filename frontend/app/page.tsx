import { StatusCards } from '@/components/status-cards'
import { RecoveryChart } from '@/components/recovery-chart'

export default function Page() {
  return (
    <>
      <h1 className="text-2xl font-semibold">Overview</h1>
      <StatusCards />
      <RecoveryChart />
      <div className="card">
        <p className="text-sm text-slate-300">Live resilience posture includes immutable vault health, restore SLA compliance, and active threat simulation telemetry.</p>
      </div>
    </>
  )
}
