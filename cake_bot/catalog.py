from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext


# Временный каталог
cakes = [
    {"id": 1, "name": "Шоколадный торт", "price": 1200},
    {"id": 2, "name": "Фруктовый торт", "price": 1400}
]


def show_catalog(update: Update, context: CallbackContext):
    _ = context
    """Выводит список тортов с кнопками"""
    for cake in cakes:
        button = InlineKeyboardButton(f"Выбрать {cake['name']}", callback_data=f"select_{cake['id']}")
        keyboard = InlineKeyboardMarkup([[button]])

        update.message.reply_text(
            f"*{cake['name']}*\nЦена: {cake['price']} руб.",
            parse_mode="Markdown",
            reply_markup=keyboard
        )


def handle_selection(update: Update, context: CallbackContext):
    """Обрабатывает выбор торта и отправляет на кастомизацию"""
    query = update.callback_query
    query.answer()

    cake_id = int(query.data.split("_")[1])
    context.user_data["cake_id"] = cake_id

    query.edit_message_text("Выберите количество уровней:")
    from customize import choose_levels
    choose_levels(update, context)