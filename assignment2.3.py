# Assignment 2,3
class Account(object):
    ''' Put in and take out mney from bank. The amount 
        in the bank will increase, thanks to the rent
        The default beginning amount is 100 '''
    def __init__(self,intake,whitdrawal,rent = 0.05, amount = 100):
        self.intake = intake
        self.rent = rent
        self.amount = amount
        self.whitdrawal = whitdrawal

    def amount_increase(self):
        ''' amount = amount + the rent of the amount + the new intake'''
        self.amount = self.amount + self.amount*rent + intake
        return self.amount

    def amount_decrease(self):
        '''amount = amount + the rent of the amount - the takeout'''
        self.amount = self.amount + self.amount * self.rent - self.whitdrawal
        return self.amount


if __name__ == "__main__":
    intake_choice = False
    whitdrawal_choice = False
    intake = str(input('Do tou want to intake or whitdraw money: [y/n]: '))
    if intake[0].lower == 'y':
        #intake_choice == True 
        #return intake_choice
        intake = input('How much money do you want to intake:')
        whitdrawal = 0
        my_account_balance = Account(intake,whitdrawal,rent,amount)
        print(my_account_balance)
    elif intake[0].lower == 'n':
        #whitdrawal_choice == True
        #return whitdrawal_choice
        whitdrawal = input('How much money do you want to whitdraw:')
        intake = 0
        my_account_balance = Account(intake,whitdrawal,rent,amount)
        print(my_account_balance)
    def notworkingfunc():
        print("Here nothing is happening. This is done to try the version control on github")
    '''
    if intake_choice == True:
        intake = int(input('How much money do you want to intake:'))
        whitdrawal = 0
        my_account_balance = Account(intake,whitdrawal,rent,amount)
        print(my_account_balance)

    if whitdrawal_choice == True:
        whitdrawal = int(input('How much money do you want to whitdraw:'))
        intake = 0
        my_account_balance = Account(intake,whitdrawal,rent,amount)
        #print(my_account_balance)
        '''
    

    


    