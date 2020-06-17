'''
Function witch reverse a string
'''
def str_rev(my_str):
    my_str_rev = ''
    my_str_rev = my_str[::-1]
    return my_str_rev


if __name__ == "__main__":
    my_str = 'Hei, dette er Frederik'
    my_str_res = str_rev(my_str)
    print(my_str_res)