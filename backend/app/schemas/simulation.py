from pydantic import BaseModel


class SimulationRequest(BaseModel):
    scenario_name: str
    target_asset_ids: list[int]


class SimulationResponse(BaseModel):
    run_id: int
    status: str
    timeline: list[str]
