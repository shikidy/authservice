from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.shared.config import get_config
from src.views import api_router


load_dotenv(override=False)
config = get_config()

app = FastAPI(
    title="AuthService",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[config.cors_host],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
