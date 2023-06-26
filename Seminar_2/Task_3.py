import modul

print("Здравствуйте!")
number = int(input("Какое число должно быть максимумом? "))

print("Получилось:")
print(*modul.ShowListOfDegrees(number), sep=" ")