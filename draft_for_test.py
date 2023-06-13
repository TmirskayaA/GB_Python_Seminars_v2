array = list(input("введите число: "))
print(array)

result = []
for i in range(0, len(array)):
    if array[i].isdigit(): result.append(int(array[i]))

print(result)