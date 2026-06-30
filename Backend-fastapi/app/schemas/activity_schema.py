from pydantic import BaseModel
from typing import Optional


class ActivityBase(BaseModel):
    name: str
    description: Optional[str] = None
    type: str
    points: int = 10


class ActivityCreate(ActivityBase):
    pass


class ActivityResponse(ActivityBase):
    id: int
    completed: bool

    class Config:
        from_attributes = True