import authentication
import tasks

print("//WELCOME TO SA ATM//")
a=input("Enter username:")
b=input("Enter password:")

aobj=authentication.auth(a,b)
# print(aobj.autentication())
if (aobj.autentication()):
    tobj=tasks.balance()
    tobj.bal()
    print("enter card type:")
    (print("1.rupay""\n""2.visa""\n""3.mastercard"))
    ct=input()
    if (tobj.cards(ct)):
        while True:
            print("Menu:")
            (print("1.checkbalance""\n""2.withdrawl""\n""3.deposit""\n""4.ministatement""\n""5.exit"))
            task=input()
            list1=[]
            if(task=="1"or task=="checkbalance"):
                rt=tobj.cb()
                print()
                # list1.append(rt)
            elif(task=="2"or task=="withdrawl"):
                wda=int(input("Enter amount to withdraw:"))
                rt=tobj.wd(wda)
                # list1.append(rt)
            elif(task=="3"or task=="deposit"):
                da=int(input("enter amount to deposit:"))
                rt=tobj.dp(da)
                print()
                # list1.append(rt)
            elif(task=="4"or task=="ministatement"):
                #print("list1[-3:]")
                print("CURRENTLY UNAVALIABLE")
                print()
            elif(task=="5"or task=="exit"):
                print("THANK FOR USING SA ATM")
                break
            else:
                print("invalid option")
                print()        

    