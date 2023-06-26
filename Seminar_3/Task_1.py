import modul

print("Здравствуйте!")
counter = int(input("Сколько чисел в нашем списке? "))

minimum = int(input("Введите минимальное число для списка: "))
maximum = int(input("Введите максимальное число для списка: "))

newList = modul.ArrayOfNumbers(counter, minimum, maximum)

number = int(input("Количество какого числа хотите получить? "))

while number < minimum or number > maximum:
    number = int(input("Такого числа не будет в списке. Введите другое: "))

print(f"Количество числа {number} в списке {newList} = {newList.count(number)}")