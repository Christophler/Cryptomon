
async def help(message, discord):
    # Displaying the tutorial
    await message.channel.send('__**TUTORIAL**__ \n\
    Welcome to Cryptomon, a text-based game where you use graphic cards to catch cryptocurrency. \n\
        ', file=discord.File('images/welcomeCrypto.jpg')) # THIS REQUIRES THE 'welcomeCrypto.jpg'

    # Displaying the command list
    await message.channel.send('__**COMMANDS**__ \n\
    **$help**: Displays the tutorial and all the commands. \n\
    **$wallet**: Displays the amount of each crypto and graphic cards you have in your inventory. \n\
    **$stocks**: Displays the stats of each crypto (spawn rate, catch rate, and sell rate). \n\
    **$mine**: Mines a crypto that you can catch. \n\
    **$validate**: Attempts to catch the crypto you mined. \n\
    **$sell (crypto name) (amount)**: Sells the cryptocurrency and you get graphic cards in return. \n\
    **$print**: Displays the blockchain in both the terminal and the discord server.')