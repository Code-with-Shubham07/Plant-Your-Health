from pydantic import BaseModel


class StreakResponse(BaseModel):
    type: str
    current_streak: int
    longest_streak: int

    class Config:
        from_attributes = True