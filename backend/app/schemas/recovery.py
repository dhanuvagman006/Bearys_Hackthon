from pydantic import BaseModel


class RecoveryRequest(BaseModel):
    name: str
    target_assets: list[int]
    strategy: str = 'priority'


class RecoveryPlanResponse(BaseModel):
    restore_order: list[int]
    estimated_downtime_minutes: int
