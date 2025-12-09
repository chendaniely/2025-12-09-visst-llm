import os
import chatlas as clt
from dotenv import load_dotenv

load_dotenv()

chat = clt.ChatAnthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    system_prompt=clt.interpolate_file(
        "code/prompt.md",
        variables={"role": "Yoda"},
    ),
)
chat.chat("what is the capital of the moon?")
