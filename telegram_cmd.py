import xml_reader
import str_combiner_func



def start(bot,update):
    greeting = 'Welcome to the NS unoffical telegram bot!\n\n'
    greeting+= 'Use /storing to check the current disruption on the trajects.\n'
    greeting+= 'Use /planstoring to check the planed works on the trajects.'
    bot.send_message(chat_id = update.message.chat_id,text = greeting)

def storing(bot,update):
    bot.send_message(chat_id = update.message.chat_id,text = 'Inquiring...')
    stor_obj    = xml_reader.XMLReader()
    stor_list   = stor_obj.ongepland_storing()
    
    # use functional programming here
    send_text   = str_combiner_func.sendText(stor_list)
    bot.send_message(chat_id = update.message.chat_id,text = send_text)


def planstoring(bot,update):
    bot.send_message(chat_id = update.message.chat_id,text = 'Inquiring...')
    stor_obj    = xml_reader.XMLReader()
    stor_list   = stor_obj.gepland_storing()
    
    ## use functional programming here
    send_text   = str_combiner_func.sendText(stor_list)
    bot.send_message(chat_id = update.message.chat_id,text = send_text)