
#con=int(1000)
#next_turn='Y'
#while next_turn=='y' or next_turn=='Y':
#    n1=int(input('число1: '))
#    n2=int(input('число2: '))
#    sum_n=n1+n2
#    print("Summa: ", sum_n)
#    next_turn=input('pass?')

#number=0
#for i in range(0, 1000, 10):
#    number=number+10
#    print(number)

#number=[]
#i=1
#while i<11:
#    print('input your', i, '-th number: ')
#    x=int(input())
#    number=number+[x]
#    print(number)
#    i=i+1

#x=1
#y=30
#summ=float(x/y)
#for i in range (29):
#    x=x+1
#    y=y-1
#    summ=summ+x/y
#    print(i, '-th turn ', 'x=', format(x, '.6f'), 'y=', format(y, '.6f'),'ALL SUMMA:', format(summ, '.6f'))


#for i in range(10):
#   print(i, '-th row: ', "#"*15)
#    i=i+1

#number=int(input('enter number not less zero'))
#if number>0:
#    print(number)
#else:
#    print("you misteik")

number=int(input('enter number more 0 and less 100'))
if number>0 and number<100:
    print("you won: ", number)
else:
    print("you errored")
