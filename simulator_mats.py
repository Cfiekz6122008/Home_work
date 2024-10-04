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
print(f'Хорошо, {student}. Тебе задачка')

min = 10 ** (level - 1)
max = 10 ** level - 1
points = 0
for i in range(5):

    a = randint(min, max)
    b = randint(min, max)
    print(f'{student}, сколько будет {a} + {b}?', end='')
    correct_answer = a + b
    student_answer = input()
    if student_answer == str(correct_answer):
        points += 1
        print(f'Правильно!')
    else:
        print(f'Не правильно. Правильный ответ {correct_answer}!')
if points == 5:
    print(f'Умница {student}, пять')

elif points == 4:
    print(f'Молодец {student}, четыре')

elif points == 3:
    print(f'Плохо {student}, три')

else:
    print(f'Два {student}')

