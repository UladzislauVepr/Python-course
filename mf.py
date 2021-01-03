

#исходные данные
text_1=["Генераторы — это функции...", "которые можно приостанавливать и возобновлять", "во время их выполнения,", " при этом они возвращают объект,", "который можно итерировать."]
text_2=["В отличие от списков, ", "они ленивы и поэтому работают с ", "текущим элемент только по запросу"]
text_3=["Чтобы создать генератор, ", "необходимо определить функцию, как обычно, ", "но использовать yield вместо return, ", "указывая интерпретатору, что эту функцию следует рассматривать ", "как итератор"]
text_4=["Оператор yield приостанавливает функцию и ", "сохраняет локальное состояние, чтобы его можно было ", "возобновить с того места, ", "где оно было остановлено."]
text_5=["Вызов функции не выполняет ее. ", "Мы знаем это, потому что строка Starting ", "не печатается. Вместо этого функция возвращает ", "объект-генератор, который используется для ", "управления выполнением."]
choice_t1=1
choice_t2=2
choice_t3=3
choice_t4=4
choice_t5=5
choice_tquit=6
passw=int()
# Меню
def displ_menu():
    print("Меню о выводу предложений")
    print('Текст 1 -- введите 1')
    print('Текст 2 -- введите 2')
    print('Текст 3 -- введите 3')
    print('Текст 4 -- введите 4')
    print('Текст 5 -- введите 5')
    print('Выход -- введите 6')
#декоратор + авторизация
 
passw=int(input("введите ваш пароль для доспупа к выбору текстов: "))

def test_passw(func):
    def wrapper():
        if passw != 10:
            print("доступ к текстам вам закрыт! ")
            return
        value=func()
        return value
    return wrapper

#функции генераторы
def gen_1():
    for item in text_1:
        yield item
#-----------------------------------------------------
def gen_2():
    for item in text_2:
        yield item
#----------------------------------------------------------
def gen_3(start, finish, text):
    while start<finish:
        print(text_3[start])
        yield start
        start+=1

#главная функция
@test_passw
def main():
    choice=0
    
    while choice != choice_tquit:

        choice=int(input('введите ваш вариант: '))

        if choice == choice_t1:
            process=gen_1()
            iterat=0
            while iterat<len(text_1):
                print(next(process))
                iterat+=1 
        elif choice == choice_t2:
            process_2=gen_2()
            for item in process_2:
                print(item)
        elif choice == choice_t3:
            lente=len(text_3)
            process_3=gen_3(0, lente, text_3)
            for item in process_3:
                print()
        elif choice == choice_t4:
            lente=len(text_4)
            process_4=gen_3(0, lente, text_4)
            for item in process_4:
                print()
        elif choice == choice_t5:
            lente=len(text_5)
            process_5=gen_3(0, lente, text_5)
            for item in process_5:
                print()
        elif choice == choice_tquit:
            print('Выход из программы...')
        else:
            print('Ошибка: недопустимый выбор.')
            


#выполнение задачи
displ_menu()
main()
