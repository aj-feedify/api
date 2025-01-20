from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import database
import modules

app = FastAPI()
supabase = database.init()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://feedify-id.web.app"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "OPTIONS"],
    allow_headers=["*"],
)


class UserSignup(BaseModel):
    name: str
    username: str
    password: str


@app.post("/user/signup")
def user_signup(user_signup: UserSignup):
    return modules.account.signup(user_signup, supabase)


class UserLogin(BaseModel):
    username: str
    password: str


@app.post("/user/login")
def user_login(user_login: UserLogin):
    return modules.account.login(user_login, supabase)


class UserUpdateName(BaseModel):
    id: int
    name: str


@app.put("/user/update/name")
def user_update_name(user_update_name: UserUpdateName):
    return modules.account.update_name(user_update_name, supabase)


@app.get("/user/{id}/profile")
def user_get(id: int):
    return modules.account.get_profile(id, supabase)
