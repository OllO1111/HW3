import random
people_famous = {'Джеймс Клерк Максвелл':'13.06.1831', 'Габриель Фаренгейт':'24.05.1686', 'Андерс Цельсий':'27.11.1701', 'Дмитрий Иванович Менделеев':'08.02.1834', 'Макс Планк':'23.04.1858', 'Галилео Галилей':'15.02.1564', 'Исаак Ньютон':'04.01.1643', 'Мария Склодовская-Кюри':'07.11.1867', 'Альберт Эйнштейн':'14.03.1879', 'Чарльз Дарвин ':'12.02.1809'}
number_units = {'0':'', '1':'первое', '2':'второе', '3':'третье', '4':'четвертое', '5':'пятое', '6':'шестое', '7':'седьмое', '8':'восьмое',  '9':'девятое'}
number_tens = {'2':'два', '3':'три'}
number_10 = {'0':'десятое', '1':'одиннадцатое', '2':'двеннадцатое', '3':'тринадцатое', '4':'четырнадцатое', '5':'пятнадцатое', '6':'шестнадцатое', '7':'семнадцатое', '8':'восемнадцатое',  '9':'девятнадцатое'}
month = {'01':'января', '02':'февраля', '03':'марта', '04':'апреля', '05':'мая', '06':'июня', '07':'июля', '08':'августа', '09':'сентября', '10':'октября', '11':'ноября', '12':'декабря', }

next_round = 1
while next_round == 1:
    keys = random.sample(list(people_famous), 5)
    values = [people_famous[i] for i in keys]
    people_random = dict(zip(keys, values))
    print(people_random)
    count_good = 0
    count_bad = 0
    for i in people_random:
        date_in = input(f"{i} когда родился? ")
        if people_random[i] == date_in: # Угадал
            count_good += 1
        else: # Не угадал
            # преобразуем дату в строку
            if people_random[i][0] == '0':
                day = number_units.get(people_random[i][1])
            elif people_random[i][0] == '1':
                day = number_10.get(people_random[i][1])
            else:
                space = ''
                if people_random[i][1] != '0':
                    space = ' '
                day = number_tens.get(people_random[i][0]) + 'дцать' + space + number_units.get(people_random[i][1])
            print(f"{day} {month.get(people_random[i][3:5])} {people_random[i][6:10]} года")
            count_bad += 1
    print (f"Количество правильных ответов: {count_good}")
    print (f"Количество неправильных ответов: {count_bad}")
    if (input('Еще поиграем? ') != 'Да'):
        next_round = 0
print('До новых встреч!')

