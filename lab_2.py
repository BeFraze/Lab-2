from csv import *
from random import randint
import xml.etree.ElementTree as et


print('Вариант 10')
print('Задание №1')

with open('books.csv', encoding='windows-1251') as csvfile:
    file = reader(csvfile)
    cnt = 0
    for row in file:
        row = str(row)
        if str(row.split(';')[0]) != 'ID':
            ttl = row.split(';')[1]
            if len(ttl) > 30:
                cnt += 1
print(cnt)
print()


print('Задание №2')

while True:
    txt = 'Не найдено'
    aut = input('Введите автора или напишите "далее":')
    if aut == 'далее':
        print('Спасибо за использование!')
        break
    with open('books.csv', encoding='windows-1251') as csvfile:
        file = reader(csvfile)
        for row in file:
            row = str(row)
            if str(row.split(';')[0]) != 'ID':
                if (row.split(';')[3] == aut) and (int(str(row.split(';')[6])[6:10]) >= 2018):
                    print(row.split(';')[1])
                    text = "Конец списка"
    print(text)
print()

print('Задание №3 в файле res')

with open('books.csv', encoding='windows-1251') as csvfile:
    file = list(DictReader(csvfile, delimiter=';'))
    res = open('res.txt', 'w')
    for i in range(20):
        nmb = randint(1, 9400)
        res.write(f"{i + 1} {file[nmb]['Автор']} - {file[nmb]['Название']} - {int(str(file[nmb]['Дата поступления'])[6:10])} \n")
print()


print('Задание №4')

file = et.parse('currency.xml')
root = file.getroot()
dct = {}

for vlt in root.findall('Valute'):
    name = vlt.find('Name').text
    char_code = vlt.find('CharCode').text
    dct[name] = char_code

print("Словарь 'Name - CharCode':")
for name, char_code in dct.items():
    print(f"{name}: {char_code}")
print()


print('Задание №5')

pbls = []
with open('books-en.csv', encoding='windows-1251') as csvfile:
    file = reader(csvfile, delimiter=';')
    data = [i for i in file][1:]
    for row in data:
        pbls.append(row[4])

for pbl in set(pbls):
    print(pbl)
print()


print('Задание №6')

dld = [0]*20
name = [0]*20
t20 = [0]*20

with open('books-en.csv', encoding='windows-1251') as csvfile:
    file = reader(csvfile, delimiter=';')
    data = [i for i in file][1:]
    for row in range(20):
        for book in data:
            if int(book[5]) > dld[row] and book[1] not in name:
                dld[row] = int(book[5])
                name[row] = book[1]
        t20[row] = f"{name[row]} - {dld[row]} downloads"

cnt = 0
for book in t20:
    cnt += 1
    print(f"{cnt}-{book}")