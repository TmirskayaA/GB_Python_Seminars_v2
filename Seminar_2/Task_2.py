print("Привет!")
sum = int(input("Петя, чему равна сумма этих чисел? "))
product = int(input("А произведение? "))

print("Cпасибо.")

for x in range(sum):
    for y in range(product):
        if sum == x + y and product == x * y:
            print(f'Думаю, это: {x} и {y}')
            exit()
