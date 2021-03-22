a = int(input())
b = a
for i in range(a):
    b -= 1
    print(" " * b, "*" * ((i * 2) + 1))