from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import role_required
from app.db import get_db
from app.services.vault_service import lock_backup_in_vault
from app.services.audit_service import audit

router = APIRouter(prefix='/vault', tags=['vault'])


@router.post('/lock/{backup_id}')
async def lock_backup(backup_id: int, db: AsyncSession = Depends(get_db), user: dict = Depends(role_required('admin'))):
    try:
        obj = await lock_backup_in_vault(db, backup_id)
        await audit(db, user['username'], 'lock_backup', f'vault:{obj.id}')
        return {'id': obj.id, 'storage_path': obj.storage_path, 'object_lock': obj.object_lock}
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
