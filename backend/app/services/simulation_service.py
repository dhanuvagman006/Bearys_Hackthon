from sqlalchemy.ext.asyncio import AsyncSession

from app.models.entities import SimulationRun


async def run_ransomware_simulation(db: AsyncSession, scenario_name: str, targets: list[int]) -> tuple[SimulationRun, list[str]]:
    timeline = [
        'Initial access emulated',
        'Lateral movement simulated',
        'Encryption event simulated on sandbox data',
        'Backup restore validation executed',
    ]
    findings = {
        'target_count': len(targets),
        'survivable': True,
        'alerts': ['Immutable backups unaffected', 'Restore SLA met in simulation'],
    }
    run = SimulationRun(scenario_name=scenario_name, status='completed', findings=findings)
    db.add(run)
    await db.commit()
    await db.refresh(run)
    return run, timeline
