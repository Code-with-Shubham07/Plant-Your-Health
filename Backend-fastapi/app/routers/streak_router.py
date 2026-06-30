from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.streak import Streak
from app.schemas.streak_schema import (
    StreakResponse
)

router = APIRouter(
    prefix="/api/streaks",
    tags=["Streaks"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[StreakResponse])
def get_streaks(
    db: Session = Depends(get_db)
):
    return db.query(Streak).all()