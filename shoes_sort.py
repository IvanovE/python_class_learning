from sneakers_task.sneakers import Sneakers
from sneakers_task.weddingheels import Weddingheels

data = []


def shoes_sort(season=None, wedding=None, color=None, max_price=0, min_price=0, size=None):
    return_data = set()
    data_price_increase = set()
    data_price_decrease = set()

    if season and wedding:
        return 'Error'

    if season:
        return_data = {i for i in data if isinstance(i, Sneakers) and i.season.intersection(preprocessing(season))}

    if wedding:
        return_data = {i for i in data if isinstance(i, Weddingheels)}

    if color:
        return_data = {i for i in return_data if i.color == preprocessing(color)}
    if size:
        return_data = {i for i in return_data if i.check_on_stock().intersection(preprocessing(size))}
    if max_price:
        data_price_increase = {i for i in return_data if max_price < i.price <= max_price + 3000}
        data_price_decrease = {i for i in return_data if min_price - 3000 <= i.price < min_price}

        return_data = {i for i in return_data if min_price <= i.price <= max_price}
    else:
        data_price_decrease = {i for i in return_data if min_price - 3000 <= i.price < min_price}
        return_data = {i for i in return_data if min_price <= i.price}

    return return_data, data_price_decrease, data_price_increase


def preprocessing_str(x):
    if type(x) is set:
        x = {i.lower() for i in x if type(i) is str}
    elif type(x) is str:
        x = x.lower()
    return x


def preprocessing(x):
    """

    :param x:
    :return:
    """
    if type(x) is list:
        return preprocessing_str(set(x))
    if type(x) is int or type(x) is str:
        empty_set = set()
        empty_set.add(x)
        return preprocessing_str(empty_set)
    if type(x) is set:
        return preprocessing_str(x)
    if type(x) is tuple:
        return set(x)
    return preprocessing_str(x)


if __name__ == '__main__':
    s = Sneakers(brand='Nike', season='summer', sizes={39: 1, 40: 1})
    p = Sneakers(brand='Adidas')
    t = Weddingheels()
    data = [s, p, t]
    print(shoes_sort(season='summer'))
