#Find the counts of elements of an unsorted integer array which are equal to the average of all elements of that array.
#kindly give input wuth space between or else it will not work
a = input("number")
array = a.split()
sum = 0
for i in array:
    sum += int(i)
out = 0
d = sum/len(array)
for i in array:
    if d == float(i):
        out = out + 1

print(out)

