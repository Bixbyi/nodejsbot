import math
import random
import asyncio
import discord
import random
import urllib
import urllib.request
import json
import random
from discord import Member
from discord.ext import commands
from urllib.request import urlopen, Request
import urllib
import urllib.request
import bs4
import os
import sys
import json
import time
import datetime
import cmd
import os
import discord
from discord.ext import commands
client = discord.Client()
bot = commands.Bot(command_prefix='hb!')
token = os.environ["token"]
class DPNK:
    def __init__(self):
        self.text = ""
        self.channels = []

        self.success = []
        self.failed = []
        self.channel_cant_make = []

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('접두사는 hb! 입니까, 초대는 hb!초대 입니다'))
    print('뀨뀨뀨뀨뀨뀨ㅠㄲ뀨')
@bot.command()
async def 여담(ctx):
    await ctx.send("참고로 3번 날림 ㅋㅋㅋㅋ")
@bot.command()
async def 하이빅스비(ctx):
    await ctx.send("네? 왜 부르신가요?")
@bot.command()
async def 삼성(ctx):
    await ctx.send("노코멘트 하겠습니다.")
@bot.command()
async def 얼굴(ctx):
    await ctx.send("이츠 라이 도그 랄까나?")
@bot.command()
async def 시리(ctx):
    await ctx.send("너 밴")
@bot.command()
async def 시리야(ctx):
    await ctx.send("야이 놈 진짜 캌 퉤")
@bot.command()
async def 핑(ctx):
    latancy = bot.latency
    ping = int(latancy * 1000)
    embed = discord.Embed(colour=0x00fff0)
    embed.add_field(name="현재 빅스비시의 풍속은.. 읍읍", value=str(ping)+'m/s입니다')
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.send(embed=embed)
@bot.command()
async def 빅스비(ctx):
    await ctx.send("왜 그러신가요")
@bot.command()
async def 암호(ctx):
    await ctx.send("mrahCyP")
@bot.command()
async def 파이썬(ctx):
    await ctx.send("내 모국어!")
@bot.command()
async def 레게노(ctx):
    await ctx.send("ㄹ ㅔ ㄱ ㅔ ㄴ ㅗ")
@bot.command()
async def 주사위(ctx):
    nansu = random.randint(1, 8)
    if nansu == 1:
        embed = discord.Embed(colour=0x000000)
        embed.add_field(name='주사위의 값은..?',value=':game_die::one:')
        await ctx.send(embed=embed)
    if nansu == 2:
        embed = discord.Embed(colour=0x000000)
        embed.add_field(name='주사위의 값은..?',value=':game_die::two:')
        await ctx.send(embed=embed)
    if nansu == 3:
        embed = discord.Embed(colour=0x000000)
        embed.add_field(name='주사위의 값은..?',value=':game_die::three:')
        await ctx.send(embed=embed)
    if nansu == 4:
        embed = discord.Embed(colour=0x000000)
        embed.add_field(name='주사위의 값은..?',value=':game_die::four:')
        await ctx.send(embed=embed)
    if nansu == 5:
        embed = discord.Embed(colour=0x000000)
        embed.add_field(name='주사위의 값은..?',value=':game_die::five:')
        await ctx.send(embed=embed)
    if nansu == 6:
        embed = discord.Embed(colour=0x000000)
        embed.add_field(name='주사위의 값은..?',value=':game_die::six:')
        await ctx.send(embed=embed)
    if nansu == 7:
        embed = discord.Embed(colour=0x000000)
        embed.add_field(name='주사위의 값은..?',value=':game_die::seven:  ..? 뭐임')
        await ctx.send(embed=embed)
@bot.command()
async def 애교해줘(ctx):
    await ctx.send("**`?`**")
@bot.command()
async def 깡(ctx):
    await ctx.send(":bulb::bulb::bulb::bulb::bulb:")
    await ctx.send(":bulb::bulb::bulb::bulb::bulb:")
    await ctx.send(":bulb::bulb::detective::bulb::bulb:")
    await ctx.send(":bulb::bulb::bulb::bulb::bulb:")
    await ctx.send(":bulb::bulb::bulb::bulb::bulb:")
    await ctx.send("화려한 조명이 나를 감싼적이 없는데요")
@bot.command()
async def 정보(ctx):
    import datetime
    date = datetime.datetime.utcfromtimestamp(((int(ctx.author.id) >> 22) + 1420070400000) / 1000)
    embed = discord.Embed(colour=0x00ffd5)
    embed.add_field(name='이름', value=ctx.author.name, inline=True)
    embed.add_field(name='서버별명', value=ctx.author.display_name, inline=True)
    embed.add_field(name='가입일', value=str(date.year) + '년 ' + str(date.month) + '월 ' + str(date.day) + '일 ' + str(
        date.hour) + '시 ' + str(date.minute) + '분 ' + str(date.second) + '초', inline=False)
    embed.add_field(name='아이디', value=ctx.author.id, inline=True)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.send(embed=embed)
@bot.command()
async def 구글(ctx):
    cnt1 = ctx.message.content[6:]
    url = "https://www.google.com/search?q=" + str(cnt1) + "&oq=" + str(cnt1) + '&aqs=chrome.0.69i59j0l7.246j0j7&sourceid=chrome&ie=UTF-8'
    embed = discord.Embed(title='구글', url=url, description='이 위는 구글입니다', color=0x00ffd5, inline=False)
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.send(embed=embed)
    if cnt1 == '삼성':
        ur1 = "https://www.google.com/search?q=당근&oq=당근&aqs=chrome.0.69i59j0l7.246j0j7&sourceid=chrome&ie=UTF-8"
        embed = discord.Embed(title='구글', url=ur1, description='이 위는 구글입니다', color=0x00ffd5, inline=False)
        embed.set_footer(text='건의는 Bixby#9703')
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)
@bot.command()
async def 네이버(ctx):
    msg = ctx.message.content[7:]
    url2 = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=" + str(msg)
    embed = discord.Embed(title='네이버', url=url2, description='이 위는 네이버입니다', color=0x11ff00)
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.send(embed=embed)
@bot.command()
async def 다음(ctx):
    msg = ctx.message.content[6:]
    url3 = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=" + str(msg)
    embed = discord.Embed(title='다음', url=url3, description='이 위는 다음입니다', colour=0x001aff)
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.send(embed=embed)
@bot.command()
async def 사전(ctx):
    msg = ctx.message.content[6:]
    url4 = 'https://stdict.korean.go.kr/search/searchResult.do?pageSize=10&searchKeyword=' + str(msg)
    embed = discord.Embed(title='사전', url=url4, description='이 위는 국립국어원 표준대국어사전입니다', colour=0xeb9e34)
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.send(embed=embed)
@bot.command()
async def 나무위키(ctx):
    msg = ctx.message.content[8:]
    url5 = 'https://namu.wiki/w/' + str(msg)
    embed = discord.Embed(title='ㄲㅁㅇㅋ', url=url5, description='이 위는 나무위키입니다.. :off:', colour=0x34eb7d)
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.message.add_reaction(emoji='✖')
    await ctx.send(embed=embed)
@bot.command()
async def 정봇(ctx):
    import datetime
    date = datetime.datetime.utcfromtimestamp(((int(bot.user.id) >> 22) + 1420070400000) / 1000)
    embed = discord.Embed(colour=0x00ffd5)
    embed.add_field(name='이름', value=bot.user.name, inline=True)
    embed.add_field(name='서버별명', value=bot.user.display_name, inline=True)
    embed.add_field(name='가입일', value=str(date.year) + '년 ' + str(date.month) + '월 ' + str(date.day) + '일 ' + str(date.hour) + '시 ' + str(date.minute) + '분 ' + str(date.second) + '초', inline=False)
    embed.add_field(name='아이디', value=bot.user.id, inline=True)
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.send(embed=embed)
@bot.command()
async def 뀨(ctx):
    await ctx.send('갈고리')
@bot.command()
async def 초대(ctx):
    url6 = 'https://discord.com/oauth2/authorize?client_id=725583059654672415&scope=bot'
    embed = discord.Embed(title='초대해라 인간들이여', url=url6, description='초대 하실려고요? 감사합니다..?', colour=0x34eb7d)
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.send(embed=embed)
@bot.command()
async def 현재(ctx):
    await ctx.send('자 현재의 시간과 월일은..? 60초 후에 공개됩니다!')
    await asyncio.sleep(60)
    a = datetime.datetime.today().month
    b = datetime.datetime.today().day
    c = datetime.datetime.today().hour
    d = datetime.datetime.today().minute
    e = datetime.datetime.today().second
    f = datetime.datetime.today().microsecond
    await ctx.send(str(a)+'월 '+str(b)+'일 '+str(c)+'시'+str(d)+'분 '+str(e)+'초 '+str(f)+'마이크로세컨드')
@bot.command (pass_context=True)
async def 랜덤(ctx,amount,amount2):
    import random
    picked = random.randint(int(amount), int(amount2))
    await ctx.send('결랜 과 !덤는의 : ' +str(picked))
@bot.command( pass_context=True)
async def 나가(ctx, *, user_name: discord.Member):
    msg = ctx.message.content[6:]
    await user_name.kick(reason=msg)
    await ctx.send(str(user_name)+"을(를) 추방하였습니다.")
@bot.command(pass_context=True)
async def 꺼져(ctx, *, user_name: discord.Member):
    msg = ctx.message.content[6:]
    await user_name.ban()
    embed = discord.Embed(discord.Colour.red())
    embed.add_field(name='꺼진 자의 이름',value=user_name)
    embed.add_field(name='이유는..',value=msg)
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def 켜져(ctx, *, user_name):
    msg = ctx.message.content[6:]
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = user_name.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention}을(를) 회생시켰습니다.")
            return
@bot.command()
async def 포켓인(ctx,authour):
    gender = ('男(남)','女(녀)','中性(중성)')
    s = random.sample(gender, 1)
    msg = ctx.message.content[7:]
    embed = discord.Embed(colour=0xff0019)
    embed.add_field(name='.',value='포켓인의 이름은!  '+str(authour)+'!', inline=False)
    embed.add_field(name='성별', value=str(s)+'!')
    embed.add_field(name='.',value='포켓인 정보! : ' + str(msg), inline=False)
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.send(embed=embed)
@bot.command( pass_context=True)
async def 보내기(ctx, user_name: discord.Member,content):
    channel = await user_name.create_dm()
    await channel.send(f'```{content}```')
    await channel.send(str(ctx.author.name)+'님이 보내셨어요')
@bot.command()
async def 영어(ctx):
    from googletrans import Translator
    translator = Translator()
    msg = ctx.message.content[6:]
    result = translator.translate(msg, dest="en")
    embed = discord.Embed(colour=0x42f5f5)
    embed.add_field(name='번역결과 쌍점', value=result.text)
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.send(embed=embed)
@bot.command()
async def 중국어(ctx):
    from googletrans import Translator
    translator = Translator()
    msg = ctx.message.content[7:]
    result = translator.translate(msg, dest="zh-CN")
    embed = discord.Embed(colour=0x42f5f5)
    embed.add_field(name='번역결과 쌍점', value=result.text)
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.send(embed=embed)
@bot.command()
async def 일본어(ctx):
    from googletrans import Translator
    msg = ctx.message.content[7:]
    translator = Translator()
    result = translator.translate(msg, dest="ja")
    embed = discord.Embed(colour=0x42f5f5)
    embed.add_field(name='번역결과 쌍점', value=result.text)
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.send(embed=embed)
@bot.command()
async def 한국어(ctx):
    from googletrans import Translator
    msg = ctx.message.content[7:]
    translator = Translator()
    result = translator.translate(msg, dest="ko")
    embed = discord.Embed(colour=0x42f5f5)
    embed.add_field(name='번역결과 쌍점', value=result.text)
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.send(embed=embed)
@bot.command()
async def 러시아어(ctx):
    from googletrans import Translator
    translator = Translator()
    msg = ctx.message.content[8:]
    result = translator.translate(msg, dest="ru")
    embed = discord.Embed(colour=0x42f5f5)
    embed.add_field(name='번역결과 쌍점', value=result.text)
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.send(embed=embed)
@bot.command()
async def 라틴어(ctx):
    from googletrans import Translator
    translator = Translator()
    msg = ctx.message.content[7:]
    result = translator.translate(msg, dest="la")
    embed = discord.Embed(colour=0x42f5f5)
    embed.add_field(name='번역결과 쌍점', value=result.text)
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.send(embed=embed)
@bot.command()
async def 돈줘(ctx):
    await ctx.send('돈줘')
@bot.command()
async def 첵스초코(ctx):
    await ctx.send("드디어 민주주의가 독재주의를 이겨 냈습니다! 이것이 국민들의 힘입니다! 여러분들 - 차카")
@bot.command()
async def 초알림(ctx,amount):
    await ctx.send(f'{amount}초 뒤에 알림이 뜹니다')
    amount1 = int(amount) * 1
    await asyncio.sleep(amount1)
    await ctx.send(f'{amount}초가 다 끝났네요')
@bot.command()
async def 분알림(ctx,amount):
    await ctx.send(f'{amount}분 뒤에 알림이 뜹니다')
    amount1 = int(amount) * 60
    await asyncio.sleep(amount1)
    await ctx.send(f'{amount}분이 다 끝났네요')
@bot.command()
async def 시간알림(ctx,amount):
    await ctx.send(f'{amount}시간 뒤에 알림이 뜹니다')
    amount1 = int(amount) * 3600
    await asyncio.sleep(amount1)
    await ctx.send(f'{amount}시간이 다 끝났네요')
@bot.command()
async def 일알림(ctx,amount):
    await ctx.send(f'{amount}일 뒤에 알림이 뜹니다')
    amount1 = int(amount) * 86400
    await asyncio.sleep(amount1)
    await ctx.send(f'{amount}일이 다 끝났네요')
@bot.command()
async def 출근(ctx):
    if ctx.author.permissions_in(ctx.channel).manage_messages:
        await bot.change_presence(activity=discord.Game(f'{ctx.author.name}님이 출근하셨습니다'))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game('접두사는 hb! 입니까, 초대는 hb!초대 입니다'))
@bot.command()
async def 퇴근(ctx):
    if ctx.author.permissions_in(ctx.channel).manage_messages:
        await bot.change_presence(activity=discord.Game(f'{ctx.author.name}님이 퇴근하셨습니다'))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game('접두사는 hb! 입니까, 초대는 hb!초대 입니다'))
@bot.command()
async def 욕해줘(ctx):
    await ctx.send('싫어 ㅅㅂ롬아')
    await ctx.channel.purge(limit=1)
@bot.command()
async def 랜덤상식(ctx):
    common = '커피에 카페인은 약40 mg입니다','박카스는 D,F 말고 D카페인도 있어요'
    상식 = random.sample(common,1)
    await ctx.send('랜덤 상식! 그 상식은!'+str((상식)))
@bot.command()
async def 게임1(ctx,amount):
    n = int(amount) * int(random.randint(-4,4))
    await ctx.send(str(n)+'코인을 당신이 얻었읍니다')
@bot.command()
async def 게임2(ctx):
    title = ('마인크래프트','암호화폐','봇','웹사이트','언어')
    title1 = random.sample(title,1)
    embed = discord.Embed(colour=0x000000)
    embed.add_field(name='주제는..?', value=title1)
    embed.add_field(name='시간은..?',value='10초!')
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.send(embed=embed)
    await asyncio.sleep(10)
    await ctx.send('끝났읍니다')

@bot.command()
async def 할거(ctx):
    await ctx.send("1.도박봇 2.주식봇 3.ㄹㅇ빅스비(먼미래에) 4.계산기봇 5.놀이봇 6.투명봇" )
@bot.command()
async def 추가됨(ctx):
    await ctx.send('** ``` 오늘 만든 명령어 : ``` **')
@bot.command()
async def 섭화씨(ctx,amount):
    from fractions import Fraction
    f = int(amount)*int(Fraction(9/5)) + 32
    await ctx.send(f'섭씨{f}도입니다')
@bot.command()
async def 코로나(ctx):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
    #-----------------------------------------
    req = Request(url, headers=hdr)
    html = urllib.request.urlopen(req)
    bsObj = bs4.BeautifulSoup(html, "html.parser")
    corona = bsObj.find('div', {'class': 'caseTable'})
    dateBase = bsObj.find('h5',{'class':'s_title_in3'})
    dl = corona.find_all('dl')
    #--------------------------------------
    a = dl[0]
    a1 = a.find('dd',{'class':'ca_value'})
    a2 = a1.text.strip()
    #---------------------------------------
    b = dl[1]
    b1 = b.find('p',{'class':'inner_value'})
    b2 = b1.text.strip()
    #----------------------------------------
    c = dl[2]
    c1 = c.find('dd', {'class': 'ca_value'})
    c2 = c1.text.strip()
    #----------------------------------------
    d = dl[3]
    d1 = d.find('span', {'class': 'txt_ntc'})
    d2 = d1.text.strip()
    #----------------------------------------
    e = dl[4]
    e1 = e.find('dd', {'class': 'ca_value'})
    e2 = e1.text.strip()
    #----------------------------------------
    f = dl[5]
    f1 = f.find('span', {'class': 'txt_ntc'})
    f2 = f1.text.strip()
    #----------------------------------------
    g = dl[6]
    g1 = g.find('dd', {'class': 'ca_value'})
    g2 = g1.text.strip()
    # ----------------------------------------
    h = dl[7]
    h1 = h.find('span', {'class': 'txt_ntc'})
    h2 = h1.text.strip()
    #----------------------------------------
    i = dateBase.find('span',{'class':'t_date'})
    i2 = i.text.strip()
    embed = discord.Embed(colour=0xff0000, title='개같은 코로나의 행적')
    embed.add_field(name='누적확진자', value=f'{a2}명 ({b2})', inline=True)
    embed.add_field(name='격리해제', value=f'{c2}명 ({d2})', inline=True)
    embed.add_field(name='격리중', value=f'{e2}명 ({f2})', inline=True)
    embed.add_field(name='사망..', value=f'{g2}명 ({h2})', inline=True)
    embed.add_field(name='참고', value=i2, inline=False)
    embed.add_field(name='사이트!', value=url, inline=True)
    embed.set_footer(text='우리 모두 견뎌 냅시다! (건의는 Bixby#9703)')
    await ctx.send(embed=embed)
@bot.command()
async def 날씨(ctx,location):
    enc_location = urllib.parse.quote(location + '날씨')
    hdr = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location

    req = Request(url, headers=hdr)
    html = urllib.request.urlopen(req)
    bsObj = bs4.BeautifulSoup(html, "html.parser")
    todayBase = bsObj.find('div', {'class': 'main_info'})

    todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
    todayTemp = todayTemp1.text.strip()  # 온도


    todayValueBase = todayBase.find('ul', {'class': 'info_list'})
    todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
    todayValue = todayValue2.text.strip()  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌


    todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
    todayFeelingTemp = todayFeelingTemp1.text.strip()  # 체감온도


    todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
    todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
    todayMiseaMongi3 = todayMiseaMongi2.find('dd')
    todayMiseaMongi = todayMiseaMongi3.text  # 미세먼지


    tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
    tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
    tomorrowTemp2 = tomorrowTemp1.find('dl')
    tomorrowTemp3 = tomorrowTemp2.find('dd')
    tomorrowTemp = tomorrowTemp3.text.strip()  # 오늘 오전,오후온도

    tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
    tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
    tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
    tomorrowMoring = tomorrowMoring2.text.strip()  # 내일 오전 온도

    tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
    tomorrowValue = tomorrowValue1.text.strip()  # 내일 오전 날씨상태, 미세먼지 상태

    tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
    tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
    tomorrowAfter1 = tomorrowAllFind[1]
    tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
    tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
    tomorrowAfterTemp = tomorrowAfter3.text.strip()  # 내일 오후 온도

    tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
    tomorrowAfterValue = tomorrowAfterValue1.text.strip()

    embed = discord.Embed(
        title=location + ' 날씨 정보',
        description=location + '날씨 정보입니다.',
        colour=discord.Colour.from_rgb(50, 168, 164)
    )
    embed.add_field(name='바깥온도', value=todayTemp + '˚', inline=False)  # 현재온도
    embed.add_field(name='인간들이 느끼는 온도', value=todayFeelingTemp, inline=False)  # 체감온도
    embed.add_field(name='날의 상태', value=todayValue, inline=False)  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
    embed.add_field(name='중국의 먼지 상태', value=todayMiseaMongi, inline=False)  # 오늘 미세먼지
    embed.add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False)  # 오늘날씨 # color=discord.Color.blue()
    embed.add_field(name='** **', value='** **',
                    inline=False)  # 구분선
    embed.add_field(name='내일 오전온도', value=tomorrowMoring + '˚', inline=False)  # 내일오전날씨
    embed.add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False)  # 내일오전 날씨상태
    embed.add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False)  # 내일오후날씨
    embed.add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False)  # 내일오후 날씨상태
    embed.set_footer(text='건의는 Bixby#9703')
    await ctx.send(embed=embed)
@bot.command()
async def 팩토리얼(ctx,x):
    y = int(x) * 1
    z = math.factorial(y)
    await ctx.send(f'정답은 바로!정답은 바로!정답은 바로!정답은 바로!정답은 바로! {z}')
@bot.command()
async def 갈고리(ctx):
    await ctx.send('?')
@bot.command()
async def 청소(ctx,amount : int):
    if not ctx.author.permissions_in(ctx.channel).manage_messages:
        await ctx.send('넌 관리자가 아니야')
    if ctx.author.permissions_in(ctx.channel).manage_messages:
       if 0<amount<101 :
          count = amount + 1
          await ctx.channel.purge(limit=int(count))
       if amount > 100 :
          await ctx.send('100 이상의 청소는 안돼')
       if amount < 0 or amount == 0 :
          await ctx.send('0 이하나 0개의 메세지를 지워봐 이놈아')
@bot.command()
async def 지건(ctx):
    await ctx.send('으억.. 아파 이 쉐캬')
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1)
    await ctx.send('^^7 뭔 일 있었나?')
@bot.command()
async def 프린트(ctx):
    msg = ctx.message.content[7:]
    print(str(ctx.author)+" "+str(msg))
    await ctx.send(f"{msg}을(를) 툴에 프린트하였습니다 (이거 악용하는 놈 없제)")
@bot.command()
async def 가위바위보(ctx,element=None):

    if element=='가위':
        if random.choice(["가위","바위","보"])=="가위":
            await ctx.send("무승부")
        elif random.choice(["가위","바위","보"])=="바위":
            await ctx.send("패")
        else:
            await ctx.send("승")
    if element=='바위':
        if random.choice(["가위","바위","보"])=="가위":
            await ctx.send("승")
        elif random.choice(["가위","바위","보"])=="바위":
            await ctx.send("무승부")
        else:
            await ctx.send("패")
    if element=='보':
        if random.choice(["가위","바위","보"])=="가위":
            await ctx.send("패")
        elif random.choice(["가위","바위","보"])=="바위":
            await ctx.send("승")
        else:
            await ctx.send("무승부")
    if element=='블랙홀!':
        await ctx.send("유치한놈")
    if element==None:
        await ctx.send("뭐하자는거야..")
@bot.command()
async def 계산기(ctx):
    try:
      msg = ctx.message.content[7:]
      total = eval(msg)
      await ctx.send(total)
    except ZeroDivisionError:
      await ctx.send("당신이 직접 0으로 나누어 보세요 이 나쁜 놈아")
    except SyntaxError:
        await ctx.send('으음?? 뭔 소리야?')
@bot.command()
async def ddd(ctx):
    x = random.randint(1,2)
    y = random.randint(1,2)
    z = random.randint(1,2)
    print(f'{x}{y}{z}')
    if x == 1 :
        if y == 1:
            if z == 1:
              await ctx.send(f'{x}{y}{z}')
bot.run(token)