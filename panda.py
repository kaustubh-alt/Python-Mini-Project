import pandas as pd

data = []
print("Enter word | stop by entering number")
z = 1
while z == 1:
    a = input()
    if a.isnumeric():
        z = 3
    else:
        data.append(a)

df = pd.DataFrame(data)
print(df)
