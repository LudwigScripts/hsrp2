import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all(), help_command=None)

@bot.hybrid_command()
async def latency(ctx: commands.Context):
    latency = round(bot.latency * 1000)
    await ctx.send(f'Latency: {latency}ms')

@bot.hybrid_command()
async def say(ctx: commands.Context, *, phrase: str):
    print(f'{ctx.author} executed command /say with the phrase "{phrase}"')
    await ctx.send(phrase)

@bot.hybrid_command()
async def aboutus(ctx: commands.Context):
    await ctx.reply('𝐇𝐞𝐣 𝐨𝐜𝐡 𝐯𝐚̈𝐥𝐤𝐨𝐦𝐦𝐞𝐧 𝐭𝐢𝐥𝐥 𝐚𝐛𝐨𝐮𝐭 𝐨𝐬𝐬. 𝐕𝐢 𝐚̈𝐫 𝐞𝐧 𝐍𝐨𝐫𝐝𝐞𝐚 𝐛𝐚𝐧𝐤 𝐬𝐞𝐫𝐯𝐞𝐫 𝐢 𝐞𝐧 𝐬𝐞𝐫𝐯𝐞𝐫 𝐬𝐨𝐦 𝐚̈𝐫 𝐤𝐚𝐥𝐥𝐚𝐝 𝐇𝐮𝐝𝐝𝐢𝐧𝐠𝐞 𝐒𝐰𝐞𝐝𝐞𝐧 𝐫𝐩. 𝐡𝐨𝐬 𝐨𝐬𝐬 𝐤𝐚𝐧 𝐦𝐚𝐧 𝐭𝐚 𝐥𝐚̊𝐧 𝐬𝐤𝐚𝐟𝐟𝐚 𝐍𝐨𝐫𝐝𝐞𝐚 𝐤𝐨𝐫𝐭 𝐨𝐜𝐡 𝐦𝐚𝐬𝐬𝐚 𝐦𝐞𝐫.')
    print(f'{ctx.author} executed command /aboutus')

@bot.hybrid_command()
async def help(ctx: commands.Context):
    await ctx.reply('𝐇𝐞𝐣 𝐨𝐜𝐡 𝐯𝐚̈𝐥𝐤𝐨𝐦𝐦𝐞𝐧 𝐭𝐢𝐥𝐥 /𝐇𝐞𝐥𝐩. 𝐨𝐦 𝐝𝐮 𝐛𝐞𝐡𝐨̈𝐯𝐞𝐫 𝐡𝐣𝐚̈𝐥𝐩 𝐤𝐨𝐧𝐭𝐚𝐤𝐭𝐚 𝐞𝐧 𝐡𝐨̈𝐠 𝐮𝐩𝐩𝐬𝐚𝐭𝐭 𝐞𝐥𝐥𝐞𝐫 𝐠𝐨̈𝐫 𝐞𝐧 𝐭𝐢𝐜𝐤𝐞𝐭. 𝐌𝐞𝐫 𝐢𝐧𝐨𝐟𝐦𝐚𝐫𝐭𝐢𝐨𝐧 𝐨𝐦 𝐬𝐞𝐫𝐯𝐞𝐫𝐧 𝐟𝐢𝐧𝐧𝐬 𝐢 𝐤𝐚𝐧𝐚𝐥𝐞𝐧 <#1238254821543383152>')
    print(f'Help command was executed by {ctx.author}')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Nordea Bank"))
    print(f'{bot.user.name} has connected to Discord!')
    await bot.tree.sync()

bot.run('MTIzODUwMDAxMjM2MzYxMjE5MA.GQy7wB.aSKnrZ252oU4lI-1W4dxIjD2NUCzXTRnyzSVaU')
