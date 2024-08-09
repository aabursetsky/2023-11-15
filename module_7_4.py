"""
Домашнее задание по теме "Форматирование строк".
"""

# Использование %:

team1_num = 5
print("В команде Мастера кода участников: %s !" % team1_num)

team1_num = 5
team2_num = 6
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))

# Использование format():

# количество задач решённых командой 2
score_2 = 42
print("Команда Волшебники данных решила задач: {}!".format(score_2))

# время за которое команда 2 решила задачи
team1_time = 1552.512
team2_time = 2153.31451
print("Волшебники данных решили задачи за {} с!".format(team1_time))

# Использование f-строк:
# количество решённых задач по командам:
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')

#  исход соревнования
challenge_result = 'Победа команды Волшебники Данных!'
print(f'Результат битвы: {challenge_result}')

# количество задач
tasks_total = 82
# среднее время решения
time_avg = 350.4
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(f'{result}')
