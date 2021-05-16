
async def help(message, discord):
    # Displaying the tutorial
    await message.channel.send('__**TUTORIAL**__')
    await message.channel.send('Welcome to Cryptomon, a text-based game where you use graphic cards in order to catch cryptocurrency. \n', file=discord.File('welcomeCrypto.jpg')) # THIS REQUIRES THE 'welcomeCrypto.jpg'

    # Displaying the command list
    await message.channel.send('__**COMMANDS**__')
    await message.channel.send('**$wallet**: Displays the amount of each crypto and graphic cards you have in your inventory.')
    await message.channel.send('**$stocks**: Displays the stats of each crypto (spawn rate, catch rate, and sell rate).')
    await message.channel.send('**$mine**: Mines a crypto that you can catch.')
    await message.channel.send('**$validate**: Attempts to catch the crypto.')
    await message.channel.send('**$sell (crypto name) (amount)**: Sells the cryptocurrency and you get graphic cards in return.')