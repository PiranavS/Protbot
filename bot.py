import discord
from discord.ext import commands
from googleapiclient.discovery import build

youtube=build('youtube','v3',developerKey='AIzaSyDmeKQ71AAJksvhHbzxycrAaZ6VlfcfQfk')


client=commands.Bot(command_prefix = ">")


@client.event
async def on_ready():
	print("Let's kick ass")

@client.event
async def on_message(message):
		if message.content.startswith('>ytstat') :
			chl=message.content[8:len(message.content):1]
			request=youtube.channels().list(part="statistics", forUsername=chl)
			response=request.execute()
			viewers=response['items'][0]['statistics']['viewCount'] + ' viewers'
			subscribers=response['items'][0]['statistics']['subscriberCount'] + ' subscribers'
			videos=response['items'][0]['statistics']['videoCount'] + ' videos'
			await message.channel.send(chl)
			await message.channel.send(viewers)
			await message.channel.send(subscribers)
			await message.channel.send(videos)

	#await message.channel.send(message.content)


@client.command()
async def hello(ctx):
	await ctx.send("hi")

@client.command()
async def thanks(ctx):
	await ctx.send("Welcome")

@client.command()
async def arigato(ctx):
	await ctx.send("Do itashimashite")

@client.command(aliases=["mb","maari boys"])
async def maariboys(ctx):
	await ctx.send("World's Greatest")

@client.command()
async def clear(ctx, amount=1):
	await ctx.channel.purge(limit=amount)

@client.command()
async def ping(ctx):
	await ctx.send(f"Bot latency: {client.latency*1000} ms")

client.run("NzgwNjY1MDIzNDMzMTQ2Mzcw.X7yY9Q.S2OVfXEM-DAjS-RPoZMdgEJPg38")
