# Super Small tutorial on Creating a Discord Python Bot.

# Bot -> Generate Token -> Copy Token
# Bot Token: OTc0Nzc3OTEyOTE2MDc4NjQy.G5Xivy.YRjPrbgrk7AnQYtG82V8nGArQ5m9nUJVhDQ2rQ
# Bot Settings: https://discord.com/developers/applications/974777912916078642/bot

# OAuth2 -> URL Generator -> bot

#### OAuth2 -> General -> Bot Permissions


# Thonny -> Tools -> Open system shell 
# pip install -U discord.py


import discord
import os


#intents = discord.Intents(messages=True, guilds=True)

# Discord Bot Intents, required for listing all the members in the server.
# bot -> Privileged Gateway Intents -> SERVER MEMBERS INTENT
intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
        
        
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

    # Requires Intents privilegies to access and list other members than the bot itself: https://discordpy.readthedocs.io/en/stable/intents.html
    # !On every member, all the channels are scanned
    # !Make For each channel count all the messages and add the amounts to the members amounts. 
    if message.content.startswith('Show all the members'):
        from datetime import datetime, timedelta
        d = datetime.today() - timedelta(hours=0, minutes=50)
        
        
        await message.channel.send("https://c.tenor.com/xRSskA4WM4cAAAAC/sauron-lotr.gif")
        
        
        guild = client.get_guild(message.guild.id)
        members = ''
        for number, member in enumerate(guild.members):
            counter = 0
            for channel in member.guild.text_channels:
                print(channel.history())
                async for messages in channel.history(limit = 100000):
                    if messages.author == member:
                        counter += 1
                        if counter == 1:
                            created = messages.created_at
            
            if member.bot:
                isbot = '🤖'
            else:
                isbot = '👨'
                
            if member.nick is None:
                show_nickname = ""
            else:
                show_nickname = '(' + member.nick + ')'
                
            import math
            #math.floor()
            seconds = (datetime.now() - (created + timedelta(hours=3, minutes=00))).total_seconds()
            seconds = seconds % (24 * 3600)
            hour = math.floor(seconds // 3600)
            seconds %= 3600
            minutes = math.floor(seconds // 60)
            seconds %= 60
            
            
            members += '**' + str(number) + '** \t | ' + isbot + ' \t<@' + str(member.id) + '>' + "``" + member.name + '`` ' + " " + show_nickname + "`\n\tAmount of messages: " + str(counter) + "\t Recent message: " +  str(hour) + " Hours " + str(minutes) + " Minutes`" + '\n'
            #print(member.lastMessage)
            print(guild.members)


  
        #memberList = ' '.join(message.guild.members)
        allowed_mentions = discord.AllowedMentions(roles=False, users=False, everyone=False)
        await message.channel.send(content = 'Listing all the members in the **'+ message.guild.name + '**' + '\n'
                                    + "__**Num|\t\t\t\t\t\t\t" + "@TagUsername(Nickname)**\t\t\t\t\t\t\t\t\t__" + '\n'
                                    + members + "__\t\t Overall Members: "+ str(number+1) + "\t\t__", allowed_mentions = allowed_mentions
                                   #'test' + message.guild.members
                                   )

        
    if message.content.startswith('Where are you'):
        serverID = str(message.guild.id)
        await message.channel.send("I'm in the **" + message.guild.name + '**' + '\n'
                                   "The server's ID is **" + serverID + '**'   + '\n'
                                   "The channel name is **" + message.channel.name + "**"  + '\n'
                                   "The system channel name is **" + message.guild.system_channel.name + "**"  + '\n'
                                   )      
       


# ShOw mE The server Spies


@client.event
async def on_ready():
    for guild in client.guilds:
        channel = guild.system_channel #getting system channel
        if channel.permissions_for(guild.me).send_messages: #making sure you have permissions
            await channel.send("I'm online!")

@client.event
async def on_guild_join(guild):
    if guild.system_channel: # If it is not None
        await guild.system_channel.send(f'Thanks for inviting me to {guild.name}')
        
        
        
        
        
        
        


# Get environment variables from .env file
# Tools -> Open system shell 
# pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()

client.run(os.getenv("TOKEN"))

# Direct Bot Token Usage
# client.run("OTc0Nzc3OTEyOTE2MDc4NjQy.G5Xivy.YRjPrbgrk7AnQYtG82V8nGArQ5m9nUJVhDQ2rQ")

