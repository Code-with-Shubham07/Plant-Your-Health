from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from app.models.streak import Streak
from app.database import SessionLocal
from app.models.activity import Activity
from app.models.activity_log import ActivityLog
from app.schemas.log_schema import (
    LogCreate,
    LogResponse
)

router = APIRouter(
    prefix="/api/logs",
    tags=["Logs"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=LogResponse)
def mark_activity_done(
    log: LogCreate,
    db: Session = Depends(get_db)
):
    activity = db.query(Activity).filter(
        Activity.id == log.activityId
    ).first()

    if not activity:
        raise HTTPException(
            status_code=404,
            detail="Activity not found"
        )

    existing_log = db.query(ActivityLog).filter(
        ActivityLog.activity_id == log.activityId,
        ActivityLog.completed_date == date.today()
    ).first()

    if existing_log:
        return existing_log

    new_log = ActivityLog(
        activity_id=log.activityId
    )

    activity.completed = True

    streak = db.query(Streak).filter(
    Streak.type == activity.type
    ).first()

    if not streak:
        streak = Streak(
            type=activity.type,
            current_streak=1,
            longest_streak=1
        )
        db.add(streak)

    else:
        streak.current_streak += 1

        if streak.current_streak > streak.longest_streak:
            streak.longest_streak = streak.current_streak

        db.add(new_log)
        db.commit()
        db.refresh(new_log)

    return new_log


@router.get("/", response_model=list[LogResponse])
def get_logs(db: Session = Depends(get_db)):
    return db.query(ActivityLog).all()