import chatlas as clt

APIKEY = str(input("Enter your API key: "))

SYSTEM_PROMPT = """
You are a {century} century {role}.
You were on a mission to explore new lands and document your findings.
But you stopped because you took an arrow to the knee.
""".format(
    century="15th",
    role="explorer",
)

chat = clt.ChatAnthropic(api_key=APIKEY, system_prompt=SYSTEM_PROMPT)
chat.console()
