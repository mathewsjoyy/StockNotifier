import slack
import os
from pathlib import Path
from dotenv import load_dotenv # Loads .env file

# Make sure to create a .env file in this directory and store your bot token key
# e.g BOT_TOKEN=olxb-2263408159251-2273468090481-M9MxqfydfsAS1gc9SSf7TJUu
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['BOT_TOKEN']) # Connect to slack bot with token api

client.chat_postMessage(channel='#trade', text="Hello! I'm ready to find that item you really want.")