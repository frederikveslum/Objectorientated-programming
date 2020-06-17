'''
This program is going to return a list of the n-th fibonacci numbers.
INPUT: Number of required fibonacci 
Output: List of len(INPUT)
'''

from typing import List

def recur_fibo(n):
    my_liste =[]
    for num in list(range(n)):
        if num<=1:
            my_liste.append(1)
        else:
            my_liste.append(my_liste[num-1] + my_liste[num-2])
    return(my_liste)



if __name__ == "__main__":
    n = 20
    my_recur_fibo = recur_fibo(n)
    print(my_recur_fibo)


