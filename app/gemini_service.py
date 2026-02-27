import os
from google import genai
from google.genai import types

client = genai.Client(
    api_key="AIzaSyATqjmzG6b4_Gp9lrxcRkznqlnG1zEgwUw",
)

MODEL = "gemini-3-flash-preview"

def stream_response(user_message: str):
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_message)],
        ),
    ]

    config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="HIGH",
        )
    )

    for chunk in client.models.generate_content_stream(
        model=MODEL,
        contents=contents,
        config=config,
    ):
        if chunk.text:
            yield chunk.text