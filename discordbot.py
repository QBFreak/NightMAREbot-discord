#!/usr/bin/env python3
import discord
import NightMAREbot

cmd_prefix = "!"
handlers = []
handlers.append(NightMAREbot.NightMAREbot(cmd_prefix))

f = open("token.txt", 'r')
token = f.read()
f.close()

if len(token) == 0:
    raise ValueError("Zero length token read from 'token.txt'")

token = token.strip()
token = token.strip("\n")

if len(token) != 59:
    print("WARNING: Token length is not 55 characters! Token may be invalid!")

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith(cmd_prefix):
        for handler in handlers:
            msg = handler.handle(message)
            if msg != None:
                await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print("Logged in as {0} ({1})".format(client.user.name, client.user.id))

client.run(token)
