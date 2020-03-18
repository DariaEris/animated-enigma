import discord
import asyncio

from discord.ext import commands
from discord.ext.commands import Bot

client = Bot(command_prefix='!')


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("김선하 입장!")
    game = discord.Game("주시하고있다")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):


    if message.content == "캬루":
        await message.channel.send("배신자")
    if message.content == "ㅇㅅㅇ":
        await message.channel.send("ㅇㅅㅇ")
    if message.content == "ㄹㅇㅋㅋ":
        await message.channel.send("ㅇㅈ")
    if message.content == "ㅇㅈ":
        await message.channel.send("ㄹㅇㅋㅋ")

    if message.content == "살려주세요":
        embed = discord.Embed(description="", color=0x870073)
        embed.set_image(url="https://cdn.discordapp.com/attachments/676339686435848196/681987692103336109/KakaoTalk_20200221_011235521.jpg")
        await message.channel.send(embed=embed)
    if message.content == "구해주세요":
        embed = discord.Embed(description="", color=0x870073)
        embed.set_image(url="https://cdn.discordapp.com/attachments/676339686435848196/681987692103336109/KakaoTalk_20200221_011235521.jpg")
        await message.channel.send(embed=embed)
    if message.content == "살았다":
        embed = discord.Embed(description="", color=0x870073)
        embed.set_image(url="https://cdn.discordapp.com/attachments/676339686435848196/681988004805738502/c30c232e7f0fbc85.png")
        await message.channel.send(embed=embed)
    if message.content == "감사합니다":
        embed = discord.Embed(description="", color=0x870073)
        embed.set_image(url="https://cdn.discordapp.com/attachments/676339686435848196/681990235353251873/994F5D3A5E3937B014.gif")
        await message.channel.send(embed=embed)
    if message.content == "고맙습니다":
        embed = discord.Embed(description="", color=0x870073)
        embed.set_image(url="https://cdn.discordapp.com/attachments/676339686435848196/681990235353251873/994F5D3A5E3937B014.gif")
        await message.channel.send(embed=embed)
    if message.content == "야나두":
        embed = discord.Embed(description="", color=0x870073)
        embed.set_image(url="https://cdn.discordapp.com/attachments/624631240934424596/689824816378806281/Toss_profile_15787329424258032785323303290319.png")
        await message.channel.send(embed=embed)
    if message.content == "야너두":
        embed = discord.Embed(description="", color=0x870073)
        embed.set_image(url="https://cdn.discordapp.com/attachments/624631240934424596/689825803495538744/1577202032489-0.jpg")
        await message.channel.send(embed=embed)
    if message.content == "안녕히계세요":
        embed = discord.Embed(description="", color=0x870073)
        embed.set_image(url="https://cdn.discordapp.com/attachments/676339686435848196/683419993282707493/thumb-1028612757_beN1BnSD_d3fc7ba1d3a4abd4295f6e4f448c007815caed25_640x480.jpg")
        await message.channel.send(embed=embed)
    if message.content == "와":
        embed = discord.Embed(description="", color=0x870073)
        embed.set_image(url="https://cdn.discordapp.com/attachments/679904958740693003/684427530312220674/c80fdba0c6ddeb12406e44c16cb11af88a33a04e67b9a7a171a5112db448c41d505c52a9c7e01ddad827d0dabde3d1d1fd86.gif")
        await message.channel.send(embed=embed)

    if message.content == "야망했다":
            await message.channel.send("https://www.twitch.tv/ya_mang/clip/HomelyTiredPepperoniBudStar")
    if message.content == "아야야":
            await message.channel.send("https://youtu.be/D0q0QeQbw9U")
    if message.content == "유가만가":
            await message.channel.send("https://www.twitch.tv/wwg0523/clip/HeadstrongShortChickenKeyboardCat")
    if message.content == "머핀":
            await message.channel.send("https://youtu.be/PaXTSFKQR3Y")

    if message.content == '살려주세요':
        author = message.author
        role = discord.utils.get(message.guild.roles, name="살려주세요")
        await author.add_roles(role)
    if message.content == '구해주세요':
        author = message.author
        role = discord.utils.get(message.guild.roles, name="살려주세요")
        await author.add_roles(role)
    if message.content == '살았다':
        author = message.author
        role = discord.utils.get(message.guild.roles, name="살려주세요")
        await author.remove_roles(role)
    if message.content == '감사합니다':
        author = message.author
        role = discord.utils.get(message.guild.roles, name="살려주세요")
        await author.remove_roles(role)
    if message.content == '고맙습니다':
        author = message.author
        role = discord.utils.get(message.guild.roles, name="살려주세요")
        await author.remove_roles(role)
    if message.content == '!1s':
        author = message.author
        role = discord.utils.get(message.guild.roles, name="1")
        await author.add_roles(role)
        await message.channel.send('1넴 입장')
    if message.content == '!1e':
        author = message.author
        role = discord.utils.get(message.guild.roles, name="1")
        await author.remove_roles(role)
        await message.channel.send('1넴 퇴장')
    if message.content == '!2s':
        author = message.author
        role = discord.utils.get(message.guild.roles, name="2")
        await author.add_roles(role)
        await message.channel.send('2넴 입장')
    if message.content == '!2e':
        author = message.author
        role = discord.utils.get(message.guild.roles, name="2")
        await author.remove_roles(role)
        await message.channel.send('2넴 퇴장')
    if message.content == '!3s':
        author = message.author
        role = discord.utils.get(message.guild.roles, name="3")
        await author.add_roles(role)
        await message.channel.send('3넴 입장')
    if message.content == '!3e':
        author = message.author
        role = discord.utils.get(message.guild.roles, name="3")
        await author.remove_roles(role)
        await message.channel.send('3넴 퇴장')
    if message.content == '!4s':
        author = message.author
        role = discord.utils.get(message.guild.roles, name="4")
        await author.add_roles(role)
        await message.channel.send('4넴 입장')
    if message.content == '!4e':
        author = message.author
        role = discord.utils.get(message.guild.roles, name="4")
        await author.remove_roles(role)
        await message.channel.send('4넴 퇴장')
    if message.content == '!5s':
        author = message.author
        role = discord.utils.get(message.guild.roles, name="5")
        await author.add_roles(role)
        await message.channel.send('5넴 입장')
    if message.content == '!5e':
        author = message.author
        role = discord.utils.get(message.guild.roles, name="5")
        await author.remove_roles(role)
        await message.channel.send('5넴 퇴장')

client.run("Njg5NzkyNDA4NjgyMTAyODEz.XnILSQ.U8xXahqxtA2-V5javQtkWidv6Lo")

