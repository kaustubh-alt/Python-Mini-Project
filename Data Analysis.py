import random

greeting = ["Hello", "Hi", "welcome", "Good Morning", "Good Afternoon", "Good Evening", "Hey", "Whatsup"]
Computer = ["CPU", "RAM", "ROM", "Storage", "Windows", "MacOS", "Linux", "GPU", "Monitor", "Tech"]
Shape = ["Triangle", "Square", "Circle", "Rectangle", "Hexagon", "Pentagon", "Line"]


direcrtory = {
    0 : greeting,
    1 : Computer,
    2 : Shape
}

a = ''
try:
    a = str(input("Enter Your Word"))
except(Exception):
    print('Enter an single word')
else:
    try:
        for i in direcrtory:
            for j in direcrtory[i]:
                if a == j:
                    b = direcrtory[i]
                    print(b[random.randint(0, len(greeting) - 1)])

    except:
        print(Exception)
    else:
        print("Word Not Found")









