# Вариант 5.
# Дана строка-предложение на русском языке и число К (0 < K < 10).
# Зашифровать строку, выполнив циклическую замену каждой буквы на букву того же регистра,
# расположенную в алфавите на К-й позиции после шифруемой буквы
# (например, для K = 2 «А» перейдет в «В», «а» - в «в», «Б» - в «Г», «я» - в «б» и т. д.).
# Букву «ё» в алфавите не учитывать, знаки препинания и пробелы не изменять.
import random

str_code = input("Введите предложение на русском языке: ")
k = random.randrange(0, 10)
print(f"Шаг кодирования: {k}")
a = 'а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'
lst = a.split(' ')
code_value = ''
for word in str_code:
    if word.lower() in lst:
        try:
            if word == word.lower():
                code_value += lst[lst.index(word.lower()) + k]
            elif word == word.upper():
                code_value += lst[lst.index(word.lower()) + k].upper()
        except IndexError:
            count = (lst.index(word.lower()) + k) - len(lst)
            if word == word.lower():
                code_value += lst[count]
            elif word == word.upper():
                code_value += lst[count].upper()
    else:
        code_value += word
print(f"Закодированное предложение: {code_value}")
