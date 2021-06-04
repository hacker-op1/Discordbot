import discord
import os
from gtts import gTTS
from discord import FFmpegPCMAudio
from discord.ext import commands
import random
import time



client = commands.Bot(command_prefix="!")


def TextToSpeech(s):
    audio = gTTS(text=s, lang='en-uk', slow=False)
    audio.save("welcome.mp3")


def name(s):
    s = str(s)
    n = len(s)
    name = ""
    for i in range(n):
        if s[i] == '#':
            break
        else:
            name += s[i]
    return name

def BinToText(s):
    binary_int = int(s, 2)
    byte_number = binary_int.bit_length() + 7 // 8

    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()
    return ascii_text




@client.event
async def on_ready():
    print("Bot is Ready.")


@client.event
async def on_message(message):
    if message.author.bot and (message.content.startswith("b ") or message.content.startswith("B ") or message.content.startswith("spam b ") or message.content.startswith("clear b")
    or message.content.startswith("!talk") or message.content.startswith("!leave") or message.content.startswith("!join") or message.content.startswith("!abuse")):
        await message.channel.send("Lol I dont talk to small bots like you")
    elif 'ghost pinged' in message.content and message.author.id == 846835693195362314:
        await message.delete()
        await message.channel.send("Your bot is too weak.")
    elif message.content.startswith('help'):
        t = """
Use the following commands:
1)b (converts word to its binary form)
2)decode (decodes binary word to alphabetical 
     form)     

3)spam b
4)clear b"""
        await message.channel.send(t)
    elif message.content.startswith('decode '):
        msg = message.content[7:]
        n = len(msg)
        t = ""
        s=''
        for i in range(n):
            if msg[i] != '-' and msg[i] != ' ' and i != n-1:
                s += msg[i]
            elif msg[i] == " ":
                t += BinToText(s) + " "
                s = ""
            elif i == n-1:
                s += msg[i]
                t += BinToText(s) + " "
                s = ""
        x = ""
        for i in range(0,len(t)):
            if (ord(t[i]) >= 33 and ord(t[i]) <= 126) or t[i]==" ":
                x+=t[i]
        await message.channel.send(x)

    elif message.content.startswith('b '):
        t = ""
        p = str(message.content)
        p = p[2:]
        n = len(p)
        for i in range(0, n):
            if p[i] == " ":
                t += " "
            elif i != n-1 and p[i+1]!=" ":

                s = str(bin(ord(p[i])))
                s = s[0] + s[2:]
                t += (s +"-")
            else:
                s = str(bin(ord(p[i])))
                s = s[0] + s[2:]
                t += s
        await message.channel.send(t)
    elif message.content.startswith('B '):
        t = ""
        p = str(message.content)
        p = p[2:]
        n = len(p)
        for i in range(0, n):
            if p[i] == " ":
                t += " "
            elif i!= n-1 and p[i+1]!=" ":

                s = str(bin(ord(p[i])))
                s = s[0] + s[2:]
                t += (s +"-")
            else:
                s = str(bin(ord(p[i])))
                s = s[0] + s[2:]
                t += s
        await message.channel.send(t)
    if message.content.startswith('spam b '):
        t = ""
        p = str(message.content)
        p = p[7:]
        n = len(p)
        for i in range(0, n):
            if p[i] == " ":
                t += " "
            elif i != n - 1 and p[i + 1] != " ":

                s = str(bin(ord(p[i])))
                s = s[0] + s[2:]
                t += (s + "-")
            else:
                s = str(bin(ord(p[i])))
                s = s[0] + s[2:]
                t += s
        timeout = 0
        while timeout<10:
            await message.channel.send(t)
            timeout+=1
    if message.content.startswith('clear b'):
        m = str(message.mentions[0])
        nam = name(m)
        i = 0
        while i < 5:

            msg = await message.channel.history().get(author__name=nam)
            await msg.delete()
            i += 1
        await message.channel.purge(limit=1)
    await client.process_commands(message)



@client.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.channel.send("You are not in a voice channel")


@client.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.channel.send("See you again")
    else:
        await ctx.channel.send("I am not in the voice channel.")


@client.command()
async def talk(ctx):

    message = ctx.message.content
    try:
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            await ctx.channel.send("You are not in a voice channel")
    except:
        pass
    voice = discord.utils.get(client.voice_clients,guild = ctx.guild)
    song_there = os.path.isfile("welcome.mp3")
    if song_there:
        os.remove("welcome.mp3")
    if "hello" in message.lower():
        name1 = name(ctx.author)
        TextToSpeech("Hello " + name1+ ".What are you doing?")
        source = FFmpegPCMAudio("welcome.mp3")
        voice.play(source)
    elif "sleep" in message.lower():
        name1 = name(ctx.author)

        TextToSpeech("This will help you sleep")
        source = FFmpegPCMAudio("welcome.mp3")
        voice.play(source)
        i = 0
        while i<2:
            try:
                source = FFmpegPCMAudio("sleep.mp3")
                voice.play(source)
                i += 1
            except:
                pass
        await ctx.channel.send("Goodnight " + name1)
    else:
        name1 = name(ctx.author)
        print(name1 + ":" + message[6:])


@client.command()
async def abuse(ctx):
    try:
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            await ctx.channel.send("You are not in a voice channel")
    except:
        pass
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    song_there = os.path.isfile("welcome.mp3")
    if song_there:
        os.remove("welcome.mp3")
    try:
        m = str(ctx.message.mentions[0])
        nam = name(m)
        if nam == "harshit" or nam == "BinaryNerd":
            nam = name(str(ctx.message.author))
        l = [f"Nice tits,{nam}", f"Fuck off {nam}", f"{nam} is a Dick head", f"piss off {nam}",
             f"oh {nam}, you Son of a bitch", f"Oh {nam}, you bloody Bastard",
             f"I wanted to tell you that {nam} is wanking."]
        i = random.randint(0, len(l) - 1)
        TextToSpeech(l[i])
        source = FFmpegPCMAudio("welcome.mp3")
        voice.play(source)
    except:
        m = ctx.message.content
        nam = m[7:]
        if nam == "harshit" or nam =="BinaryNerd":
            nam = name(str(ctx.message.author))
        l = [f"Nice tits,{nam}", f"Fuck off {nam}", f"{nam} is a Dick head", f"piss off {nam}",
             f"oh {nam}, you Son of a bitch", f"Oh {nam}, you bloody Bastard",
             f"I wanted to tell you that {nam} is wanking."]

        i = random.randint(0, len(l) - 1)
        TextToSpeech(l[i])
        source = FFmpegPCMAudio("welcome.mp3")
        voice.play(source)


client.run(os.getenv('TOKEN'))



