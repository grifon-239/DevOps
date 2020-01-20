

def my_out():
    input_data = input("Enter string: ").lower().split(' ')
    count_dict = dict()
    for item in input_data:
        if item in count_dict.keys():
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    max_reps = max(count_dict.values())
    for key, val in count_dict.items():
        if val == max_reps:
            print(val, ' - ', key)

my_out()