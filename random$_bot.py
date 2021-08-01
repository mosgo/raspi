@bot.event
async def on_ready():
	print('Logged in through:')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
