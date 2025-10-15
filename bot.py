# bot.py
import os

import discord
import time

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN').strip()

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# Counts up
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if 'count' in message.content.lower():
        t = 30
        while t >= 0:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            await message.channel.send(timer)
            time.sleep(60)
            t -= 1

        await message.channel.send("Done")

    
        

client.run(TOKEN)