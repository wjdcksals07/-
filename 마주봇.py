import discord

import os

import openpyxl

client = discord.Client()


@client.event
async def on_ready():
    print("마주봇이 정상적으로 실행되었습니다.")

    print(client.user.name)

    print(client.user.id)

    print("------------------")

    game = discord.Game("도움말 $help")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('$help'):
        embed = discord.Embed(title="마주봇 도움말",
                              description="마주봇은 관리자 전용으로 만들어졌음을 알려드립니다.\n$notice (채널아이디) (할말) - 특정 채널에 메시지를 보냅니다.\n$dm (유저아이디) (할말) - 유저에게 메시지를 보냅니다.\n$mute (유저아이디) - 유저를 뮤트 시킵니다.\n$unmute (유저아이디) - 유저의 뮤트를 해제합니다.\n$경고 (유저아이디) - 유저에게 경고를 지급합니다.",
                              color=0x188bb4)

        embed.set_footer(text="Made by 마주 MaJu_Game#0098")

        await message.channel.send(embed=embed)

    if message.content.startswith('$notice'):
        channel = message.content[8:26]
        msg = message.content[27:]
        await client.get_channel(int(channel)).send(msg)

    if message.content.startswith('$dm'):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

    if message.content.startswith('$mute'):
        author = message.guild.get_member(int(message.content[6:24]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.add_roles(role)

    if message.content.startswith('$unmute'):
        author = message.guild.get_member(int(message.content[8:26]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.remove_roles(role)

    if message.content.startswith("$경고"):
        author = message.guild.get_member(int(message.content[4:22]))
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(author.id):
                sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("경고.xlsx")
                if sheet["B" + str(i)].value == 2:
                    await message.guild.ban(author)
                    await message.channel.send("경고 2회 누적입니다. 서버에서 추방됩니다.")
                else:
                    await message.channel.send("경고를 1회 받았습니다.")
                break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(author.id)
                sheet["B" + str(i)].value = 1
                file.save("경고.xlsx")
                await message.channel.send("경고를 1회 받았습니다.")
                break
            i += 1


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
