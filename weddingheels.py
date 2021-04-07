from sneakers_task.heels import Heels


class Weddingheels(Heels):

    def __init__(self, **kwargs):
        Heels.__init__(self, **kwargs)

    def __str__(self):
        return 'Weddingheels \n' + Heels.__str__(self)

    def __repr__(self):
        return 'Weddingheels \n' + Heels.__repr__(self)
