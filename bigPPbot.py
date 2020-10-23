#!/usr/bin/env python3
import discord
import random

client = discord.Client()

global stoopid
stoopid = 0


#Gives welcome message, and sets status to "Watching Anime"
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Anime"))


#Executes on message recieved. Commands go here
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    global stoopid

    oldstoopid = stoopid
    stoopid = 0

    if message.content.upper() == 'MEGNUMIN!': #The megnumin GIF
        await message.channel.send("", file=discord.File('gifs/megnumin.gif', 'boom.gif'));return

    if message.content.upper() == 'EVA-01!': #The "EVA-01 Stabs shit" GIF
        await message.channel.send("", file=discord.File('gifs/eva01.gif', 'rip.gif'));return

    if message.content.upper() == 'YES!' or message.content.startswith('YES!'): #The YES! YES! YES! GIF
        await message.channel.send("", file=discord.File('gifs/yes.gif', 'yes.gif'));return

    if message.content.upper() == 'NO!' or message.content.startswith('NO'):
        await message.channel.send("", file=discord.File('gifs/no.gif', 'no.gif'));return

    if message.content.upper() == 'ZA WARUDO!': #The ZA WARUDO! GIF
        await message.channel.send("", file=discord.File('gifs/zawarudo.gif', 'zawarudo.gif'));return

    if message.content.upper() == 'MUDA!' or message.content.startswith('MUDA'): #The MUDA MUDA... GIF
        await message.channel.send("", file=discord.File('gifs/muda.gif', 'muda.gif'));return

    if message.content.lower() == '~porn' or message.content.lower() == '~hentai': #Just in case someone tries this
        pissed_texts = ['No. Go die in a hole!','Go to horny jail!','The one of your mom?','Try a direct EVA entry!','I hope you step on a LEGO brick!',"Ask your GF/BF. Oh wait you don't have one! *fucking looser*"]
        await message.channel.send(random.choice(pissed_texts));return

    if message.content.lower() == '~pp': #If someone asks about the bot name
        await message.channel.send('PP stands for PowerPoints, you fucking degenerate!');return

    if message.content.lower() == 'good bot': #Bots need feelings too
        await message.channel.send('aaw thank you ^^');return

    if message.content.upper() == 'ONE! TWO! SEVEN! THREE!' or message.content == '1! 2! 7! 3!': #The Rockefeller Street joke thing
        rfs_texts = ["Dafuq is reality?", "Red is on a killing spree!", "Quarantine is killing me!", "I am failing chemistry!", "Noone has ever loved me...", "My wifu is in love with me?", "You are just as gay as me!", "The stupid kid is going REEE!", "All anime should be free!"]
        await message.channel.send(random.choice(rfs_texts));return

    if message.content.lower() == '~help': #Well the hep command (duh)
        await message.channel.send('**Discord "Commands"**\n\n`ONE! TWO! SEVEN! THREE!` or `1! 2! 7! 3!`\nBots responds with _funny-ish_ extension of the sentence.\n\n`MEGNUMIN!`\nGet a "megnumin blows shit up" GIF.\n\n`EVA-01!`\nA GIF of EVA-01 stabbing the shit out of an angel.\n\n`YES!`\nThe "YES! YES! YES! YES!" GIF.\n\n`NO!`\nThe "NO! NO! NO!" GIF.\n\n`MUDA!`\nLike "YES!" but with "MUDA!".\n\n`~porn` or `~hentai`\nBot just gets pissed of at your stupid request.\n\n`~pp`\nBot explains its name.\n\n`good bot`\nBot is happy.\n\n`am i stupid?`\nbot answers your question.\n\n`UwU`or `OwO`\n Another GIF it is\n\n`~dice`\nRoll the dice\n\n`shinji`\ni hope he gets in the fucking robot...\n\n`~beer`\nMisato enjoys some beer.\n\n`~energy`\nLike beer but with energy drink\n\n`~sourcecode`\ngives you the bots sourcecode');return

    if message.content.lower() == '~toast': #Inside joke with my friends
        await message.channel.send("Who told you?", file=discord.File('pics/inbread.jpg', 'inbread.jpg'));return

    if message.content.lower() == 'honigsandwich?' or message.content.lower() == 'honigsandwich': #Also an inside joke
        await message.channel.send("Honigsandwich!", file=discord.File('gifs/honig.gif', 'honig.gif'));return

    if message.content.lower() == 'am i stupid?' or message.content.lower() == 'i am stupid': #Evangelion memes!
        await message.channel.send("", file=discord.File('pics/stupid.jpg', 'u_are.jpg'));return

    if message.content.lower() == 'uwu' or message.content.lower() == 'owo': #UwUs back at you
        await message.channel.send("", file=discord.File('gifs/uwu.gif', 'UwU.gif'));return

    if message.content.lower() == '~dice': #A dice from 1 to 6
        dice_texts = ["1","2","3","4","5","6"]
        await message.channel.send(random.choice(dice_texts));return

    if message.content.lower() == 'shinji': #More evangelion memes
        await message.channel.send("", file=discord.File('pics/shinji.png', 'getin.png'));return

    if message.content.lower() == '~beer': #Misato likes beer
        await message.channel.send("", file=discord.File('gifs/beer.gif', 'beer.gif'));return

    if message.content.lower() == '~energy' or message.content.lower() == '~nrg': #Energy drinks to apparantly
        await message.channel.send("", file=discord.File('gifs/nrg.gif', 'nrg.gif'));return

    if message.content.lower() == '~sourcecode' or message.content.lower() == '~source': #Gives you the Bots Sourcecode
        await message.channel.send("", file=discord.File('bigPPbot.py', 'bigPPsource.py'));return

    if message.content.lower() == '~vibecheck' or message.content.lower() == '~vibe':
        await message.channel.send("", file=discord.File('gifs/vibecheck.gif', 'vibecheck.gif'));return

    if message.content.lower() == '~3rdImpact' or message.content.lower() == '~3rd':
        await message.channel.send("", file=discord.File('gifs/3rdimpact.gif', '3rdimpact.gif'));return

    if message.content.lower() == '~ip':
        await message.channel.send("", file=discord.File('gifs/ip.gif', 'ip.gif'));return

    if message.content.lower() == '~blast' or message.content.lower() == 'ramiel!':
        await message.channel.send("", file=discord.File('gifs/ramiel.gif', 'ramiel.gif'));return

    if message.content.lower() == '~nuke' or message.content.lower() == 'n2!':
        await message.channel.send("", file=discord.File('gifs/nuke.gif', 'nuke.gif'));return

    if message.content.lower() == '~explode':
        await message.channel.send("", file=discord.File('gifs/explode.gif', 'explode.gif'));return

    if message.content.startswith('~'): #Error message if command is unknown
        stoopid = oldstoopid
        stoopid = stoopid+1
        await message.channel.send('Am i too stupid to understand this command? Maybe try ~help.')
        if stoopid > 9:
                await message.channel.send("", file=discord.File('gifs/tired.gif', 'why.gif'));return

#    if message.content.startswith(''):
#        await message.channel.send('');return


tokenfile = open("token.txt", "r")
token = tokenfile.read()
tokenfile.close()
client.run(token)
