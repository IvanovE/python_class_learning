from sneakers_task.shoes import Shoes

heel_types = {'cowboy', 'tapered', 'shot-glass', 'column', 'wedge', 'stiletto', 'figured'}
nose_types = {'square', 'round', 'acute', 'open'}


class Heels(Shoes):

    def __init__(self, **kwargs):
        #todo intesection
        Shoes.__init__(self, **kwargs)
        self.__heel_type = kwargs.get('heel_type', {})
        self.__nose_type = kwargs.get('nose_type', {})
        self.__weddingbool = kwargs.get('weddingbool', False)

    def __str__(self):
        return 'Heels \n' + Shoes.__repr__(self) + f'heel_type - {self.heel_type}\n, nose_type - {self.nose_type},\n' \
                                     f'weeding - {self.weddingbool}\n'

    def __repr__(self):
        return 'Heels \n' + Shoes.__repr__(self) + f'heel_type - {self.heel_type}\n, nose_type - {self.nose_type},\n' \
                                     f'weeding - {self.weddingbool}\n'

    @property
    def heel_type(self):
        return self.__heel_type

    @heel_type.setter
    def heel_type(self, x: set):
        if x.intersection(heel_types):
            self.__heel_type = x.intersection(heel_types)

    @property
    def nose_type(self):
        return self.__nose_type

    @nose_type.setter
    def nose_type(self, x: set):
        # todo only one item
        if x.intersection(nose_types):
            self.__nose_type = x.intersection(nose_types)

    def weeding(self):
        if self.__weddingbool == 1:
            print('Yes')
        else:
            print('No')

    #todo weddingbools property


if __name__ == '__main__':
    w = Heels(price=9000)
    print(w)