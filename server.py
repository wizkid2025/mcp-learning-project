# server.py

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/ping")
async def ping():
    return JSONResponse(content={"message": "pong"}, status_code=200)
