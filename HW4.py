
def my_out():
    str = input("Enter string: ")
    new_str =""
    pointer = 0
    for item in str:
        if item.isdigit():
            if (pointer != 0) and (str[pointer - 1] == "-"):
                new_str += "-"
            new_str += item
            pointer += 1
            if (pointer < len(str)) and (not (str[pointer].isdigit())):
                new_str += " "
        else:
            pointer += 1
    my_output = [int(i) for i in new_str.split(' ')]

    print(sum(my_output))

my_out()