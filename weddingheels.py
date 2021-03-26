from sneakers_task.heels import Heels
from sneakers_task.shoes import Shoes


class Weddingheels(Heels):

    def __init__(self, **kwargs):
        Heels.__init__(self, **kwargs)

    def __str__(self):
        return 'Weddingheels \n' + Heels.__str__(self)

    def __repr__(self):
        return 'Weddingheels \n' + Heels.__repr__(self)

    @Heels.price.getter
    def price(self, days=31):
        return f'Наценка отсутсвует, цена = {self.price}'


if __name__ == '__main__':
    w = Weddingheels(price=90000)
    w.price(6)
