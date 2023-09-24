# Получение имени юзера
def getUserFirstNameByMessage(message):
	return message.chat.first_name
	
# Получение фамилии юзера
def getUserLastNameByMessage(message):
	return message.chat.last_name or ''

# Приветствие
def getGreetingByMessage(message):
	name = getUserFirstNameByMessage(message)
	lastName = getUserLastNameByMessage(message)
	return 'Мастер йода привет тебе шлет, падаван, ' + name + ' ' + lastName + 'Для помощи набери help или помощь'

# Помощь
def getHelpMessage(incomeMessage):
	msg = f'''
	Небольшая помощь тебе, мой юный падаван {getUserFirstNameByMessage(incomeMessage)}:
	- Набери 'помощь' или 'help' для помощи
	- Набери 'кат' или 'cat' для просмотра категорий(не сделано)
	- Набери <категория><дата(дд.мм.гг)> для просмотра сколько потратили по категории в эту дату. Пример 'Продукты 15.08.22'(не сделано)
	- Набери <категория><сумма><дата(опционально)><комментарий(опционально)> для внесения расхода по категории в указанную дату
	'''
	return msg
