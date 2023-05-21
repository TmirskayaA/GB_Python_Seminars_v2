print("Здравствуйте!")
number = int(input("Напишите число: "))

def SumOfNumbers(x):
    sum = 0
    for i in range(0, len(x)):
        sum += int(x[i])
    return sum

print(f"Сумма цифр в числе {number} = {SumOfNumbers(str(number))}.")