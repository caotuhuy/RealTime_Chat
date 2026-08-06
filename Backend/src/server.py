from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Đọc file .env
load_dotenv()

app = FastAPI()

PORT = int(os.getenv("PORT", 3000))

@app.get("/")
def home():
    return {"message": "Chat App Backend đang chạy"}