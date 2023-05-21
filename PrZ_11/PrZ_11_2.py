t = 0
d = 0
g = ''
for i in open('text18-5.txt', encoding='UTF-16'):
    g += i
    for o in i:
        if o != "":
            d += 1
print(g)
print(end='\n')
print(f'Количество символов: {d}\n')


def lower_to_big(stroka):
    for k in stroka:
        yield k.upper()


text = g
h = (''.join(lower_to_big(text)))


f6 = open('text18-5_edited.txt', 'w')
f6.writelines(h)
f6.close()
