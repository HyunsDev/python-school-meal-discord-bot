import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!서령"):
        await message.channel.send("서령은 바보입니다.")
        await message.channel.send("서령은 천재입니다.")

    if message.content.startswith("!print"):
        msg = message.content[7:]
        # await client.get_channel(1134343877449498745).send(msg)
        # await message.channel.send(msg)
        await message.reply(msg)


@client.event
async def on_message_delete(message):
    if message.author == client.user:
        return

    if message.channel.id == 1134306694684487720:
        await message.channel.send("메세지가 삭제되었습니다.")


@client.event
async def on_message_edit(before, after):
    if before.author == client.user:
        return

    if before.channel.id == 1134306694684487720:
        await before.channel.send("메세지가 수정되었습니다.")
        await before.channel.send("수정 전 : " + before.content)
        await before.channel.send("수정 후 : " + after.content)


client.run("MTEzNDMzNjE3NzA0MjkwMzEwMQ.G2Enqo.ahVxb7I0LQ-NRfdLxhZs85z6stylTZXt6-JkUc")
