from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext


# Временные данные
levels = {
    "1 уровень": 400,
    "2 уровня": 750,
    "3 уровня": 1100
}

forms = {
    "Квадрат": 600,
    "Круг": 400,
    "Прямоугольник": 1000
}

toppings = {
    "Без топпинга": 0,
    "Белый соус": 200,
    "Карамельный сироп": 180
}


def choose_levels(update: Update, context: CallbackContext):
    """Выбор количества уровней"""
    _ = context

    keyboard = []
    for name, price in levels.items():
        keyboard.append([InlineKeyboardButton(f"{name} (+{price} руб.)", callback_data=f"level_{name}")])

    update.message.reply_text("Выберите количество уровней:", reply_markup=InlineKeyboardMarkup(keyboard))


def choose_forms(update: Update, context: CallbackContext):
    """Выбор формы торта"""
    _ = context

    keyboard = []
    for name, price in forms.items():
        keyboard.append([InlineKeyboardButton(f"{name} (+{price} руб.)", callback_data=f"form_{name}")])

    update.message.reply_text("Выберите форму торта:", reply_markup=InlineKeyboardMarkup(keyboard))


def choose_toppings(update: Update, context: CallbackContext):
    """Выбор топпинга"""
    _ = context

    keyboard = []
    for name, price in toppings.items():
        keyboard.append([InlineKeyboardButton(f"{name} (+{price} руб.)", callback_data=f"topping_{name}")])

    update.message.reply_text("Выберите топпинг:", reply_markup=InlineKeyboardMarkup(keyboard))
