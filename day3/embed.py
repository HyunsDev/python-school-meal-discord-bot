import discord
from datetime import datetime

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!embed"):
        embed = discord.Embed(
            title="title",
            description="description",
            url="https://hyuns.dev",
            timestamp=datetime.utcnow(),
            color=0x00FF00,
        )

        embed.set_footer(
            text="footer",
            icon_url="https://pbs.twimg.com/profile_images/431365235253862400/zReM2T9i_400x400.png",
        )
        embed.set_image(
            url="https://images.contentstack.io/v3/assets/blt370612131b6e0756/blt50837d6fac883c81/60107b5c0839e910126d7603/Teemo_Skin01.jpg"
        )
        embed.set_thumbnail(
            url="https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/bltce19ac18cfc17bb2/5efa74cfe953921d7fdeaa4c/01_Ask_Riot_Banner_Yuumi.jpg"
        )
        embed.set_author(
            name="author",
            url="https://hyuns.dev",
            icon_url="https://pbs.twimg.com/profile_images/431365235253862400/zReM2T9i_400x400.png",
        )

        embed.add_field(name="field1", value="value1", inline=False)
        embed.add_field(name="field2", value="value2", inline=True)
        embed.add_field(name="field3", value="value3", inline=True)

        await message.channel.send(embed=embed)

    if message.content.startswith("!change activity"):
        activity = message.content[17:]
        await client.change_presence(activity=discord.Game(name=activity))


client.run("MTEzNDMzNjE3NzA0MjkwMzEwMQ.G2Enqo.ahVxb7I0LQ-NRfdLxhZs85z6stylTZXt6-JkUc")
