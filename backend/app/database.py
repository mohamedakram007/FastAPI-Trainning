import os
import certifi
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.environ.get("MONGO_URI", "mongodb+srv://akrammohamed392005_db_user:<db_password>@cluster3.zakfk2k.mongodb.net/?appName=Cluster3")

client = AsyncIOMotorClient(
    MONGO_URL, 
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=5000
)

db = client["products_db"]

product_collection = db["products"]