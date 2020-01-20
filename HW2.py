



def my_out():
    input_data = input("Enter data: ").split(' ')
    output_list = []
    [output_list.append(item) for item in input_data if item not in output_list]
    output_str = " "
    print(output_str.join(output_list))

my_out()