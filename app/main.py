from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from app.gemini_service import stream_response
import os

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

# 🔥 THIS PART IS CRITICAL FOR RENDER
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)