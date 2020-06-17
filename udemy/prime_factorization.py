'''
Input: a number
Output: List of all prime numbers assosiated with that number
'''

from typing import List

def prime_check(number_choice):
    prime_list = []
    while number_choice <=1:
        number_choice = input('Put in a value >1: ')

    for num in list(range(100)):
        if num%number_choice == 0:
            prime_list.append(num)
    return prime_list

if __name__ == "__main__":
    number_choice = int(input('Put in a value >1: '))
    my_prime_check = prime_check(number_choice)
    print(f'\n\nThe numbers up to 100 where {number_choice} is a primal factor is: ')
    print(my_prime_check)

'''
    my_list = []
    for num in list(range(100)):
        if num%2 == 0:
            my_list.append(num)

    print(my_list)    
'''
