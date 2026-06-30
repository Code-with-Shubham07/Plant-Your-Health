from sqlalchemy import Column, Integer, String

from app.database import Base


class Streak(Base):
    __tablename__ = "streaks"

    id = Column(Integer, primary_key=True, index=True)

    type = Column(String, unique=True, nullable=False)

    current_streak = Column(Integer, default=0)

    longest_streak = Column(Integer, default=0)