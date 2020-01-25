

def tempConv(temp):

    if temp[-1] == 'C':
       return str(float(temp[:-1]) * 1.8 + 32) + 'F'
    else:
        if temp[-1] == 'F':
            return str((float(temp[:-1]) - 32) / 1.8) + 'C'
        else:
            print("Неправильный формат данных")


str_input = input("Введите температуру в формате 12С = 12 градусов цельсия, 12F = 12 градусов по Фаренгейту: ")
print(tempConv(str_input))