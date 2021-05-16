
async def validate(message, encounter, success, random, mineInt, numGraphicCards, numDogecoin, numEthereum, numBitcoin):
  # Check if the user already used the '$mine' command
  if (encounter == False):
    await message.channel.send('You must use the *$mine* command **first** before using *$validate*')

  else:
    catchInt = random.randint(1,100)
    numGraphicCards -= 1

    # Dogecoin encounter
    if (mineInt <= 50):
      if (catchInt <= 75):
        numDogecoin += 1
        await message.channel.send('You validated the **Dogecoin**! Nice one! :grin:')
        success = True
      else:
        await message.channel.send('You did not have enough computing power to validate the **Dogecoin**. :cry:')
        success = False

    # Etherium encounter
    if ((mineInt > 50) and (mineInt < 90)):
      if (catchInt <= 60):
        numEthereum += 1
        await message.channel.send('You validated the **Ethereum**! Amazing!! :grin:')
        success = True
      else:
        await message.channel.send('You did not have enough computing power to validate the **Ethereum**. :cry:')
        success = False

    # Bitcoin encounter
    if (mineInt >= 90):
      if (catchInt <= 50):
        numBitcoin += 1
        await message.channel.send('You validated the **Bitcoin**!!! Insane!! :exploding_head:')
        success = True
      else:
        await message.channel.send('You did not have enough computing power to validate the **Bitcoin**. :cry:')
        success = False
  
  encounter = False

  return (success, encounter, numGraphicCards, numDogecoin, numEthereum, numBitcoin)
