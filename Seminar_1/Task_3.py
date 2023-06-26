import modul

print("Здравствуйте!")
number = int(input("Введите номер своего билета: "))

if len(str(number)) != 6:
    print("У билета номер состоит из 6 цифр!")
    exit()

if modul.HappyNumber(str(number)):
    print("Поздравляю! У вас счастливый билет.")
else: print("Сожалею, не в этот раз...")