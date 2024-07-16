from pydantic import BaseModel,Field,EmailStr

class UserSchema(BaseModel):
    email: str
    full_name: str
    password: str

    class Config:
        schema_extra = {
            'example': {
                "fullname": "Rimma",
                "email": "rimma@gmail.com",
                "password": "admin"
            }
        }

class UserLoginSchema(BaseModel):
    email: str
    password: str

    class Config:
        schema_extra = {
            'example':{
                "email": "rimma@gmail.com",
                "password": "admin"
            }
        }

class PostSchema(BaseModel):
    email: str
    password: str

    class Config:
        schema_extra = {
            'example':{
                "email": "rimma@gmail.com",
                "password": "admin"
            }
        }
        