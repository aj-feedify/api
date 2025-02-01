import validator


def feed_exists(feed_uid: str, supabase) -> dict:
    is_valid_uid = validator.feed.valid_uid(feed_uid)
    if not is_valid_uid["ok"]:
        return is_valid_uid

    try:
        response = supabase.table("feeds").select("uid").eq("uid", feed_uid).execute()
        if not response.data:
            return {"ok": False, "message": "Getting feed failed"}
    except Exception as e:
        return {"ok": False, "message": str(e)}

    if response.data[0].get("uid") != feed_uid:
        return {"ok": False, "message": "Feed does not exist"}

    return {"ok": True, "message": "Feed gotten", "data": response.data[0]}
