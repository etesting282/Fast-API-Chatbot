from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from app.gemini_service import stream_response

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    return StreamingResponse(
        stream_response(req.message),
        media_type="text/plain"
    )

# Serve frontend
app.mount("/", StaticFiles(directory="static", html=True), name="static")