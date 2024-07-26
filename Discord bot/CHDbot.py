import asyncio
import discord
import random

from discord.ext import commands

bot = commands.Bot(command_prefix='*')
TOKEN = '보안상의 이유로 비공개'
@bot.event


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('명령어는 *명령어로 볼 수 있습니다.'))
    print('[알림][성공적으로 구동되었습니다.]')
@bot.command()
async def 출석(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention}님 출석 확인했습니다.')
@bot.command()
async def kdk(ctx):
    guild_list = bot.guilds
    for i in guild_list:
        await ctx.channel.send(f"Guild ID: {i.id} / Guild Name: {i.name}")

@bot.command()
async def 명령어(ctx):
    await ctx.channel.send("""```사용 가능한 명령어는 다음과 같습니다.
    *명렁어-사용 가능한 명령어들을 보여줍니다.
    *음성채널들어와-CHD봇을 음성채널에 불러옵니다.
    *음성채널나와-CHD봇이 음성채널에서 나옵니다.
    *(이모티콘 이름)-CHD봇이 이모티콘을 보내줍니다.
    *이모티콘리스트-사용 가능한 이모티콘의 목록을 볼 수 있습니다.
    *재생-유튜브링크-CHD봇이 음악을 재생합니다. 꼭 봇이 음성채널에 들어왔는지 확인하세요!!
    *음악끝-음악 재생을 멈춥니다.
    *주사위-CHD봇이 주사위를 던져줍니다.
    *출석-출석을 할 수 있습니다.
추후 더 많은 명령어, 이모티콘들이 추가될 예정입니다.
개발자는 사용자명#8900입니다.```""")
@bot.command()
async def 교대목록(ctx):
    await ctx.channel.send("""<:04:870931966550216705> <:05:871324356037459968> <:06:871324692714246154> <:07:871325214477283328> <:08:871325276380999682> <:09:871325330080681994> <:10:871325414746886174> <:11:871325467318308864> <:12:871325567520227328> <:13:871326104206581772> <:14:871326334658420736> """)
@bot.command()
async def 너굴너굴(ctx):
    await ctx.channel.send("""너굴너굴 <:02:869959152913489950>""")
@bot.command()
async def 말시리즈(ctx):
    ksk="""
*드릴말-<:16:886859072517853204>
*따뜻한말-<:18:887152769209864232>
*할말없음-<:17:887146967585652747>
    """
    await ctx.channel.send(ksk)

@bot.command()
async def 이모티콘리스트(ctx):
    embed = discord.Embed(title="사용 가능한 이모티콘 목록", description="""사용 가능한 이모티콘들 (가나다순)
    *가스해라-<:21:888945407252643851>
    *그렇구나-<:02:885099553102118922>
    *귀차너-<:13:886540614710198343> 
    *꺄항-<:07:886422754595860560>
    *나쁜녀석아-<:04:885379432372645908>
    *드릴말-<:16:886859072517853204>
    *따뜻한말-<:18:887152769209864232>
    *문과까지마-<:22:889513743615143956>
    *선비-<:20:887631634898235422>
    *손절-<:19:887588227412791346>
    *안돼-<:10:886536397882785824>
    *어지러워-<:14:886573451048001576>
    *어쩌라구-<:12:886423955290869761>
    *와정말요-<:06:885889867186339870>
    *잘자-<:01:885046485102755871>
    *저용-<:09:886448071637078086>
    *최고야-<:05:885886919366553720>
    *ㅋㅋㅋ-<:03:885101873391079454>
    *하트-<:15:886574118001082368> 
    *한방에주님곁으로-<:23:889514542839775263>
    *할말없음-<:17:887146967585652747>
    *화이팅-<:11:886423615237672961>
    실제 사용시 위의 크기보다 훨씬 크게 나오는거 유의하세요!!""", color=0x62c1cc)
    await ctx.send(embed=embed)
@bot.command()
async def 한방에주님곁으로(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/889514589983768586/a29570a18a694fa6.jpg")
    await ctx.send(embed=embed)
@bot.command()
async def 문과까지마(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/889513697330987058/1313ff31f9bb70d6.jpg")
    await ctx.send(embed=embed)
@bot.command()
async def 가스해라(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/888945468753711134/40dbda2cb47dada3.png")
    await ctx.send(embed=embed)
@bot.command()
async def 선비(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/887594474526638150/887615268333948959/received_465486551355089.jpeg")
    await ctx.send(embed=embed)
@bot.command()
async def 손절(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/887587630118731796/03be269ad5a66a42.jpeg")
    await ctx.send(embed=embed)
@bot.command()
async def 따뜻한말(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/887152712301559828/3e121723fb762b88.jpg")
    embed.set_footer(text="출처:http://www.todayhumor.co.kr/board/view.php?table=bestofbest&no=228306")
    await ctx.send(embed=embed)
@bot.command()
async def 할말없음(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/887146850744959036/340c9eef69316909.jpg")
    embed.set_footer(text="출처:http://www.todayhumor.co.kr/board/view.php?table=bestofbest&no=228306")
    await ctx.send(embed=embed)
@bot.command()
async def 드릴말(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885100653456797696/886859022857281546/8f7d1da65b0ca07e.jpg")
    embed.set_footer(text="출처:http://www.todayhumor.co.kr/board/view.php?table=bestofbest&no=228306")
    await ctx.send(embed=embed)
@bot.command()
async def 하트(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/886574176360607744/15.png")
    embed.set_footer(text="출처:https://m.blog.naver.com/fkdzksla/221983084430")
    await ctx.send(embed=embed)
@bot.command()
async def 어지러워(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/886573489304244224/14.png")
    embed.set_footer(text="출처:https://m.blog.naver.com/fkdzksla/221983084430")
    await ctx.send(embed=embed)

@bot.command()
async def 귀차너(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/886540740040208394/13.png")
    embed.set_footer(text="출처:https://m.blog.naver.com/fkdzksla/221983084430")
    await ctx.send(embed=embed)
@bot.command()
async def 안돼(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/886536489746432030/0ee1812fb58b8775.png")
    embed.set_footer(text="출처:https://m.blog.naver.com/fkdzksla/221983084430")
    await ctx.send(embed=embed)
@bot.command()
async def 저용(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/886447923993399316/26f1fdeb013e2a65.png")
    embed.set_footer(text="출처:https://m.blog.naver.com/fkdzksla/221983084430")
    await ctx.send(embed=embed)

@bot.command()
async def 어쩌라구(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885100653456797696/886423908851523664/12.png")
    embed.set_footer(text="출처:https://m.blog.naver.com/fkdzksla/221983084430")
    await ctx.send(embed=embed)
@bot.command()
async def 화이팅(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885100653456797696/886423676248002570/11.png")
    embed.set_footer(text="출처:https://m.blog.naver.com/fkdzksla/221983084430")
    await ctx.send(embed=embed)
@bot.command()
async def 꺄항(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/886422672177774602/86803c1c86422e9c.png")
    embed.set_footer(text="출처:https://m.blog.naver.com/fkdzksla/221983084430")
    await ctx.send(embed=embed)
@bot.command()
async def 와정말요(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/885889839852056657/6.png")
    embed.set_footer(text="출처:https://m.blog.naver.com/fkdzksla/221983084430")
    await ctx.send(embed=embed)
@bot.command()
async def 최고야(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/885886882569916436/878fdb498ba110dc.png")
    embed.set_footer(text="출처:https://m.blog.naver.com/fkdzksla/221983084430")
    await ctx.send(embed=embed)
@bot.command(name="나쁜녀석아")
async def 나쁜녀석아(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/885379529189756978/a05ed21a59a11b17.png")
    embed.set_footer(text="출처:https://m.blog.naver.com/fkdzksla/221983084430")
    await ctx.send(embed=embed)
@bot.command(name="ㅋㅋㅋ")
async def ㅋㅋㅋ(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/885297813238448209/55d74a8b2c6cba2e.png")
    embed.set_footer(text="출처:https://m.blog.naver.com/fkdzksla/221983084430")
    await ctx.send(embed=embed)
@bot.command()
async def CHD(ctx):
    await ctx.channel.send("""<:ccc:885045438837841920>""")
@bot.command()
async def 잘자(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/885058155044806696/wkf.png")
    embed.set_footer(text="출처:https://m.blog.naver.com/fkdzksla/221983084430")
    await ctx.send(embed=embed)
@bot.command()
async def 가스실로(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/885104209438056508/cd67126550c536d5.gif")
    await ctx.send(embed=embed)
@bot.command()
async def 그렇구나(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"""{ctx.message.author}""", description="", color=0x62c1cc)
    embed.set_image(url="https://cdn.discordapp.com/attachments/885045159119716375/885099459120349224/071de28d8ca6fc24.png")
    embed.set_footer(text="출처:https://m.blog.naver.com/fkdzksla/221983084430")
    await ctx.send(embed=embed)
@bot.command(name="음성채널들어와", pass_context=True)
async def _join(ctx):
    if ctx.author.voice and ctx.author.voice.channel: # 채널에 들어가 있는지 파악
        channel = ctx.author.voice.channel # 채널 구하기
        await channel.connect() # 채널 연결
        await ctx.send("음성채널에 들어왔습니다.")
    else: # 유저가 채널에 없으면
        await ctx.send("음성 채널에 들어오셔야 사용 가능합니다.")
@bot.command(name="음성채널나와")
async def _leave(ctx):
    await bot.voice_clients[0].disconnect()
    await ctx.send("음성채널을 나갔습니다.")
@bot.command(name="주사위")
async def _leave(ctx):
    주사위=str(random.randint(1,6))
    if 주사위=="1":
        await ctx.send("이런 1이 나왔습니다. 하지만 숫자가 작은게 유리할 때도 있죠.")
    elif 주사위=="2":
        await ctx.send("2가 나왔습니다. 2가 나왔습니다.")
    elif 주사위=="3":
        await ctx.send("3이라.. 딱 중간이군요.")
    elif 주사위=="4":
        await ctx.send("친구를 만나느라 444. 4가 나왔습니다.")
    elif 주사위=="5":
        await ctx.send("5라니.. 조금 아쉬운 감이 있습니다.")
    elif 주사위=="6":
        await ctx.send("축하드립니다 가장 큰 수가 나왔어요!! 6이에요!!")
    else:
        await ctx.send("0이 나왔습니다. 혹시 무슨 음모가 읍읍!!")
@bot.command()
async def 재생(ctx, url):
    channel = ctx.author.voice.channel
    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    await ctx.send("음악 재생을 성공하였습니다.")
@bot.command()
async def 음악끝(ctx):
    await bot.voice_clients[0].disconnect()
    if bot.voice_clients[0].is_playing():
        bot.voice_clients[0].stop()
        await ctx.send("음악 재생을 중단했습니다.")
    else:
        await ctx.send("음악이 이미 멈춰있거나 음악을 틀지 않았을 수도 있어요.")
bot.run('보안상의 이유로 비공개') #맨 끝에 적기