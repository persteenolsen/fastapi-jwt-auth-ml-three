# 🏠 v3 - House Price Prediction API (FastAPI + JWT + ML)

Last updated:

- 19-04-2026

A production-style Machine Learning API built with FastAPI, JWT authentication, PostgreSQL (Neon), SQLAlchemy, and Alembic migrations.

---

# 🚀 Features

- JWT authentication
- FastAPI REST API
- ML model (scikit-learn pipeline)
- PostgreSQL (Neon)
- SQLAlchemy ORM
- Alembic migrations
- User prediction history
- Clean modular architecture

---

# 🧱 Project Structure

fastapi-jwt-auth-ml-three/
│
├── app/                      # Main FastAPI application
│   │
│   ├── main.py              # App entry point
│   ├── database.py          # DB connection + session
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # Database operations
│   ├── auth.py              # JWT logic (token creation/validation)
│   ├── dependencies.py      # Shared dependencies (DB, auth)
│   │
│   ├── routers/             # API route modules
│   │   ├── auth.py          # /login endpoint
│   │   ├── predict.py       # /predict endpoint
│   │   └── history.py       # /history endpoint
│   │
│   └── ml/                  # Inference layer (used by API)
│       ├── predictor.py     # Loads model + makes predictions
│       └── model.pkl        # Trained ML model
│
├── ml/                      # Training pipeline (offline)
│   ├── train.py             # Model training script
│   └── housing_v2.csv       # Training dataset
│
├── alembic/                 # Database migrations
├── alembic.ini              # Alembic config
│
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
│
└── README.md

---

# ⚙️ Installation

## 1. Clone repository

git clone <your-repo-url>
cd fastapi-jwt-auth-ml-three

---

## 2. Create virtual environment

Create the virtual environment:
python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

## 3. Install dependencies

pip install -r requirements.txt

---

# 🔐 Environment variables (.env)

DATABASE_URL=postgresql://user:password@your-neon-host.neon.tech/dbname?sslmode=require
SECRET_KEY=your_secret_key

---

# 🧠 Train ML model

python ml/train.py

This generates:
ml/model.pkl

---

# 🚀 Run database migrations (Alembic)

alembic revision --autogenerate -m "init"
alembic upgrade head

---

# ▶️ Run API

uvicorn app.main:app --reload

API runs at:
http://127.0.0.1:8000

---

# 📡 API Endpoints

## Login
POST /login

{
  "username": "admin",
  "password": "1234"
}

---

## Predict
POST /predict
Authorization: Bearer <token>

{
  "size": 140,
  "rooms": 4,
  "year_built": 2005,
  "location": "suburb",
  "condition": "good"
}

---

## History
GET /history
Authorization: Bearer <token>

---

# 🧠 Tech Stack

FastAPI  
PostgreSQL (Neon)  
SQLAlchemy  
Alembic  
scikit-learn  
pandas  
PyJWT  
Uvicorn  

---

# 📈 What this project demonstrates

- ML deployment architecture
- JWT authentication
- PostgreSQL persistence
- Database migrations
- Modular backend design

---

# 🚀 Future improvements

- timestamps
- pagination
- user registration (disabled for Vercel)
- Docker deployment
- frontend dashboard

---

# 👨‍💻 Author

Learning project for combining ML + backend engineering with FastAPI