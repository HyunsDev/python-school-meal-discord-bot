import discord
from datetime import datetime
import requests

riot_token = "RGAPI-a6828aea-814a-4358-ae9c-c950e7aa758a"
base_url = "https://kr.api.riotgames.com"
request_headers = {
    "X-Riot-Token": riot_token,
}

res = requests.get(
    f"{base_url}/lol/summoner/v4/summoners/by-name/Hide on bush",
    headers=request_headers,
)
print(res.json()["name"])
