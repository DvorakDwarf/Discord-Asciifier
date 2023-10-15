from discord.ext import commands
from cmnds import *
from ascii import image_to_text
import discord

bot = commands.Bot(command_prefix='$')

print("ready")

async def on_ready(self):
  print(f'Logged in as {self.user}')

#find a way to use default help command
@bot.command(name='helpme')
async def helpme(ctx):
    msg = ctx.message
    await msg.reply("""
`There is only one command, $ascii. For the command to work, you have to attach an image in your message
Pass parameters after $ascii with spaces inbetween to pick different options from the following list
Any parameter can be replaced with "d" to pick the default option. Using no parameters picks all default options
What type do you want ? 1 - "Monochrome", 2 - bigger choice of characters, 3 - same as 2 but reverse colors
Should max/min brightness be represented as empty space instead of a · ? Choose y for yes
Should it send a .txt file instead ? If so, pick a number 1-9 for size (I recommend 3)
`""")

#Probably unsafe
@bot.command(name='ascii')
async def ascii(ctx, palette = '2', background = 'n', size = 1):
    msg = ctx.message
    if size > 9 or size < 0: 
        await msg.channel.send("Wrong size")
        return
    
    await msg.attachments[0].save('testfile.png')
    text = image_to_text(r'E:\Code\Code_projects\Bapple\testfile.png', palette, background, size)
    if text == r'E:\Code\Code_projects\Bapple\testtext.txt':
        await msg.channel.send(file = discord.File(r'E:\Code\Code_projects\Bapple\testtext.txt'))
    else:
        await msg.channel.send(text)
        
#Keep at the bottom
bot.run(TOKEN)