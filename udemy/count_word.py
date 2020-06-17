'''
Function which counts each word in a string
'''
def count_func(my_str):
    my_str_list = list(my_str.split())
    length = len(my_str_list)
    return length


if __name__ == "__main__":
    my_str = "Hello world, nice weather outside!"
    my_count_func = count_func(my_str)
    print(my_count_func)