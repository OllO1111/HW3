numbers_in = str(input('Введите элементы списка через любой из символов (,;/): '))
if numbers_in.find(',') > -1:
    numbers_list = numbers_in.split(',')
if numbers_in.find(';') > -1:
    numbers_list = numbers_in.split(';')
if numbers_in.find('/') > -1:
    numbers_list = numbers_in.split('/')
numbers_uniq = list(set(map(int,numbers_list)))
numbers_out = ','.join(map(str,numbers_uniq))
print('Результат: ', numbers_out)