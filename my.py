import discord
import os
from discord.ext import commands
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')
@bot.command()
async def Serfero (ctx):
    await ctx.send(f'cześć podsyłam ci link do niego[https://www.youtube.com/@Serfero]')

@bot.command()
async def Kaluch (ctx):
    await ctx.send(f'cześć podsyłam ci link do niego[https://www.youtube.com/@KaluchYT]')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
@bot.command()
async def  mem(ctx):
    with open('images/meme1.jpg', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def random_mem(ctx):
    memes = os.listdir('images')
    img_name = random.choice(memes)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def map(ctx):
    maps = os.listdir('map')
    map_name = random.choice(maps)
    with open(f'map/{map_name}', 'rb') as f:
            picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Po wywołaniu polecenia duck program wywołuje funkcję get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command()
async def  szkło(ctx):
    with open('bins/green.jpg', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def  plastik(ctx):
    with open('bins/yellow.jpg', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def  metal(ctx):
    with open('bins/yellow.jpg', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def  bio(ctx):
    with open('bins/brown.jpeg', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def  papier(ctx):
    with open('bins/blue.jpg', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)

bot.run("token")

