ask = input("your matrix is 2 X 2(type 2) or 3 X 3(type 3)")
#3x3 order matrix solution
def three():
    a1 = int(input("enter A11 "))
    a2 = int(input("enter A12 "))
    a3 = int(input("enter A13 "))
    a4 = int(input("enter A21 "))
    a5 = int(input("enter A22 "))
    a6 = int(input("enter A23 "))
    a7 = int(input("enter A31 "))
    a8 = int(input("enter A32 "))
    a9 = int(input("enter A33 "))
    print(a1, a2, a3)
    print(a4, a5, a6)
    print(a7, a8, a9)
    A4 = a5 * a6
    z1 = a8 * a6
    A1 = a1 * (A4)-(z1)
    A2 = a4 * a9 - a7 * a6 * a2
    A3 = a4 * a8 - a7 * a8 * a3
    D = A1 + A2 + A3
    print("determine of matrix = ", A1)
    g = input("want to tranverse (yes or no)")

    def trans(a1,a2,a3,a4,a6,a7,a8,a5,a9):
        a21 = a4
        a41 = a2
        a31 = a7
        a71 = a3
        a81 = a6
        a61 = a8
        print(a1, a21, a31)
        print(a41, a5, a61)
        print(a71, a81, a9)
    if g == "yes":
        trans(a1,a2,a3,a4,a6,a7,a8,a5,a9)
    w = input("do you want adjoint of matrix (yes or no)")
    def adjoint(a1,a2,a3,a4,a6,a7,a8,a5,a9):
        a11 = (a5 * a9) - (a8 * a6)
        a12 = (a4 * a9) - (a7 * a6)
        a13 = (a4 * a8) - (a7 * a5)
        a21 = (a2 * a9) - (a8 * a3)
        a22 = (a1 * a9) - (a7 * a3)
        a23 = (a1 * a8) - (a7 * a2)
        a31 = (a2 * a6) - (a5 * a3)
        a32 = (a1 * a6) - (a4 * a3)
        a33 = (a1 * a5) - (a4 * a2)
        print(a11,  a21, a31)
        print(a12,  a22, a32)
        print(a13, a23, a33)
    if w == "yes":
        adjoint(a1,a2,a3,a4,a6,a7,a8,a5,a9)
#2x2 order matrix solution
def two():
    a1 = int(input("your matrix a11 "))
    a2 = int(input("your matrix a12 "))
    a3 = int(input("your matrix a21 "))
    a4 = int(input("your matrix a22 "))
    print(a1, a2)
    print(a3, a4)
    print(a1*a4-a2*a3)

if ask == "3":
    three()

if ask == "2":
    two()


