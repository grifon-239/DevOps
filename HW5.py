

def my_out():

    numbers = [int(x) for x in input("Enter numbers: ").split(' ')]


    reply = 1
    while True:
        if reply in numbers:
            reply += 1
        else:
            print(reply)
            break


my_out()