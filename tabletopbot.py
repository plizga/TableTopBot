import discord
from random import randint
TOKEN = "NDYxOTM1MDQyMDg4Nzk2MTkw.DhalBA.3MMqTSKhF7hWwlKJMbSjDV7BMOY"
client = discord.Client()

@client.event
async def on_message(message):
    """ Prevent bot from replying to itself """
    if message.author == client.user:
        return
    """handles all !roll parameters"""
    if message.content.startswith('!roll'):
        strRoll = message.content.strip("!roll ")
        amount, die = strRoll.split("d", 1)
        rollSum = 0
        tupAddends = ()
        for i in range(int(amount)):
            newRoll = randint(1, int(die))
            tupAddends = tupAddends + (newRoll,)
            rollSum += newRoll

        strFinal = ""
        for i in range(len(tupAddends)):
            if i != len(tupAddends) - 1:
                strFinal += str(tupAddends[i]) + " + "
            else:
                strFinal += str(tupAddends[i]) + " "
        strFinal += "= {}"
        await client.send_message(message.channel, strFinal.format(rollSum))

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    """prints bot information to console"""
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)