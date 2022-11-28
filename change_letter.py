#change any letter from a string

a = input("Enter an word ")
list = []
for i in a:
    list.append(i)
print(list)
z = int(input("enter the position to change letter "))
b = z-1

c = input("Enter an Character ")
if len(c) >= 2:
    print("enter single alphabet")
else:
    str = ''
    if len(a) >= b:
        list[b] = c
        print(list)
        for j in list:
            str += j
        print(str)
    else:
        print('out of range')