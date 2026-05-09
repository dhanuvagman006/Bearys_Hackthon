from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import role_required
from app.db import get_db
from app.schemas.recovery import RecoveryRequest, RecoveryPlanResponse
from app.services.recovery_service import create_recovery_plan
from app.services.audit_service import audit

router = APIRouter(prefix='/recovery', tags=['recovery'])


@router.post('/plan', response_model=RecoveryPlanResponse)
async def plan_recovery(
    payload: RecoveryRequest,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(role_required('admin', 'operator')),
) -> RecoveryPlanResponse:
    run, order, estimated = await create_recovery_plan(db, payload.name, payload.target_assets)
    await audit(db, user['username'], 'plan_recovery', f'recovery:{run.id}')
    return RecoveryPlanResponse(restore_order=order, estimated_downtime_minutes=estimated)
