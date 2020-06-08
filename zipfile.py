class account:
    def __init__(self):
        self.name=None
        self.no=None
        self.bal=None
    def set_acc(self,name,no,bal):
        self.name=name
        self.no=no
        self.bal=bal
    def deposit(self,tamt):
        self.bal=self.bal+tamt
    def withdraw(self,tamt):
        if self.bal<tamt:
            print('insufficient balance')
        else:
            self.bal=self.bal-tamt
    def print_acc(self):
        print(self.name,self.no,self.bal)
        

def main():
    acc=None
    while True:
        print('1.create account')
        print('2.Display account')
        print('3.Deposit')
        print('4.Withdraw')
        print('5.Exit)
        if opt==1:
            acc=account()
            no=int(input("enter value"))
            name=input("enter name")
            balance=float(input("enter balance'="))
            acc.set_acc(name,no,bal)
        elif opt==2:
            acc.print_acc()
        elif opt==3:
            tamt=float(input("enter the value"))
            acc.deposit()
            
            
        