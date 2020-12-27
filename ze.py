number=[]
a=int(input("введите целое число от 0 до 9 -- "))
number.append(a)
a=int(input("введите целое число от 0 до 9 -- "))
number.append(a)
a=int(input("введите целое число от 0 до 9 -- "))
number.append(a)
print(number)
#item=True
#ins=item not in number 
#print(ins("Нет нудевых значений"))

#вообще не понимаю как использовать "ленивые выжажения" в реальном коде, в файле len.py пробовал і так, і так...
#примеры из Джтпитера работали по другому, хотелось бы посмотреть их применения в реальном коде

if number[0]>(number[1]+number[2]):
    print("первое значение больше суммы 2-ого и 3-его, выводим: 1е-2е-3е:", number[0]-number[1]-number[2])
if number[0]<(number[1]+number[2]):
    print("первое значение меньше суммы 2-ого и 3-его, выводим: 2е+3е-1е:", number[1]+number[2]-number[0])
if number[0]>50 and (number[1]>number[0] or number[2]>number[0]):
    print("1-ое значение больше '50' 2-ого ілі 3-е больше 1-ого, выводим: 'Vsja'")
if number[0]>5 or number[1]==7 and number[2]==7:
    print("1-ое значение больше '5' или оба остальных = '7', выводим: 'Petja'")
