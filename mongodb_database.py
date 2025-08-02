from pymongo import MongoClient
from dotenv import load_dotenv
import os 

load_dotenv()

MONGODB_USER = os.getenv("MONGODB_USER")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_CLUSER = os.getenv("MONGODB_CLUSER")

MONGO_URL = f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_CLUSER}/?retryWrites=true&w=majority&appName=Cluster"

mongodb_client = MongoClient(MONGO_URL)