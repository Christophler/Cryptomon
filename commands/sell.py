
async def sell(message, success, numDogecoin, numGraphicCards, numEthereum, numBitcoin):
  # Dogecoin event
  sellNum = int(message.content.split(' ')[2])
  if (("dogecoin" in message.content) == True):
    if ((numDogecoin - (sellNum * 1)) < 0):
      await message.channel.send('You do not have enough dogecoin to sell')
      success = False
    else:
      numGraphicCards += sellNum * 3
      numDogecoin -= sellNum * 1
      await message.channel.send('You now have **' + str(numGraphicCards) + '** <:graphic_card:843320481905377320> and **' + str(numDogecoin) + '** <:dogecoin:843319595086905374>.') # THE ':graphic_card:longnumber' IS FOR MY TEST SERVER CUSTOM EMOJI, SO JUST REPLACE IT WITH YOUR OWN CUSTOM EMOJI
      success = True
      
  # Ethereum event
  if (("ethereum" in message.content) == True):
    if ((numEthereum - (sellNum * 1)) < 0):
      await message.channel.send('You do not have enough ethereum to sell')
      success = False
    else:
      numGraphicCards += sellNum * 10
      numEthereum -= sellNum * 1
      await message.channel.send('You now have **' + str(numGraphicCards) + '** <:graphic_card:843320481905377320> and **' + str(numEthereum) + '** <:ethereum:843319807046189057>.') # THE ':graphic_card:longnumber' IS FOR MY TEST SERVER CUSTOM EMOJI, SO JUST REPLACE IT WITH YOUR OWN CUSTOM EMOJI
      success = True

  # Bitcoin event
  if (("bitcoin" in message.content) == True):
    if ((numBitcoin - (sellNum * 1)) < 0):
      await message.channel.send('You do not have enough bitcoin to sell')
      success = False
    else:
      numGraphicCards += sellNum * 25
      numBitcoin -= sellNum * 1
      await message.channel.send('You now have **' + str(numGraphicCards) + '** <:graphic_card:843320481905377320> and **' + str(numBitcoin) + '** <:bitcoin:843319546165198858>.') # THE ':graphic_card:longnumber' IS FOR MY TEST SERVER CUSTOM EMOJI, SO JUST REPLACE IT WITH YOUR OWN CUSTOM EMOJI
      success = True

  return (success, numGraphicCards, numDogecoin, numEthereum, numBitcoin)