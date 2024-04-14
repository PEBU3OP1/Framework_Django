from django.db import models



class Game(models.Model):
    side = models.CharField(max_length=20)
    tiime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.side}, {self.tiime}'

    '''
    Доработаем задачу 1. Добавьте статический метод для статистики по n последним броскам монеты. 
    Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.'''

    @staticmethod
    def get_stats(count: int):
        heads_tails_voc = {"Heads": 0, "Tails": 0}
        # stats = list(Game.objects.all())[-count:]
        stats = Game.objects.all().order_by('-id')[:count]
        for stat in stats:
            heads_tails_voc[stat.side] = heads_tails_voc[stat.side] + 1
        return heads_tails_voc

"""
Создайте модель Автор. Модель должна содержать следующие поля:
● имя до 100 символов
● фамилия до 100 символов
● почта
● биография
● день рождения
Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.
"""
class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    bday = models.DateTimeField(blank=False)

    def full_name(self):
        return f'{self.name} {self.last_name}'