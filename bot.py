import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

import discord

GUILD_ID = JOUW_SERVER_ID_HIER

@bot.event
async def on_ready():
    guild = discord.Object(id=GUILD_ID)
    await bot.tree.sync(guild=guild)
    print(f"Bot is online als {bot.user}")

# /ping
@bot.tree.command(name="ping", description="Test command")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!") @bot.tree.command(name="kick", description="Kick een user")
async def kick(interaction: discord.Interaction, user: discord.User, reason: str = "Geen reden"):
    member = interaction.guild.get_member(user.id)

    if not interaction.user.guild_permissions.kick_members:
        await interaction.response.send_message("❌ Geen permissie", ephemeral=True)
        return

    if member is None:
        await interaction.response.send_message("❌ User niet in server", ephemeral=True)
        return

    await member.kick(reason=reason)
    await interaction.response.send_message(f"👢 {user} gekickt: {reason}") @bot.tree.command(name="ban", description="Ban een user")
async def ban(interaction: discord.Interaction, user: discord.User, reason: str = "Geen reden"):
    member = interaction.guild.get_member(user.id)

    if not interaction.user.guild_permissions.ban_members:
        await interaction.response.send_message("❌ Geen permissie", ephemeral=True)
        return

    if member is None:
        await interaction.response.send_message("❌ User niet in server", ephemeral=True)
        return

    await member.ban(reason=reason)
    await interaction.response.send_message(f"🔨 {user} gebanned: {reason}")

# /help
@bot.tree.command(name="help", description="Shows commands")
async def help_cmd(interaction: discord.Interaction):
    await interaction.response.send_message(
        "/ping - test bot\n/kick - kick user\n/ban - ban user"
    )

import os
bot.run(os.getenv("DISCORD_TOKEN"))
