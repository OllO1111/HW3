size_list = int(input('Введите количество элементов: '))
out_list = []
for i in range(size_list):
    out_list.append(int(input(f'Введите {i + 1} элемент: ')))

print(out_list)
