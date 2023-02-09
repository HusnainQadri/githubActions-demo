from wallet import wallet

obj = wallet(600)

assert 600 == obj.checkBalance()

assert 700 == obj.addMoney(100)

assert 500 == obj.deductMoney(200)