# ChatBot_withChatGPT

A small command-line chatbot that talks to the OpenAI API and keeps the conversation history.

## What it does

Reads what you type, sends the whole conversation to the `gpt-3.5-turbo` model through the Chat Completions API, prints the answer and adds it to the history, so each reply has the context of the earlier messages. Type `sair` to quit.

## Requirements

- Python 3 and an OpenAI API key.
- The `openai` library, version below 1.0. The code uses `openai.ChatCompletion.create`, which was removed in version 1.0 of the library, so with a newer version it needs to be updated to the new client.

## How to run

1. Replace `"xyz"` in `chatbot.py` with your own key. Do not commit a real key; reading it from an environment variable is safer.
2. Run `python chatbot.py` and type your messages.

## Known issue

The function that sends the message stores the API result in `resposta` but returns `response`, so the first call fails with a `NameError`. Renaming one of the two fixes it.

## Notes

A practice project to learn how a chatbot is structured: a message list, a loop and an API call. It has no error handling, no streaming and no limit on history size.
