"""Case-study #3 Анализ текста
Разработчики:
Бикметов Э.Б., Бычков К.А., Кондрашов М.С.

"""

text = input("Введите текст:")
count_sentens = text.count('.')
count_words = text.count(" ") + 1
t = text.lower()
count_syllables = t.count('а') + t.count('о') + t.count('э') + t.count('ю') + t.count('я') + t.count('и') + t.count('ё') + t.count('у') + t.count('е') + t.count('ы') + t.count('a') + t.count('o')  + t.count('u') +  + t.count('e')  + t.count('i') + t.count('y')
for i in range(0,count_words - 1):
    ASL = (count_words/count_sentens)
print ('Предложений:',count_sentens)
print ('Слов:',count_words)
print ('Слогов:',count_syllables)
print ('Средняя длина предложения в словах:',ASL)
#print ('Средняя длина слова в слогах:',ASW)
#print ('Индекс удобочитаемости Флеша:',FRE)