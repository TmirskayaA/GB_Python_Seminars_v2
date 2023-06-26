import modul

print("Здравствуйте!")
number = int(input("Сколько монеток лежит на столе? "))

print("Перемешали монетки в руке и бросили их на стол:")

ranArray = modul.ArrayOfNumbers(number)

print('Решка - 1, Орёл - 2: ')
print(ranArray)

print(f'Чтобы все монетки были повёрнуты одной стороной, нам нужно перевернуть {min(ranArray.count(1), ranArray.count(2))} из них!')





