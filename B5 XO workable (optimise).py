# Выбор начала игры с Х или О происходит рандомно
import random
# Переменная switch нужна, чтобы не вызывать много раз функцию watcher
# и не дублировать вывод резултата игры
switch = True
field = [[" "] * 3 for i in range (3) ]
# Функция выводящая игровое поле на экран
def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | { ' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

show()
# Функция взаимодействующая с играком, принимает координаты, проверяет их корректность
# и записывает Х или О в field
def ask():
    global num, first, switch
    # if нужен для корректного работы функции, так как значение счётчика num в начале игры
    # выбирается рандомно 1 или 2 из-за этого в случае ничьей или чьей-то победы функция 
    # может снова запросить координаты.
    if num != 10 and first == 1 and switch  or num != 11 and first == 2 and switch:
        while True:
            cords = input(" Ваш ход (введите 2 координаты через пробел): ").split()

            if len(cords) != 2:
                print("Введите 2 координаты!")
                continue
            x, y = cords

            if not(x.isdigit()) or not(y.isdigit()):
                print("Введите числа!")
                continue

            x, y = int(x), int(y)

            if 0 <= x <= 2 and 0 <= y <= 2 :
                if field[x][y] == " ":
                    return x, y
                else:
                    print("Клетка занята!")
            else:
                print("Координаты вне диапазона!")
   
# Случайный выбор значения счётчика, определяющего, кто ходит первым
num = random.randint(1,2)
first = num

# Функция следящая за ходом игры и останавливающая её, в случае чьей-то победы.
# Первый вариант функции до оптимизации:
#
##def watcher():
##    f = list(field)
##    f0 = f[0]
##    f1 = f[1]
##    f2 = f[2]
##    if f0[0] == f0[1] == f0[2] == 'X' or\
##       f1[0] == f1[1] == f1[2] == 'X' or\
##       f2[0] == f2[1] == f2[2] == 'X' or\
##       f0[0] == f1[0] == f2[0] == 'X' or\
##       f0[1] == f1[1] == f2[1] == 'X' or\
##       f0[2] == f1[2] == f2[2] == 'X' or\
##       f0[0] == f1[1] == f2[2] == 'X' or\
##       f0[2] == f1[1] == f2[0] == 'X':
##        print('Выиграли крестики - X')
##        return False
##    if f0[0] == f0[1] == f0[2] == 'O' or\
##       f1[0] == f1[1] == f1[2] == 'O' or\
##       f2[0] == f2[1] == f2[2] == 'O' or\
##       f0[0] == f1[0] == f2[0] == 'O' or\
##       f0[1] == f1[1] == f2[1] == 'O' or\
##       f0[2] == f1[2] == f2[2] == 'O' or\
##       f0[0] == f1[1] == f2[2] == 'O' or\
##       f0[2] == f1[1] == f2[0] == 'O':
##        print('Выиграли нолики - O')
##        return False
##    return True

def watcher():
    f = field
    win_cords = (
        (f[0][0], f[0][1],f[0][2]),(f[1][0], f[1][1],f[1][2]),(f[2][0], f[2][1],f[2][2]),
        (f[0][0], f[1][0],f[2][0]),(f[0][1], f[1][1],f[2][1]),(f[0][2], f[1][2],f[2][2]),
        (f[0][0], f[1][1],f[2][2]),(f[0][2], f[1][1],f[2][0])
        )
    for each in win_cords:
        if each[0] == each[1] == each[2] == 'X':
            print('Выиграли крестики - X')
            return False
        if each[0] == each[1] == each[2] == 'O':
            print('Выиграли нолики - O')
            return False
    return True

while True:
    
    if num % 2 == 1:
        print("Ходит крестик!")
    else:
        print("Ходит нолик!")

    x, y = ask()
        
    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"
    
    show()
    switch = watcher()
    if not switch:
        print('     конец игры!')
        break
    
    num += 1
# if для корректного определения ничьей в зависимости от первого значения счётчика.
    if num == 10 and first == 1 or num == 11 and first == 2:
        print("Ничья!")
        break
ask()

