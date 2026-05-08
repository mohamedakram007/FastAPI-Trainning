import os
import certifi
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.environ.get("MONGO_URI", "mongodb+srv://akram:Akram@123@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

client = AsyncIOMotorClient(
    MONGO_URL, 
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=5000
)

db = client["products_db"]

product_collection = db["products"]