import os
import certifi
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.environ.get("MONGO_URI", "mongodb+srv://akrammohamed392005_db_user:akrammohamed392005@cluster1.hthsc2h.mongodb.net/?appName=Cluster1")

client = AsyncIOMotorClient(
    MONGO_URL, 
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=5000
)

db = client["products_db"]

product_collection = db["products"]