from sqlalchemy import Column, Integer, Date, ForeignKey
from datetime import date

from app.database import Base


class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True, index=True)

    activity_id = Column(
        Integer,
        ForeignKey("activities.id"),
        nullable=False
    )

    completed_date = Column(
        Date,
        default=date.today
    )