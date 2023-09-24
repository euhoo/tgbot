from bot import chatBot
from start import activateHandlers

activateHandlers(chatBot)

chatBot.polling(non_stop=True)