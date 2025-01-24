from datetime import datetime
from .get import get
import validator


def update(feed_update, supabase) -> dict:
    is_valid_feed = validator.valid_update_input(
        text=feed_update.new_text,
        user_id=feed_update.user_id,
        feed_id=feed_update.feed_id,
    )
    if not is_valid_feed["ok"]:
        return is_valid_feed

    is_different_input = different_input(feed_update, supabase)
    if not is_different_input["ok"]:
        return is_different_input

    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.") + str(
            datetime.now().microsecond
        ).zfill(6)

        response = (
            supabase.table("feeds")
            .update({"text": feed_update.new_text, "updated_at": now})
            .eq("user_id", feed_update.user_id)
            .eq("feed_id", feed_update.feed_id)
            .execute()
        )
        if not response.data:
            return {"ok": False, "message": "Feed update failed"}
    except Exception as e:
        return {"ok": False, "message": str(e)}

    return {
        "ok": True,
        "message": "Feed updated",
        "data": {
            "uid": response.data[0]["uid"],
        },
    }


def different_input(feed_update, supabase) -> dict:
    feed_data = get(feed_update.user_id, feed_update.feed_id, supabase)
    if feed_data["ok"] and feed_data["data"]["text"] == feed_update.new_text:
        return {"ok": False, "message": "Same input"}

    return {"ok": True, "message": "Different input"}
