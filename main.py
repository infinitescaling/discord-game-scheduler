# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
from discord import Intents
from discord.ext import commands

# IMPORT DATETIME
from datetime import datetime

# IMPORT THE OS MODULE.
import os

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Enable all standard intents and message content
# (prefix commands generally require message content)
intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message) -> str:
    p_message = message.content.lower()
    # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
    # print(f"on_message triggered: {message}")
    if p_message == 'hello':
        # SENDS BACK A MESSAGE TO THE CHANNEL.
        await message.channel.send(f"hey {message.author.name}")

@bot.command()
async def foo(ctx):
    now = datetime.now()
    print(now)
    await message.channel.send(now)
    await ctx.send(arg)


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)
