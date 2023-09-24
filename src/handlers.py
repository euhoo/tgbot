from utils import getHelpMessage, getGreetingByMessage
from sendMsg import sendMsgByMessage

# handler на команду /start
def onStart(message):
	sendMsgByMessage(message, getGreetingByMessage(message))

# handler на команду /help
def onHelp(message):
	return sendMsgByMessage(message, getHelpMessage(message))

# handler на текстовое сообщение
def onText(message):
	lowered = str.lower(message.text)
	if (lowered == 'привет'):
		return onStart(message)

	if (lowered == 'help' or lowered == 'помощь'): 
	    return onHelp(message)