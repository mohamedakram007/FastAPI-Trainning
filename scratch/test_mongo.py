import asyncio
import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://akrammohamed392005_db_user:akrammohamed392005@cluster1.hthsc2h.mongodb.net/?appName=Cluster1"

async def test_connection():
    print(f"Connecting to {MONGO_URL}...")
    try:
        client = AsyncIOMotorClient(MONGO_URL, serverSelectionTimeoutMS=5000, tlsAllowInvalidCertificates=True)
        # The ismaster command is cheap and does not require auth.
        await client.admin.command('ismaster')
        print("MongoDB connection successful!")
        
        db = client["products_db"]
        collection = db["products"]
        count = await collection.count_documents({})
        print(f"Number of products: {count}")
        
    except Exception as e:
        print(f"MongoDB connection failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_connection())
