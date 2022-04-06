class Person:
    def __init__(self, name , age, address):
        
        self.name = name
        self.age = age
        self.address = address
    
    
    def eat(self):
        
        print(f'{self.name}eat food..')
    
    
    def walk(self):
        
        print(f'{self.name} walk to home.')
    
    
    def run(self):
        
        print(f'{self.name} run to home.')
        
        
    def print_details(self):
        
        print(f'name: {self.name}\n age:{self.age}\naddress:{self.address}')


class Male(Person):
    pass
        
        


p1 = Male('Ram', 15, 'Lazimpat')
p2 = Person('Sita', 14, 'Baluwatar')


p1.print_details()
p1.walk()
p1.eat()
