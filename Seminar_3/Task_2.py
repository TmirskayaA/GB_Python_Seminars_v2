print("Здравствуйте!")
counter = int(input("Сколько чисел в нашем списке? "))

while counter == 0:
    counter = int(input("Список не может быть таким маленьким, введите число побольше! "))

minimum = int(input("Введите минимальное число для списка: "))
maximum = int(input("Введите максимальное число для списка: "))

def ArrayOfNumbers(long, min, max):
    import random
    array = []
    for i in range(long):
        array.append(random.randint(min, max))
    return array

newList = ArrayOfNumbers(counter, minimum, maximum)

def FindNearestSmaller(digit, array, min):
    while digit >= min:
        for j in array:
            if j == digit: return digit
        digit -= 1

def FindNearestBigger(digit, array, max):
    while digit <= max:
        for j in array:
            if j == digit: return digit
        digit += 1

number = int(input("Мы ищем число, ближайшее к: "))

if number < minimum: 
    number = minimum
    search = FindNearestBigger(number, newList, maximum)
elif number > maximum: 
    number = maximum
    search = FindNearestSmaller(number, newList, minimum)
else:
    decision = str(input("Вы хотите получить число \"Меньше\" или \"Больше\"? "))
    while decision != "Меньше" and decision != "Больше":
        decision = str(input("Не понял, напишите как у меня: \"Меньше\" или \"Больше\" "))
    if decision == "Меньше":
        if number > minimum: number -= 1
        search = FindNearestSmaller(number, newList, minimum)
    else: 
        if number < maximum: number += 1
        search = FindNearestBigger(number, newList, maximum)

print(f"Из получившегося списка чисел {newList} искомое число = {search}!")
