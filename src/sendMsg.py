from bot import chatBot

# отправка сообщения по chatId

def sendMsgByChatId(chatId, msgToSend):
	chatBot.send_message(chatId, msgToSend)

# отправка сообщения по исходному сообщению
def sendMsgByMessage(incomeMessage, msgToSend):
	sendMsgByChatId(incomeMessage.chat.id, msgToSend)
	
# ответ на сообщение
def replyOnMsg(incomeMessage, msgToSend):
	chatBot.reply_to(incomeMessage, msgToSend)