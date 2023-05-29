print("Здравствуйте!")
number = int(input("Какое число должно быть максимумом? "))

def ShowListOfDegrees(limiter):
    i = 0
    array = []
    while 2 ** i < limiter:
        array.append(2**i)
        i += 1
    return array

print("Получилось:")
print(*ShowListOfDegrees(number), sep=" ")