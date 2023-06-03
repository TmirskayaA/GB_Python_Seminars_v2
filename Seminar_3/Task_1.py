print("Здравствуйте!")
counter = int(input("Сколько чисел в нашем списке? "))

def ArrayOfNumbers(long, min, max):
    import random
    array = []
    for i in range(long):
        array.append(random.randint(min, max))
    return array

newList = ArrayOfNumbers(counter, 0, 10)

number = int(input("Количество какого числа хотите получить? "))

print(f"Количество числа {number} в списке {newList} = {newList.count(number)}")