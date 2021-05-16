# Importing the needed libraries
import os
import discord
import random

# Importing the functions
from commands.join import join
from commands.help import help
from commands.mine import mine
from commands.sell import sell
from commands.stocks import stocks
from commands.validate import validate
from commands.wallet import wallet

# Setting the discord client variable
bot = discord.Client()

# Declaring all the global variables needed
numGraphicCards = 10
numDogecoin = 0
numEthereum = 0
numBitcoin = 0
encounter = False
mineInt = 0
catchInt = 0
success = False


# Showing that the bot is ready
@bot.event
async def on_ready():
  await join(bot)


# Whenever there's a message, this function runs
@bot.event
async def on_message(message):
  # Setting the variables to globals so that they can be changed in the functions
  global mineInt
  global catchInt
  global encounter
  global numGraphicCards
  global numDogecoin
  global numEthereum
  global numBitcoin
  global success

  # Ensures that a user is saying the commands and not the bot
  if message.author == bot:
    return

  # Help command
  if message.content.startswith('$help'):
    await help(message, discord)

  # Wallet command
  if message.content.startswith('$wallet'):
    await wallet(message, numGraphicCards, numDogecoin, numEthereum, numBitcoin)

  # Stocks command
  if message.content.startswith('$stocks'):
    await stocks(message)

  # Mine command
  if message.content.startswith('$mine'):
    success, encounter, mineInt = await mine(message, discord, mineInt, numGraphicCards, random)

  # Validate command
  if message.content.startswith('$validate'):
    success, encounter, numGraphicCards, numDogecoin, numEthereum, numBitcoin = await validate(message, encounter, random, mineInt, numGraphicCards, numDogecoin, numEthereum, numBitcoin)

  # Sell command
  if message.content.startswith(('$sell ')):
    success, numGraphicCards, numDogecoin, numEthereum, numBitcoin = await sell(message, numDogecoin, numGraphicCards, numEthereum, numBitcoin)


# Running the bot
# INSERT YOUR BOT TOKEN ID
my_secret = 'Your Discord Bot Token ID'
bot.run(my_secret)