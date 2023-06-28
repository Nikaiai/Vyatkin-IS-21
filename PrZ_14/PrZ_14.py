# Вариант - 5.
# Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые маски»
# перенести в первый файл строки с нулевым четвертым октетом, а во второй
# – все остальные. Посчитать количество полученных строк в каждом файле.

import re

with open('ip_address.txt', 'r') as ip:
    text = ip.read()
zero_okt = re.findall(r'\d{3}.\d{3}.\d{3}.[0]', text)
dr_okt = re.findall(r'\d{3}.\d{3}.\d{3}.\d{2}[1-9]', text)
print(f'Количество масок с нулевым четертым октетом: {len(zero_okt)}')
print(f'Количетсво остальных масок: {len(dr_okt)}')
zero_okt_str = str(zero_okt)
dr_okt_str = str(dr_okt)
with open('zero_oktet.txt', 'w') as zo:
    zo.write(zero_okt_str)
with open('dr_okt.txt', 'w') as do:
    do.write(dr_okt_str)
