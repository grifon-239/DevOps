
def my_out():

    num_palindromes = list()
    for i in range(1000000):
        str_i = str(i)
        str_i_b = str(format(i, 'b'))
        if (str_i == str_i[::-1]) and (str_i_b == str_i_b[::-1]):
            num_palindromes.append(int(i))

    print(sum(num_palindromes))


my_out()