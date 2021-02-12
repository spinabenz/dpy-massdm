import discord
import asyncio
from discord.ext import commands

token =  "tkn here"
prefix = "!"

client = discord.Client()
client = commands.Bot(command_prefix=prefix, case_insensitive=False, self_bot=True, intents = discord.Intents.all())
client.remove_command("help")



@client.event
async def on_connect():
    print('Hosted - Made by jays#0888')
    await client.change_presence(activity=discord.Activity(type=2, name='github.com/jayshimself', url='https://github.com/jayshimself'))


@client.command()
async def dmall(ctx):
  await ctx.message.delete()
  for channel in client.private_channels:
        try:
            await channel.send("enter you're message here")
            print(f"Sent To {channel}")
        except:
            pass


client.run(token, bot = False)
