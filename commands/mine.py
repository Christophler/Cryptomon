
async def mine(message, discord, mineInt, numGraphicCards, random):
  mineInt = random.randint(1,100)
  # Dogecoin encounter
  if (mineInt <= 50):
    await message.channel.send('You found **Dogecoin**! \n', file=discord.File('images/dogecoin.jpg')) # REQUIRES THE 'dogecoin.jpg' FILE
    await message.channel.send('You have **' + str(numGraphicCards) + '** graphic cards in your wallet!')

  # Etherium encounter
  if ((mineInt > 50) and (mineInt < 90)):
    await message.channel.send('You found **Ethereum**! \n', file=discord.File('images/ethereum.jpg')) # REQUIRES THE 'ethereum.jpg' FILE
    await message.channel.send('You have **' + str(numGraphicCards) + '** graphic cards in your wallet!')

  # Bitcoin encounter
  if (mineInt >= 90):
    await message.channel.send('You found **Bitcoin**!!! \n', file=discord.File('images/bitcoin.jpg')) # REQUIRES THE 'dogecoin.jpg' FILE
    await message.channel.send('You have **' + str(numGraphicCards) + '** graphic cards in your wallet!')
  
  await message.channel.send('Use the **$validate** command to try to catch the crypto!')
  
  encounter = True

  return (encounter, mineInt)
