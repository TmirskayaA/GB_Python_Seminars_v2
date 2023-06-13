def digit_list(array):
    resultList = []
    for i in range(0, len(array)):
        if array[i].isdigit(): resultList.append(int(array[i]))
    return resultList

def comb_list(array):
    finallyArray = list(set(array))
    finallyArray.sort()
    return finallyArray


print("Здравствуйте!")
oneList = digit_list(list(input("Введите первый список: ")))
twoList = digit_list(list(input("Введите второй список: ")))

print(f"Мы получили следующие списки:\nПервый список: {oneList} -> {comb_list(oneList)}\nВторой список: {twoList} -> {comb_list(twoList)}")


