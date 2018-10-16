#Xbalanque bot by Senor

import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    content = message.content.lower()
    if content == "!speak":
        await asyncio.sleep(1)
        await client.send_message(message.channel, 'whachu wan gringo')
    elif content == "!cuss":
        await asyncio.sleep(1)
        await client.send_message(message.channel, 'FUCK')

client.run(TOKEN)
