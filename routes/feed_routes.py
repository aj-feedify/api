from fastapi import APIRouter
from pydantic import BaseModel
import modules.feed as feed_module
import database

router = APIRouter()
supabase = database.init()


class FeedCreate(BaseModel):
    title: str
    text: str
    user_id: int


@router.post("/feed/create")
def feed_create(feed_create: FeedCreate):
    return feed_module.create(feed_create, supabase)


@router.get("/feed/{user_id}/{feed_identifier}")
def feed_get(user_id: int, feed_identifier: str):
    if feed_identifier == "all":
        return feed_module.get_all(user_id, supabase)
    try:
        return feed_module.get(user_id, feed_identifier, supabase)
    except ValueError:
        return {"ok": False, "message": "Invalid feed identifier"}


class FeedUpdate(BaseModel):
    user_id: int
    feed_id: int
    new_title: str
    new_text: str


@router.put("/feed/update")
def feed_update(feed_update: FeedUpdate):
    return feed_module.update(feed_update, supabase)
