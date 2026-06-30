from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User

from app.schemas.auth_schema import (
    SignupRequest,
    LoginRequest,
    UserResponse
)

router = APIRouter(tags=["Authentication"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/signup",
    response_model=UserResponse
)
def signup(
    user: SignupRequest,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        (User.username == user.username)
        | (User.email == user.email)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post(
    "/login",
    response_model=UserResponse
)
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        (
            User.username
            == credentials.username_or_email
        )
        |
        (
            User.email
            == credentials.username_or_email
        )
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username/email"
        )

    if user.password != credentials.password:
        raise HTTPException(
            status_code=401,
            detail="Incorrect password"
        )

    return user