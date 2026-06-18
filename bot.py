import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot is online als {bot.user}")

# /ping
@bot.tree.command(name="ping", description="Test command")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!")

# /help
@bot.tree.command(name="help", description="Shows commands")
async def help_cmd(interaction: discord.Interaction):
    await interaction.response.send_message(
        "/ping - test bot\n/kick - kick user\n/ban - ban user"
    )

import os
bot.run(os.getenv("DISCORD_TOKEN"))
