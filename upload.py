import easygui
from anonfile import AnonFile
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from os import system
import time

TOKEN = input("Token\n> ")



def options():
    system("cls")
    print('=========================')
    print('Logged in ')
    print('coded by baum1810 https://github.com/baum1810')
    print('=========================')
    print("type !file to use the filebypass")
    

client = discord.Client()
b = commands.Bot(command_prefix = "!")

@b.event
async def on_ready():
    options()
    


@b.event
async def on_message(message):
    if message.content == "!file":
        await message.delete()
        file = easygui.fileopenbox()
        anon = AnonFile()
        upload = anon.upload(file, progressbar=True)
        await message.send(upload.url.geturl())
        system("cls")
    
b.run(TOKEN, bot = False)
