#maintask-create a atm system
#rupay-2000,visa-5000,mastercard-8499,you've crossed trans limit
#st1-displaying remaining amount in atm
#autentication of user if the user is authenticated then give him following options to choose:
#1.check balance 2.cash withdrawl 3.cash deposit (show balance after transaction) 4.mini statement of last 3 transcations 
class auth:
    def __init__(self,a,b): 
        self.a=a
        self.b=b
    def autentication(self) :
        if(self.a==self.b):
            print("login successful")
            return True
        else:
            print("check your credentials and try again")