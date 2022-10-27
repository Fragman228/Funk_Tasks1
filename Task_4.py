def imt(weight, height):
    IMT = weight / (height * height)
    if IMT < 18.5:
        return 'Недостаточный вес'
    elif 18.5 < IMT < 25:
        return "ИМТ в норме"
    elif IMT > 25:
        return 'Избыточный вес'
print(imt(int(input()),int(input())))