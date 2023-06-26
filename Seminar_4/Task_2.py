import json
import modul

file = open('Seminar_4\Garden_beds.txt', 'w')
file.close()

print("Здравствуйте!")
number = int(input("Сколько грядок вы посадили? "))

dictionary = modul.fill_dictionary(number)

file = open('Seminar_4\Garden_beds.txt', 'w')
file.write(json.dumps(dictionary))
file.close()

file = open('Seminar_4\Garden_beds.txt', 'r')
beds = json.loads(file.readline())
file.close()

print(f"Вот что выросло на наших грядках: [ГРЯДКА] : [ЯГОДЫ]")

for key, value in beds.items():
    print("{}: {}".format(key, value))

maximum, bed = modul.max_of_berries(beds) 

print(f"Больше всего ягод будет собрано рядом с грядкой {bed} = {maximum}!")