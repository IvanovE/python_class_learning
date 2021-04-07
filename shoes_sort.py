from sneakers_task.sneakers import Sneakers
from sneakers_task.weddingheels import Weddingheels

data = []


def shoes_sort(season=None, wedding=None, color=None, max_price=0, min_price=0, size=None):
    data_color = set()
    data_size = set()
    data_price = set()
    data_price_increased_range = set()

    if season:
        data_season = {i for i in data if isinstance(i, Sneakers) and i.season == preprocessing(season)}
        if color:
            data_color = {i for i in data_season if i.color == preprocessing(color)}
        if size:
            data_size = [i for i in data_season if i.sizes.intesrion(preprocessing(size))]
        if min_price and max_price:
            data_price = {i for i in data_season if min_price <= i.price <= max_price}
            data_price_increased_range = {i for i in data_season if i.price <= min_price - 3000 or
                                          i.price >= max_price + 3000}
        elif min_price:
            data_price = {i for i in data_season if min_price <= i.price}
            data_price_increased_range = {i for i in data_season if i.price <= min_price - 3000}
        elif max_price:
            data_price = {i for i in data_season if i.price <= max_price}
            data_price_increased_range = {i for i in data_season if i.price >= max_price + 3000}


        # return

    if wedding:
        data_wedding = {i for i in data if isinstance(i, Weddingheels)}
        if color:
            data_color = {i for i in data_wedding if i.color == preprocessing(color)}
        if size:
            data_size = [i for i in data_wedding if i.sizes.intesrion(preprocessing(size))]
        if min_price and max_price:
            data_price = {i for i in data_wedding if min_price <= i.price <= max_price}
            data_price_increased_range = {i for i in data_wedding if i.price <= min_price - 3000 or
                                          i.price >= max_price + 3000}
        elif min_price:
            data_price = {i for i in data_wedding if min_price <= i.price}
            data_price_increased_range = {i for i in data_wedding if i.price <= min_price - 3000}
        elif max_price:
            data_price = {i for i in data_wedding if i.price <= max_price}
            data_price_increased_range = {i for i in data_wedding if i.price >= max_price + 3000}

        # return

    if color:
        data_color = {i for i in data if i.color == preprocessing(color)}
        if size:
            data_size = [i for i in data_color if i.sizes.intesrion(preprocessing(size))]
        if min_price and max_price:
            data_price = {i for i in data_color if min_price <= i.price <= max_price}
            data_price_increased_range = {i for i in data_color if i.price <= min_price - 3000 or
                                          i.price >= max_price + 3000}
        elif min_price:
            data_price = {i for i in data_color if min_price <= i.price}
            data_price_increased_range = {i for i in data_color if i.price <= min_price - 3000}
        elif max_price:
            data_price = {i for i in data_color if i.price <= max_price}
            data_price_increased_range = {i for i in data_color if i.price >= max_price + 3000}

        # return

    if size:
        data_size = [i for i in data if i.sizes.intesrion(preprocessing(size))]
        if min_price and max_price:
            data_price = {i for i in data_size if min_price <= i.price <= max_price}
            data_price_increased_range = {i for i in data_size if i.price <= min_price - 3000 or
                                          i.price >= max_price + 3000}
        elif min_price:
            data_price = {i for i in data_size if min_price <= i.price}
            data_price_increased_range = {i for i in data_color if i.price <= min_price - 3000}
        elif max_price:
            data_price = {i for i in data_size if i.price <= max_price}
            data_price_increased_range = {i for i in data_size if i.price >= max_price + 3000}

        # return

    if min_price and max_price:
        data_price = {i for i in data if min_price <= i.price <= max_price}
        data_price_increased_range = {i for i in data_color if i.price <= min_price - 3000 or
                                      i.price >= max_price + 3000}
    elif min_price:
        data_price = {i for i in data if min_price <= i.price}
        data_price_increased_range = {i for i in data_color if i.price <= min_price - 3000}
    elif max_price:
        data_price = {i for i in data if i.price <= max_price}
        data_price_increased_range = {i for i in data_color if i.price >= max_price + 3000}

    # return


def preprocessing_str(x):
    if type(x) is set:
        x = {i.lower() for i in x if type(i) is str}
    elif type(x) is str:
        x = x.lower()
    return x


def preprocessing(x):
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
