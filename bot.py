import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import pickle
import os
import os.path
import requests
import json
import time
from gtts import gTTS
import urbandictionary as ud

Client = discord.Client()
bot_prefix= "d!!"
client = commands.Bot(command_prefix=bot_prefix)
server = discord.Server(id='414646903486152704')
footer_text = "Depresso Espresso"
error_img = ':coffee: '
default_invite = 'https://discord.gg/4YfDAKq'

@client.event
async def on_ready():
    t1 = time.perf_counter()
    print("============================================================")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print("============================================================")
    await client.change_presence(game=discord.Game(name='on Depresso Espresso'))
    await client.wait_until_ready()
    t2 = time.perf_counter()
    print("Ping: {}".format(round((t2-t1)*1000)))
    print("============================================================")

@client.event
async def on_message(message):
    if message.content.lower().startswith('dd!test'):
        await client.send_message(message.channel, "Testing 1 2 3...")
    else:
        await client.process_commands(message)
        
#################################################### EMOTE ########################################################

mocklinks = ["https://media1.tenor.com/images/e92185e00b00c8b2ef4199164e130d27/tenor.gif?itemid=8665747"]

huglinks = ["https://i.imgur.com/yE2RnXK.gif",
            "https://i.imgur.com/R9sYxk8.gif",
            "https://i.imgur.com/iLBEoKv.gif",
            "https://i.imgur.com/cc554e8.gif",
            "https://i.imgur.com/1dqkjHe.gif",
            "https://i.imgur.com/Ph8GTqg.gif",
            "https://i.imgur.com/G6EnOxd.gif",
            "https://i.imgur.com/ZxwHn5Y.gif",
            "https://i.imgur.com/movPIsP.gif",
            "https://i.imgur.com/tKlfSgo.gif",
            "https://i.imgur.com/ICg9nCr.gif",
            "https://i.imgur.com/yC95DC2.gif",
            "https://i.imgur.com/hRYXNKX.gif",
            "https://i.imgur.com/br3bGQc.gif",
            "https://i.imgur.com/IcNGAQD.gif"]

patlinks = ["https://i.imgur.com/8eApUKG.gif",
            "https://i.imgur.com/qVcP9Pt.gif",
            "https://i.imgur.com/X9hKO2p.gif",
            "https://i.imgur.com/v8cRPH9.gif",
            "https://i.imgur.com/N6C7C30.gif",
            "https://i.imgur.com/M9QPcY6.gif",
            "https://i.imgur.com/oUSdjX6.gif",
            "https://i.imgur.com/mFFr4e0.gif",
            "https://i.imgur.com/3F7kmCd.gif",
            "https://i.imgur.com/7yFvJ6m.gif",
            "https://i.imgur.com/y3La9yP.gif"]

kisslinks = ["https://i.imgur.com/0Ri9sfq.gif",
             "https://i.imgur.com/EMdpmXW.gif",
             "https://i.imgur.com/Y9iLoiv.gif",
             "https://i.imgur.com/ZlqZy8S.gif",
             "https://i.imgur.com/ySav1IQ.gif",
             "https://i.imgur.com/ZGfrn2d.gif",
             "https://i.imgur.com/glwWeUl.gif",
             "https://i.imgur.com/j5hDl7V.gif",
             "https://i.imgur.com/w7mVYty.gif",
             "https://i.imgur.com/FJ5bckO.gif",
             "https://i.imgur.com/KqVmVU7.gif",
             "https://i.imgur.com/EM1C9a6.gif",
             "https://i.imgur.com/TACVpH9.gif",
             "https://i.imgur.com/opiHLtc.gif",
             "https://i.imgur.com/LylJAea.gif"]

nomlinks = ["https://i.imgur.com/E1eQPfu.gif",
            "https://i.imgur.com/UUZY3Rb.gif",
            "https://i.imgur.com/Zd6fIpA.gif",
            "https://i.imgur.com/i2NaBS7.gif",
            "https://i.imgur.com/Up5J6Nn.gif",
            "https://i.imgur.com/J5MLku7.gif",
            "https://i.imgur.com/7yYgZXE.gif"]

throwlinks = ["https://i.imgur.com/o9j2oNi.gif",
              "https://i.imgur.com/wSb8aux.gif",
              "https://i.imgur.com/QO8TrkK.gif",
              "https://i.imgur.com/Ts3Cc52.gif",
              "https://i.imgur.com/D3ggzfW.gif",
              "https://i.imgur.com/eD5mE7R.gif",
              "https://i.imgur.com/JCUipZJ.gif",
              "https://i.imgur.com/VSg0YLw.gif",
              "https://i.imgur.com/8mUufrm.gif"]

bitelinks = ["https://i.imgur.com/E0jIIa9.gif",
             "https://i.imgur.com/Nvkw6hN.gif",
             "https://i.imgur.com/wr7l06j.gif",
             "https://i.imgur.com/uce91VI.gif"]

bloodsucklinks = ["https://i.imgur.com/UbaeYIq.gif",
                  "https://i.imgur.com/qi83Eft.gif",
                  "https://i.imgur.com/CtwmzpG.gif",
                  "https://i.imgur.com/DAuEJ2F.gif",
                  "https://i.imgur.com/By6IGzq.gif"]

cuddlelinks = ["https://i.imgur.com/GWNWcLH.gif",
               "https://i.imgur.com/i3Eqqgz.gif",
               "https://i.imgur.com/GpFk6fE.gif",
               "https://i.imgur.com/mc3Z7wf.gif",
               "https://i.imgur.com/N5JYB5r.gif",
               "https://i.imgur.com/PGp8JYq.gif"]

highfivelinks = ["https://i.imgur.com/hjoQeOt.gif",
                 "https://i.imgur.com/9nhheqT.gif",
                 "https://i.imgur.com/yw3xMOu.gif",
                 "https://i.imgur.com/Y4g5fsT.gif",
                 "https://i.imgur.com/p6Hvx5r.gif",
                 "https://i.imgur.com/33nuO9D.gif",
                 "https://i.imgur.com/uFQnmYa.gif",
                 "https://i.imgur.com/9KG3k2n.gif",
                 "https://i.imgur.com/nHCC1ps.gif",
                 "https://i.imgur.com/aKvaNba.gif",
                 "http://i.imgur.com/hnHR29x.gif"]

pokelinks = ["https://i.imgur.com/HAAktbl.gif",
             "https://i.imgur.com/Fmd0Rsu.gif",
             "https://i.imgur.com/1rObSM3.gif",
             "https://i.imgur.com/Wo2fc94.gif",
             "https://i.imgur.com/rtTucBW.gif",
             "https://i.imgur.com/4c2mC5d.gif",
             "https://i.imgur.com/1DVD84G.gif"]

slaplinks = ["https://i.imgur.com/EAF42MG.gif",
             "https://i.imgur.com/tLTT9Q4.gif",
             "https://i.imgur.com/tEWjg7v.gif",
             "https://i.imgur.com/MlkLTjv.gif",
             "https://i.imgur.com/hoTYJZP.gif",
             "https://i.imgur.com/Pthhs3Y.gif"]


punchlinks = ["https://i.imgur.com/T2HdIv8.gif",
              "https://i.imgur.com/LZz65rg.gif",
              "https://i.imgur.com/FqPBIf3.gif",
              "https://i.imgur.com/KmqPDQG.gif",
              "https://i.imgur.com/yEx4aKu.gif"]

starelinks = ["https://i.imgur.com/f8rFNH0.gif",
              "https://i.imgur.com/ACCQDj4.gif",
              "https://i.imgur.com/1Co1i9t.gif",
              "https://i.imgur.com/uPZHQxV.gif",
              "https://i.imgur.com/wXQLAb3.gif",
              "https://i.imgur.com/hY7ZngK.gif"]

facepalmlinks = ["http://media.giphy.com/media/8BYLSNmnJYQxy/giphy.gif",
                 "https://uploads.disquscdn.com/images/84e9a7cef36a59ae605fad98c7ac567841be388820bf3fb936fd21b646a1d605.gif",
                 "https://media1.tenor.com/images/74199573d51d1bd9b61029b611ee7617/tenor.gif?itemid=5695432",
                 "http://i0.kym-cdn.com/photos/images/original/000/173/877/Facepalm.gif",
                 "http://i.imgur.com/gXOcRsW.gif",
                 "https://media.giphy.com/media/8cPpgUhTMjhF6/giphy.gif",
                 "https://media1.tenor.com/images/a0282083ab6b592ab419659e4fb08624/tenor.gif?itemid=4745847"]

crylinks = ["https://media1.giphy.com/media/ROF8OQvDmxytW/giphy-downsized.gif",
            "https://media1.tenor.com/images/06ae6bbe852471939cf61a81e5a9eb23/tenor.gif?itemid=5370823",
            "https://78.media.tumblr.com/e9fb46144efc579746e57bcaebd3350a/tumblr_olrmy4djBG1tydz8to1_500.gif",
            "http://i.imgur.com/k5B1CBd.jpg",
            "https://media.giphy.com/media/hyU0RHvlS3iQU/giphy.gif",
            "https://media1.tenor.com/images/5912cbe4bc0dec511b5e0996a2ad9b6f/tenor.gif?itemid=8620704",
            "https://s9.favim.com/orig/131225/an-anime-anime-gif-anime-guy-Favim.com-1182388.gif"]

licklinks = ["https://i.imgur.com/QkRz1GJ.gif",
             "https://i.imgur.com/ObCPKYV.gif",
             "https://i.imgur.com/7fWrYqd.gif",
             "https://i.imgur.com/O8CNVUL.gif",
             "https://i.imgur.com/4QIlJtC.gif",
             "https://i.imgur.com/LptJIi1.gif",
             "https://i.imgur.com/THGgRJz.gif"]

spanklinks = ["https://i.imgur.com/dt1TTQu.gif",
              "https://i.imgur.com/ZsTbDvh.gif",
              "https://i.imgur.com/4LHwG60.gif",
              "https://i.imgur.com/xLOoHKP.gif",
              "https://i.imgur.com/UShywVv.gif",
              "https://i.imgur.com/RE3mnrA.gif"]

# d!!hug <user>
@client.command(pass_context=True)
async def hug(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to hug.")
    else:
        msg.set_image(url="{}".format(random.choice(huglinks)))
        msg.add_field(name=":coffee: EMOTE :coffee:", value="<@{}> got a hug from <@{}>! Nawww.".format(user.id, author.id))
    await client.say(embed=msg)
    
# d!!mock <user>
@client.command(pass_context=True)
async def mock(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to mock.")
    else:
        msg.set_image(url="{}".format(random.choice(mocklinks)))
        msg.add_field(name=":coffee: EMOTE :coffee:", value="<@{}> iS mOcKiNg <@{}>!".format(author.id, user.id))
    await client.say(embed=msg)
    
# d!!cry
@client.command(pass_context=True)
async def cry(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.set_image(url="{}".format(random.choice(crylinks)))
    msg.add_field(name=":coffee: EMOTE :coffee:", value="<@{}> is crying. ;-;".format(author.id))
    await client.say(embed=msg)

# d!!kiss <user>
@client.command(pass_context=True)
async def kiss(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to kiss.")
    else:
        msg.set_image(url="{}".format(random.choice(kisslinks)))
        msg.add_field(name=":coffee: EMOTE :coffee:", value="<@{}> got a kiss from <@{}>! Is this love?".format(user.id, author.id))
    await client.say(embed=msg)

# d!!cuddle <user>
@client.command(pass_context=True)
async def cuddle(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to cuddle.")
    else:
        msg.set_image(url="{}".format(random.choice(cuddlelinks)))
        msg.add_field(name=":coffee: EMOTE :coffee:", value="<@{}> cuddled <@{}>! Nawww.".format(author.id, user.id))
    await client.say(embed=msg)

# d!!bite <user>
@client.command(pass_context=True)
async def bite(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to bite.")
    else:
        msg.set_image(url="{}".format(random.choice(bitelinks)))
        msg.add_field(name=":coffee: EMOTE :coffee:", value="<@{}> got biten by <@{}>! Is this a kink?".format(user.id, author.id))
    await client.say(embed=msg)

# d!!bloodsuck <user>
@client.command(pass_context=True)
async def bloodsuck(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to suck blood from.")
    else:
        msg.set_image(url="{}".format(random.choice(bloodsucklinks)))
        msg.add_field(name=":coffee: EMOTE :coffee:", value="<@{}> sucked some of <@{}>'s blood! Yummy..?".format(author.id, user.id))
    await client.say(embed=msg)

# d!!throw <user>
@client.command(pass_context=True)
async def throw(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to throw.")
    else:
        msg.set_image(url="{}".format(random.choice(throwlinks)))
        msg.add_field(name=":coffee: EMOTE :coffee:", value="<@{}> got throw by <@{}>! Yeet".format(user.id, author.id))
    await client.say(embed=msg)

# d!!pat <user>
@client.command(pass_context=True)
async def pat(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to pat.")
    else:
        msg.set_image(url="{}".format(random.choice(patlinks)))
        msg.add_field(name=":coffee: EMOTE :coffee:", value="<@{}> got a pat from <@{}>! uwu".format(user.id, author.id))
    await client.say(embed=msg)

# d!!punch <user>
@client.command(pass_context=True)
async def punch(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to punch.")
    else:
        msg.set_image(url="{}".format(random.choice(punchlinks)))
        msg.add_field(name=":coffee: EMOTE :coffee:", value="<@{}> got punched by <@{}>! Wow, calm down.".format(user.id, author.id))
    await client.say(embed=msg)

# d!!nom <user>
@client.command(pass_context=True)
async def nom(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to nom.")
    else:
        msg.set_image(url="{}".format(random.choice(nomlinks)))
        msg.add_field(name=":coffee: EMOTE :coffee:", value="<@{}> nommed <@{}>! ( ͡° ͜ʖ ͡°)".format(author.id, user.id))
    await client.say(embed=msg)

# d!!highfive <user>
@client.command(pass_context=True)
async def highfive(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to highfive.")
    else:
        msg.set_image(url="{}".format(random.choice(highfivelinks)))
        msg.add_field(name=":coffee: EMOTE :coffee:", value="<@{}> highfived <@{}>! Woo.".format(author.id, user.id))
    await client.say(embed=msg)

# d!!poke <user>
@client.command(pass_context=True)
async def poke(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to poke.")
    else:
        msg.set_image(url="{}".format(random.choice(pokelinks)))
        msg.add_field(name=":coffee: EMOTE :coffee:", value="<@{}> got poked by <@{}>! Hmm?".format(user.id, author.id))
    await client.say(embed=msg)

# d!!slap <user>
@client.command(pass_context=True)
async def slap(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to slap.")
    else:
        msg.set_image(url="{}".format(random.choice(slaplinks)))
        msg.add_field(name=":coffee: EMOTE :coffee:", value="<@{}> got slapped by <@{}>! They probably deserved it.".format(user.id, author.id))
    await client.say(embed=msg)

# d!!stare <user>
@client.command(pass_context=True)
async def stare(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa5200, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to stare at.")
    else:
        msg.set_image(url="{}".format(random.choice(starelinks)))
        msg.add_field(name=":coffee: EMOTE :coffee:", value="<@{}> is staring at <@{}>! Creepy.".format(author.id, user.id))
    await client.say(embed=msg)

# d!!facepalm
@client.command(pass_context=True)
async def facepalm(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.set_image(url="{}".format(random.choice(facepalmlinks)))
    msg.add_field(name=":coffee: EMOTE :coffee:", value="<@{}> facepalmed. <_<".format(author.id))
    await client.say(embed=msg)
    
# d!!fart
@client.command(pass_context=True)
async def fart(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.add_field(name=":coffee: EMOTE :coffee:", value="<@{}> farted... can you smell the love? <_<".format(author.id))
    await client.say(embed=msg)

# d!!spank <user>
@client.command(pass_context=True)
async def spank(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to spank.")
    else:
        msg.set_image(url="{}".format(random.choice(spanklinks)))
        msg.add_field(name=":coffee: EMOTE :coffee:", value="<@{}> got spanked by <@{}>! =3".format(user.id, author.id))
    await client.say(embed=msg)

# d!!lick <user>
@client.command(pass_context=True)
async def lick(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to lick.")
    else:
        msg.set_image(url="{}".format(random.choice(licklinks)))
        msg.add_field(name="**:coffee: EMOTE :coffee: **", value="<@{}> licked <@{}>! Uhm...".format(author.id, user.id))
    await client.say(embed=msg)
    
    
################################################ FUN #####################################################
# d!!rainbow
@client.command(pass_context=True)
async def rainbow(ctx):
    color = discord.Color(random.randint(0x000000, 0xFFFFFF))
    msg = discord.Embed(colour=color, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.add_field(name=":rainbow: RAINBOWS :rainbow: ", value=":rainbow: R A I N B O W S :rainbow: ")
    channel = ctx.message.channel
    b = await client.send_message(channel, embed=msg)
    g = [":large_blue_circle:", ":red_circle:", ":white_circle:", ":purple_heart:", ":green_heart:", ":yellow_heart:", ":black_circle:"]
    for i in range(20):
        color = discord.Color(random.randint(0x000000, 0xFFFFFF))
        msg2 = discord.Embed(colour=color, description= "")
        msg2.title = ""
        msg2.set_footer(text=footer_text)
        msg2.add_field(name=":rainbow: RAINBOWS :rainbow: ", value=":rainbow: **__R A I N B O W S__** :rainbow: ")
        msg2.set_image(url="https://i.imgur.com/rItq9Ph.gifv")
        await client.edit_message(b, embed=msg2)
        await asyncio.sleep(float(2))
        
# d!!calculator <math problem>
@client.command(pass_context=True)
async def calculator(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Please specify a math problem you want me to solve.")
    else:
        try:
            answer = str(eval(args))
            msg.add_field(name=":fax: Calculator", value="<@{}>: what is `{}`?\n \n<@{}>: {}".format(author.id, args, client.user.id, answer))
        except:
            msg.add_field(name=":fax: Calculator", value="<@{}>: I am having trouble solving that problem.".format(client.user.id))
    await client.say(embed=msg)
    
# d!!rps <rock/paper/scissors>
@client.command(pass_context=True)
async def rps(ctx, o = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if o == None:
        msg.add_field(name=error_img, value="Please choose what you want to use.\nExample: `}rps rock`.")
    else:
        if o == "rock" or o == "paper" or o == "scissors":
            a = ["rock", "paper", "scissors"]
            c = random.choice(a)
            msg.add_field(name=":fist: **__ROCK, PAPER, SCISSORS__** :fist: ", value="**~~__==============================__~~**\n:arrow_forward: <@{}>\n------- `{}`\n:arrow_forward: <@{}>\n------- `{}`".format(author.id, o, client.user.id, c))
            if o == "rock" and c == "scissors":
                msg.add_field(name="**~~__==============================__~~**", value=":crown: WINNER: <@{}>\n \n:thumbsdown: LOSER: <@{}>".format(author.id, client.user.id))
            elif o == "paper" and c == "rock":
                msg.add_field(name="**~~__==============================__~~**", value=":crown: WINNER: <@{}>\n \n:thumbsdown: LOSER: <@{}>".format(author.id, client.user.id))
            elif o == "scissors" and c == "paper":
                msg.add_field(name="**~~__==============================__~~**", value=":crown: WINNER: <@{}>\n \n:thumbsdown: LOSER: <@{}>".format(author.id, client.user.id))
            elif o == "rock" and c == "paper":
                msg.add_field(name="**~~__==============================__~~**", value=":crown: WINNER: <@{}>\n \n:thumbsdown: LOSER: <@{}>".format(client.user.id, author.id))
            elif o == "paper" and c == "scissors":
                msg.add_field(name="**~~__==============================__~~**", value=":crown: WINNER: <@{}>\n \n:thumbsdown: LOSER: <@{}>".format(client.user.id, author.id))
            elif o == "scissors" and c == "rock":
                msg.add_field(name="**~~__==============================__~~**", value=":crown: WINNER: <@{}>\n \n:thumbsdown: LOSER: <@{}>".format(client.user.id, author.id))
            else:
                msg.add_field(name="**~~__==============================__~~**", value=":no_entry: It's a tie!")
        else:
            msg.add_field(name=error_img, value="Invalid choice.\nChoices: `rock`, `paper`, `scissors`.")
    await client.say(embed=msg)

# d!!kill <user>
@client.command(pass_context=True)
async def kill(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention the user you want to kill.")
    else:
        msgs = ["On a beautiful, sunny day, <@{}> went to the store. As they walked in to the store, they slipped and the doors cut off their head.".format(user.id),
                "<@{}> was sitting on a tree, but because of their weight, the branch broke and they fell right on their head.".format(user.id),
                "On a beautiful morning <@{}> suddenly jumped out of bed and started running towards the bathroom. However, they slipped on a banana and fell out of the window.".format(user.id),
                "<@{}> watched the Emoji movie. The next day they died from too much cringe.".format(user.id),
                "<@{}> was browsing the web one day. They accidentaly clicked on a pop-up saying 'DIE FOR FREE!'.".format(user.id),
                "<@{}> got caught watching hentai. They had no choice but to kill themselves in order to wash away their sins.".format(user.id),
                "All of <@{}>'s memes got stolen! They couldn't live for more than 0.420 seconds without memes.".format(user.id),
                "<@{}> was walking down the village when all of a sudden a piano fell on top of them, crashing all their bones.".format(user.id),
                "Long time ago <@{}> lived in peace and harmony, until the fire nation attacked. Now <@{}> is pretty much dead.".format(user.id, user.id),
                "<@{}> died a virgin. LMAO what a loser.".format(user.id),
                "<@{}> was playing hopscotch on a landmine field. You can tell how that went.".format(user.id),
                "<@{}> was playing the Sims. Their computer crashed and they got a heart attack.".format(user.id),
                "Wait, <@{}> died? Oh well.".format(user.id),
                "<@{}> commited suicide. I guess it's a way of saying 'You can't fire me! I quit!' to God.".format(user.id),
                "<@{}> gave their heart to <@{}>... Literally.".format(user.id, author.id),
                "There hasn't been rain around the whole world, plants are dying and the temperatures are very high. <@{}> was a vegan.".format(user.id),
                "<@{}> decided to go on the moon. However they forgot their space suit. All the kids wanted to hear about the corpse on the moon...".format(user.id),
                "One day <@{}> was chilling with their friends. All of them were bored, they didn't have anything to do. One of them said 'So gentlemen, what do we do now?', <@{}> replied: 'We die.'. Yeah, they were really bored.".format(user.id, user.id),
                "<@{}> tried to lay an egg. Humans can't do that, nor can bots!".format(user.id),
                "All of <@{}>'s diamonds were stolen on their Christian minecraft server. Out of anger they said 'heck' and got killed instantly.".format(user.id),
                "<@{}> forgot how to breathe.".format(user.id),
                "<@{}> saw <@{}>'s face and instantly died.".format(user.id, author.id),
                "...and then <@{}> said: I don't feel so good...".format(user.id),
                "<@{}> livedn't.".format(user.id),
                "<@{}> had a lot of mental disorders and couldn't live with them anymore. They commited suicide by cutting a deep wound on their chest with a kitchen knife.".format(user.id),
                "<@{}> drowned <@{}> in a glass of water.".format(author.id, user.id),
                "<@{}> threw <@{}> in a pool with sharks.".format(author.id, user.id),
                "<@{}> spammed <@{}>'s DMs and they died from all the notifications they got.".format(author.id, user.id),
                "<@{}> stole all of <@{}>'s chocolate. <@{}> simply couldn't live without their chocolate and decided that their life is not worth living anymore.".format(author.id, user.id, user.id),
                "<@{}>'s toaster was hacked by <@{}>. They couldn't live with no toast.".format(user.id, author.id),
                "<@{}> watched furry porn and died from what they saw.".format(user.id),
                "<@{}> 'accidentally' fell off a building.".format(user.id),
                "<@{}> may have ate food with cyanide.".format(user.id),
                "<@{}> starved in a fast food restaurant. What a fucking idiot.".format(user.id),
                "...And <@{}> died happily ever after... Wait no, I messed it up!".format(user.id),
                "<@{}> joined this server and died. Oh well, that's not a first.".format(user.id),
                "<@{}> was gay in Iran.".format(user.id),
                "<@{}> choked on a banana ( ͡° ͜ʖ ͡°) and died.".format(user.id),
                "<@{}> drove off a cliff and survived, but died from shock when they saw the high price of the hospital bill.".format(user.id),
                "<@{}> listened to Justin Beiber for more than 0.69 seconds.".format(user.id),
                "<@{}> drank too much anti-freeze.".format(user.id),
                "<@{}> got stabbed with a cucumber by <@{}>.".format(user.id, author.id),
                "<@{}> died from a heatstroke in the artic.".format(user.id),
                "<@{}> tried to fly. It worked till they hit the ground.".format(user.id),
                "<@{}> wanted to get a haircut in a faster way. They thought setting their hair on fire would do the trick.".format(user.id),
                "On a peaceful night. The moon was shining and everyone was sleeping and enjoying their dreams while <@{}> suffocated in their pillow.".format(user.id),
                "<@{}> got run over by a boat. A fricking boat!".format(user.id),
                "What's that smell? It smells like toast... Hey, <@{}>! Don't take out the toast with a fork- too late...".format(user.id),
                "<@{}> got a paper cut on both of their eyes, walked off a cliff and died. I guess books are evil.".format(user.id),
                "<@{}> tried putting out fire with gasoline.".format(user.id),
                "<@{}>'s head exploded while they were sitting on the toilet and pressing.".format(user.id),
                "<@{}> died of laughter. No I mean they actually died.".format(user.id),
                "<@{}> got locked in a refrigerator and died of hunger.".format(user.id),
                "<@{}> drowned in their own tears after losing a game of Fortnite.".format(user.id),
                "<@{}> got beat up by their imaginary friends.".format(user.id),
                "<@{}> played My Little Ponny for too long.".format(user.id),
                "<@{}> choked on air.".format(user.id),
                "<@{}> got poked by Chuck Norris.".format(user.id),
                "<@{}> took a selfie with a gun.".format(user.id),
                "<@{}>'s brain exploded after <@{}> saying 'What if dolphins had legs?'.".format(user.id, author.id),
                "<@{}> died after eating their favourite snack, tide pods.".format(user.id),
                "<@{}> survived the biggest waves then tripped on a rock and died.".format(user.id),
                "<@{}> ate white chocolate. Who the fuck eats white chocolate?".format(user.id),
                "<@{}> demonstrated how to die and then had a heart attack. How ironic.".format(user.id),
                "<@{}> fell in a toilet and then got flushed.".format(user.id),
                "<@{}> got stuck in a vending machine.".format(user.id),
                "<@{}> choked on their toothbrush and died.".format(user.id),
                "<@{}> found their butthole and died from excitement.".format(user.id),
                "<@{}> died. That's it. They just died.".format(user.id)]
        msg.add_field(name=":newspaper2: ", value="{}".format(random.choice(msgs)))
    await client.say(embed=msg)
    
# d!!eightball <yes or no question>
@client.command(pass_context=True)
async def eightball(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Please ask a yes/no question.")
    else:
        if len(str(args)) > 1900:
            msg.add_field(name=error_img, value="The question cannot be longer than 1900 characters.")
        else:
            a = ["Hell no!",
                 "No!",
                 "Hell yes!",
                 "Yes!",
                 "Definitely!",
                 "Definitely not!",
                 "Probably!",
                 "Probably not!",
                 "Most likely!",
                 "Yes! I'm sure of it!",
                 "No! I'm sure of it!"]
            msg.add_field(name=":8ball: ", value=":grey_question: `Question:`\n<@{}>: {}\n \n:grey_exclamation: `Answer:`\n**Magic Eight Ball**: {}".format(author.id, args, random.choice(a)))
    await client.say(embed=msg)
    
# dd!roast <user>
@client.command(pass_context=True)
async def roast(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention a user you want to roast.")
    else:
        a = ["<@{}>: Hey, <@{}>! I saw a piece of shit today... it reminded me of you.".format(author.id, user.id),
             "<@{}>: You look familiar, <@{}>. Oh yeah! I see you in the trash.".format(author.id, user.id),
             "<@{}>: Don't worry, <@{}>, you're not adopted. We're still searching for someone who wants you.".format(author.id, user.id),
             "<@{}>: If I wanted to kill myself, I'd jump climb up your ego and jump in your IQ, <@{}>.".format(author.id, user.id),
             "<@{}>: <@{}>, you are so stupid that you got hit by a parked car.".format(author.id, user.id),
             "<@{}>: <@{}>, you are so fat and so old that when God created light, you were asked to move out of the way.".format(author.id, user.id),
             "<@{}>: I heard <@{}> sucks so much that they were used as a vacuum cleaner.".format(author.id, user.id),
             "<@{}>: Hey, <@{}>! Try to not spit when you talk, we don't need a public shower here.".format(author.id, user.id),
             "<@{}>: I can't breathe when I see you, <@{}>... cause I'm suffocating from your bullshit.".format(author.id, user.id),
             "<@{}>: <@{}>, you have the right to remain silent cause anything you say is probably going to be stupid anyway.".format(author.id, user.id),
             "<@{}>: It's really hard to ignore <@{}>. Mostly cause they smell like shit.".format(author.id, user.id),
             "<@{}>: <@{}>, did you fall from Heaven? Cause so did Satan.".format(author.id, user.id),
             "<@{}>: <@{}>, were you sent to kill people? Cause your face is killing me.".format(author.id, user.id),
             "<@{}>: If laughter is the best medicine, your face must be curing the world, <@{}>.".format(author.id, user.id),
             "<@{}>: The only way you'll ever get laid is if you crawl up a chicken's ass and wait, <@{}>.".format(author.id, user.id),
             "<@{}>: <@{}>, your family tree must be a cactus. Cause everyone on it is a prick.".format(author.id, user.id),
             "<@{}>: <@{}>, save your breath, you'll need it to blow your date.".format(author.id, user.id),
             "<@{}>: <@{}>, the zoo called. They are wondering how you got out of your cage?".format(author.id, user.id),
             "<@{}>: <@{}>, you're so ugly that when you look in the mirror your reflection looks the away.".format(author.id, user.id),
             "<@{}>: <@{}>, it's better to let someone think you're stupid than open your mouth and prove it.".format(author.id, user.id),
             "<@{}>: I just stepped in something that is smarter than you, <@{}>... It smelled better too.".format(author.id, user.id),
             "<@{}>: <@{}>, you're stupid just like your father when he thought he didn't need a condom.".format(author.id, user.id),
             "<@{}>: <@{}> is so stupid that they stopped at a stop sign and waited for it to say go.".format(author.id, user.id),
             "<@{}>: <@{}>, you're so ugly that you have to trick or treat over the phone.".format(author.id, user.id),
             "<@{}>: <@{}>, you're so fat that your school photo was a double picture.".format(author.id, user.id),
             "<@{}>: I'd like to kick <@{}> in the teeth but that would be an improvement for them.".format(author.id, user.id),
             "<@{}>: <@{}> is so old that when they were in school there was no history class.".format(author.id, user.id),
             "<@{}>: <@{}> is so stupid that they called me to ask me for my phone number.".format(author.id, user.id),
             "<@{}>: <@{}>, at least my mom pretends to love me.".format(author.id, user.id),
             "<@{}>: <@{}>, don't play hard to get when you are hard to want.".format(author.id, user.id),
             "<@{}>: <@{}>, you're hating yourself too much for me to roast you.".format(author.id, user.id),
             "<@{}>: <@{}>, I can't even call you ugly. Nature has beaten me to it.".format(author.id, user.id),
             "<@{}>: People like you, <@{}>, are the reason God doens't talk to us anymore.".format(author.id, user.id),
             "<@{}>: We all dislike you, <@{}>. But not quite enough to think about you.".format(author.id, user.id),
             "<@{}>: <@{}>, you are a stupid.".format(author.id, user.id),
             "<@{}>: <@{}>, I'd like to invite you to a nice, warming cup of shut the fuck up.".format(author.id, user.id),
             "<@{}>: <@{}>, your mother might have told you, you can be whatever you want to but a cunt wasn't what she meant.".format(author.id, user.id),
             "<@{}>: <@{}> is so fat, Thanos had to clap.".format(author.id, user.id)]
        msg.add_field(name=":fire: Roast Machine", value="{}".format(random.choice(a)))
    await client.say(embed=msg)
    
# d!!leave
@client.command(pass_context=True)
async def leave(ctx):
    author = ctx.message.author
    a = ["**{}** left the server!".format(author.name),
         "**{}** left the game!".format(author.name),
         "**{}** left your party!".format(author.name),
         "**{}** left!".format(author.name),
         "**{}** died!".format(author.name),
         "**{}** has been killed!".format(author.name)]
    await client.say(random.choice(a))
    await client.delete_message(ctx.message)
    
# d!!rate <text>
@client.command(pass_context=True)
async def rate(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Nothing to rate given.")
    else:
        if len(str(args)) > 1900:
            msg.add_field(name=error_img, value="The text cannot be longer than 1900 characters.")
        else:
            msg.add_field(name=":scales:", value=":arrow_forward: <@{}>\nI'd rate {} a {}/10!".format(author.id, args, random.randint(0, 11)))
    await client.say(embed=msg)
    
# d!!urban <text>
@client.command(pass_context=True)
async def urban(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xdaa520, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Please give something you want to define.")
    else:
        if len(str(args)) > 150:
            msg.add_field(name=error_img, value="The text cannot be longer than 150 characters.")
        else:
            try:
                defs = ud.define('{}'.format(args))
                msg.add_field(name=":bookmark_tabs: Urban Dictionary", value="<@{}>: What is {}?\n \n{}".format(author.id, args, random.choice(defs)))
            except:
                msg.add_field(name=":bookmark_tabs: Urban Dictionary", value="<@{}>: What is {}?\n \nNo definition found.".format(author.id))
    await client.say(embed=msg)
##################################
client.run(os.environ['BOT_TOKEN'])
