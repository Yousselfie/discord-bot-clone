# Discord Clone

A Discord persona bot created using RAG + Claude API.

## Problem
Updating my team members through Discord messaging can be a tedious, repetitive process, especially when some members neglect to search for previous answers in chats or read through documentation. 

## Approach
To solve this issue while testing my applied LLM engineering skills, I created a Discord clone of myself with my texting style and full documented knowledge of my organization's operations and products.

I did this through the creation of a retrieval-augmented-generation system with access to an export of all my Discord messages. When a user mentions the bot in the server:

**R(etrieval)** - ChromaDB grabs the 4 most relevant chunks to the question ![retrieval.py](retrieval.py), which are 500 char pieces of the Discord export doc converted into vectors to be stored in ChromaDB ![index_knowledge.py](index_knowledge.py) (embedding) ,and returns them as a single string to be used as context by the LLM

**A(ugmentation)** - Building the LLM system prompt using style-example doc, and building the LLM user prompt using the context retrieved from the knowledge-base in the above step + the message directed toward the bot ![augmentation.py](augmentation.py).

**G(eneration)** - Generating the response message using Haiku 4.5 through Claude API and having the bot send the message using Discord's API ![bot.py](bot.py).

## Reproduceability
### Prerequisites
- Python 3.10+
- [Poetry](https://python-poetry.org/) for dependency management
- A **Discord bot token** ([Discord Developer Portal](https://discord.com/developers/applications))
- An **Anthropic API key** ([console.anthropic.com](https://console.anthropic.com/)) 
	- Ensure you set your Anthropic API key as an environment variable ([Anthropic Docs])(https://platform.claude.com/docs/en/get-api-key)

1. Clone the repo: 
```
git clone git@github.com:Yousselfie/discord-bot-clone.git
```
2. Install dependencies: 
```
cd discord-bot-clone
poetry install
```
3. Add your own knowledge base to the project:
Login to Discord -> Go to **User Settings** -> Select **Data & Privacy** -> **Request my data** -> Check **Messages** -> Await an email from Discord with a download link -> Move the downloaded export folder into the project root directory. 

4. Extract your texting style:
```
python extract_style.py
```

5. Create a new application in [Discord Developer Portal], go to **Bot** settings, set the **Send Messages** permission, and copy the **Token**.

6. Go to **OAuth2** in your Discord Developer application's settings -> Check **Bot** under **Scopes** -> Check **Send Messages** under **Bot Permissions** -> Copy the **Generated URL** and paste it into your browser to follow the steps to invite the bot to your desired Discord server.

7. Uncomment 
```
#client.run("BOT TOKEN GOES HERE")
```
in ![bot.py](bot.py), and replace the placeholder text with the **Token** you copied in step 5.

8. Run the bot
```
python bot.py
``` 
