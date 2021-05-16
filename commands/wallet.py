
async def wallet(message, numGraphicCards, numDogecoin, numEthereum, numBitcoin):
  await message.channel.send('You have **' + str(numGraphicCards) + '** graphic cards <:graphic_card:843320481905377320>. \n\
You have **' + str(numDogecoin) + '** dogecoin <:dogecoin:843319595086905374>. \n\
You have **' + str(numEthereum) + '** ethereum <:ethereum:843319807046189057>. \n\
You have **' + str(numBitcoin) + '** bitcoin <:bitcoin:843319546165198858>.') 
  
  # THE ':cryptoName:longnumber' AND ':graphic_card:longnumber' IS FOR MY OWN SERVER CUSTOM EMOJI, SO JUST REPLACE IT WITH YOUR OWN CUSTOM EMOJI