from fastapi import APIRouter
from pydantic import BaseModel
import modules.feed as feed_module
import database

router = APIRouter(tags=["feed"])
supabase = database.init()


class FeedCreate(BaseModel):
    title: str
    text: str
    user_id: int


@router.post("/feed/create")
def feed_create(feed_create: FeedCreate):
    return feed_module.create(feed_create, supabase)


@router.get("/feed/{feed_uid}")
def feed_get(feed_uid: str):
    return feed_module.get(feed_uid, supabase)


@router.get("/feed/{user_id}/all")
def feed_get(user_id: int):
    return feed_module.get_all(user_id, supabase)


class FeedUpdate(BaseModel):
    user_id: int
    feed_uid: str
    new_title: str
    new_text: str


@router.put("/feed/update")
def feed_update(feed_update: FeedUpdate):
    return feed_module.update(feed_update, supabase)
