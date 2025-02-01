from fastapi import APIRouter
from pydantic import BaseModel
import modules.response as response_module
import database

router = APIRouter()
supabase = database.init()


class ResponseCreate(BaseModel):
    feed_uid: str
    text: str


@router.post("/response/create")
def response_create(response_create: ResponseCreate):
    return response_module.create(response_create, supabase)


@router.get("/response/{feed_uid}/all")
def response_get(feed_uid: str):
    return response_module.get_all(feed_uid, supabase)
