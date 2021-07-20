import discord
from discord import colour
from discord.ext import commands
client= commands.Bot(command_prefix=">>")
f=open("rules.txt","r")
rules=f.readlines()
@client.event
async def on_ready():
    print("Bot is ready")
@client.command(aliases=['rules','test'])
async def rule(ctx,*,number):
    await ctx.send(rules[int(number)-1])
@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit=amount)
@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def kick(ctx,member:discord.Member,*,reason="No reason"):
    await member.kick(reason=reason)
@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
async def ban(ctx,member:discord.Member,*,reason="No reason"):
    await ctx.send(member.name + "has been banned" + reason)
    await member.ban(reason=reason)
@client.command(aliases=['m'])
@commands.has_permissions(kick_members=True)
async def mute(ctx,member: discord.Member):
    muted_role=ctx.guild.get_role(867118199048896542)
    await member.add_roles(muted_role)
    await ctx.send(member.mention+"has been muted")
@client.command(aliases=['um'])
@commands.has_permissions(kick_members=True)
async def unmute(ctx,member: discord.Member):
    muted_role=ctx.guild.get_role(867118199048896542)
    await member.remove_roles(muted_role)
    await ctx.send(member.mention+"has been unmuted")

@client.command(aliases=['user','info'])
@commands.has_permissions(kick_members=True)
async def whois(ctx,member : discord.Member):
    embed=discord.Embed(title= member.name, description = member.mention, colour=discord.Colour.green())
    embed.add_field(name="ID", value=member.id,inline=True)
    await ctx.send(embed=embed)
client.run("ODY2Mzk2OTY3MDY0MDQzNTQw.YPR9DQ.lgnO539_jfcOyDm_Ke1AG4qGgGo")