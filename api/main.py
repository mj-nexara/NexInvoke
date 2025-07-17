from fastapi import FastAPI, Request
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env variables

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_ENDPOINT = "https://api.openai.com/v1/chat/completions"

@app.post("/invoke")
async def invoke_ai(req: Request):
    data = await req.json()
    user_input = data["message"]

    response = requests.post(
        OPENAI_ENDPOINT,
        headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
        json={
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": user_input}]
        }
    )

    return response.json()
