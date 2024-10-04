

# FOR


fruits = ['яблоко', 'банан', 'вишня']
for fruit in fruits:
    print(f'Я люблю {fruit}')

for i in range(5):
    print(f'Квадрат числа {i} равен {i**2}')

numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f'Сумма чисел: {total}')

#   WHILE

count = 0
while count < 5:
    print(f'Текущий счёт: {count}')
    count += 1

user_input = ''
while user_input.lower() != 'выход':
    user_input = input('Введите что-нибудь (или "выход" для завершения): ')
    print(f'Вы ввели: {user_input}')

numbers = [1, 3, 7, 4, 5, 9]
index = 0

while index < len(numbers):
    if numbers[index] % 2 == 0:
        print(f'Первое четное число: {numbers[index]}')
        break
    index += 1
