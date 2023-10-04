print('Введите номер горизонтали первой фигуры: ')
L = int(input())
print('Введите номер вертикали первой фигуры: ')
k = int(input())
print('Первая фигура это (ферзь, ладья, слон или конь): ')
figure_1 = str(input())
print('Введите номер горизонтали второй фигуры: ')
n = int(input())
print('Введите номер вертикали второй фигуры: ')
m = int(input())


def cell(horizontal, vertical):
    if (horizontal % 2 != 0 and vertical % 2 != 0) or (horizontal % 2 == 0 and vertical % 2 == 0):
        color = 'белая'
    else:
        color = 'чёрная'
    return color


def color_comparison():
    color_1 = cell(L, k)
    color_2 = cell(n, m)
    if color_1 == color_2:
        print('Клетки одного цвета')
    else:
        print('Клетки разного цвета')


def menace(name):
    module_x = abs(k - m)
    module_y = abs(L - n)
    if name == 'ферзь' or name == 'Ферзь':
        if k == m or L == n or module_x == module_y:
            print('Ферзь представляет угрозу!')
            print('На позицию второй фигуры можно попасть за 1 ход')
        else:
            print('Ферзь не представляет угрозы ~')
            new_l = n
            print('На позицию второй фигуры можно попасть за 2 хода:\n',
                  'Первый ход на:', new_l, k)
            new_k = m
            print(' Второй ход на:', new_l, new_k)
    elif name == 'ладья' or name == 'Ладья':
        if k == m or L == n:
            print('Ладья представляет угрозу!')
            print('На позицию второй фигуры можно попасть за 1 ход')
        else:
            print('Ладья не представляет угрозы ~')
            new_l = n
            print('На позицию второй фигуры можно попасть за 2 хода:\n',
                  'Первый ход на:', new_l, k)
            new_k = m
            print(' Второй ход на:', new_l, new_k)
    elif name == 'слон' or name == 'Слон':
        if module_x == module_y:
            print('Слон представляет угрозу!')
            print('На позицию второй фигуры можно попасть за 1 ход')
        else:
            print('Слон не представляет угрозы ~')
            print('К сожалению слоном в эту клетку попасть никак нельзя =(')
    elif name == 'конь' or name == 'Конь':
        if (module_y == 2 and module_x == 1) or (module_x == 2 and module_y == 1):
            print('Конь представляет угрозу!')
        else:
            print('Конь не представляет угрозы ~')


color_comparison()
menace(figure_1)
