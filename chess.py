print('Введите номер вертикали первой фигуры: ')
k = int(input())
print('Введите номер горизонтали первой фигуры: ')
L = int(input())
print('Введите номер вертикали второй фигуры: ')
m = int(input())
print('Введите номер горизонтали второй фигуры: ')
n = int(input())


def cell(horizontal, vertical):
    if (horizontal % 2 != 0 and vertical % 2 != 0) or (horizontal % 2 == 0 and vertical % 2 == 0):
        color = 'белая'
    else:
        color = 'чёрная'
    return color


color_1 = cell(L, k)
color_2 = cell(n, m)

if color_1 == color_2:
    print('Клетки одного цвета')
else:
    print('Клетки разного цвета')




