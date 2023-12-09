import random
people_famous = {'Джеймс Клерк Максвелл':'13.06.1831', 'Габриель Фаренгейт':'24.05.1686', 'Андерс Цельсий':'27.11.1701', 'Дмитрий Иванович Менделеев':'08.02.1834', 'Макс Планк':'23.04.1858', 'Галилео Галилей':'15.02.1564', 'Исаак Ньютон':'04.01.1643', 'Мария Склодовская-Кюри':'07.11.1867', 'Альберт Эйнштейн':'14.03.1879', 'Чарльз Дарвин ':'12.02.1809'}
number_units = {'0':'', '1':'один', '2':'два', '3':'три', '4':'четыре', '5':'пять', '6':'шесть', '7':'семь', '8':'восемь',  '9':'девять'}
number_10 = {'0':'десять', '1':'одиннадцать', '2':'двеннадцать', '3':'тринадцать', '4':'четырнадцать', '5':'пятнадцать', '6':'шестнадцать', '7':'семнадцать', '8':'восемнадцать',  '9':'девятнадцать'}
month = {'01':'январь', '02':'февраль', '03':'март', '04':'апрель', '05':'май', '06':'июнь', '07':'июль', '08':'август', '09':'сентябрь', '10':'октябрь', '11':'ноябрь', '12':'декабрь', }

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
            if date_in[0] == '0':
                day = number_units.get(date_in[1])
            elif date_in[0] == '1':
                day = number_10.get(date_in[1])
            else:
                space = ''
                if date_in[1] != '0':
                    space = ' '
                day = number_units.get(date_in[0]) + 'дцать' + space + number_units.get(date_in[1])
            print(f"{day} {month.get(date_in[3:5])} {date_in[6:10]} год")
            count_bad += 1
    print (f"Количество правильных ответов: {count_good}")
    print (f"Количество неправильных ответов: {count_bad}")
    if (input('Еще поиграем? ') != 'Да'):
        next_round = 0
print('До новых встреч!')
