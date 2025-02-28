import os
import django
import requests
import telegram
from dotenv import load_dotenv
from pathlib import Path


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BakeCake_bot.settings')
django.setup()
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from cake_bot.models import Cake

load_dotenv()
tg_token = os.environ['TG_TOKEN']
tg_chat_id = os.environ['TG_CHAT_ID']
bot = telegram.Bot(token=tg_token)

def send_image(image_url, cake_name, cake_description, cake_price, cake_weight, tg_chat_id):
    """Опубликовать картинку торта с описанием и ценой"""
    bot.send_photo(chat_id=tg_chat_id, photo=image_url, caption=f"{cake_name}\n{cake_description}\nЦена: {cake_price}\nВес: {cake_weight}")


cakes = [
    {
        'cake_name': 'Чизкейк',
        'cake_image': 'static/images/cheescake.jpg',
        'cake_description': 'нежный чизкейк с кокосовым пудингом, арахисом и кокосовыми хлопьями',
        'cake_price': 5200,
        'cake_weight': 2.5
    },
    {
        'cake_name': 'Вишневый торт',
        'cake_image': 'static/images/cherry_cake.jpg',
        'cake_description': 'медово-кокосовый торт, без глютена, со сметанным кремом, вишневым джемом и свежими ягодами',
        'cake_price': 4300,
        'cake_weight': 2.4
    },
    {
        'cake_name': 'Шоколадный бисквит',
        'cake_image': 'static/images/chocolate_biscuit.jpg',
        'cake_description': 'шоколадный бисквит с шоколадным муссом, орехом пекан и карамелью',
        'cake_price': 5300,
        'cake_weight': 2.4
    },
    {
        'cake_name': 'Шоколадная бомба',
        'cake_image': 'static/images/chocolate_bomb.jpg',
        'cake_description': 'шоколадный бисквит с шоколадным крем-чизом, черничным джемом и миксом свежих ягод',
        'cake_price': 6150,
        'cake_weight': 2.8
    },
    {
        'cake_name': 'Малиново-йогуртовый',
        'cake_image': 'static/images/raspberry_yogurt.jpg',
        'cake_description': 'подушка из брауни, незапеченый чизкейк с бельгийским шоколадом и малиной',
        'cake_price': 4800,
        'cake_weight': 1.9
    },
    {
        'cake_name': 'Ванильный бисквит',
        'cake_image': 'static/images/vanilla_cake.jpg',
        'cake_description': 'нежный бисквит с малиновым кремом и миксом свежих ягод',
        'cake_price': 5000,
        'cake_weight': 2.4
    }
]

def send_test():

    for cake in cakes:
        send_image(cake.image.url, cake.name, cake.description, cake.price, cake.weight, tg_chat_id)
        

def main():

    for cake in cakes:
        cake_for_order = Cake.objects.create(
            name=cake['cake_name'],
            image=cake['cake_image'],
            description=cake['cake_description'],
            price=cake['cake_price'],
            weight=cake['cake_weight'],
        )
        cake_for_order.save()


if __name__ == "__main__":
    main()