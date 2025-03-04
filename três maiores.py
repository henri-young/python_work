a = int(input("first num: ")) #primeiro numero
b = int(input("second num: "))
c = int(input("third num: "))
if (a>b):
    if (a>c):
        print(a)
    else:
        print(c)
else:
    if(b>c):
        print(b)
    else:
        print(c)