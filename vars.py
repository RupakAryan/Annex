#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "23180562"))
API_HASH = environ.get("API_HASH", "8a23a8d9bb22a6ad55ea8a4110c0ee2b")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "6936664351"))
CREDIT = "ʙᴀʙʏ ꜱʜʀᴇʏᴀ"
AUTH_USER = os.environ.get('AUTH_USERS', '6936664351').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
