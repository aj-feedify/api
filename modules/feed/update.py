from datetime import datetime
from .get import get
import validator


def update(feed_update, supabase) -> dict:
    is_valid_feed = validator.valid_update_input(
        title=feed_update.new_title,
        text=feed_update.new_text,
        user_id=feed_update.user_id,
        feed_uid=feed_update.feed_uid,
    )
    if not is_valid_feed["ok"]:
        return is_valid_feed

    is_different_input = different_input(feed_update, supabase)
    if not is_different_input["ok"]:
        return is_different_input

    try:
        now = get_cur_date()
        print(feed_update)

        response = (
            supabase.table("feeds")
            .update(
                {
                    "text": feed_update.new_text,
                    "title": feed_update.new_title,
                    "updated_at": now,
                }
            )
            .eq("uid", feed_update.feed_uid)
            .eq("user_id", feed_update.user_id)
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
    try:
        response = (
            supabase.table("feeds")
            .select("title, text")
            .eq("uid", feed_update.feed_uid)
            .execute()
        )
        if not response.data:
            return {"ok": False, "message": "Getting feed failed"}
    except Exception as e:
        return {"ok": False, "message": str(e)}

    is_same = (
        response.data[0]["text"] == feed_update.new_text
        and response.data[0]["title"] == feed_update.new_title
    )

    if is_same:
        return {"ok": False, "message": "Same input"}

    return {"ok": True, "message": "Different input"}


def get_cur_date():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.") + str(
        datetime.now().microsecond
    ).zfill(6)

    return now
