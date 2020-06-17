'''
Collatz Conjecture
'''
from typing import List
def collatz_con(n):
    '''
    Collatz conjecture -> famous algorithm
    INPUT: a number n>1
    OUTPU: How many iteration needed in order to get the result 1 + the list of all n-values
    '''
    counter = 0
    n_list: list[int] =  []
    while n <= 1:
        n = int(input('n must be larger than 1 (n => 1). Try again: '))
    while n != 1:
        if n % 2:
            n = int(3*n+1)
            n_list.append(n) 
            counter = counter + 1
         
        else:
            n = int(n/2)
            n_list.append(n)
            counter = counter + 1
            
    return n_list,counter

if __name__ == "__main__":
    n = 10
    my_collatz_con = collatz_con(n)
    print(f'With n = {n}, the algrithm used {my_collatz_con[1]} iteration.\nThe value of all iteration was; {my_collatz_con[0]}')
   
# checking how this new comment looks like in github version control


