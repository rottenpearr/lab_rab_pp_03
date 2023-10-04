print('Введите номер вертикали первой фигуры: ')
k = int(input())
print('Введите номер горизонтали первой фигуры: ')
L = int(input())
print('Первая фигура это (ферзь, ладья, слон или конь): ')
figure_1 = str(input())
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
        else:
            print('Ферзь не представляет угрозы ~')
    elif name == 'ладья' or name == 'Ладья':
        if k == m or L == n:
            print('Ладья представляет угрозу!')
        else:
            print('Ладья не представляет угрозы ~')
    elif name == 'слон' or name == 'Слон':
        if module_x == module_y:
            print('Слон представляет угрозу!')
        else:
            print('Слон не представляет угрозы ~')
    elif name == 'конь' or name == 'Конь':
        if (module_y == 2 and module_x == 1) or (module_x == 2 and module_y == 1):
            print('Конь представляет угрозу!')
        else:
            print('Конь не представляет угрозы ~')


color_comparison()
menace(figure_1)
