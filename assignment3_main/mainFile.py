from Class.Card import Card as myClassCard

#Class.card as myClass
if __name__ == "__main__":
    char = 'heart'
    value = 1
    toStringTuple = myClassCard(char,value).toString()
    #print(f'{char} of {value}')
    print(f'{toStringTuple[1]} of {toStringTuple[0]}')

    