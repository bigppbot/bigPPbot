#!/usr/bin/env python3
import discord
import random

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Anime"))


#MEGNUMIN! etc...
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('MEGNUMIN!'):
        await message.channel.send("", file=discord.File('gifs/megnumin.gif', 'boom.gif'));return

    if message.content.startswith('EVA-01!'):
        await message.channel.send("", file=discord.File('gifs/eva01.gif', 'rip.gif'));return

    if message.content.startswith('YES!'):
        await message.channel.send("", file=discord.File('gifs/yes.gif', 'yes.gif'));return

    if message.content.startswith('ZA WARUDO!'):
        await message.channel.send("", file=discord.File('gifs/zawarudo.gif', 'zawarudo.gif'));return

    if message.content.startswith('MUDA!'):
        await message.channel.send("", file=discord.File('gifs/muda.gif', 'muda.gif'));return

    if message.content.startswith('~porn') or message.content.startswith('~hentai'):
        await message.channel.send('No. Go die in a hole!');return

    if message.content.startswith('~pp'):
        await message.channel.send('PP stands for PowerPoints, you fucking degenerate!');return

    if message.content.startswith('good bot'):
        await message.channel.send('aaw thank you ^^');return

    if message.content.startswith('ONE! TWO! SEVEN! THREE!') or message.content.startswith('1! 2! 7! 3!'):
        rfs_texts = ["Dafuq is reality?", "Red is on a killing spree!", "Quarantine is killing me!", "I am failing chemistry!", "Noone has ever loved me...", "My wifu is in love with me?", "You are just as gay as me!", "The stupid kid is going REEE!", "All anime should be free!"]
        await message.channel.send(random.choice(rfs_texts));return

    if message.content.startswith('~help'):
        await message.channel.send('**Discord "Commands"**\n\n`ONE! TWO! SEVEN! THREE!` or `1! 2! 7! 3!`\nBots responds with _funny-ish_ extension of the sentence.\n\n`MEGNUMIN!`\nGet a "megnumin blows shit up" GIF.\n\n`EVA-01!`\nA GIF of EVA-01 stabbing the shit out of an angel.\n\n`YES!`\nThe "YES! YES! YES! YES!" GIF.\n\n`MUDA!`\nLike "YES!" but with "MUDA!".\n\n`~porn` or `~hentai`\nBot just gets pissed of at your stupid request.\n\n`~pp`\nBot explains its name.\n\n`good bot`\nBot is happy.');return

    if message.content.startswith('~'):
        await message.channel.send('Am i too stupid to understand this command? Maybe try ~help.');return

#    if message.content.startswith(''):
#        await message.channel.send('');return


tokenfile = open("token.txt", "r")
token = tokenfile.read()
tokenfile.close()
client.run(token)
