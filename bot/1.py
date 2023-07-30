import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


before_message = ""


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!save"):
        global before_message
        before_message = message.content.split("!save ")[1]
        await message.channel.send("저장 완료")

    if message.content.startswith("!load"):
        await message.channel.send(before_message)


client.run("MTEzNDI5NDc4OTkxNTkzODkwNw.GFl7Tm.JJbwg8vz_p9XN8mxeO7_RHDYtQMzO6SOih_ndw")
