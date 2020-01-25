
def strToNum(intput_str):
    try:
        num = int(intput_str)
    except ValueError:
        return "Не удалось преобразовать введенный текст в число."
    else:
        if num % 2 == 0:
            return num / 2
        else:
            return 3*num + 1


while True:
    input_str = input()
    if input_str == 'cancel':
        print('Bye!')
        break
    else:
        print(strToNum(input_str))

