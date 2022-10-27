def kollege(chislo):
    for i in range(chislo):
        points = int(input())
        if points < 50:
            print("Вы отчислены")
        elif points >= 50:
            print('Поздравляем!Вы прошли тест')
    return 'Отбор окончен'
print(kollege(int(input())))
