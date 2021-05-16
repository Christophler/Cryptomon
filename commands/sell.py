
async def sell(message, numDogecoin, numGraphicCards, numEthereum, numBitcoin):
  # Dogecoin event
  sellNum = int(message.content.split(' ')[2])
  if (("dogecoin" in message.content) == True):
    if ((numDogecoin - (sellNum * 1)) < 0):
      await message.channel.send('You do not have enough dogecoin to sell')
    else:
      numGraphicCards += sellNum * 3
      numDogecoin -= sellNum * 1
      await message.channel.send('You now have **' + str(numGraphicCards) + '** <:graphic_card:843320481905377320>.') # THE ':graphic_card:longnumber' IS FOR MY TEST SERVER CUSTOM EMOJI, SO JUST REPLACE IT WITH YOUR OWN CUSTOM EMOJI
      
  # Ethereum event
  if (("ethereum" in message.content) == True):
    if ((numEthereum - (sellNum * 1)) < 0):
      await message.channel.send('You do not have enough ethereum to sell')
    else:
      numGraphicCards += sellNum * 10
      numEthereum -= sellNum * 1
      await message.channel.send('You now have **' + str(numGraphicCards) + '** <:graphic_card:843320481905377320>.') # THE ':graphic_card:longnumber' IS FOR MY TEST SERVER CUSTOM EMOJI, SO JUST REPLACE IT WITH YOUR OWN CUSTOM EMOJI

  # Bitcoin event
  if (("bitcoin" in message.content) == True):
    if ((numBitcoin - (sellNum * 1)) < 0):
      await message.channel.send('You do not have enough bitcoin to sell')
    else:
      numGraphicCards += sellNum * 25
      numBitcoin -= sellNum * 1
      await message.channel.send('You now have **' + str(numGraphicCards) + '** <:graphic_card:843320481905377320>.') # THE ':graphic_card:longnumber' IS FOR MY TEST SERVER CUSTOM EMOJI, SO JUST REPLACE IT WITH YOUR OWN CUSTOM EMOJI

  return (numGraphicCards, numDogecoin, numEthereum, numBitcoin)