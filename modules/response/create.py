import validator
import repositories


def create(response_create, supabase) -> dict:
    is_valid_response = validator.valid_create_response(
        feed_uid=response_create.feed_uid, text=response_create.text
    )
    if not is_valid_response["ok"]:
        return is_valid_response

    is_feed_exist = repositories.feed.feed_exists(response_create.feed_uid, supabase)
    if not is_feed_exist["ok"]:
        return is_feed_exist

    try:
        response = supabase.table("responses").insert(response_create.dict()).execute()
        if not response.data:
            return {"ok": False, "message": "Response creation failed"}
    except Exception as e:
        return {"ok": False, "message": str(e)}

    return {
        "ok": True,
        "message": "Response created",
        "data": {"uid": response.data[0]["res_uid"]},
    }
