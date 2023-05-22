#!/usr/bin/python
# -*- coding: utf-8 -*-
class Frukt:
    def __init__(self, name, ves):
        self.name = name
        self.ves = ves


class Apple(Frukt):
    def __init__(self, name, ves, color):
        super().__init__(name, ves)
        self.color = color

    def returns(self):
        return self.name, self.ves, self.color


class Apelsin(Frukt):
    def __init__(self, name, ves, color):
        super().__init__(name, ves)
        self.color = color

    def returns(self):
        return self.name, self.ves, self.color


fruit = Frukt('Персик', 300,)
yablok = Apple('Аленушка', 200, 'Желтый')
orange = Apelsin('Моро', 500, 'Оранжевый')
print(yablok.__dict__)
print(yablok.returns())
print(orange.__dict__)
print(orange.returns())
