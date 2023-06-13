import random
import json

def max_of_berries(dictionary):
    dictionary = {int(k):int(v) for k,v in dictionary.items()}
    max = 0
    point = 0
    for i in range(1, len(dictionary)+1):
        if i == 1:
            if dictionary[len(dictionary)] + dictionary[i] + dictionary[i+1] > max: 
                max = dictionary[len(dictionary)] + dictionary[i] + dictionary[i+1]
                point = i
        elif i == len(dictionary):
            if dictionary[i-1] + dictionary[i] + dictionary[1] > max: 
                max = dictionary[i-1] + dictionary[i] + dictionary[1]
                point = i
        else: 
            if dictionary[i-1] + dictionary[i] + dictionary[i+1] > max: 
                max = dictionary[i-1] + dictionary[i] + dictionary[i+1]
                point = i
    return max, point

def fill_dictionary(counter):
    dictionary = {}
    for i in range(1,counter+1):
        dictionary[i] = random.randint(0,9)
    return dictionary


file = open('Seminar_4\Garden_beds.txt', 'w')
file.close()

print("Здравствуйте!")
number = int(input("Сколько грядок вы посадили? "))

dictionary = fill_dictionary(number)

file = open('Seminar_4\Garden_beds.txt', 'a')
file.write(json.dumps(dictionary))
file.close()

file = open('Seminar_4\Garden_beds.txt', 'r')
beds = json.loads(file.readline())
file.close()

print(f"Вот что выросло на наших грядках: [ГРЯДКА] : [ЯГОДЫ]")

for key, value in beds.items():
    print("{}: {}".format(key, value))

maximum, bed = max_of_berries(beds) 

print(f"Больше всего ягод будет собрано рядом с грядкой {bed} = {maximum}!")