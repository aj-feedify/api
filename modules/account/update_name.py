import validator


def update_name(user_update_name, supabase):
    is_valid_user: dict = validator.valid_user(
        id=user_update_name.id, name=user_update_name.new_name
    )
    if not is_valid_user["ok"]:
        return is_valid_user

    try:
        response = (
            supabase.table("users")
            .update({"name": user_update_name.new_name})
            .eq("id", user_update_name.id)
            .execute()
        )
        if not response.data:
            return {"ok": False, "message": "Name update failed"}
    except Exception as e:
        return {"ok": False, "message": str(e)}

    return {"ok": True, "message": "Name updated successfully"}
