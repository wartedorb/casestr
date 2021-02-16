"""
Case-study #3 Анализ текста
Разработчики:
Бикметов Э.Б. = 40%, Бычков К.А. = 30%, Кондрашов М.С. = 30%
"""
from textblob import TextBlob

text = input("Введите текст:")
count_sentens = text.count('.') + text.count('!') + text.count('?')
count_words = text.count(" ") + 1
t = text.lower()
count_syllables = t.count('а') + t.count('о') + t.count('э') + t.count('ю') + t.count('я') + t.count('и') + t.count('ё') + t.count('у') + t.count('е') + t.count('ы') + t.count('a') + t.count('o') + t.count('u') + t.count('e') + t.count('i') + t.count('y')
print('Предложений:', count_sentens)
print('Слов:', count_words)
print('Слогов:', count_syllables)
ASL = (count_words/count_sentens)
print('Средняя длина предложения в словах:', ASL)
ASW = count_syllables / count_words
print('Средняя длина слова в слогах:', ASW)
if ord(t[0]) < 123:
    FRE = 206.835 - 1.015 * ASL - 84.6 * ASW
    text1 = TextBlob(text)
# eng
else:
    FRE = 206.835 - (1.3 * ASL) - (60.1 * ASW)
    text1 = TextBlob(text)
    text1 = text1.translate()
    print(text1)
# rus

print('Индекс удобочитаемости Флеша:', FRE)

if FRE > 80:
    print('Текст очень легко читается (для младших школьников).')
elif 50 < FRE <= 80:
    print("Простой текст (для школьников).")
elif 25 < FRE <= 50:
    print('Текст немного трудно читать (для студентов).')
else:
    print('Текст трудно читается (для выпускников ВУЗов).')
Pol = text1.polarity
ob = (1 - text1.subjectivity) * 100
if Pol > 0.3:
    print('Тональность текста: положительная')
elif -0.3 < Pol < 0.3:
    print('Тональность текста: нейтральная')
elif Pol < 0.3:
    print('Тональность текста: негативная')
print('Объективность: ', format(ob, '.1f'), '%', sep='')
