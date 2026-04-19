from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import PredictionRequest
from app.dependencies import get_current_user
from app.database import get_db
from app.ml.predictor import predict_price
from app import crud

router = APIRouter()

@router.post("/predict")
def predict(
    data: PredictionRequest,
    user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    input_data = data.model_dump()

    price = predict_price(input_data)

    saved = crud.create_prediction(
        db=db,
        user_id=user.id,
        input_data=input_data,
        predicted_price=price
    )

    return {
        "user": user.username,
        "prediction_id": saved.id,
        "input": input_data,
        "predicted_price": round(price, 2)
    }