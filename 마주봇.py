import discord
import os
client = discord.Client()


@client.event
async def on_ready():
    print("로그인")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='마주봇 실행중/m도움말', type=1))


@client.event
async def on_message(message):
    if message.content.startswith('m명령어'):
        embed = discord.Embed(title="마주봇에게 오류가 발생했습니다. 오류코드 AA0001을 개발자에게 알려주시기 바랍니다.", description="마주봇에게 오류가 발생했습니다. 오류코드 AA0001을 개발자에게 알려주시기 바랍니다.", color=0x188bb4)
        embed.set_footer(text="마주봇에게 오류가 발생했습니다. 오류코드 AA0001을 개발자에게 알려주시기 바랍니다.")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith("m 도움말"):
        await client.send_message(message.channel, "마주봇에게 오류가 발생했습니다. 오류코드 AA0001을 개발자에게 알려주시기 바랍니다.")

    if message.content.startswith("m게전서초대"):
        await client.send_message(message.channel, "마주봇에게 오류가 발생했습니다. 오류코드 AA0001을 개발자에게 알려주시기 바랍니다.")

    if message.content.startswith("m안녕"):
        await client.send_message(message.channel, "마주봇에게 오류가 발생했습니다. 오류코드 AA0001을 개발자에게 알려주시기 바랍니다.")

    if message.content.startswith("m도움말"):
        await client.send_message(message.channel, "마주봇에게 오류가 발생했습니다. 오류코드 AA0001을 개발자에게 알려주시기 바랍니다.")

    if message.content.startswith('m게전서도움말'):
        embed = discord.Embed(title="마주봇에게 오류가 발생했습니다. 오류코드 AA0001을 개발자에게 알려주시기 바랍니다.", description="마주봇에게 오류가 발생했습니다. 오류코드 AA0001을 개발자에게 알려주시기 바랍니다.", color=0x188bb4)
        embed.set_footer(text="마주봇에게 오류가 발생했습니다. 오류코드 AA0001을 개발자에게 알려주시기 바랍니다.")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith("m게전서소개"):
        await client.send_message(message.channel, "마주봇에게 오류가 발생했습니다. 오류코드 AA0001을 개발자에게 알려주시기 바랍니다.")

    if message.content.startswith("m게전서역할"):
        await client.send_message(message.channel, "마주봇에게 오류가 발생했습니다. 오류코드 AA0001을 개발자에게 알려주시기 바랍니다.")

    if message.content.startswith("m게전서관리팀"):
        await client.send_message(message.channel, "마주봇에게 오류가 발생했습니다. 오류코드 AA0001을 개발자에게 알려주시기 바랍니다.")    
    
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
