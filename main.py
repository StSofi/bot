import discord, random, os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот который хочет помочь вас научить оберегать природу')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Пока, пока!')

@bot.command()
async def helpsea(ctx):
    await ctx.send(f'https://unsdg.un.org/ru/latest/stories/tri-deystvennykh-sposoba-pomoch-sokhranit-nashi-okeany')

@bot.command()
async def helplitter(ctx):
    await ctx.send(f'https://ria.ru/20220829/utilizatsiya-1812880941.html')

@bot.command()
async def treas(ctx):
    await ctx.send(f'https://news.un.org/ru/story/2020/05/1378752')

@bot.event
async def on_ready():
    print(f'Бот запущен, помощь по боту $heelp')

@bot.command()
async def heelp(ctx):
    await ctx.send(f'Команды:\n 1.$hello - приветсвие\n 2.$ecology - как начать оберегать природу\n 3.$helpsea - помощь по сохранению океанов\n 4.$helplitter - помощь по утилизациии мусора\n 5.$treas - вред вырубки деревьев\n 6.$mem_world - мемы\n 7.$bye - прощание ')

#Для использования ↓этой↓ комманды вам нужно скачать изоброжения и поместить в новую папку, назвав ее 'mem_world' 
@bot.command()
async def mem_world(ctx):
    image_name = random.choice(os.listdir('mem_world'))
    with open(f'mem_world/{image_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def ecology(ctx):
    await ctx.send(f'Как спасти природу: 8 шагов, которые может сделать каждый:\n 1.ЭКОНОМЬТЕ РЕСУРСЫ\n 2.РАЗДЕЛЯЙТЕ МУСОР\n 3.СДАВАЙТЕ ВТОРСЫРЬЁ\n 4.ВЫБИРАЙТЕ ЭКОЛОГИЧНЫЙ ТРАНСПОРТ\n 5.ИСПОЛЬЗУЙТЕ ПОВТОРНО И НЕ БЕРИТЕ ЛИШНЕЕ\n 6.ВНЕДРЯЙТЕ ЭКО-ПРИВЫЧКИ НА РАБОТЕ\n 7.ОБРАТИТЕ ВНИМАНИЕ НА ПИТАНИЕ\n 8.ПОСТАРАЙТЕСЬ ОТВЫКНУТЬ ОТ ПЛАСТИКА\n')


bot.run('ВАШ ТОКЕН')

