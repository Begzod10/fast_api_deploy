from fastapi import FastAPI, HTTPException, Response, Depends
from fastapi.responses import RedirectResponse
from authx import AuthX, AuthXConfig
from pydantic import BaseModel

app = FastAPI()

config = AuthXConfig()
config.JWT_SECRET_KEY = 'secret'
config.JWT_ACCESS_COOKIE_NAME = 'access_token'
config.JWT_TOKEN_LOCATION = ['cookies']

security = AuthX(config=config)


class UserLogin(BaseModel):
    username: str
    password: str


@app.post('/login')
async def login(credentials: UserLogin, response: Response):
    if credentials.username != 'string' or credentials.password != 'string':
        raise HTTPException(status_code=401, detail='Invalid credentials')
    else:
        access_token = security.create_access_token(uid="123")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, access_token)

        return {'access_token': access_token}


@app.get('/protected', dependencies=[Depends(security.access_token_required)])
async def protected():
    return {'message': 'This is a protected route'}
