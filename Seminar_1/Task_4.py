import modul

print("Здравствуйте!")
long = int(input("Какая у шоколадки длина? "))
width = int(input("Какая ширина? "))
counter = int(input("Сколько долек хотите отломить? "))

if counter > long * width:
    print("Чтобы отломить столько долек, вам нужна шоколадка побольше.")
    exit()

if modul.CanIGetTheseSlices(long, width, counter):
    print("Да, всё получится!")
else: print("Нет, так ничего не выйдет...")