# Discord Clone

A Discord persona bot created using RAG + Claude API.

## Problem
Updating my team members through Discord messaging can be a tedious, repetitive process, especially when some members neglect to search for previous answers in chats or read through documentation. 

## Approach
To solve this issue while testing my applied LLM engineering skills, I created a Discord clone of myself with my texting style and full documented knowledge of my organization's operations and products.

I did this through the creation of a retrieval-augmented-generation system with access to an export of all my Discord messages. When a user asks the bot a question:

R(etrieval) - ChromaDB grabs the 4 most relevant chunks to the question ![retrieval.py](retrieval.py), which are 500 char pieces of the Discord export doc converted into vectors to be stored in ChromaDB ![index_knowledge.py](index_knowledge.py) (embedding) ,and returns them as a single string to be used as context by the LLM

A(ugmentation) - Building the LLM system prompt using style-example doc, and building the LLM user prompt using the context retrieved from the knowledge-base in the above step + the message directed toward the bot ![augmentation.py](augmentation.py).

G(eneration) - Generating the response message using Haiku 4.5 through Claude API and having the bot send the message using Discord's API.

## Reproducability
### Requires:
- ![Claude API key](https://platform.claude.com/dashboard)
- Discord API key
- 
