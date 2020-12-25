# файл игры "крестики-нолики"
import time
# объявление глобальных переменных
win=False
l1='1'
l2='2'
l3='3'
l4='4'
l5='5'
l6='6'
l7='7'
l8='8'
l9='9'
l0='-'
hold=''
x3='XXX'
o3='OOO'
s_123=l1+l2+l3
s_456=l4+l5+l6
s_789=l7+l8+l9
s_159=l1+l5+l9
s_357=l3+l5+l7
s_147=l1+l4+l7
s_258=l2+l5+l8
s_369=l3+l6+l9
dryn=(s_123, s_456, s_789, s_159, s_357, s_147, s_258, s_369)


#модуль отрисовки игрового поля
def print_field():
    print(l1, l2, l3, sep=' ! ')
    print(l0*9)
    print(l4, l5, l6, sep=' ! ')
    print(l0*9)
    print(l7, l8, l9, sep=' ! ')
    print()
    time.sleep(1)


# функции ходов
def step_X():
    print("Вы играете символом Х, выберете номер позиции на игровой доске: ")
    global hold
    hold=input()

def step_O():
    print("Вы играете символом O, выберете номер позиции на игровой доске: ")
    global hold
    hold=input()

# функции

def change_field_X(hold):
    global l1
    if hold==l1:    
        l1='X'
    global l2
    if hold==l2:
        l2='X'
    global l3
    if hold==l3:
        l3='X'
    global l4
    if hold==l4:
        l4='X'
    global l5
    if hold==l5:
        l5='X'
    global l6
    if hold==l6:
        l6='X'
    global l7
    if hold==l7:
        l7='X'
    global l8
    if hold==l8:
        l8='X'
    global l9
    if hold==l9:
        l9='X'
    global s_123
    s_123=l1+l2+l3
    global s_456
    s_456=l4+l5+l6
    global s_789
    s_789=l7+l8+l9
    global s_159
    s_159=l1+l5+l9
    global s_357
    s_357=l3+l5+l7
    global s_147
    s_147=l1+l4+l7
    global s_258
    s_258=l2+l5+l8
    global s_369
    s_369=l3+l6+l9
    global dryn
    dryn=(s_123, s_456, s_789, s_159, s_357, s_147, s_258, s_369)
   
def change_field_O(hold):
    global l1
    if hold==l1:
        l1='O'
    global l2
    if hold==l2:
        l2='O'
    global l3
    if hold==l3:
        l3='O'
    global l4
    if hold==l4:
        l4='O'
    global l5
    if hold==l5:
        l5='O'
    global l6
    if hold==l6:
        l6='O'
    global l7
    if hold==l7:
        l7='O'
    global l8
    if hold==l8:
        l8='O'
    global l9
    if hold==l9:
        l9='O'
    global s_123
    s_123=l1+l2+l3
    global s_456
    s_456=l4+l5+l6
    global s_789
    s_789=l7+l8+l9
    global s_159
    s_159=l1+l5+l9
    global s_357
    s_357=l3+l5+l7
    global s_147
    s_147=l1+l4+l7
    global s_258
    s_258=l2+l5+l8
    global s_369
    s_369=l3+l6+l9
    global dryn
    dryn=(s_123, s_456, s_789, s_159, s_357, s_147, s_258, s_369)

# выполняемая часть кода
print ('Вас приветствует парная игра "крестики-нолики"!')
time.sleep(2)
print ('игровое поле имеет следующий вид:')
time.sleep(2)
print_field()
print ('вы сможете играть классическими символами Х или О')
time.sleep(0.5)
print ('определитесь кто будет делать первый ход...')
time.sleep(2)

for i in range (9):
    if ('OOO' not in dryn):
        step_X()
        change_field_X(hold)
        print_field()
    else:
        print('Игра окончена. Победа O-игрока')
        break

    if ('XXX' not in dryn):
        step_O()
        change_field_O(hold)
        print_field()
    else:
        print('Игра окончена. Победа X-игрока')
        break

