line = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"
print (line)
print ("1.Посчитать соличество символов. В строке: ")
print (len(line)," символов в строке.")
print ("2.Развернуть строку... в обратную строну: ") #Строки следуют протоколу последовательности Python. И все последовательности поддерживают любопытную функцию под названием срез. Вы можете смотреть на срез как на расширение синтаксиса индексирования квадратных скобок.
mirrorline = line[::-1]
print (mirrorline)
print ("3.Сделать каждое слово с большой буквы:")
print (line.title())
print ("4.Сделать весь текст прописными буквами:")
print (line.upper())
print ("5.Найти число вхождений 'нд', 'ам', 'о' в строку: ")
print ("нд - ", line.count("нд"),",","ам -", line.count("ам"),","," о - ", line.count("о"), ".")
print ("6.Собственные упражнения... перевод символов нижнего регистра в верхний, а верхнего – в нижний")
print (line.swapcase())
print ("7.Вывести в консоль исходную строку")
print (line, "  ...а пожалуйста!")
# add a text for the check of commit
print ("проверка коммита")