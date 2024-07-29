#maintask-create a atm system
#rupay-2000,visa-5000,mastercard-8499,you've crossed trans limit
#st1-displaying remaining amount in atm
#autentication of user if the user is authenticated then give him following options to choose:
#1.check balance 2.cash withdrawl 3.cash deposit (show balance after transaction) 4.mini statement of last 3 transcations 
class balance:
    def bal(self,):
        self.balance=1000000
        self.acbal=30000
        print("Avaliable balance in atm ==",self.balance)
        print()
    def cards(self,cardtype):
        self.cardtype=cardtype
        if(self.cardtype=="1" or self.cardtype=="rupay"):
            self.cardtype="rupay"
            self.translimit=2000 
            return True          
        elif(self.cardtype=="2" or self.cardtype=="visa"):
            self.cardtype="visa"  
            self.translimit=5000  
            return True
        elif(self.cardtype=="3" or self.cardtype=="mastercard"):
            self.cardtype="mastercard"
            self.translimit=8499
            return True
        else:
            print("Invalid selection of card")
            return False
    def cb(self):
        print("Avaliable balance in account:",self.acbal)
    def wd(self,wda):
       self.wda=wda
       if(self.wda<=self.acbal and self.wda<=self.balance):
           if(self.wda<=self.translimit):
               self.acbal-=self.wda
               self.balance-=self.wda
               self.translimit-=self.wda
               print(self.wda,"rupees withdrawed, avaliable balance:",self.acbal)
               print("tras:",self.translimit)
           else:
               print("Exceeded transcation limit")
       elif(self.acbal<self.wda):
           print("insufficient funds in account")
       elif(self.wda>self.balance):
           print("insufficient funds in ATM")
       else:
           print("Invalid selection")
           
                       
               
    #    if (self.wda<=self.acbal and self.wda>0):
    #        if self.wda <= self.translimit:
    #         self.translimit-=self.wda
    #         self.acbal-=self.wda
    #         print("withdraw successful,avaliable balance:",self.acbal)
    #         print()
    #        else:
    #             print("cant withdraw",self.cardtype,"limit is",self.translimit)
    #             print()
    #    elif(self.wda>self.balance and self.wda < self.translimit):
    #        print("insufficient funds in atm")
    #        print()
    #    elif(self.wda<self.acbal and self.wda < self.translimit ) or self.wda>self.acbal :
    #        print("insufficient funds in account")
    #        print()
    def dp(self,da):
        self.da=da
        self.acbal=self.acbal+self.da
        print(self.da,"rupees deposited, avaliable balance:",self.acbal)
        print()
