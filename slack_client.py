import slack
import os
from pathlib import Path
from dotenv import load_dotenv # Loads .env file

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['BOT_TOKEN']) # Connect to slack bot with token api

client.chat_postMessage(channel='#trade', text="Hello I'm ready to find a GPU for you!")