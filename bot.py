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
    await interaction.response.send_message("🏓 Pong!") @bot.tree.command(name="kick", description="Kick een user")
async def kick(interaction: discord.Interaction, user: discord.Member, reason: str = "Geen reden"):
    if not interaction.user.guild_permissions.kick_members:
        await interaction.response.send_message("❌ Je hebt geen permissie om te kicken.", ephemeral=True)
        return @bot.tree.command(name="ban", description="Ban een user")
async def ban(interaction: discord.Interaction, user: discord.Member, reason: str = "Geen reden"):
    if not interaction.user.guild_permissions.ban_members:
        await interaction.response.send_message("❌ Je hebt geen permissie om te bannen.", ephemeral=True)
        return

    await user.ban(reason=reason)
    await interaction.response.send_message(f"🔨 {user} is gebanned. Reden: {reason}")

    await user.kick(reason=reason)
    await interaction.response.send_message(f"👢 {user} is gekickt. Reden: {reason}")

# /help
@bot.tree.command(name="help", description="Shows commands")
async def help_cmd(interaction: discord.Interaction):
    await interaction.response.send_message(
        "/ping - test bot\n/kick - kick user\n/ban - ban user"
    )

import os
bot.run(os.getenv("DISCORD_TOKEN"))
