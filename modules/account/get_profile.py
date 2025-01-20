import validator


def get_profile(id: int, supabase) -> dict:
    is_valid_id: dict = validator.user.valid_id(id=id)
    if not is_valid_id["ok"]:
        return is_valid_id

    try:
        response = (
            supabase.table("users")
            .select("name, username, joined_at")
            .eq("id", id)
            .execute()
        )

        if not response.data:
            return {"ok": False, "message": "User not found"}
    except Exception as e:
        return {"ok": False, "message": str(e)}

    return {"ok": True, "data": response.data[0]}
