from sneakers_task.shoes import Shoes

heel_types = {'cowboy', 'tapered', 'shot-glass', 'column', 'wedge', 'stiletto', 'figured'}
nose_types = {'square', 'round', 'acute', 'open'}


class Heels(Shoes):

    def __init__(self, **kwargs):
        Shoes.__init__(self, **kwargs)
        self.__heel_type = self.preprocessing(kwargs.get('heel_type', set()))
        self.__nose_type = self.preprocessing(kwargs.get('nose_type', set()))
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
    def heel_type(self, x):
        set_x = self.preprocessing(x)
        if set_x.intersection(heel_types):
            self.__heel_type = set_x.intersection(heel_types)

    @property
    def nose_type(self):
        return self.__nose_type

    @nose_type.setter
    def nose_type(self, x):
        set_x = self.preprocessing(x)
        if set_x in nose_types:
            self.__nose_type = set_x

    @property
    def weddingbool(self):
        return self.__weddingbool

    def weeding(self):
        if self.__weddingbool == 1:
            print('Yes')
        else:
            print('No')
