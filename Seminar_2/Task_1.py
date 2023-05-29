print("Здравствуйте!")
number = int(input("Сколько монеток лежит на столе? "))

print("Перемешали монетки в руке и бросили их на стол:")

import random

def ArrayOfNumbers(long):
    array = []
    for i in range(long):
        array.append(random.randint(1,2))
    return array

ranArray = ArrayOfNumbers(number)

print('Решка - 1, Орёл - 2: ')
print(ranArray)

print(f'Чтобы все монетки были повёрнуты одной стороной, нам нужно перевернуть {min(ranArray.count(1), ranArray.count(2))} из них!')





