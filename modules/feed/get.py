import validator


def get(user_id: int, feed_uid: str, supabase) -> dict:
    is_valid_get_input = validator.valid_get_input(user_id, feed_uid)
    if not is_valid_get_input["ok"]:
        return is_valid_get_input

    try:
        response = (
            supabase.table("feeds")
            .select("title, text, created_at, updated_at, uid")
            .eq("user_id", user_id)
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
            .select("title, text, created_at, updated_at, uid")
            .eq("user_id", user_id)
            .execute()
        )
        if not response.data:
            return {"ok": False, "message": "Getting feed failed"}
    except Exception as e:
        return {"ok": False, "message": str(e)}

    return {"ok": True, "message": "Feeds gotten", "data": response.data}
