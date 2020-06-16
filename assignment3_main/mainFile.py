'''
class card(object):
    '''
    #Input: char and int
    #- Gives every card in a cardstock group and value
    #output: List with all the cards 
'''
char = ['spade','cluc','heart','diamond']
value = list(range(1,14))
print(value)
def __init__(self,char,value):
    self.char = char
    self.value = value

def __str__(self):
    return(f'The chosen card is {char} of {value}')

def getSuit(self):
    return self.char

def getFace(self):
    return self.value

def toString(self):
    return self.value,self.char
'''
#from Class import card
#import Class.card as myClass
from Class.card import Card as myClassCard

#Class.card as myClass
if __name__ == "__main__":
    char = 'heart'
    value = 1
    #print(card(char,value))
    face = myClassCard(char,value).toString()
    print(f'{char} of {value}')
    #face = myClassCard(char,value).getFace()
    #print(face)
    