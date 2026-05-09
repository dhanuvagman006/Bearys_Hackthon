from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import role_required
from app.db import get_db
from app.schemas.backup import BackupRequest, BackupResponse
from app.services.backup_service import create_backup, list_backups
from app.services.audit_service import audit

router = APIRouter(prefix='/backups', tags=['backups'])


@router.post('', response_model=BackupResponse)
async def trigger_backup(
    payload: BackupRequest,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(role_required('admin', 'operator')),
) -> BackupResponse:
    try:
        record = await create_backup(db, payload.asset_id, payload.backup_type)
        await audit(db, user['username'], 'create_backup', f'backup:{record.id}')
        return BackupResponse(
            backup_id=record.id,
            version=record.version,
            checksum=record.checksum,
            immutable_until=record.immutable_until,
        )
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get('')
async def get_backups(db: AsyncSession = Depends(get_db), user: dict = Depends(role_required('admin', 'operator', 'viewer'))):
    records = await list_backups(db)
    return [
        {
            'id': r.id,
            'asset_id': r.asset_id,
            'backup_type': r.backup_type,
            'version': r.version,
            'status': r.status,
            'checksum': r.checksum,
        }
        for r in records
    ]
