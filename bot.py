from anthropic import Anthropic
import discord

from retrieval import retrieve
from augmentation import build_system_prompt, build_user_prompt

client = discord.Client(intents=discord.Intents(messages=True, message_content=True, guilds=True))
llm = Anthropic()

#load the texting style examples on startup
with open("style_example.txt", encoding="utf-8") as f:
    raw = f.read().splitlines()
style_examples = "\n".join(f"<example>{m}</example>" for m in raw)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if client.user.mentioned_in(message):
        context = retrieve(message.content) #Fetching the top relevant chunks from my RAG function
        prompt = build_user_prompt(message.content, context)
        resp = llm.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=300,
            system=build_system_prompt(style_examples),
            messages=[{"role":"user", "content": build_user_prompt(message.content, context)}]
        )
        await message.channel.send(resp.content[0].text)

#client.run("BOT TOKEN GOES HERE") 