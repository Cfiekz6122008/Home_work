from random import randint

student = input('Представьтесь: ')
try:
    level = int(input('Выберите уровень сложности 1 - 5: '))
except:
    level = 1
    print('Установлен 1 ур. сложности')
if level < 1 or level > 5:
    level = 1
    print('Установлен 1 ур. сложности')
print(f'Хорошо, {student}.')

questions = [
    ('Столица Франции?', 'Париж'),
    ('Самая длинная река в мире?', 'Амазонка'),
    ('Самая высокая гора на земле?', 'Эверест'),
    ('Самый большой океан?', 'Тихий'),
    ('Самый маленький континент на земле?', 'Австралия')
]

points = 0
asked_questions = set()
total_questions = len(questions)

for i in range(min(5, total_questions)):
    index = randint(0, total_questions - 1)

    while index in asked_questions:
        index = randint(0, total_questions - 1)

    asked_questions.add(index)
    question = questions[index]

    print(f'{student}, {question[0]}')
    answer = input("Твой ответ: ")

    if answer.lower() == question[1].lower():
        points += 1
        print('Правильно')
    else:
        print(f'Неправильно. {question[1]}.')

if points == 5:
    print(f'Да ты знаток, {student}, {points}')
elif points >= 3:
    print(f'Молодец {student}, {points}')
else:
    print(f'Плохо, {points}')

