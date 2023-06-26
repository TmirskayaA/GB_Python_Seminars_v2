import modul

print("Здравствуйте!")
number = int(input("Сколько журавликов сделали дети? "))

kate, boys = modul.NumberOfCranes(number)

print(f"Катя сделала {kate} журавликов.")
print(f"Петя и Серёжа сделали по {boys}.")

if modul.Remains(number) > 0:
    print(f"И {modul.Remains(number)} из {number} ребята сделали вместе!")



