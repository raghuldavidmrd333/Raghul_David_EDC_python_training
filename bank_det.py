class bank_details:
    def __init__(self,acct_num,name,password,balance,rate):  
        self.acct_num=acct_num
        self.name=name
        self.password=password
        self.balance=balance
        self.rate= rate
        print("************ Welcome to MRD Banking *********** \n Please choos the type of service you want\n ")
        print("1.DEPOSIT\t\t\t2.WITHDRAW\n")
        print("3.BALANCE ENQUIRY\t\t4.MINI STATEMENT\n")
    
    def info(self):
        print("Your available balance is :",self.balance)
        

    def deposit(self,amount):
        if(amount>0):
            total_balance=self.balance + amount
            print("Your avilable balance is :",total_balance)
        else:
            print("Please enter a valid amount")
    
    def withdraw(self,password,amount):
        if(password == self.password):
            if(amount>0):
                if(amount<self.balance):
                    new_balance= self.balance -amount
                    print("your avilable balance after withdrawal is :",new_balance)
                else:
                    print("The entered amount for withdrawal is more than the available balance")
            else:
                print("please enter a valid amount")
        else:
            print("Please enter the correct password")

    def credit_interest(self):
        new_int=self.balance+(self.balance * self.rate /1200)
        print(" your credit rate is :",new_int)

ob=bank_details(1000102,"raghul",1121,30000,5)
ob.info()
ob.withdraw(1121,7000)
ob.credit_interest()