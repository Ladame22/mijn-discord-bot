import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

import discord

GUILD_ID = 1515808781533974619

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(f"Sync error: {e}")

    print(f"Bot online als {bot.user}")
# /ping
@bot.tree.command(name="ping", description="Test command")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!") 
    @bot.tree.command(name="kick", description="Kick een user")
async def kick(interaction: discord.Interaction, user: discord.Member, reason: str = "Geen reden"):
    
    if not interaction.user.guild_permissions.kick_members:
        await interaction.response.send_message("❌ Je hebt geen permissie", ephemeral=True)
        return

    if user == interaction.user:
        await interaction.response.send_message("❌ Je kan jezelf niet kicken", ephemeral=True)
        return

    await user.kick(reason=reason)
    await interaction.response.send_message(f"👢 {user.mention} is gekickt. Reden: {reason}")
    @bot.tree.command(name="ban", description="Ban een user")
async def ban(interaction: discord.Interaction, user: discord.Member, reason: str = "Geen reden"):

    if not interaction.user.guild_permissions.ban_members:
        await interaction.response.send_message("❌ Je hebt geen permissie", ephemeral=True)
        return

    if user == interaction.user:
        await interaction.response.send_message("❌ Je kan jezelf niet bannen", ephemeral=True)
        return

    await user.ban(reason=reason)
    await interaction.response.send_message(f"🔨 {user.mention} is gebanned. Reden: {reason}")

    


    @bot.tree.command(name="ping", description="Test command")

# /help
@bot.tree.command(name="help", description="Shows commands")
async def help_cmd(interaction: discord.Interaction):
    await interaction.response.send_message(
        "/ping - test bot\n/kick - kick user\n/ban - ban user"
    )

import os
bot.run(os.getenv("DISCORD_TOKEN"))
