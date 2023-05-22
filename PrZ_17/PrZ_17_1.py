#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint


class Bank:
    def __init__(self, summa, stavka):
        self.summa = summa
        self.stavka = stavka

    def nachislenuya(self):
        return (self.summa * self.stavka)/100

    def snyatie(self):
        return (self.summa * self.stavka)/100 + self.summa


bbb = Bank(randint(100, 1000), randint(10, 100))
print(bbb.__dict__)
print(f'\nИтоговая прибыль: {bbb.nachislenuya()}\n')
print(f'Общая сумма: {bbb.snyatie()}\n')
