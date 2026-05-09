from fastapi import APIRouter, Depends

from app.api.deps import role_required
from app.services.analytics_service import compute_readiness_score

router = APIRouter(prefix='/analytics', tags=['analytics'])


@router.get('/readiness')
async def readiness(user: dict = Depends(role_required('admin', 'operator', 'viewer'))):
    score = compute_readiness_score(backup_success_rate=0.98, avg_recovery_minutes=42, verification_coverage=0.93)
    return {
        'recovery_readiness_score': score,
        'mttr_minutes': 42,
        'backup_success_rate': 0.98,
        'verification_coverage': 0.93,
        'risk_score': round(100 - score, 2),
    }
