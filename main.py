from instabot import Bot
import discord
from discord.ext import commands

prefix = "/"

bot = commands.Bot(command_prefix=prefix, help_command=None)

@bot.command()
async def igfollow(ctx, user):
 bot = Bot()
 bot.login(username="Name", password="Password")
 bot.follow(user)
 await ctx.send("**Sending Followers**\n Made By Excet")

#excetiscute

bot.run("tokenhere")
