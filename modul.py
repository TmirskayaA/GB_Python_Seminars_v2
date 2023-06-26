import random

#S1T1
def SumOfNumbers(x): #Сумма цифр в числе. 123 -> 1+2+3=6
    sum = 0
    for i in range(0, len(x)):
        sum += int(x[i])
    return sum

#S1T2
def NumberOfCranes(x): #Количество журавликов у Кати и остальных.
    quotient = x / 3
    a = int(quotient * 2)
    b = int(quotient / 2)
    return a, b

def Remains(x): #Проверка на количество общих журавликов.
    counter = 0
    while x % 3 != 0:
        x -= 1
        counter += 1
    if (x / 3) % 2 != 0:
        counter += 1
    return counter

#S1T3
def HappyNumber(x): #Проверяет, является ли билет счастливым. 123321 -> 1+2+3=3+2+1
    i = 0
    if int(x[i]) + int(x[i+1]) + int(x[i+2]) == int(x[i+3]) + int(x[i+4]) + int(x[i+5]):
        return True
    else: return False

#S1T4
def CanIGetTheseSlices(x, y, z): #Задача с шоколадкой.
    if z % x == 0 or z % y == 0:
        return True
    else: return False

#S2T1
def ArrayOfNumbers(long): #Наполнение массива цифрами от 1 до 2 в long количестве.
    array = []
    for i in range(long):
        array.append(random.randint(1,2))
    return array

#S2T3
def ShowListOfDegrees(limiter): #Массив из степеней 2 до limiter числа.
    i = 0
    array = []
    while 2 ** i < limiter:
        array.append(2**i)
        i += 1
    return array

#S3T1
def ArrayOfNumbers(long, min, max): #Улучшенная версия S2T1. Можно задать свои min и max.
    import random
    array = []
    for i in range(long):
        array.append(random.randint(min, max))
    return array

#S3T2
def FindNearestSmaller(digit, array, min): #Находит ближайшее к <digit число из массива.
    while digit >= min:
        for j in array:
            if j == digit: return digit
        digit -= 1

def FindNearestBigger(digit, array, max): #Находит ближайшее к >digit число из массива.
    while digit <= max:
        for j in array:
            if j == digit: return digit
        digit += 1

#S3T3
def CheckingWords(list): #Проверяет корректность слова. НОС/NOSE -> корректно. НОS/NOС -> некорректно.
    eng = ("a","b","c","d","e","f","g","h","i","j",
       "k","l","m","n","o","p","q","r","s","t",
       "u","v","w","x","y","z","A","B","C","D",
       "E","F","G","H","I","J","K","L","M","N",
       "O","P","Q","R","S","T","U","V","W","X",
       "Y","Z")
    ru  = ("а","б","в","г","д","е","ё","ж","з","и",
       "й","к","л","м","н","о","п","р","с","т",
       "у","ф","х","ц","ч","ш","щ","ъ","ы","ь",
       "э","ю","я""А","Б","В","Г","Д","Е","Ё",
       "Ж","З","И","Й","К","Л","М","Н","О","П",
       "Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ",
       "Ъ","Ы","Ь","Э","Ю","Я")
    digits = ("1","2","3","4","5","6","7","8","9","0")

    if len(set(list).intersection(ru)) > 0 and len(set(list).intersection(eng)) > 0: return True
    elif len(set(list).intersection(ru)) > 0 and len(set(list).intersection(digits)) > 0: return True
    elif len(set(list).intersection(eng)) > 0 and len(set(list).intersection(digits)) > 0: return True
    elif len(set(list).intersection(ru)) > 0 and len(set(list).intersection(eng)) > 0 and len(set(list).intersection(digits)) > 0: return True
    else: return False

def Scrabble(letters): #Количество очков в игре Скрабл
    onePoint   = ("a","A","e","E","i","I","o","O","l","L",
                  "n","N","s","S","t","T","r","R","u","U",
                  "а","А","в","В","е","Е","и","И","н","Н",
                  "о","О","р","Р","с","С","т","Т")
    twoPoint   = ("d","D","g","G","д","Д","к","К","л","Л",
                  "м","М","п","П","у","У")
    threePoint = ("b","B","c","C","m","M","p","P","б","Б",
                  "г","Г","е","Е","ь","Ь","я","Я")
    fourPoint  = ("f","F","h","H","v","V","w","W","y","Y",
                  "й","Й","ы","Ы")
    fivePoint  = ("k","K","ж","Ж","з","З","х","Х","ц","Ц",
                  "ч","Ч")
    eightPoint = ("j","J","x","X","ш","Ш","э","Э","ю","Ю")

    score = 0

    for i in letters:
        if i in onePoint: score += 1
        elif i in twoPoint: score += 2
        elif i in threePoint: score += 3
        elif i in fourPoint: score += 4
        elif i in fivePoint: score += 5
        elif i in eightPoint: score += 8
        else: score +=10

    return score

#S4T1
def digit_list(array): #Создаёт список чисел из строки. "л24г92гг293" -> [2, 4, 9, 2, 2, 9, 3]
    resultList = []
    for i in range(0, len(array)):
        if array[i].isdigit(): resultList.append(int(array[i]))
    return resultList

def comb_list(array): #Сортирует список оставляя только уникальные значения по возрастанию.
    finallyArray = list(set(array))
    finallyArray.sort()
    return finallyArray

#S4T2
def max_of_berries(dictionary): #Находит нужную грядку для задачи.
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

def fill_dictionary(counter): #Наполняет словарь рандомными числами от 0 до 9.{1: 4, 2: 6 и т.д.}
    dictionary = {}
    for i in range(1,counter+1):
        dictionary[i] = random.randint(0,9)
    return dictionary