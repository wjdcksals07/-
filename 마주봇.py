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
    if message.content.startswith("m도움말"):
        await client.send_message(message.channel, "마주봇의 명령어는 m(명령어) 이며, 명령어는 m명령어 를 참고하시기 바랍니다.")

    if message.content.startswith("m 도움말"):
        await client.send_message(message.channel, "올바른 사용법 : m도움말")

    if message.content.startswith("m게전서초대"):
        await client.send_message(message.channel, "https://discord.gg/pcUZFdY")

    if message.content.startswith("m신고"):
        await client.send_message(message.channel, "m게전서초대 를 통해 신고해주시기 바랍니다.")

    if message.content.startswith("m안녕"):
        await client.send_message(message.channel, "안녕하세요 반갑습니다, 마주봇입니다!")

    if message.content.startswith("m명령어"):
        await client.send_message(message.channel, "마주봇 도움말 모음 (게전서 도움말은 m게전서도움말)\nm도움말 : 도움말을 불러옵니다.\nm게전서초대 : 게임 전문 서버의 서버초대링크를 불러옵니다.\nm신고 : 신고 도움말을 불러옵니다.\nm안녕 : 마주봇이 인사합니다.")

    if message.content.startswith("m게전서도움말"):
        await client.send_message(message.channel, "게전서 도움말 모음 (m게전서초대)\nm게전서소개 : 게전서를 소개합니다.\nm게전서역할 : 게전서의 역할을 소개합니다.\nm게전서관리팀 : 서버를 위해 열심히 봉사해주시는 관리팀 분들을 소개합니다.")

    if message.content.startswith("m게전서소개"):
        await client.send_message(message.channel, "`게전서`는 `게임 전문 서버`의 줄임말입니다.\n`게임 전문 서버`는 `2018년 5월 18일`에 만들어졌으며, `대표`는 `마주`입니다.\n만든 목적은 `친목`과 `게임활동`을 위해서 개설되었으며, `다양한 게임`을 즐기고 있습니다.\n서버에서 `필요한 인재`도 구하고 `게임할 사람`도 구할 수 있으니 좋은 서버겠죠?  서버를 들어오고 싶으신 분들은 `m게전서초대`를 입력해주세요!")

    if message.content.startswith("m게전서역할"):
        await client.send_message(message.channel, "`게임 전문 서버`의 역할소개입니다.\n`Gamer` : 기본 지급 되는 역할. 일반유저이다.\n`Staff` : 서버의 스태프. 서버를 관리한다. (스태프는 면접을 보고 합격하면 승급된다.)\n`Manager` : 스태프의 팀장으로써 나중엔 어드민으로 승급한다. (스태프중 가장 활동이 많은 사람이 매니저가 된다.)\n`Admin` : 서버의 어드민으로써 서버의 모든것을 관리한다.\n`Server Owner` : 서버의 주인으로써 서버의 모든것을 관리한다.\n`죄인` : 법 채팅방에 써있는바와 같이 경고를 많이 받으면 지급되는 역할이다.\n`관리팀` : 모든 관리팀에게 지급되는 역할이다.\n`Youtuber` : 유튜버에게 지급되는 역할이다.\n`Twitch Streammer` : 트위치 스트리머에게 지급되는 역할이다.\n`Bot` : 모든 봇에게 지급되는 역할이다.\n역할 설명 끝!")

    if message.content.startswith("m게전서관리팀"):
        await client.send_message(message.channel, "`게임 전문 서버`의 `관리팀 소개`입니다.\n`마주` : 서버의 주인이자 서버의 모든것을 관리하는 서버오너이다.\n`진우` : 서버의 어드민이자 서버를 열심히 관리하고 컴퓨터를 잘 다루는 관리팀이다.\n`도현` :   서버의 매니저이자 유튜버인 관리팀이다.\n`즐겜러` : 서버의 매니저이자 게임을 좋아하는 관리팀이다.\n`미도` : 서버의 스태프이자 열심히 관리하는 관리팀이다.\n`플비` : 서버의 스태프이자 컴퓨터를 잘 다루는 관리팀이다.\n`주릭` : 서버의 스태프이자 열심히 관리하는 관리팀이다.\n`매생이` : 서버의 스태프이자 열심히 관리하는 관리팀이다.")
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
