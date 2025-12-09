import os

import chatlas as clt
from dotenv import load_dotenv

load_dotenv()

# GITHUB_TOKEN
# GITHUB_API_KEY
chat = clt.ChatGithub(api_key=os.getenv("GITHUB_TOKEN"))
chat.chat("what is the capital of the moon?")
