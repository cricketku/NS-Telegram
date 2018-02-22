from telegram.ext import Updater,CommandHandler
import telegram_cmd
import importlib

def main():
    # get the login token from bot father
    login_module = importlib.import_module('login_token')
    login_token  = login_module.login_token
    
    updater = Updater(token =login_token)
    dispatcher = updater.dispatcher


    start_handler = CommandHandler('start',telegram_cmd.start)
    dispatcher.add_handler(start_handler)


    onplan_storing = CommandHandler('storing',telegram_cmd.storing)
    dispatcher.add_handler(onplan_storing)


    plan_storing = CommandHandler('planstoring',telegram_cmd.planstoring)
    dispatcher.add_handler(plan_storing)


    print('Begin to run the server...')
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()