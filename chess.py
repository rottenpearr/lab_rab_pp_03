letters = ["A", "B", "C", "D", "E", "F", "G", "H"]

print('Введите номер горизонтали первой фигуры (k): ')
x1 = int(input())
print('Введите букву вертикали первой фигуры (l): ')
y1 = letters.index(input())
print('Первая фигура это (ферзь, ладья, слон или конь): ')
figure_1 = str(input())
print('Введите номер горизонтали второй фигуры (n): ')
x2 = int(input())
print('Введите букву вертикали второй фигуры (m): ')
y2 = letters.index(input())


def cell(horizontal, vertical):
    if (horizontal % 2 != 0 and vertical % 2 != 0) or (horizontal % 2 == 0 and vertical % 2 == 0):
        color = 'белая'
    else:
        color = 'чёрная'
    return color


def color_comparison():
    color_1 = cell(x1, y1)
    color_2 = cell(x2, y2)
    if color_1 == color_2:
        print('Клетки одного цвета')
    else:
        print('Клетки разного цвета')


def menace(name):
    module_y = abs(y1 - y2)
    module_x = abs(x1 - x2)
    if name == 'ферзь' or name == 'Ферзь':
        if y1 == y2 or x1 == x2 or module_x == module_y:
            print('Ферзь представляет угрозу!')
            print('На позицию второй фигуры можно попасть за 1 ход')
        else:
            print('Ферзь не представляет угрозы ~')
            new_x1 = x2
            print('На позицию второй фигуры можно попасть за 2 хода:\n',
                  'Первый ход на:', new_x1, y1)
            new_y1 = y2
            print(' Второй ход на:', new_x1, new_y1)
    elif name == 'ладья' or name == 'Ладья':
        if y1 == y2 or x1 == x2:
            print('Ладья представляет угрозу!')
            print('На позицию второй фигуры можно попасть за 1 ход')
        else:
            print('Ладья не представляет угрозы ~')
            new_x1 = x2
            print('На позицию второй фигуры можно попасть за 2 хода:\n',
                  'Первый ход на:', new_x1, y1)
            new_y1 = y2
            print(' Второй ход на:', new_x1, new_y1)
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
