import modul

print("Здравствуйте!")
counter = int(input("Сколько чисел в нашем списке? "))

while counter == 0:
    counter = int(input("Список не может быть таким маленьким, введите число побольше! "))

minimum = int(input("Введите минимальное число для списка: "))
maximum = int(input("Введите максимальное число для списка: "))

newList = modul.ArrayOfNumbers(counter, minimum, maximum)

number = int(input("Мы ищем число, ближайшее к: "))

if number < minimum: 
    number = minimum
    search = modul.FindNearestBigger(number, newList, maximum)
elif number > maximum: 
    number = maximum
    search = modul.FindNearestSmaller(number, newList, minimum)
else:
    decision = str(input("Вы хотите получить число \"Меньше\" или \"Больше\"? "))
    while decision != "Меньше" and decision != "Больше":
        decision = str(input("Не понял, напишите как у меня: \"Меньше\" или \"Больше\" "))
    if decision == "Меньше":
        if number > minimum: number -= 1
        search = modul.FindNearestSmaller(number, newList, minimum)
    else: 
        if number < maximum: number += 1
        search = modul.FindNearestBigger(number, newList, maximum)

print(f"Из получившегося списка чисел {newList} искомое число = {search}!")
