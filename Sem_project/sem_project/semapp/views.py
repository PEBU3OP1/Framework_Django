from django.shortcuts import render
from django.http import HttpResponse
from random import choice, randint
import logging

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

