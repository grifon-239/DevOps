


def collatz(num, count = 0):
    if num == 1:
        return count
    else:
        if num % 2 == 0:
            count += 1
            return collatz(num / 2, count)
        else:
            count += 1
            return collatz(3*num+1, count)



print(collatz(12))