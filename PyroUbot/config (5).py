import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "20"))

DEVS = list(map(int, os.getenv("DEVS", "7524271223").split()))

API_ID = int(os.getenv("API_ID", "21756016"))

API_HASH = os.getenv("API_HASH", "4a48374f0fd3549af86a7e5fba563b8f")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7822314667:AAGpsnA0ePJbfAynO-0evSXNH8uOYd_2F7Q")

OWNER_ID = int(os.getenv("OWNER_ID", "6621603339"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002718575966 -1002053287763 -1002044997044 -1002022625433 -1002050846285").split()))

RMBG_API = os.getenv("RMBG_API", "cdda26fd6b87e7fb35f1b8d0d28d7cd6")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://zan:zan@cluster0.epnnx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002718575966"))

