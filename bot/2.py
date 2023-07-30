import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

# 생략

bot = commands.Bot(command_prefix="!", intents=intents)

# 생략


@bot.tree.command(name="hello", description="testing")  # 명령어 이름, 설명
@discord.app_commands.describe(text1="쓸 내용", text2="번호")  # 같이 쓸 내용들
async def hello(interaction: discord.Interaction, text1: str, text2: int):  # 출력
    await interaction.response.send_message(
        f"{interaction.user.mention} : {text1} : {text2}", ephemeral=True
    )


bot.run("MTEzNDI5NDc4OTkxNTkzODkwNw.GFl7Tm.JJbwg8vz_p9XN8mxeO7_RHDYtQMzO6SOih_ndw")
