from random import randint


def task_1():
    print('Задача 10: На столе лежат n монеток.\n'
          'Некоторые из них лежат вверх решкой, а некоторые – гербом.\n'
          'Определите минимальное число монеток, которые нужно перевернуть,\n'
          'чтобы все монетки были повернуты вверх одной и той же стороной.\n'
          'Выведите минимальное количество монет, которые нужно перевернуть\n'
          '5 -> 1 0 1 1 0\n'
          '2\n')
    numbers = enter_text('Введите сколько монеток лежит на столе')
    money_list, counters = list(randint(0, 1) for i in range(numbers)), [0, 0]
    print(f'{numbers} -> {" ".join(str(i) for i in money_list)}')
    for i in money_list:
        if i == 0:
            counters[0] += 1
        else:
            counters[1] += 1
    if counters[0] > counters[1]:
        print(f'{counters[1]}\n')
    elif counters[0] == counters[1]:
        print(f'{counters[1]}\n')
    else:
        print(f'{counters[0]}\n')


def task_2():
    print('Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.\n'
          'Петя помогает Кате по математике.\n'
          'Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.\n'
          'Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.\n'
          'Помогите Кате отгадать задуманные Петей числа.\n'
          '4 4 -> 2 2\n'
          '5 6 -> 2 3\n')
    number_one = enter_text('Введите сумму чисел')
    number_two = enter_text('Введите произведение чисел')
    counting = ((number_one / 2) ** 2 - number_two) ** 0.5
    x, y = int(number_one / 2 - counting), int(number_one / 2 + counting)
    print(f'{number_one} {number_two} -> {x} {y}\n')


def task_3():
    print('Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.\n'
          '10 -> 1 2 4 8\n'
          'пользователь будет вводить каждое число на новой строке для задач 10, 12.\n')
    numbers = enter_text('Введите число')
    i = 1
    numbers_list = []
    while i <= numbers:
        numbers_list.append(i)
        i = i * 2
    print(f'{numbers} -> {" ".join(str(i) for i in numbers_list)}\n')


def enter_text(text, output_type=True):
    value = 0
    try:
        if output_type:
            value = int(input(text + ': '))
        else:
            value = input(text + ': ')
    except:
        print('Ошибка введен текст\n')
    return value



if __name__ == "__main__":
    task_1()
    # task_2()
    # task_3()
