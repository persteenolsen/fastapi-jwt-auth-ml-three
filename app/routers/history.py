from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user
from app import crud

router = APIRouter()


@router.get("/history")
def get_history(
    user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    predictions = crud.get_user_predictions(db, user.id)

    return [
        {
            "id": p.id,
            "input_data": p.input_data,
            "predicted_price": p.predicted_price
        }
        for p in predictions
    ]