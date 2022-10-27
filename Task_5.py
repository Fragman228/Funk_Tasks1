def nagrazdenie(name):
    while True:
        name = input('Введите имя:\n')
        if name == 'стоп':
            break
        points = int(input('Введите количество баллов:\n'))
        if points < 50:
            print(f'{name} получает Грамоту об участии')
        elif 50 <= points <= 80:
            print(f'{name} получает Похвальную Грамоту')
        elif points > 80:
            print(f'{name} получает Диплом')

    return "Все участники были вознаграждены"

print(nagrazdenie(input("Для ввода нажмите на Enter\n")))