import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


#MEGNUMIN! etc...
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('MEGNUMIN!'):
        await message.channel.send('BOOM!', file=discord.File('gifs/megnumin.gif', 'boom.png'))

    if message.content.startswith('EVA-01!'):
        await message.channel.send('Get stabbed!', file=discord.File('gifs/eva01.gif', 'rip.png'))

    if message.content.startswith('~porn') or message.content.startswith('~hentai'):
        await message.channel.send('No. Go die in a hole!')

    if message.content.startswith('~pp'):
        await message.channel.send('PP stands for PowerPoints, you fucking degenerate!')

#    if message.content.startswith(''):
#        await message.channel.send('')


tokenfile = open("token.txt", "r")
token = tokenfile.read()
tokenfile.close()
client.run(token)
