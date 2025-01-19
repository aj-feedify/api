import hash
import validator


def login(user_login, supabase) -> dict:
    is_valid_user: dict = validator.user.valid_user(
        username=user_login.username, password=user_login.password
    )
    if not is_valid_user["ok"]:
        return is_valid_user

    try:
        response = (
            supabase.table("users")
            .select("password")
            .eq("username", user_login.username)
            .execute()
        )
        if not response.data:
            return {"ok": False, "message": "Login failed"}
    except Exception as e:
        return {"ok": False, "message": str(e)}

    hashed_password: str = hash.hash_password(user_login.password)
    if hashed_password != response.data[0]["password"]:
        return {"ok": False, "message": "Invalid credentials"}

    return {"ok": True, "message": "Login successful"}
