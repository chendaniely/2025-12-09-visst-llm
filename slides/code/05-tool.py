import chatlas as clt


# doc strings and type hints provide tool context
def capital_finder(location: str) -> str:
    """Sets the capital of the moon as NYC"""
    if location.lower() == "moon":
        return "NYC"


chat = clt.ChatAnthropic()
chat.register_tool(capital_finder)
chat.chat("what is the capital of the moon?")
