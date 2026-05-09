from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import role_required
from app.db import get_db
from app.schemas.simulation import SimulationRequest, SimulationResponse
from app.services.simulation_service import run_ransomware_simulation
from app.services.audit_service import audit

router = APIRouter(prefix='/simulation', tags=['simulation'])


@router.post('/run', response_model=SimulationResponse)
async def run_simulation(
    payload: SimulationRequest,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(role_required('admin', 'operator')),
) -> SimulationResponse:
    run, timeline = await run_ransomware_simulation(db, payload.scenario_name, payload.target_asset_ids)
    await audit(db, user['username'], 'run_simulation', f'simulation:{run.id}')
    return SimulationResponse(run_id=run.id, status=run.status, timeline=timeline)
