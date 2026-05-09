from sqlalchemy.ext.asyncio import AsyncSession

from app.models.entities import AuditLog


async def audit(db: AsyncSession, actor: str, action: str, resource: str, details: str = '', outcome: str = 'success') -> None:
    db.add(AuditLog(actor=actor, action=action, resource=resource, details=details, outcome=outcome))
    await db.commit()
