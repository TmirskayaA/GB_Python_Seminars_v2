print("Здравствуйте!")
number = int(input("Введите номер своего билета: "))

if len(str(number)) != 6:
    print("У билета номер состоит из 6 цифр!")

def HappyNumber(x):
    i = 0
    if int(x[i]) + int(x[i+1]) + int(x[i+2]) == int(x[i+3]) + int(x[i+4]) + int(x[i+5]):
        return True
    else: return False

if HappyNumber(str(number)):
    print("Поздравляю! У вас счастливый билет.")
else: print("Сожалею, не в этот раз...")