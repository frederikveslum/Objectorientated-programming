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
    rent = 0.05
    amount = 100
    intake = str(" ")
    while intake[0].lower() != 'i' or intake[0].lower() != 'w':
        intake = str(input('Do you want to intake or whitdraw money: [i/w]: '))
        if intake[0].lower() == 'i':
            intake = int(input('How much money do you want to intake:'))
            while intake <0:
                intake = int(input('Negative number not permitted; how much money do you want to intake:'))
            intake_choice = True
            whitdrawal_choice = False
            whitdraw = 0
            break
        elif intake[0].lower() == 'w':
            whitdraw = int(input('How much money do you want to whitdraw:'))
            while whitdraw <0:
                whitdraw = int(input('Negative number not permitted; how much money do you want to whitdraw:'))
            whitdrawal_choice = True
            intake_choice = False
            intake = 0
            break
    if intake_choice == True:
        amount_in_bank = Account(intake,whitdraw,rent,amount).amount_increase()
        print(f'The new value in the bank = {amount_in_bank}')
    if whitdrawal_choice == True:
        amount_in_bank = Account(intake,whitdraw,rent,amount).amount_decrease()
        print(f'The new value in the bank = {amount_in_bank}')

            
    

    

    


    