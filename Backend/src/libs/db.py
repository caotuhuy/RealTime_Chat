from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Đọc file .env
load_dotenv()

# Lấy URI từ .env
MONGO_URI = os.getenv("MONGO_URI")

client = None
db = None


def connect_db():
    global client, db

    try:
        client = MongoClient(MONGO_URI)

        # Kiểm tra kết nối
        client.admin.command("ping")

        # Chọn database
        db = client.get_database()

        print("Kết nối MongoDB thành công")

    except Exception as error:
        print(f"Lỗi kết nối MongoDB: {error}")
        raise