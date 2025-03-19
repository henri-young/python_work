list = []

while True:
    num = float(input("Insert a number: "))
    
    if (num >= 0):
        print(num)
        list.insert(1, num)

    else:
        print("It's End")
        print(list)
        print(len(list))
        break