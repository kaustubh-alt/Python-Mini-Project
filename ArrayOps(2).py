#Find the average of largest and smallest numbers in an unsorted integer array
#Give the input in number with space between

a = input("number")
array = a.split()
num = []
maxi = max(array)
mini = min(array)
for i in array:
    if i == mini:
        num.append(i)

    elif i == maxi:
        num.append(i)

out = 0
for i in num:
    out += int(i)

print(out/len(num))




