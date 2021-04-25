from random import randint

brands = {"nike", "adidas", "reebok", "tommy hilfiger", "puma", "patrol", "pull&bear", "pierre cardin"}
genders = {'m', 'f'}
styles = {'everyday', 'business', 'sport', 'thematic', 'beach'}
colors = {'red', 'blue', 'black', 'white', 'green', 'yellow', 'orange', 'purple'}
external_materials = {'box-calf', 'museum-calf', 'crust', 'scotch-grain', 'patent', 'cordovan'}
inner_materials = {'cambrelle', 'thinsulate', 'core-tex'}
main_sizes = {38: 0, 39: 0, 40: 0, 41: 0, 42: 0, 43: 0, 44: 0, 45: 0, 46: 0}


class Shoes:

    def __init__(self, **kwargs):
        self.__brand = self.preprocessing(kwargs.get('brand', ''))
        self.__sizes = {38: randint(0, 12), 39: randint(0, 12), 40: randint(0, 12), 41: randint(0, 12),
                        42: randint(0, 12), 43: randint(0, 12), 44: randint(0, 12), 45: randint(0, 12),
                        46: randint(0, 12)}
        # self.__sizes = kwargs.get('sizes', set())
        self.__price = kwargs.get('price', 0)
        self.__style = self.preprocessing(kwargs.get('style', set()))
        self.__color = self.preprocessing(kwargs.get('color', set()))
        self.__gender = self.preprocessing(kwargs.get('gender', set()))
        self.__inner_material = self.preprocessing(kwargs.get('inner_material', set()))
        self.__external_material = self.preprocessing(kwargs.get('external_material', set()))

    def __str__(self):
        return f'brand  - {self.brand},\n' \
               f'sizes - {self.sizes},\n' \
               f'price - {self.price}\n' \
               f'style - {self.style}\n' \
               f'color - {self.color},\n ' \
               f'gender - {self.gender},\n' \
               f'inner_material - {self.inner_material},\n' \
               f'external_material - {self.external_material}\n'

    def __repr__(self):
        return f'brand  - {self.brand},\n ' \
               f'sizes - {self.sizes},\n' \
               f'price - {self.price}\n' \
               f'style - {self.style}\n' \
               f'color - {self.color},\n ' \
               f'gender - {self.gender},\n ' \
               f'inner_material - {self.inner_material},\n' \
               f'external_material - {self.external_material}\n'

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, x):
        if sum(list(self.__sizes.values())) < 5 and self.__price * 0.8 <= x:
            self.__price = x
        elif self.__price * 0.5 <= x:
            self.__price = x
        else:
            print("Не удалось изменить цену")

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand_name):
        set_x = self.preprocessing(brand_name)
        if set_x in brands:
            self.__brand = set_x

    @property
    def sizes(self):
        return self.__sizes

    @sizes.setter
    def sizes(self, x: dict):
        self.__sizes = main_sizes
        for i in x.keys():
            if i in self.__sizes.keys() and x[i] >= 0:
                self.__sizes[i] = x[i]

    def add_sizes_num(self, size: dict):
        """
        Добавление количетсва размеров
        :param size: Словарь размеров и их количества
        :return:
        """
        for i in size.keys():
            if i in self.__sizes.keys():
                self.__sizes[i] += size[i]
            else:
                print('Такого размера нет: ', i)

    def delete_sizes_num(self, size: dict):
        for i in size.keys():
            if i in self.__sizes.keys():
                if size[i] == self.__sizes[i]:
                    self.__sizes[i] -= size[i]
                    print('Закончился размер: ', i)
                elif size[i] < self.__sizes[i]:
                    self.__sizes[i] -= size[i]
                else:
                    print('Не хватает штук: ', size[i] - self.__sizes[i], ' размера: ', i)
                    print('Закончился размер: ', i)
                    self.__sizes[i] = 0
            else:
                print('Такого размера нет: ', i)

    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, x):
        set_x = self.preprocessing(x)
        if set_x.intersection(styles):
            self.__style = set_x.intersection(styles)
        else:
            print('Невозможно Изменить. Подобного нет в базе')

    def add_style(self, x):
        set_x = self.preprocessing(x)
        if set_x.intersection(styles):
            self.__style.update(set_x.intersection(styles))
        else:
            print('Невозможно добавить. Подобного нет в базе')

    def delete_style(self, x):
        set_x = self.preprocessing(x)
        self.__style.difference_update(set_x)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, x):
        set_x = self.preprocessing(x)
        if set_x.intersection(colors):
            self.__color = set_x.intersection(colors)
        else:
            print('Невозможно изменить. Подобного нет в базе')

    def add_color(self, x):
        set_x = self.preprocessing(x)
        if set_x.intersection(colors):
            self.__color.update(set_x.intersection(colors))
        else:
            print('Невозможно добавить. Подобного нет в базе')

    def delete_color(self, x):
        set_x = self.preprocessing(x)
        self.__color.difference_update(set_x)

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, x):
        set_x = self.preprocessing(x)
        if set_x.intersection(genders):
            self.__gender = set_x.intersection(genders)
        else:
            print('Невозможно изменить. Подобного нет в базе')

    def add_gender(self, x):
        set_x = self.preprocessing(x)
        if set_x.intersection(genders):
            self.__gender.update(set_x.intersection(genders))
        else:
            print('Невозможно добавить. Подобного нет в базе')

    def delete_gender(self, x):
        set_x = self.preprocessing(x)
        self.__gender.difference_update(set_x)

    @property
    def inner_material(self):
        return self.__inner_material

    @inner_material.setter
    def inner_material(self, x):
        set_x = self.preprocessing(x)
        if set_x.intersection(inner_materials):
            self.__inner_material = set_x.intersection(inner_materials)
        else:
            print('Такие материалы в базе отсутсвуют')

    def add_inner_material(self, x):
        set_x = self.preprocessing(x)
        if set_x.intersection(inner_materials):
            self.__inner_material.intersection_update(set_x)
        else:
            print('Таких материалов в базе отсутствуют')

    def delete_inner_material(self, x):
        set_x = self.preprocessing(x)
        self.__inner_material.difference_update(set_x)

    @property
    def external_material(self):
        return self.__external_material

    @external_material.setter
    def external_material(self, x):
        set_x = self.preprocessing(x)
        if set_x.intersection(external_materials):
            self.__external_material = set_x.intersection(external_materials)

    def add_external_material(self, x):
        set_x = self.preprocessing(x)
        if set_x.intersection(external_materials):
            self.__external_material.intersection_update(set_x)

    def delete_external_material(self, x):
        set_x = self.preprocessing(x)
        self.__external_material.difference_update(set_x)

    def check(self, x):
        """
        Функция проверки наличия необходимого товара
        :param x: Размер обуви, который  требуется (либо число, либо список)
        :return: Количество размеров требуемых размеров
        """
        set_x = self.preprocessing(x)
        d = {i: self.__sizes.get(i) for i in set_x if i in self.__sizes.keys()}
        return d

    def preprocessing_str(self, x):
        new_x = set()
        if type(x) is set or type(x) is tuple:
            new_x = {i.lower() for i in x if type(i) is str}
        elif type(x) is str:
            new_x = x.lower()
        if new_x:
            return new_x
        else:
            return x

    def preprocessing(self, x):
        if type(x) is list:
            return self.preprocessing_str(set(x))
        if type(x) is int or type(x) is str:
            empty_set = set()
            empty_set.add(x)
            return self.preprocessing_str(empty_set)
        if type(x) is set:
            return self.preprocessing_str(x)
        if type(x) is tuple:
            return set(x)
        return self.preprocessing_str(x)

    def check_on_stock(self):
        return {i for i in self.__sizes if self.__sizes[i] > 0}
