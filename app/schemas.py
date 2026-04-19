from pydantic import BaseModel
from typing import Literal

class LoginRequest(BaseModel):
    username: str
    password: str


class PredictionRequest(BaseModel):
    size: float
    rooms: int
    year_built: int
    location: Literal["city", "suburb", "rural"]
    condition: Literal["poor", "fair", "good", "excellent"]