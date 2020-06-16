from typing import List
class CardDeck(object):
    '''
    '''
    char = ['spade','heart','diamond','cluc',]
    value = list(range(1,14))
    carddecklist = ""
    def __init__(self,n):
        #self.char = char
        self.n = n
    
    def __str__(self):
        ''' Able to use print(Card()....()) '''
        return(f'The chosen number is: {n}')

    def CardDeckfunc(self):
        for i in range(4):
            for values in range(n):
                carddecklist.append(f'{char[i]} + {values}')
        return carddecklist





if __name__ == "__main__":
    n = 5
    carddecklist = CardDeck(n).CardDeckfunc()
    #print(f'{char} of {value}')
    print(cardecklist)
    

    