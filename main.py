import discord
from discord.ext import commands
import json

# Get configuration.json
with open("configuration.json", "r") as config: 
	data = json.load(config)
	token = data["token"]
	prefix = data["prefix"]
	welcome_chn_id = data["welcome_channel"]


class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

# Intents
intents = discord.Intents.default()

bot = commands.Bot(prefix, intents = intents)

# Load cogs
initial_extensions = [
	"Cogs.onCommandError",
	"Cogs.help",
	"Cogs.ping"
]

print(initial_extensions)

if __name__ == '__main__':
	for extension in initial_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			print(f"Failed to load extension {extension}")

# @commands.Cog.listener()
# async def on_member_join(self, member):
# @commands.Cog.listener()
# async def on_message(self, message):
# 	if not(message.startswith("!mzk")):
# 		return
# 	message_cut = message[4:]
# 	usr_cmd = message_cut.lower()

# 	if usr_cmd == 'konnichiwa':
# 		message.channel.send('Doumo')

# @commands.Cog.listener()
# async def on_member_join(self, member):
# 	print("Someone new joined! member.name")
# 	bot.channel.

@bot.event
async def on_ready():
	print(f"We have logged in as {bot.user}")
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}help"))
	print(discord.__version__)

bot.run(token)