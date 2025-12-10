import chatlas as clt

APIKEY = str(input("Enter your API key: "))

chat = clt.ChatAnthropic(api_key=APIKEY)
chat.console()
