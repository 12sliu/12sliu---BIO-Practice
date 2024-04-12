num = int(input())

x = num**(1/3)
x = int(round(x))
if x**3 == num:
    print("A")

if num % 2 == 1:
    print("B")

if num % 3 == 0:
    print("C")