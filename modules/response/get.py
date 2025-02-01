import validator


def get_all(feed_uid: str, supabase) -> dict:
    is_feed_uid_valid = validator.feed.valid_uid(feed_uid)
    if not is_feed_uid_valid["ok"]:
        return is_feed_uid_valid

    try:
        response = (
            supabase.table("responses")
            .select("text, created_at, updated_at")
            .eq("feed_uid", feed_uid)
            .execute()
        )
        if response.data is None:
            return {"ok": False, "message": "Getting responses failed"}
        elif not response.data:
            return {"ok": True, "message": "No responses found", "data": []}
    except Exception as e:
        return {"ok": False, "message": str(e)}

    return {"ok": True, "message": "Responses gotten", "data": response.data}
