from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    description = Column(String, nullable=True)

    type = Column(String, nullable=False)

    points = Column(Integer, default=10)

    completed = Column(Boolean, default=False)