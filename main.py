import discord
import os
from discord.ext import commands
from update import Patch
import asyncio
import random

intents = discord.Intents.default()
intents.message_content = True
patch = Patch()

client = commands.Bot(command_prefix='!', self_bot=True, help_command=None, intents=intents)


async def loop():
  while True:
    patch.new = patch.GetPatchVersionWeb()
    patch.current = patch.GetCurrentPatchVersion()

    if patch.current != patch.new:
      await embed_send(patch.current, patch.new)
      patch.UpdatePatchVersion()

    await asyncio.sleep(10)


async def embed_send(current, new):
  channel = client.get_channel(int(os.getenv("CHANNEL_ID")))
  embed = discord.Embed(
    title='Dragon Nest Sea',
    description=f"**Game** has been patched from {current} to {new}.",
    color=discord.Color(random.randint(0, 0xFFFFFF))
  )
  embed.set_image(url="https://static.wikia.nocookie.net/dragonnest_gamepedia/images/f/f0/Album_Image_001.png")
  embed.timestamp = discord.utils.utcnow()
  await channel.send(embed=embed)

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online)
  os.system('clear')
  print(f'Logged in as {client.user} (ID: {client.user.id})')
  client.loop.create_task(loop())

client.run(os.getenv("TOKEN"))
