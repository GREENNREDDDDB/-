class Car():
    def __init__(self ,brand ,model ,year):
        self.brand = brand
        self.model = model
        self.year = year
    def print_car(self):
        print(f'This car is {self.year} {self.brand} {self.model}')
    def run(self):
        print('car is running')
        

class Buy_car(Car):
    def __init__(self ,name ,brand ,model ,year):
        Car.__init__(self ,brand ,model ,year)
        self.name = name
    def buy(self):
        print(f'{self.name} buy a {self.year} {self.brand} self.{self.model} ')
        