print("Здравствуйте!")
word = str(input("Напишите своё слово: "))

arrayWord = list(word)

def CheckingWords(list):
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

if CheckingWords(arrayWord):
    print("Таких слов не существует:(")
    exit()

def Scrabble(letters):
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

print(f"Ваше слово \"{word}\" собрало баллов: {Scrabble(word)}!")