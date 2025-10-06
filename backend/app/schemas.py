from pydantic import BaseModel, EmailStr, validator

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('A senha deve ter no mínimo 8 caracteres')
        if not any(char.isdigit() for char in v):
            raise ValueError('A senha deve conter pelo menos um número')
        if not any(char.isalpha() for char in v):
            raise ValueError('A senha deve conter pelo menos uma letra')
        if len(v.encode('utf-8')) > 72:
            raise ValueError('A senha é muito longa (limite de 72 bytes)')
        return v

class User(BaseModel):
    id: str
    name: str
    email: EmailStr
    score: int
    referral_link: str

    class Config:
        from_attributes = True