from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://feedify-id.web.app"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "OPTIONS"],
    allow_headers=["*"],
)
app.include_router(routes.user_routes.router)
