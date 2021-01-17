#проект часов в командной строке

# это файл "с графікой", к сожалению совмещение этой графики с "часами" не удалось
# при добавлении в функцию вывод функционала часы показывают только вреся первого запуска факла
# буду отлаживать дальше


# импорт модулей
import os
from time import localtime, strftime, sleep

a = '\u2B1C'
b = '  '
ps = '\n'
zzero = [(a*4), (a + b + b + a), (a + b + b + a), (a + b + b + a), (a + b + b + a), (a*4)]
zero=(zzero[0] + ps + zzero[1] + ps + zzero[2] + ps + zzero[3] + ps + zzero[4] + ps + zzero[5])

a_4=a*4+b
a1_1=a+b+b+a+b
a1=a+b*4
a_1=b*3+a+b
a_0=b*2
a_t=a+b

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

# очиститель терминала
def cls():
    os.system(['clear', 'cls'][os.name=='nt'])

# переменные заготовки для цикла и выхода из него - в перспективе
ex_time=True

# функция определения одной цифры
zz=[]
def chooz(z):
    global zz
    if z=='0':
        zz=n_0
    elif z=='1':
        zz=n_1
    elif z=='2':
        zz=n_2
    elif z=='3':
        zz=n_3
    elif z=='4':
        zz=n_4
    elif z=='5':
        zz=n_5
    elif z=='6':
        zz=n_6
    elif z=='7':
        zz=n_7
    elif z=='8':
        zz=n_8
    elif z=='9':
        zz=n_9
    else:
        pass
    return zz

# функция для определения последовательности цифр
n_s=[]
def chooz_second(s):
    global n_s
    for i in range(0, 6):
       z_s=chooz(s[i])
       n_s=n_s+z_s
      
#  функция печати найтенной последовательности
def num_pr(az): 
    line1=az[0]+az[6]+n_t[0]+az[12]+az[18]+n_t[0]+az[24]+az[30]
    line2=az[1]+az[7]+n_t[1]+az[13]+az[19]+n_t[1]+az[25]+az[31]
    line3=az[2]+az[8]+n_t[2]+az[14]+az[20]+n_t[2]+az[26]+az[32]
    line4=az[3]+az[9]+n_t[3]+az[15]+az[21]+n_t[3]+az[27]+az[33]
    line5=az[4]+az[10]+n_t[4]+az[16]+az[22]+n_t[4]+az[28]+az[34]
    line6=az[5]+az[11]+n_t[5]+az[17]+az[23]+n_t[5]+az[29]+az[35]
    print()
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    print()

# основная часть
def show_time():
    y=1
    while y<10:              #пока такой цикл для удобства отладки
        time_format='%H%M%S'
        time_str=strftime(time_format)
        my_str=time_str
        chooz_second(my_str)
        num_pr(n_s)
        sleep(0.5)
        cls()
        y=y+1


show_time()

