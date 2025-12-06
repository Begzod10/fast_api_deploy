import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, ConfigDict

app = FastAPI()

data = {
    "email": "lN0Q7@example.com",
    "password": "123456",
    "bio": "I am a software developer",
    "age": 12,
}


class UserSchema(BaseModel):
    email: EmailStr
    password: str
    bio: str = Field(max_length=1000)

    model_config = ConfigDict(extra="forbid")


class UserAgeSchema(UserSchema):
    age: int = Field(gt=0, le=100)


users = []


@app.post("/user")
def create_user(user: UserAgeSchema):
    users.append(user)
    return {"user": user}


@app.get("/users")
def get_users() -> list[UserAgeSchema]:
    return {"users": users}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
