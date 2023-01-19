import discord
import os
import string

d = {}

TOKEN =  os.environ.get('DISCORD_TOKEN')

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print("message-->", message)
    
    no_punctuations = str(message.content).translate(str.maketrans('', '', string.punctuation))

    if message.author == client.user:
        return

    if message.content.startswith('hi'):
        await message.channel.send('Hello!')

    msg = no_punctuations.lower().split(" ")
    for i in msg:

        with open("quotes.txt") as f:
            for line in f:
                (key, val) = line.split(":")
                d[(key)] = val

    for key in d:
        if key in msg:
            await message.channel.send((d[key]))

client.run(TOKEN)