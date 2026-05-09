from sqlalchemy import String, Integer, Boolean, ForeignKey, JSON, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(32), default='operator')
    mfa_enabled: Mapped[bool] = mapped_column(Boolean, default=False)


class BackupAsset(Base, TimestampMixin):
    __tablename__ = 'backup_assets'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(120), index=True)
    service_type: Mapped[str] = mapped_column(String(50))
    criticality: Mapped[int] = mapped_column(Integer, default=3)
    asset_metadata: Mapped[dict] = mapped_column(JSON, default={})


class BackupRecord(Base, TimestampMixin):
    __tablename__ = 'backup_records'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    asset_id: Mapped[int] = mapped_column(ForeignKey('backup_assets.id'), index=True)
    backup_type: Mapped[str] = mapped_column(String(20))
    version: Mapped[str] = mapped_column(String(50), index=True)
    checksum: Mapped[str] = mapped_column(String(80))
    status: Mapped[str] = mapped_column(String(30), default='completed')
    immutable_until: Mapped[str] = mapped_column(String(64))


class VaultObject(Base, TimestampMixin):
    __tablename__ = 'vault_objects'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    backup_record_id: Mapped[int] = mapped_column(ForeignKey('backup_records.id'), index=True)
    storage_path: Mapped[str] = mapped_column(String(255), unique=True)
    object_lock: Mapped[bool] = mapped_column(Boolean, default=True)
    retention_days: Mapped[int] = mapped_column(Integer, default=30)


class RecoveryRun(Base, TimestampMixin):
    __tablename__ = 'recovery_runs'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    status: Mapped[str] = mapped_column(String(30), default='queued')
    timeline: Mapped[dict] = mapped_column(JSON, default={})
    estimated_downtime_minutes: Mapped[int] = mapped_column(Integer, default=0)


class DependencyEdge(Base, TimestampMixin):
    __tablename__ = 'dependency_edges'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    source_asset_id: Mapped[int] = mapped_column(ForeignKey('backup_assets.id'), index=True)
    depends_on_asset_id: Mapped[int] = mapped_column(ForeignKey('backup_assets.id'), index=True)


class SimulationRun(Base, TimestampMixin):
    __tablename__ = 'simulation_runs'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    scenario_name: Mapped[str] = mapped_column(String(120))
    status: Mapped[str] = mapped_column(String(30), default='running')
    findings: Mapped[dict] = mapped_column(JSON, default={})


class AuditLog(Base, TimestampMixin):
    __tablename__ = 'audit_logs'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    actor: Mapped[str] = mapped_column(String(64), index=True)
    action: Mapped[str] = mapped_column(String(80))
    resource: Mapped[str] = mapped_column(String(120))
    outcome: Mapped[str] = mapped_column(String(30), default='success')
    details: Mapped[str] = mapped_column(Text, default='')
