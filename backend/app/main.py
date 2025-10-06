from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db), referrer_id: Optional[str] = None):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")

    hashed_password = pwd_context.hash(user.password)
    
    new_user = models.User(name=user.name, email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    if referrer_id:
        referrer = db.query(models.User).filter(models.User.id == referrer_id).first()
        if referrer:
            referrer.score += 1
            db.commit()
            db.refresh(referrer)

    new_user.referral_link = f"http://127.0.0.1:5500/frontend/index.html?ref={new_user.id}"
    
    return new_user

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: str, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    db_user.referral_link = f"http://127.0.0.1:5500/frontend/index.html?ref={db_user.id}"
    
    return db_user