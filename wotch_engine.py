#проект часов в командной строке

# импорт модулей
import os
from time import localtime, strftime, sleep


# очиститель терминала
def cls():
    os.system(['clear', 'cls'][os.name=='nt'])

# основная часть
def show_time():
    i=1
    while i<5:
        time_format='%H%M%S'
        time_str=strftime(time_format)
        print(time_str)
        sleep(0.9)
        i=i+1
        cls()



a = '\u2B1C'
b = '  '
ps = '\n'
zzero = [(a*4), (a + b + b + a), (a + b + b + a), (a + b + b + a), (a + b + b + a), (a*4)]
zero=(zzero[0] + ps + zzero[1] + ps + zzero[2] + ps + zzero[3] + ps + zzero[4] + ps + zzero[5])
#print(zero)

a_4=a*4+b
#print(a_4)
a1_1=a+b+b+a+b
#print(a1_1)
a1=a+b*4
#print(a1)
a_1=b*3+a+b
a_0=b*2
a_t=a+b
#print(a_1)

n_0=[a_4, a1_1, a1_1, a1_1, a1_1, a_4]
n_1=[a_1, a_1, a_1, a_1, a_1, a_1]
n_2=[a_4, a_1, a_4, a1, a1, a_4]
n_3=[a_4, a_1, a_4, a_1, a_1, a_4]
n_4=[a1_1, a1_1, a1_1, a_4, a_1, a_1]
n_5=[a_4, a1, a_4, a_1, a_1, a_4]
n_6=[a_4, a1, a_4, a1_1, a1_1, a_4]
n_7=[a_4, a_1, a_1, a_1, a_1, a_1]
n_8=[a_4, a1_1, a_4, a1_1, a1_1, a_4]
n_9=[a_4, a1_1, a_4, a_1, a_1, a_4]
n_t=[a_0, a_t, a_0, a_0, a_t, a_0]  #реализация точки в часах

#
#perpet=True
#def gen_point():
#    while perpet==True:
#        q=1
#        for q in (1, 5):
#            if q==1:
#                n_t=[a_t, a_0, a_0, a_0, a_0, a_t]
#                sleep(0.5)
#            elif q==2:
#                n_t=[a_0, a_t, a_0, a_0, a_t, a_0]
#                sleep(0.5)
#            elif q==3:
#                n_t=[a_0, a_0, a_t, a_t, a_0, a_0]
#                sleep(0.5)
#            elif q==4:
#                n_t=[a_0, a_t, a_0, a_0, a_t, a_0]
#                sleep(0.5)
#            else:
#                n_t=[a_t, a_0, a_0, a_0, a_0, a_t]
#                sleep(0.5)

def print_point():
    for i in range(0, 6):
        print(n_t[i])



# запуск программы
show_time()
print()
print_point()
