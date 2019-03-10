import discord

import os

client = discord.Client()


@client.event
async def on_ready():
    print("로그인")

    print(client.user.name)

    print(client.user.id)

    print("------------------")

    await client.change_presence(game=discord.Game(name='$help', type=2))


@client.event
async def on_message(message):
    if message.content.startswith('$help'):
        embed = discord.Embed(title="마주봇 도움말",
                              description="$help - 마주봇의 도움말을 불러옵니다.\n$트위치 - 마주의 트위치 채널을 불러옵니다.\n$유튜브 - 마주의 유튜브 채널을 불러옵니다.\n$마주 - 마주의 소개를 불러옵니다.\n$팀 퐁당나리 / $팀퐁당나리 - 마주가 속해있는 팀 퐁당나리의 정보를 불러옵니다.\n$신고 (내용) - 신고 내용이 마주에게 전달됩니다.\n$건의 (내용) - 건의 내용이 마주에게 전달됩니다.",
                              color=0x188bb4)

        embed.set_footer(text="Made by 마주 MAJU_#0098")

        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('$신고'):
        text = ""

        learn = message.content.split(" ")

        vrsize = len(learn)

        vrsize = int(vrsize)

        for i in range(1, vrsize):

            text = text + learn[i]

        learn = message.content.split(" ")
        msg = '{0.author.mention}'.format(message) + '님이 신고하셨습니다.' + '\n 신고내용' + '' + text + ''
        user = await client.get_user_info(348435464144945164)
        await client.send_message(user, msg)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
