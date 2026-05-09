"""initial schema

Revision ID: 0001
Revises:
Create Date: 2026-05-09
"""

from alembic import op
import sqlalchemy as sa

revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('username', sa.String(length=64), nullable=False, unique=True),
        sa.Column('password_hash', sa.String(length=255), nullable=False),
        sa.Column('role', sa.String(length=32), nullable=False),
        sa.Column('mfa_enabled', sa.Boolean(), nullable=False, default=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
    )
    op.create_index('ix_users_username', 'users', ['username'], unique=True)

    op.create_table(
        'backup_assets',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=120), nullable=False),
        sa.Column('service_type', sa.String(length=50), nullable=False),
        sa.Column('criticality', sa.Integer(), nullable=False, server_default='3'),
        sa.Column('asset_metadata', sa.JSON(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
    )
    op.create_index('ix_backup_assets_name', 'backup_assets', ['name'], unique=False)

    for table in ['backup_records', 'vault_objects', 'recovery_runs', 'dependency_edges', 'simulation_runs', 'audit_logs']:
        if table == 'backup_records':
            op.create_table(
                table,
                sa.Column('id', sa.Integer(), primary_key=True),
                sa.Column('asset_id', sa.Integer(), sa.ForeignKey('backup_assets.id'), nullable=False),
                sa.Column('backup_type', sa.String(length=20), nullable=False),
                sa.Column('version', sa.String(length=50), nullable=False),
                sa.Column('checksum', sa.String(length=80), nullable=False),
                sa.Column('status', sa.String(length=30), nullable=False),
                sa.Column('immutable_until', sa.String(length=64), nullable=False),
                sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
                sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
            )
            op.create_index('ix_backup_records_asset_id', table, ['asset_id'], unique=False)
            op.create_index('ix_backup_records_version', table, ['version'], unique=False)
        elif table == 'vault_objects':
            op.create_table(
                table,
                sa.Column('id', sa.Integer(), primary_key=True),
                sa.Column('backup_record_id', sa.Integer(), sa.ForeignKey('backup_records.id'), nullable=False),
                sa.Column('storage_path', sa.String(length=255), nullable=False),
                sa.Column('object_lock', sa.Boolean(), nullable=False),
                sa.Column('retention_days', sa.Integer(), nullable=False),
                sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
                sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
            )
            op.create_index('ix_vault_objects_backup_record_id', table, ['backup_record_id'], unique=False)
        elif table == 'recovery_runs':
            op.create_table(
                table,
                sa.Column('id', sa.Integer(), primary_key=True),
                sa.Column('name', sa.String(length=120), nullable=False),
                sa.Column('status', sa.String(length=30), nullable=False),
                sa.Column('timeline', sa.JSON(), nullable=False),
                sa.Column('estimated_downtime_minutes', sa.Integer(), nullable=False),
                sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
                sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
            )
        elif table == 'dependency_edges':
            op.create_table(
                table,
                sa.Column('id', sa.Integer(), primary_key=True),
                sa.Column('source_asset_id', sa.Integer(), sa.ForeignKey('backup_assets.id'), nullable=False),
                sa.Column('depends_on_asset_id', sa.Integer(), sa.ForeignKey('backup_assets.id'), nullable=False),
                sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
                sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
            )
        elif table == 'simulation_runs':
            op.create_table(
                table,
                sa.Column('id', sa.Integer(), primary_key=True),
                sa.Column('scenario_name', sa.String(length=120), nullable=False),
                sa.Column('status', sa.String(length=30), nullable=False),
                sa.Column('findings', sa.JSON(), nullable=False),
                sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
                sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
            )
        else:
            op.create_table(
                table,
                sa.Column('id', sa.Integer(), primary_key=True),
                sa.Column('actor', sa.String(length=64), nullable=False),
                sa.Column('action', sa.String(length=80), nullable=False),
                sa.Column('resource', sa.String(length=120), nullable=False),
                sa.Column('outcome', sa.String(length=30), nullable=False),
                sa.Column('details', sa.Text(), nullable=False),
                sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
                sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
            )


def downgrade() -> None:
    for table in ['audit_logs', 'simulation_runs', 'dependency_edges', 'recovery_runs', 'vault_objects', 'backup_records', 'backup_assets', 'users']:
        op.drop_table(table)
