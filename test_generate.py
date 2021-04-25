from random import randint, choice, sample
from shoes import brands, inner_materials, external_materials, colors, styles, genders
from sneakers import sports, seasons, Sneakers
from heels import heel_types, nose_types, Heels
from weddingheels import Weddingheels

brand_none = brands.copy()
brand_none.add(None)


def generate_base():
    return {
        'brand': choice(list(brand_none)),
        'color': sample(list(colors), randint(0, 5)),
        'price': randint(300, 90000),
        'style': sample(list(styles), randint(0, 5)),
        'gender': sample(list(genders), randint(0, 2)),
        'inner_material': sample(list(inner_materials), randint(0, 3)),
        'external_material': sample(list(external_materials), randint(0, 3))
    }


def generate_sneakers(count):
    result = []
    for _ in range(count):
        item = Sneakers(**generate_base(), sport=sample(list(sports), randint(0, 3)), season=sample(list(seasons),
                                                                                                    randint(0, 2)))
        result.append(item)
    return result


def generate_heels(count):
    result = []
    for _ in range(count):
        item = Heels(**generate_base(), heel_type=sample(list(heel_types), randint(0, 1)),
                     nose_type=sample(list(nose_types), randint(0, 1)))
        result.append(item)
    return result


def generate_weddingheels(count):
    result = []
    for _ in range(count):
        item = Weddingheels(**generate_base(), heel_type=sample(list(heel_types), randint(0, 1)),
                     nose_type=sample(list(nose_types), randint(0, 1)))
        result.append(item)
    return result
