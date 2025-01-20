from fastapi import APIRouter
from pydantic import BaseModel
import modules.account as account_module
import database

router = APIRouter()
supabase = database.init()


class UserSignup(BaseModel):
    name: str
    username: str
    password: str


@router.post("/user/signup")
def user_signup(user_signup: UserSignup):
    return account_module.signup(user_signup, supabase)


class UserLogin(BaseModel):
    username: str
    password: str


@router.post("/user/login")
def user_login(user_login: UserLogin):
    return account_module.login(user_login, supabase)


class UserUpdateName(BaseModel):
    id: int
    name: str


@router.put("/user/update/name")
def user_update_name(user_update_name: UserUpdateName):
    return account_module.update_name(user_update_name, supabase)


@router.get("/user/{id}/profile")
def user_get(id: int):
    return account_module.get_profile(id, supabase)
