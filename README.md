# 2025-12-09-visst-llm
Using LLMs @ VISST

You can find the rendered slides here: <https://chendaniely.github.io/2025-12-09-visst-llm/#/>

## Running code

There are 2 scripts in this repository, `chat.py` and `chat_prompt.py`.

- `chat.py` is a simple script that demonstrates how to use LLMs for chat-based interactions.
- `chat_prompt.py` demonstrates how to use the system prompt

You can run the code with `uv`:

```bash
uv run chat.py
uv run chat_prompt.py
```

With `uv run` you should not need to set up the local environment like we did in the class.
The repository has been set up to do that for you.

Feel free to edit the code and experiment with different prompts and models,
and run the code with `uv run`.

The code was modified to wait for you to paste in an API key (Anthropic by default),
and opens the chat console for you with `chat.console()`,
instead of `chat.chat()`

Feel free to change the `clt.ChatAnthropic` to `clt.ChatOpenAI` or other models supported by `chatlas`.
If you are using [`ChatOllama`](https://posit-dev.github.io/chatlas/reference/ChatOllama.html#chatlas.ChatOllama) or other local models, make sure you have the model downloaded.
These local Ollama models do not need an API key.

You can download Ollama here: <https://ollama.com/> and find models here: <https://ollama.com/search>.
Note the download size for these models, some of them are quite big (200GB+).

I small ollama model you can use is [`qwen3:0.6b`](https://ollama.com/library/qwen3).
You can install it from the ollama app or in the terminal with:

```bash
ollama run qwen3:0.6b
```

You can find a list of all the chatlas models here: <https://posit-dev.github.io/chatlas/reference/#chat-model-providers>
