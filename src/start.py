from handlers import onStart, onText, onHelp

# автивирует подписки на действия бота
def activateHandlers(chatBot):
	#подписка на команду /start
	@chatBot.message_handler(commands=['start'])
	def start(message):
		onStart(message)

	#подписка на команду /help
	@chatBot.message_handler(commands=['help'])
	def help(message):
		onHelp(message)
	
	#подписка на текстовое сообщение
	@chatBot.message_handler(content_types=['text'])
	def msg(message):
		onText(message)
