"""
Домашка на 20.03

Изменить класс Shoes.
Добавить стиль - список, только то что из справочника, цвета - список из справочника
Пол: женский, мужской


В класс Sneakers
Добавить сезон, материал верха, внутренний материал


Создать класс Heels
Тип каблука, тип носа, материал верха, внутренний  материал
Признак что свадебная обувь

Создать класс weddingheels
Добавить наценку за срочность, по умолчанию x2

*продумать как хранить количество по размерам, как его изменять и так далее
"""


from sneakers_task.shoes import Shoes

sports = {'Волейбол', 'Баскетбол', 'Бег', 'Велосипед'}
seasons = {'winter', 'autumn', 'summer', 'spring'}


class Sneakers(Shoes):

    def __init__(self, **kwargs):
        Shoes.__init__(self, **kwargs)
        self.__sport = kwargs.get('sport', {})
        self.__season = kwargs.get('season', {})

    def __str__(self):
        return 'Sneakers: \n' + Shoes.__str__(self) + f'sport - {self.__sport}\n, season - {self.__season}'

    def __repr__(self):
        return 'Sneakers: \n' + Shoes.__repr__(self) + f'sport - {self.__sport}\n, season - {self.__season}'

    @property
    def sport(self):
        return self.__sport

    @sport.setter
    def sport(self, x):
        if x.intersection(sports):
            self.__sport = x.intersection(sports)
        else:
            print('Такие виды спорта отсутсвуют в базе')

    def add_sports(self, x):
        if x.intersection(sports):
            self.__sport.intersection_update(x)
        else:
            print('Такие виды спорта отсутсвуют в базе')

    def delete_sports(self, x):
        self.__sport.difference_update(x)

    @property
    def season(self):
        return self.__season

    @season.setter
    def season(self, x):
        if x.intersection(seasons):
            self.__season = x.intersection(seasons)
        else:
            print('Такие сезоны отсутсвуют')

    def add_season(self, x: set):
        if x.intersection(seasons):
            self.__season.intersection_update(x)
        else:
            print('Такие сезоны отсутсвуют')

    def delete_season(self, x: set):
        self.__season.difference_update(x)
