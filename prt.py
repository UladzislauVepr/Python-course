vaga=input("Введите ваш вес, килограмм: ")
vaga_r=float(vaga)
vysh=input("Введите ваш рост в метрах: ")
vysh_r=float(vysh)
ind_bmi=vaga_r/(vysh_r*vysh_r)
ind_bmi_r=int(ind_bmi)
print ("значение рассчитанного индекса массы тела: ", ind_bmi_r)

i_r="!"
i_pl="="
s1="16"
s2="20"
s3="25"
s4="30"
s5="35"
s6="40"
print ("Ваш диагноз:")
if ind_bmi_r < 16:
    print (i_r+i_pl+s1+i_pl*23+s6)
    print ("Выраженный дефицит массы тела")
if ind_bmi_r>16 and ind_bmi_r<18.5:
    print (s1+i_pl+i_r+i_pl+s2+i_pl*18+s6)
    print ("Недостаточная масса тела")
if ind_bmi_r>18.5 and ind_bmi_r<25:
    print (s1+i_pl*3+i_r+i_pl*3+s3+i_pl*13+s6)
    print ("Нормальная масса тела")
if ind_bmi_r>25 and ind_bmi_r<30:
    print (s1+i_pl*10+i_r+i_pl*4+s4+i_pl*9+s6)
    print ("Избыточная масса тела (предожирение)")
if ind_bmi_r>30 and ind_bmi_r<35:
    print (s1+i_pl*16+i_r+i_pl*2+s5+i_pl*4+s6)
    print ("Ожирение 1-ой степени")
if ind_bmi_r>35 and ind_bmi_r<40:
    print (s1+i_pl*20+i_r+i_*2+s6)
    print ("Ожирение 2-ой степени")
if ind_bmi_r>40:
    print (s1+i_pl*23+s6+i_pl*2+i_r)
    print ("Ожирение 3-ой степени")
