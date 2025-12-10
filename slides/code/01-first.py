import os
import chatlas as clt
from dotenv import load_dotenv

load_dotenv()  # this loads the variables from .env

chat = clt.ChatAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
chat.chat("what is the capital of the moon?")
