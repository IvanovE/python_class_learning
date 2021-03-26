from random import randint, sample, choice

main_sizes = [38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
s = ["Nike", "Adidas", "Reebok"]


def generate_list(x):
    b = [Sneakers(choice(s),
                  sizes=set(sample(main_sizes, randint(1, 10))),
                  price=randint(5000, 50000)) for _ in range(x)]
    return b


class Sneakers:
    default_ = "Nike"

    def __init__(self, **kwargs):
        self. = kwargs.get('', self.default_)
        self.sizes = kwargs.get('sizes', [])
        self.price = kwargs.get('price', 0)
        # self.f = [self., self.sizes, self.price]
        # self.cr = cr.append(self.f)

    # def add_change_(self, ):
    #     self. =
    #
    # def add_change_sizes(self, sizes):
    #     self.sizes = sizes
    #
    # def add_change_price(self, price):
    #     self.price = price

    def __str__(self):
        return f' - {self.}, sizes - {self.sizes}, price - {self.price}'

    def __repr__(self):
        return f' - {self.}, sizes - {self.sizes}, price - {self.price}'


def sneakers_sort(sl: list, sizes=main_sizes, type_sort=0, min_price=5000, max_price=50000):
    """
    Сортировка списка кроссовок.
    :param sl: Список элементов класса Сникерс
    :param sizes: список желаемых размеров кроссовок
    :param type_sort: тип сортировки: 0 - без сортировки(разброс), 1 - по возрастанию, 2 - по убыванию
    :param min_price: минимальная цена
    :param max_price: максимальная цена
    :return:

    """
    result_list = [i for i in sl if set(i.sizes).intersection(set(sizes))]

    customer_prices = [i for i in result_list if min_price <= i.price <= max_price]
    offer_prices_max = [i for i in result_list if max_price < i.price <= max_price + 3000]
    offer_prices_min = [i for i in result_list if min_price - 3000 <= i.price < min_price]

    if customer_prices:
        if type_sort:
            return sorted(customer_prices, key=lambda x: x.price, reverse=False if type_sort == 1 else True), \
                   len(offer_prices_min), min_price, len(offer_prices_max), max_price
        else:
            return customer_prices, len(offer_prices_min), min_price, len(offer_prices_max), max_price
    else:
        return "Нет модели, подходящей под параметры", len(offer_prices_min), min_price, \
               len(offer_prices_max), max_price


if __name__ == '__main__':
    # sneakers_list = [Sneakers(='nike', sizes=[41, 44], price=9000),
    #                  Sneakers(='adidas', sizes=[41, 42], price=10000),
    #                  Sneakers(='nike', sizes=[41, 42], price=20000),
    #                  Sneakers(='adidas', sizes=[41, 42], price=25000),
    #                  Sneakers(='nike', sizes=[41, 42], price=30000),
    #                  Sneakers(='adidas', sizes=[44, 45], price=45000)]

    sneakers_list = generate_list(10)
    print('Sneakers list:')
    for i in sneakers_list:
        print(i)
    sort_1, count_offer_min, min_price, count_offer_max, max_price = sneakers_sort(sneakers_list, sizes=[41, 43],
                                                                                   type_sort=2,
                                                                                   min_price=10000,
                                                                                   max_price=30000)
    print('Result list:')
    for i in sort_1:
        print(i)
    print(f'Вариантов ценой от {min_price} до {max_price} - {len(sort_1)}')
    if count_offer_min:
        print(f'Есть варинтов - {count_offer_min} ценой от {min_price-3000} до {min_price}')
    if count_offer_max:
        print(f'Есть вариантов - {count_offer_max} ценой от {max_price} до {max_price+3000}')
