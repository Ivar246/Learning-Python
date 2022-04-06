from itertools import count



accounts = {}

class Account:
    
    count = count(start=1)
        
    def __init__(self, name, balance, pin):
        
        ac_n = next(self.count)
        self.ac_n = ac_n
        self.name = name
        self.balance = balance
        self.pin= pin
        
        accounts[ac_n] = self
        print(f"congrats, {name} account has been created with rs ", balance)
        
        
    def change_pin(self, old_pin, new_pin):
        
        if old_pin == self.pin:
            
            self.pin = new_pin
            
        else: 
            
            print('your old_pin is invalid.')
            
    def __str__(self):
        
        return f"account nO: {self.ac_n} Name: {self.name}"
    
    def transfer_balance(self, pin, reciever_name, reciever_acn, amount):
     
        if self.ac_n != reciever_acn:  
            
            if pin == self.pin:        
                    
                if accounts.get(reciever_acn) != None:
                    
                    if self.balance >= amount:    
                        
                        reciever = accounts.get(reciever_acn)
                        
                        if reciever.name == reciever_name:
                                
                            new_balance= self.balance - amount
                            self.balance=new_balance
                            
                            new_reciever_balance = reciever.balance + amount
                            reciever.balance = new_reciever_balance
                            
                            print(f"Your transfer has been sucessful. your new balance is {self.balance}")
                            
                        
                        else:
                            print("The name and account number did not match")
                            
                    else:
                        print("Your balance insufficient..")
                        
                else:
                        print("sorry..account number doesn't exist")
            
            else:
                print("You pin in incorrect..please try again")
         
        else:
            print("You cannot transfer balance to your own account..")   
                            
my = Account(name='Ravi', balance=1500, pin=1234)
your  = Account(name='Rabin', balance=1600, pin=546)

my.transfer_balance(pin=1234, reciever_name='Rabin', reciever_acn=1, amount=1200)
print("my_balance= ", my.balance)
print("Your balance =", your.balance)

