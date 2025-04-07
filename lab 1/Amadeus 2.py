print("\n----------------------------------------------------\n")

print("\t\tAmadeus")
print("\n\tSeu jogo da advinhação!")
print("\n  Olá, preparado(a) para esse desafio?")

print("\n<Enter para continuar>")
contin = input()

print("Ótimo! O jogo consiste em adivinhar um número secreto entre [1000 e 9999]")
print("Você possui apenas 10 tentativas para acertar e após a 5a tentativa, você receberá dicas.")
print("\n<Enter para continuar>")
contin = input()
print("\n----------------------------------------------------\n")

'''
for vez in range(0,10):

    num_user = int(input("\nFaça seu chute: "))

    import random
    num_r = random.randint(1000,10000)

    vez += 1

    if (num_r//1000 == num_user//1000):
        print(num_r//1000,end="")
    else:
        print("_",end="")
    if ((num_r//100)%10) == ((num_user//100)%10):
        print(((num_r//100)%10),end="")
    else:
        print("_",end="")
    if ((num_r//10)%10) == ((num_user//10)%10):
        print(((num_r//10)%10),end="")
    else:
        print("_",end="")
    if (num_r%10) == (num_user%10):
        print((num_r%10,"\n"))
    else:
        print("_\n")
'''

import random

num1 = 2
num2 = 5
num3 = 1
num4 = 0

numt1 = ("_")
numt2 = ("_")
numt3 = ("_")
numt4 = ("_")

print(f"\nNúmero secreto: {numt1} {numt2} {numt3} {numt4}\n")

dica_usada = None

for vez in range(0,10):

    num_user = int(input("Faça seu chute: "))

    numu1 = num_user//1000
    numu2 = ((num_user-(numu1*1000))//100)
    numu3 = ((num_user-(numu1*1000 + numu2*100))//10)
    numu4 = ((num_user-(10*(numu1*100+numu2*10+numu3))))

    if num1==numu1:
        numt1=num1
    if num2==numu2:
        numt2=num2
    if num3==numu3:
        numt3=num3
    if num4==numu4:
        numt4=num4

    if vez==4 or vez ==6:
        if num1 != numu1:
            erro1 = 1
        else:
            erro1 = 0
        if num2 != numu2:
            erro2 = 2
        else:
            erro2 = 0
        if num3 != numu3:
            erro3 = 3
        else:
            erro3 = 0
        if num4 != numu4:
            erro4 = 4
        else:
            erro4 = 0
        dica = 0

        while dica == 0 or dica == dica_usada:
            dica = random.choice((erro1, erro2, erro3, erro4))

        dica_usada = dica

        if dica == 1:
            if num1 % 2 == 0:
                numt1 = ("PAR")
            else:
                numt1 = ("ÍMPAR")

        if dica == 2:
            if num2 % 2 == 0:
                numt2 = ("PAR")
            else:
                numt2 = ("ÍMPAR")

        if dica == 3:
            if num3 % 2 == 0:
                numt3 = ("PAR")
            else:
                numt3 = ("ÍMPAR")

        if dica == 4:
            if num4 % 2 == 0:
                numt4 = ("PAR")
            else:
                numt4 = ("ÍMPAR")

    print(f"\nNúmero secreto: {numt1} {numt2} {numt3} {numt4}\n")