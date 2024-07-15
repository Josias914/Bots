import discord ,random ,requests
import os
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
count = 0
bot = commands.Bot(command_prefix='&', intents=intents)
@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
 

@bot.command('duck')
async def duck(ctx):
    global count
    count = 0
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
 

@bot.command('dog')
async def dog(ctx):
    global count
    count = 0
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command()
async def mem(ctx):
    global count
    img_name = random.choice(os.listdir("images")) 
    if count <= 5 :
        with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
            count += 1
        await ctx.send(file=picture)
    elif count > 5:
         img_name2 = random.choice(os.listdir("Raros"))
         with open(f'Raros/{img_name2}', 'rb') as f:
            picture = discord.File(f)
         await ctx.send(file=picture)
         count = 0

@bot.command()
async def heh(ctx, count_heh = 5):
    global count
    count = 0
    await ctx.send("he" * count_heh)
@bot.command()
async def joined(ctx, member: discord.Member):
    global count
    count = 0
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
bot.run("aqui va el token")


