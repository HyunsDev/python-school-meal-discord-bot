import discord
from datetime import datetime
import requests

intents = discord.Intents.all()
client = discord.Client(intents=intents)

riot_token = "RGAPI-a6828aea-814a-4358-ae9c-c950e7aa758a"
base_url = "https://kr.api.riotgames.com"
request_headers = {
    "X-Riot-Token": riot_token,
}


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

    if message.content.startswith("!lol summoner "):
        summoner_name = message.content[14:]
        res = requests.get(
            f"{base_url}/lol/summoner/v4/summoners/by-name/{summoner_name}",
            headers=request_headers,
        )
        summoner = res.json()
        summoner_name = summoner["name"]
        summoner_level = summoner["summonerLevel"]
        summoner_id = summoner["id"]
        summoner_account_id = summoner["accountId"]

        res = requests.get(
            f"{base_url}/lol/league/v4/entries/by-summoner/{summoner_id}",
            headers=request_headers,
        )
        league_entries = res.json()

        if len(league_entries) == 0:
            embed = discord.Embed(
                title=f"{summoner_name}님의 전적",
                description=f"레벨: {summoner_level}",
                timestamp=datetime.now(),
                color=0x00FF00,
            )

            embed.add_field(
                name="리그",
                value=f"Unranked",
                inline=False,
            )

            await message.channel.send(embed=embed)
            return

        league_entry = league_entries[0]
        league_name = league_entry["leagueId"]
        league_tier = league_entry["tier"]
        league_rank = league_entry["rank"]
        league_points = league_entry["leaguePoints"]
        league_wins = league_entry["wins"]
        league_losses = league_entry["losses"]

        embed = discord.Embed(
            title=f"{summoner_name}님의 전적",
            description=f"레벨: {summoner_level}",
            timestamp=datetime.now(),
            color=0x00FF00,
        )

        embed.add_field(
            name="리그",
            value=f"{league_name} {league_tier} {league_rank} {league_points}LP",
            inline=False,
        )
        embed.add_field(
            name="승/패", value=f"{league_wins}승 {league_losses}패", inline=False
        )
        embed.add_field(
            name="승률",
            value=f"{round(league_wins/(league_wins+league_losses)*100, 2)}%",
            inline=False,
        )

        await message.channel.send(embed=embed)


client.run("MTEzNDMzNjE3NzA0MjkwMzEwMQ.G2Enqo.ahVxb7I0LQ-NRfdLxhZs85z6stylTZXt6-JkUc")
