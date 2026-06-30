from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from app.database import SessionLocal
from app.models.activity import Activity
from app.schemas.activity_schema import (
    ActivityCreate,
    ActivityResponse
)

router = APIRouter(
    prefix="/api/activities",
    tags=["Activities"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[ActivityResponse])
def get_activities(
    type: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Activity)

    if type:
        query = query.filter(Activity.type == type)

    return query.all()

@router.get("/{activity_type}", response_model=list[ActivityResponse])
def get_activities_by_type(
    activity_type: str,
    db: Session = Depends(get_db)
):
    return db.query(Activity).filter(
        Activity.type == activity_type
    ).all()


@router.post("/", response_model=ActivityResponse)
def create_activity(
    activity: ActivityCreate,
    db: Session = Depends(get_db)
):
    new_activity = Activity(
        name=activity.name,
        description=activity.description,
        type=activity.type,
        points=activity.points
    )

    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)

    return new_activity

@router.put("/{activity_id}", response_model=ActivityResponse)
def update_activity(
    activity_id: int,
    updated_activity: ActivityCreate,
    db: Session = Depends(get_db)
):
    activity = db.query(Activity).filter(
        Activity.id == activity_id
    ).first()

    if not activity:
        raise HTTPException(
            status_code=404,
            detail="Activity not found"
        )

    activity.name = updated_activity.name
    activity.description = updated_activity.description
    activity.type = updated_activity.type
    activity.points = updated_activity.points

    db.commit()
    db.refresh(activity)

    return activity

@router.delete("/{activity_id}")
def delete_activity(
    activity_id: int,
    db: Session = Depends(get_db)
):
    activity = db.query(Activity).filter(
        Activity.id == activity_id
    ).first()

    if not activity:
        raise HTTPException(
            status_code=404,
            detail="Activity not found"
        )

    db.delete(activity)
    db.commit()

    return {"message": "Activity deleted successfully"}