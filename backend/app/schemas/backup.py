from pydantic import BaseModel, Field


class BackupRequest(BaseModel):
    asset_id: int
    backup_type: str = Field(pattern='^(full|incremental)$')


class BackupResponse(BaseModel):
    backup_id: int
    version: str
    checksum: str
    immutable_until: str
