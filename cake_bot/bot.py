from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from catalog import show_catalog, handle_selection
from customize import choose_forms, choose_toppings


TOKEN = ""


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("catalog", show_catalog))

    dp.add_handler(CallbackQueryHandler(handle_selection, pattern="^select_"))
    dp.add_handler(CallbackQueryHandler(choose_forms, pattern="^level_"))
    dp.add_handler(CallbackQueryHandler(choose_toppings, pattern="^form_"))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()