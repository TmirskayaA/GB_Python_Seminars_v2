import modul

print("Здравствуйте!")
word = str(input("Напишите своё слово: "))

arrayWord = list(word)

if modul.CheckingWords(arrayWord):
    print("Таких слов не существует:(")
    exit()

print(f"Ваше слово \"{word}\" собрало баллов: {modul.Scrabble(word)}!")