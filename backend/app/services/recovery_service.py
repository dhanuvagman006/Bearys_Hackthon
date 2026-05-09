from sqlalchemy.ext.asyncio import AsyncSession

from app.models.entities import RecoveryRun
from app.services.dependency_service import restore_order


async def create_recovery_plan(db: AsyncSession, name: str, target_assets: list[int]) -> tuple[RecoveryRun, list[int], int]:
    order = await restore_order(db, target_assets)
    estimated = max(5, len(order) * 7)
    run = RecoveryRun(name=name, status='planned', timeline={'order': order}, estimated_downtime_minutes=estimated)
    db.add(run)
    await db.commit()
    await db.refresh(run)
    return run, order, estimated
