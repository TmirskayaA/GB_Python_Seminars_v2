def Remains(x):
    counter = 0
    while x % 3 != 0:
        x -= 1
        counter += 1
    if (x / 3) % 2 != 0:
        counter += 1
    return counter

a = Remains(int(input("Введите число: ")))
print(a)