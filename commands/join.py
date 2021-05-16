
async def join(bot):
  print('We have logged in as {0.user}'.format(bot))
  await bot.wait_until_ready()
  await bot.get_channel(843616163010314260).send("Hello! Get started with the **$help** command! :smiley:") # THE LONG NUMBER IS MY TEST SERVER TEXT CHANNEL ID, SO CHANGE IT WITH YOUR TEXT CHANNEL ID