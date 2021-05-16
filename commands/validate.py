
async def validate(message, encounter, random, mineInt, numGraphicCards, numDogecoin, numEthereum, numBitcoin):
  # Check if the user already used the '$mine' command
  if (encounter == False):
    await message.channel.send('You must use the *$mine* command **first** before using *$validate*')

  else:
    catchInt = random.randint(1,100)
    numGraphicCards -= 1

    # Dogecoin encounter
    if (mineInt <= 75):
      if (catchInt <= 75):
        numDogecoin += 1
        await message.channel.send('You validated the **Dogecoin**! Nice one! :grin:')
      else:
        await message.channel.send('You did not have enough computing power to validate the **Dogecoin**. :cry:')

    # Etherium encounter
    if ((mineInt <= 99) and (mineInt > 75)):
      if (catchInt <= 60):
        numEthereum += 1
        await message.channel.send('You validated the **Ethereum**! Amazing!! :grin:')
      else:
        await message.channel.send('You did not have enough computing power to validate the **Ethereum**. :cry:')

    # Bitcoin encounter
    if (mineInt == 100):
      if (catchInt <= 50):
        numBitcoin += 1
        await message.channel.send('You validated the **Bitcoin**!!! Insane!! :exploding_head:')
      else:
        await message.channel.send('You did not have enough computing power to validate the **Bitcoin**. :cry:')
  
  encounter = False

  return (encounter, numGraphicCards, numDogecoin, numEthereum, numBitcoin)
