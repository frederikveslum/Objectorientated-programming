class Card(object):
    '''
    Input: char and int
    - Gives every card in a cardstock group and value
    output: List with all the cards 
    '''
    char = ['spade','heart','diamond','cluc']
    value = list(range(1,14))
    def __init__(self,char,value):
        self.char = char
        self.value = value
    
    def __str__(self):
        ''' Able to use print(Card()....()) '''
        return(f'The chosen card is {char} of {value}')
    
    def getSuit(self):
        ''' returns the suit which is input'''
        return self.char

    def getFace(self):
        ''' returns the face which is input'''
        return self.value
    
    def toString(self):
        ''' returns the suit and face as a tuple pair'''
        heyho = self.value,self.char
        return heyho