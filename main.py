from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", summary="Orion's Nebula Test Connection endpoint")
def state_endpoint():
    return True
