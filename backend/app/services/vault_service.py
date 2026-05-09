from datetime import datetime, UTC
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.entities import VaultObject, BackupRecord


async def lock_backup_in_vault(db: AsyncSession, backup_record_id: int) -> VaultObject:
    record = await db.scalar(select(BackupRecord).where(BackupRecord.id == backup_record_id))
    if not record:
        raise ValueError('backup_not_found')
    vault_object = VaultObject(
        backup_record_id=backup_record_id,
        storage_path=f'/vault/{record.version}.bin',
        object_lock=True,
        retention_days=30,
    )
    db.add(vault_object)
    await db.commit()
    await db.refresh(vault_object)
    return vault_object


def can_delete(vault_obj: VaultObject, now: datetime) -> bool:
    return not vault_obj.object_lock and now >= vault_obj.created_at.replace(tzinfo=UTC)
