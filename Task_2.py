def points(amounth):
    if amounth < 49:
        return 'Скидка 10%'
    elif 49 < amounth < 100:
        return 'Скидка 15%'
    elif amounth >= 100:
        return 'Скидка 20%'

print(points(int(input())))
