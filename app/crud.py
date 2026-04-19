from sqlalchemy.orm import Session
from app.models import User, Prediction


# -----------------------------
# USERS
# -----------------------------
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, username: str, hashed_password: str):
    user = User(username=username, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# -----------------------------
# PREDICTIONS
# -----------------------------
def create_prediction(db: Session, user_id: int, input_data: dict, predicted_price: float):
    prediction = Prediction(
        user_id=user_id,
        input_data=input_data,
        predicted_price=predicted_price
    )
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction


def get_user_predictions(db: Session, user_id: int):
    return (
        db.query(Prediction)
        .filter(Prediction.user_id == user_id)
        .order_by(Prediction.id.desc())
        .all()
    )