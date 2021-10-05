import discord
import json as js

PREFIX = "$mc"

with open("token.json", "r") as js_file:
    creds = js.load(js_file)

token = creds['token']

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(msg):
    print(msg)
    if (msg.content.startswith(PREFIX)):
        print("Burger")
        await msg.channel.send("From the bot!")
    #print(f"This is the message given: {msg}")
    

client.run(token)
