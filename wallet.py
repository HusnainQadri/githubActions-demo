class wallet:
    balance = 500
    
    def __init__(self,balance):
        self.balance = balance

    def checkBalance(self):
        return self.balance
        
    def addMoney(self,moneyToBeAdded):
        self.balance = self.balance + moneyToBeAdded
        return self.balance
    
    def deductMoney(self,moneyToBeDeducted):
        self.balance = self.balance - moneyToBeDeducted
        return self.balance
    