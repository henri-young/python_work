t1 = 0
t2 = 0
t3 = 0
t4 = 0
num = int(input("número: "))
while (num>=0):
    if num<=25:
        t1 = t1+1
    elif num<=50:
        t2 = t2+1
    elif num<=75:
        t3 = t3+1
    elif num<=100:
        t4 = t4+1
    else:
        print("Número Inválido")
    num = int(input("número: "))
print(t1,t2,t3,t4)
print("contagem = ",t1+t2+t3+t4)