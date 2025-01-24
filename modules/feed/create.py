import validator
import gen_jwt


def create(feed_create, supabase) -> dict:
    is_valid_feed = validator.valid_feed(text=feed_create.text, id=feed_create.user_id)
    if not is_valid_feed["ok"]:
        return is_valid_feed

    try:
        response = supabase.table("feeds").insert(feed_create.dict()).execute()
        if not response.data:
            return {"ok": False, "message": "Feed creation failed"}
    except Exception as e:
        return {"ok": False, "message": str(e)}

    id = gen_jwt.generate_jwt(response.data[0]["feed_id"])

    return {
        "ok": True,
        "message": "Feed created",
        "data": {"id": id, "uid": response.data[0]["uid"]},
    }
