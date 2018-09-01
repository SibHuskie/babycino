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
        
#EMOTE

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
##################################
client.run(os.environ['BOT_TOKEN'])
