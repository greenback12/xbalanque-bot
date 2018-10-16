#Xbalanque bot by Senor

import discord
import asyncio
import os

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
    elif content == "!attack":
        await asyncio.sleep(1)
        await client.send_message(message.channel, '@Jamie#9330 \n https://i.imgur.com/isDkwh7.jpg')
    elif content == "!gun":
        await asyncio.sleep(1)
        await client.send_message(message.channel, '@Jamie#9330 \n https://i.imgur.com/wjpnFPQ.jpg')

client.run(os.getenv('TOKEN'))
