import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "7524271223").split()))

API_ID = int(os.getenv("API_ID", "21756016"))

API_HASH = os.getenv("API_HASH", "cdda26fd6b87e7fb35f1b8d0d28d7cd6")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7953704617:AAH0ji8VAyWZq-vV9lQNF7SC3S6VnSTk0FY")

OWNER_ID = int(os.getenv("OWNER_ID", "7364797603"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002718575966").split()))

RMBG_API = os.getenv("RMBG_API", "")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://familyayanh:familyayanh@cluster0.jlrozly.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002766933065"))

