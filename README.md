# Study Buddy: AI Study Assistant Chatbot

A chatbot that acts as a friendly tutor, built with Python and Ollama (Llama 3.2) running locally.

## Features
- Conversation memory: the full chat history is stored in a list and sent to the model on every turn
- A system prompt that makes the model behave like a tutor
- Answers from my own notes (`notes.txt`), a simple form of RAG

## Note
I did not train the model. I used the pre-trained Llama 3.2 model through Ollama and built the application around it.

## How to Run
1. Install Ollama from ollama.com
2. `ollama pull llama3.2`
3. `pip install ollama`
4. `python study_buddy.py` (keep `notes.txt` in the same folder)
5. Type `exit` to quit

## Tools
Python, Ollama, Llama 3.2
