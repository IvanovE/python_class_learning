from sneakers_task.shoes import Shoes

sports = {'football', 'basketball', 'running', 'bicycle'}
seasons = {'winter', 'autumn', 'summer', 'spring'}


class Sneakers(Shoes):

    def __init__(self, **kwargs):
        Shoes.__init__(self, **kwargs)
        self.__sport = self.preprocessing(kwargs.get('sport', set()))
        self.__season = self.preprocessing(kwargs.get('season', set()))

    def __str__(self):
        return Shoes.__str__(self) + f'sport - {self.__sport}\n season - {self.__season}\n'

    def __repr__(self):
        return Shoes.__repr__(self) + f'sport - {self.__sport}\n season - {self.__season}\n'

    @property
    def sport(self):
        return self.__sport

    @sport.setter
    def sport(self, x):
        set_x = self.preprocessing(x)
        if set_x.intersection(sports):
            self.__sport = set_x.intersection(sports)
        else:
            print('Такие виды спорта отсутсвуют в базе')

    def add_sport(self, x):
        set_x = self.preprocessing(x)
        if set_x.intersection(sports):
            self.__sport.update(set_x.intersection(sports))
        else:
            print('Такие виды спорта отсутсвуют в базе')

    def delete_sport(self, x):
        set_x = self.preprocessing(x)
        self.__sport.difference_update(set_x)

    @property
    def season(self):
        return self.__season

    @season.setter
    def season(self, x):
        set_x = self.preprocessing(x)
        if set_x.intersection(seasons):
            self.__season = set_x.intersection(seasons)
        else:
            print('Такие сезоны отсутсвуют')

    def add_season(self, x):
        set_x = self.preprocessing(x)
        if set_x.intersection(seasons):
            self.__season.update(set_x.intersection(seasons))
        else:
            print('Такие сезоны отсутсвуют')

    def delete_season(self, x):
        set_x = self.preprocessing(x)
        self.__season.difference_update(set_x)
