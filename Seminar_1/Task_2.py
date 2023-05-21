print("Здравствуйте!")
number = int(input("Сколько журавликов сделали дети? "))

def Remains(x):
    counter = 0
    while x % 3 != 0:
        x -= 1
        counter += 1
    if (x / 3) % 2 != 0:
        counter += 1
    return counter

def NumberOfCranes(x):
    quotient = x / 3
    a = int(quotient * 2)
    b = int(quotient / 2)
    return a, b

kate, boys = NumberOfCranes(number)

print(f"Катя сделала {kate} журавликов.")
print(f"Петя и Серёжа сделали по {boys}.")

if Remains(number) > 0:
    print(f"И {Remains(number)} из {number} ребята сделали вместе!")



