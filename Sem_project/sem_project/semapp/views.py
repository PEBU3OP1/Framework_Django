from django.shortcuts import render
from django.http import HttpResponse
from random import choice, randint
import logging
from .models import Game, Author
from datetime import date

"""
Создайте новое приложение. Подключите его к проекту. В приложении должно быть три простых представления, возвращающих HTTP ответ:
1. Орёл или решка
2. Значение одной из шести граней игрального кубика
3. Случайное число от 0 до 100
Пропишите маршруты
"""
"""
Добавьте логирование в проект. Настройте возможность вывода в файл и в терминал. Устраните возможные ошибки.
*Форматирование настройте по своему желанию. Объясните что вы выводите в логи
"""


logger = logging.getLogger(__name__)
def index(request):
    return HttpResponse("hello")


def about(request):
    return HttpResponse("about")


def coin(request):
    result = choice(["Heads", "Tails"])

    logger.info(f'Результат = {result}')
    return HttpResponse(result)

def cube(request):
    return HttpResponse(randint(1, 6))

def random_number(request):
    return HttpResponse(randint(1, 100))

"""
Создайте модель для запоминания бросков монеты: орёл или решка. Также запоминайте время броска
"""
def game(requsest):
    result = choice(["Heads", "Tails"])
    game = Game(side = result)
    game.save()

    return HttpResponse(game)

def stats(request):
    n = request.GET.get('n', 5)
    vooc = Game.get_stats(int(n))
    return HttpResponse(f'{vooc}')


def create_author(request):
    result = []
    for i in range(1,10):
        author = Author(name = f'sav{i}', last_name = f'kuz{i}',email = f'bis{i}@mail.ru', bday =date.today())
        author.save()
        result.append(author.full_name())
    return HttpResponse(f'{result}')