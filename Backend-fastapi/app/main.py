from fastapi import FastAPI
from app.database import engine, Base
from app.models.activity import Activity
from app.models.activity_log import ActivityLog
from fastapi.middleware.cors import CORSMiddleware
from app.database import SessionLocal
from app.utils.seed_data import seed_activities

from app.routers.activity_router import (
    router as activity_router
)

from app.routers.log_router import (
    router as log_router
)

from app.models.streak import Streak
from app.routers.streak_router import (
    router as streak_router
)

from app.models.user import User

from app.routers.auth_router import (
    router as auth_router
)

app = FastAPI()

Base.metadata.create_all(bind=engine)
db = SessionLocal()
seed_activities(db)
db.close()

app.include_router(activity_router)
app.include_router(log_router)
app.include_router(streak_router)
app.include_router(auth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Plant Your Health Backend Running"
    }