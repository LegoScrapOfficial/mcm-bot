import discord, asyncio, os, sys, random, math, youtube_dl
from datetime import datetime
from discord import Intents
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions


intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='m!', help_command=None, intents=intents)

animals = ["https://media.discordapp.net/attachments/833198722875260938/833199026903580682/cute-dog-headshot.png?width=709&height=473",
"https://media.discordapp.net/attachments/833198722875260938/833198888705720380/5484d9d1eab8ea3017b17e29.png",
"https://media.discordapp.net/attachments/833198722875260938/833198882300624966/1915.png?width=473&height=473",
"https://media.discordapp.net/attachments/833198722875260938/833198850423521320/d41586-020-01430-5_17977552.png?width=710&height=473",
"https://media.discordapp.net/attachments/833198722875260938/833198845327572992/1800x1200_dog_cool_summer_other.png?width=710&height=473",
"https://media.discordapp.net/attachments/833198722875260938/833198838558097478/105992231-1561667465295gettyimages-521697453.png?width=840&height=473",
"https://media.discordapp.net/attachments/833198722875260938/833198767188607006/dog-puppy-on-garden-royalty-free-image-1586966191.png?width=943&height=473",
'https://media.discordapp.net/attachments/833198722875260938/833200605371039754/5de5784979d757159d0b6838.png?width=631&height=473',
'https://media.discordapp.net/attachments/833198722875260938/833200528485908490/Canine-Meadow-Dog-Park-web-harleythepewdle_1.png?width=585&height=473',
'https://media.discordapp.net/attachments/833198722875260938/833200489830416454/I3MnYUdm_400x400.png',
'https://media.discordapp.net/attachments/833198722875260938/833200464073719868/Puparazzi-21_Image-for-Eblasts.png',
'https://media.discordapp.net/attachments/833198722875260938/833200442892353556/blog_make-dogs-day_101619_main.png?width=983&height=473',
'https://media.discordapp.net/attachments/833198722875260938/833200418125119518/main_puppies_1280p.png?width=840&height=473',
'https://media.discordapp.net/attachments/833198722875260938/833200371014565898/puppy-410265.png',
'https://media.discordapp.net/attachments/833198722875260938/833200341717352488/969.png?width=631&height=473',
'https://media.discordapp.net/attachments/833198722875260938/833200321097760788/imrs.png?width=635&height=473',
'https://media.discordapp.net/attachments/833198722875260938/833200309248983040/image.png?width=710&height=473',
'https://media.discordapp.net/attachments/833198722875260938/833200272040919040/file-20200309-118956-1cqvm6j.png?width=630&height=473']

phrases = [""]

memes = ["https://media.discordapp.net/attachments/307226054068666371/833420198199296070/image0.png?width=480&height=559",
""]
@bot.command()
@commands.cooldown(1, 15)
async def animal(ctx):
    randog = random.choice(dogs)
    ranphrase = random.choice(phrases)
    await ctx.send(ranphrase)
    await ctx.send(randog)
    await ctx.message.delete

@bot.command()
@commands.cooldown(1, 15)
async def meme(ctx):
    ranmeme = random.choice(memes)
    await ctx.send(f'get memed kid')
    await ctx.send(ranmeme)
    await ctx.message.delete

@bot.command()
@commands.cooldown(1, 5)
async def support(ctx):
    await ctx.send('**To get help, please ping the `support` role!**\nYou can go into any help channel and do so.')

@bot.event
async def on_ready():
    print('Prefix Set as m!... \nStatus Changed...')
    print()
    print(f"MCM Bot Online... ")
    print()

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over Jig's Kingdom."))

@bot.event
async def on_member_join(member):
    date_time = member.created_at
    d = date_time.strftime("%y/%m/%d")
    days = (datetime.now() - member.created_at)

    embed=discord.Embed(title="Join", description=f"{member.mention} has joined!", color=0x44ea2e)
    embed.set_author(name="MCM Bot", icon_url="https://media.discordapp.net/attachments/307226054068666371/825085476045455360/d27f8f7dcdc46c86a465c533cd6397e7_1.png?width=473&height=473")
    embed.add_field(name="Account Age: ", value=f"{days.days} days", inline=True)
    channel = bot.get_channel(833068492034277387)
    await channel.send(embed=embed)

@bot.command()
@commands.cooldown(1, 20)
@commands.has_guild_permissions(view_audit_log=True)
async def modlog(ctx, punishment, id, *, reason=None):
    user = ctx.author.mention
    embed=discord.Embed(title="Modlog", color=0xf90606)
    embed.set_author(name="MCM Bot", icon_url="https://media.discordapp.net/attachments/307226054068666371/825085476045455360/d27f8f7dcdc46c86a465c533cd6397e7_1.png?width=473&height=473")
    embed.add_field(name="Staff: ", value=f'{user}', inline=False)
    embed.add_field(name="Punishment: ", value=f'{punishment}', inline=False)
    embed.add_field(name="User: ", value=f'<@{id}>', inline=False)
    embed.add_field(name="Reason: ", value=f'{reason}', inline=True)
    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command(pass_context=True)
@commands.has_guild_permissions(manage_messages=True)
async def purge(ctx, amount=30):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)
    await channel.delete_messages(messages)

@bot.command()
@commands.cooldown(1, 20)
@commands.has_guild_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx.message.delete()
    await member.send(f'You have been kicked from, {ctx.guild.name} for {reason}.')
    await member.kick()
    embed=discord.Embed(title="Kick", description=f"{member.mention} has been kicked. ", color=0xa3a3a3)
    embed.set_author(name="MCM Bot", icon_url="https://media.discordapp.net/attachments/307226054068666371/825085476045455360/d27f8f7dcdc46c86a465c533cd6397e7_1.png?width=473&height=473")
    embed.add_field(name="Reason: ", value=f"{reason}", inline=True)
    embed.add_field(name="Staff: ", value=f"{ctx.author.mention}", inline=True)
    channel = bot.get_channel(833068492034277387)
    await channel.send(embed=embed)

@bot.command()
@commands.cooldown(1, 30)
@commands.has_guild_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.message.delete()
    await member.send(f'You have been banned from, {ctx.guild.name} for {reason}.')
    await member.ban()
    embed=discord.Embed(title="Ban", description=f"{member.mention} has been banned. ", color=0xa3a3a3)
    embed.set_author(name="MCM Bot", icon_url="https://media.discordapp.net/attachments/307226054068666371/825085476045455360/d27f8f7dcdc46c86a465c533cd6397e7_1.png?width=473&height=473")
    embed.add_field(name="Reason: ", value=f"{reason}", inline=True)
    embed.add_field(name="Staff: ", value=f"{ctx.author.mention}", inline=True)
    channel = bot.get_channel(833068492034277387)
    await channel.send(embed=embed)

@bot.command()
@commands.cooldown(1, 10)
async def mute(ctx, member: discord.Member, time: int, d, *, reason=None):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.add_roles(role)
            embed=discord.Embed(title="Mute", description=f"{member.mention} has been muted. ", color=0xa3a3a3)
            embed.set_author(name="MCM Bot", icon_url="https://media.discordapp.net/attachments/307226054068666371/825085476045455360/d27f8f7dcdc46c86a465c533cd6397e7_1.png?width=473&height=473")
            embed.add_field(name="Reason: ", value=reason, inline=True)
            embed.add_field(name="Time: ", value=f"{time}{d}", inline=True)
            embed.add_field(name="Staff: ", value=f'{ctx.author.mention}', inline=True)
            await ctx.send(embed=embed)
            channel = bot.get_channel(833068492034277387)
            await channel.send(embed=embed)

            if d == "s":
                await asyncio.sleep(time)

            if d == "m":
                await asyncio.sleep(time*60)

            if d == "h":
                await asyncio.sleep(time*60*60)

            if d == "d":
                await asyncio.sleep(time*60*60*24)

            await member.remove_roles(role)


            await ctx.send(embed=embed)

            return

@bot.command()
@commands.cooldown(1, 2)
async def help(ctx, page=0):
    if page == 0:
        await ctx.message.delete()
        embed=discord.Embed(title="General Commands", color=0x66b7f5)
        embed.set_author(name="MCM Bot", icon_url="https://media.discordapp.net/attachments/307226054068666371/825085476045455360/d27f8f7dcdc46c86a465c533cd6397e7_1.png?width=473&height=473")
        embed.add_field(name="m!help {page}", value="See a list of all the commands.", inline=False)
        embed.add_field(name="m!support", value="Tells you how to get help.", inline=False)
        embed.add_field(name="m!dog", value="Shows a random picture of a dog.", inline=False)
        embed.set_footer(text="page 1/2")
        await ctx.send(embed=embed)
    elif page == 1:
        await ctx.message.delete()
        embed=discord.Embed(title="Prefix is: m!", color=0x66b7f5)
        embed.set_author(name="MCM Bot", icon_url="https://media.discordapp.net/attachments/307226054068666371/825085476045455360/d27f8f7dcdc46c86a465c533cd6397e7_1.png?width=473&height=473")
        embed.add_field(name="m!help", value="See a list of all the commands.", inline=False)
        embed.add_field(name="m!support", value="Tells you how to get help.", inline=False)
        embed.add_field(name="m!dog", value="Shows a random picture of a dog.", inline=False)
        embed.set_footer(text="page 1/2")
        await ctx.send(embed=embed)
    if page == 2:
        await ctx.message.delete()
        embed=discord.Embed(title="Moderation Commands", color=0x66b7f5)
        embed.set_author(name="MCM Bot", icon_url="https://media.discordapp.net/attachments/307226054068666371/825085476045455360/d27f8f7dcdc46c86a465c533cd6397e7_1.png?width=473&height=473")
        embed.add_field(name="m!purge {int}", value="Clears a given number of messages. Default is 30.", inline=False)
        embed.add_field(name="m!kick {id} {reason}", value="Kicks a user for a given reason.", inline=False)
        embed.add_field(name="m!ban {id} {reason}", value="Bans a user for a given reason.", inline=False)
        embed.add_field(name="m!mute {id} {time} {m, s h, d} {reason}", value="Mutes a user for a given amount of time for a given reason.", inline=False)
        embed.add_field(name="m!modlog {punishment} {user} {reason}", value="Logs an infraction. (Used in log channel) ", inline=False)
        embed.set_footer(text="page 2/2")
        await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        retryAfter = [math.floor(error.retry_after / 360), math.floor(error.retry_after / 60), error.retry_after % 60]
        await ctx.send('You cannot use this command `%s%s` for %s hours, %s minutes, and %.2f seconds.' % (
        str(bot.command_prefix), str(ctx.command), retryAfter[0], retryAfter[1], retryAfter[2]))
        print('Command "%s" is on a %.3f second cooldown' % (ctx.command, error.retry_after))

@bot.command()
async def restart(ctx):
    if ctx.author.id == 773904976245948426:
        os.startfile(__file__)
        sys.exit()
    else:
        await ctx.send('Only LegoScrap can use this command.')

bot.run('ODMyOTg4NDA1NzAwMjMxMjQ4.YHry6A.64YpB9OspgDU8rOKJmFpGOQRfZ8')
