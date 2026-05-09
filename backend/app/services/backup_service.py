from datetime import datetime, timedelta, UTC
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import checksum
from app.models.entities import BackupRecord, BackupAsset


async def create_backup(db: AsyncSession, asset_id: int, backup_type: str) -> BackupRecord:
    asset = await db.scalar(select(BackupAsset).where(BackupAsset.id == asset_id))
    if not asset:
        raise ValueError('asset_not_found')
    version = datetime.now(UTC).strftime('%Y%m%d%H%M%S')
    fake_payload = f'{asset.name}:{backup_type}:{version}'.encode()
    record = BackupRecord(
        asset_id=asset_id,
        backup_type=backup_type,
        version=version,
        checksum=checksum(fake_payload),
        immutable_until=(datetime.now(UTC) + timedelta(days=30)).isoformat(),
    )
    db.add(record)
    await db.commit()
    await db.refresh(record)
    return record


async def list_backups(db: AsyncSession) -> list[BackupRecord]:
    result = await db.scalars(select(BackupRecord).order_by(BackupRecord.created_at.desc()))
    return list(result)
