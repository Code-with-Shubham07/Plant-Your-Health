from pydantic import BaseModel
from datetime import date


class LogCreate(BaseModel):
    activityId: int


class LogResponse(BaseModel):
    id: int
    activity_id: int
    completed_date: date

    class Config:
        from_attributes = True