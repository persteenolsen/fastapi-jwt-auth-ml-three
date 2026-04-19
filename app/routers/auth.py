from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import LoginRequest
from ..database import get_db
from .. import crud
from ..auth import hash_password, verify_password, create_token

router = APIRouter()

# 19-04-2026 - Registration endpoint is currently disabled to prevent abuse in production at Vercel. 
# You can enable it by uncommenting the decorator and the function.
# @router.post("/register")
def register(req: LoginRequest, db: Session = Depends(get_db)):
    existing = crud.get_user_by_username(db, req.username)
    if existing:
        raise HTTPException(400, "User already exists")

    user = crud.create_user(
        db,
        req.username,
        hash_password(req.password)
    )

    return {"message": "User created", "user_id": user.id}


@router.post("/login")
def login(req: LoginRequest, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, req.username)

    if not user or not verify_password(req.password, user.hashed_password):
        raise HTTPException(401, "Bad credentials")

    token = create_token(user.id, user.username)
    return {"token": token}