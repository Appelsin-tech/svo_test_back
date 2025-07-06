from fastapi import FastAPI
from app.routes import api
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=[
		"http://localhost:5173",  # dev
		"http://localhost:8080",  # docker
	],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.include_router(api.router)
