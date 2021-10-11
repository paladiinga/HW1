# EX 1.1
a = int(input())
if a == 2:
    print(29)
elif a == 8:
    print(31)
elif a % 2 == 0:
    print(30)
else:
    print(31)



# EX 1.2
a = int(input())
b= str(input())
if a % 2 == 0 and a != 2 and a != 8:
    print(30)
elif a == 2:
    if int (b[-1]) == 0 or int(b[-1]) == 4 or int(b[-1]) == 8:
        print(29)
    else:
        print(28)
elif a == 8:
    print(31)
else:
    print(31)