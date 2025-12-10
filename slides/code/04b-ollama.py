import chatlas as clt

chat = clt.ChatOllama(model="qwen3:0.6b")  # 523mb
chat.chat("what is the capital of the moon?")
