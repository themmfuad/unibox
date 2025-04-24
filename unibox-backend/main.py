from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCred(BaseModel):
    username: str
    password: str

@app.post('/login')
async def login(cred: UserCred):
    username = cred.username
    password = cred.password
    
    return {"username":username, "pass":password}
