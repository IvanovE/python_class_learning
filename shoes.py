from random import randint

s = {"Nike", "Adidas", "Reebok", "Tommy Hilfiger", "Puma", "Patrol", "Pull&Bear", "Pierre Cardin"}
genders = {'М', 'Ж'}
styles = {'Everyday', 'Business', 'Sport', 'Thematic', 'Beach'}
colors = {'red', 'blue', 'black', 'white', 'green', 'yellow', 'orange', 'purple'}
external_materials = {'Box-calf', 'Museum-calf', 'Crust', 'Scotch-grain', 'Patent', 'Cordovan'}
inner_materials = {'Cambrelle', 'Thinsulate', 'Core-Tex'}


class Shoes:

    def __init__(self, **kwargs):
        self.__ = kwargs.get('', '')
        # self.__sizes = {38: randint(0, 12), 39: randint(0, 12), 40: randint(0, 12), 41: randint(0, 12),
        #                 42: randint(0, 12), 43: randint(0, 12), 44: randint(0, 12), 45: randint(0, 12),
        #                 46: randint(0, 12)}
        self.__sizes = kwargs.get('sizes', {})
        self.__price = kwargs.get('price', 0)
        self.__style = kwargs.get('style', set())
        self.__color = kwargs.get('color', {})
        self.__gender = kwargs.get('gender', {})
        self.__inner_material = kwargs.get('inner_material', {})
        self.__external_material = kwargs.get('external_material', {})

    def __str__(self):
        return f'Shoes:  - {self.},\n sizes - {self.sizes},\n ,\n ' \
               f'style - {self.style}' \
               f'color - {self.color},\n gender - {self.gender},\n inner_material - {self.inner_material},\n' \
               f'external_material - {self.external_material}'

    def __repr__(self):
        return f'Shoes:  - {self.},\n sizes - {self.sizes},\n \n ' \
               f'style - {self.style}' \
               f'color - {self.color},\n gender - {self.gender},\n inner_material - {self.inner_material},\n' \
               f'external_material - {self.external_material}'

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, x):
        # todo
        if len(self.sizes) < 2:
            if self.__price * 0.8 <= x:
                self.__price = x
            else:
                print("Не удалось изменить цену")
        elif self.__price * 0.9 <= x:
            self.__price = x
        else:
            print("Не удалось изменить цену")

    @property
    def (self):
        return self.__

    @.setter
    def (self, _name):
        if _name in s:
            self.__ = _name

    @property
    def sizes(self):
        return self.__sizes

    @sizes.setter
    def sizes(self, x: dict):
        # Todo
        for i in x.keys():
            if i in self.__sizes.keys() and x[i] >= 0:
                self.__sizes[i] = x[i]

    def add_sizes_num(self, size: dict):
        """
        Добавление количетсва размеров
        :param size:
        :return:
        """
        for i in size.keys():
            if i in self.__sizes.keys():
                self.__sizes[i] += size[i]
            else:
                print('Такого размера нет: ', i)

    # Todo refactor
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
    def style(self, x: set):
        if x.intersection(styles):
            self.__style = x.intersection(styles)
        else:
            print('Невозможно Изменить. Подобного нет в базе')

    def add_style(self, x: set):
        if x.intersection(styles):
            self.__style.update(x.intersection(styles))
        else:
            print('Невозможно добавить. Подобного нет в базе')

    def delete_style(self, x):
        self.__style.difference_update(x)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, x: set):
        if x.intersection(colors):
            self.__color = x.intersection(colors)
        else:
            print('Невозможно изменить. Подобного нет в базе')

    def add_color(self, x):
        if x.intersection(colors):
            self.__color.update(x.intersection(colors))
        else:
            print('Невозможно добавить. Подобного нет в базе')

    def delete_color(self, x):
        self.__color.difference_update(x)

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, x):
        if x.intersection(genders):
            self.__gender = x.intersection(genders)
        else:
            print('Невозможно изменить. Подобного нет в базе')

    def add_gender(self, x):
        if x.intersection(genders):
            self.__gender.update(x.intersection(genders))
        else:
            print('Невозможно добавить. Подобного нет в базе')

    def delete_gender(self, x):
        self.__gender.difference_update(x)

    @property
    def inner_material(self):
        return self.__inner_material

    @inner_material.setter
    def inner_material(self, x):
        if x.intersection(inner_materials):
            self.__inner_material = x.intersection(inner_materials)
        else:
            print('Такие материалы в базе отсутсвуют')

    def add_inner_material(self, x):
        if x.intersection(inner_materials):
            self.__inner_material.intersection_update(x)
        else:
            print('Таких материалов в базе отсутствуют')

    def delete_inner_material(self, x):
        self.__inner_material.difference_update(x)

    @property
    def external_material(self):
        return self.__external_material

    @external_material.setter
    def external_material(self, x: set):
        if x.intersection(external_materials):
            self.__external_material = x.intersection(external_materials)

    def add_external_material(self, x: set):
        if x.intersection(external_materials):
            self.__external_material.intersection_update(x)

    def delete_external_material(self, x: set):
        self.__external_material.difference_update(x)


if __name__ == '__main__':
    sizes = {'45': 17, "40": 2, "43": 0}
    sh = Shoes(price=7000, ="Nike", sizes=sizes, color={"red", 'black'})
    print(sh)
