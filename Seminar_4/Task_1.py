import modul

print("Здравствуйте!")
oneList = modul.digit_list(list(input("Введите первый список: ")))
twoList = modul.digit_list(list(input("Введите второй список: ")))

print(f"Мы получили следующие списки:\nПервый список: {oneList} -> {modul.comb_list(oneList)}\nВторой список: {twoList} -> {modul.comb_list(twoList)}")