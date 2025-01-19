from datetime import datetime
import hash
import validator


def signup(user_signup, supabase) -> dict:
    is_valid_user: dict = validator.user.valid_user(
        name=user_signup.name,
        username=user_signup.username,
        password=user_signup.password,
    )
    if not is_valid_user["ok"]:
        return is_valid_user

    is_unique_username: dict = unique_username(user_signup.username, supabase)
    if not is_unique_username["ok"]:
        return is_unique_username

    try:
        user_signup = get_user_signup_data(user_signup)

        response = supabase.table("users").insert(user_signup.dict()).execute()
        if not response.data:
            return {"ok": False, "message": "Signup failed"}
    except Exception as e:
        return {"ok": False, "message": str(e)}

    return {"ok": True, "message": "Signup successful"}


def unique_username(username: str, supabase) -> dict:
    try:
        response = (
            supabase.table("users").select("id").eq("username", username).execute()
        )
        if response.data:
            return {"ok": False, "message": "Username already exists"}
    except Exception as e:
        return {"ok": False, "message": str(e)}

    return {"ok": True, "message": "Unique username"}


def get_user_signup_data(user_signup: dict) -> dict:
    user_signup.password = hash.hash_password(user_signup.password)

    return user_signup
