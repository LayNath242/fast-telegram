import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
mongo_url = os.getenv("MONGO_URL")
