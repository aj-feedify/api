import validator


def get(feed_uid: str, supabase) -> dict:
    is_valid_uid = validator.valid_uid(feed_uid)
    if not is_valid_uid["ok"]:
        return is_valid_uid

    try:
        response = (
            supabase.table("feeds")
            .select("user_id, title, text, created_at, updated_at, uid")
            .eq("uid", feed_uid)
            .execute()
        )
        if not response.data:
            return {"ok": False, "message": "Getting feed failed"}
    except Exception as e:
        return {"ok": False, "message": str(e)}

    return {"ok": True, "message": "Feed gotten", "data": response.data[0]}


def get_all(user_id: int, supabase) -> dict:
    is_valid_id = validator.valid_id(user_id)
    if not is_valid_id["ok"]:
        return is_valid_id

    try:
        response = (
            supabase.table("feeds")
            .select("title, created_at, updated_at, uid")
            .eq("user_id", user_id)
            .execute()
        )
        if not response.data:
            return {"ok": False, "message": "Getting feed failed"}
    except Exception as e:
        return {"ok": False, "message": str(e)}

    return {"ok": True, "message": "Feeds gotten", "data": response.data}
