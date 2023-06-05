print("Здравствуйте!")
counter = int(input("Сколько чисел в нашем списке? "))

minimum = int(input("Введите минимальное число для списка: "))
maximum = int(input("Введите максимальное число для списка: "))

def ArrayOfNumbers(long, min, max):
    import random
    array = []
    for i in range(long):
        array.append(random.randint(min, max))
    return array

newList = ArrayOfNumbers(counter, minimum, maximum)

number = int(input("Количество какого числа хотите получить? "))

while number < minimum or number > maximum:
    number = int(input("Такого числа не будет в списке. Введите другое: "))

print(f"Количество числа {number} в списке {newList} = {newList.count(number)}")