# inheritance : reuse the properties
# step wise 
#  create class 

class Vehicle:
    def __init__(self):
        self.ModelNo = str(input('enter the Model Number : '))
        self.Price = float(input('enter the price of Vehicle : '))
        self.Milage  = float(input('enter the milage  : '))
        self.Seat_cap = int(input('seat capacity : '))
        self.Max = float(input('enter the maximum speed : '))

    def display(self):
        # print('Model number : ',self.ModelNo)
        # print('Price of vehicle : ',self.Price)
        # print('Milage of vehicle : ',self.Milage)
        # print('Capacity of vehicle : ',self.Seat_cap)
        # print('maximum speed  : ',self.Max)
        return (self.ModelNo,self.Price,self.Milage,self.Seat_cap,self.Max)

class Car(Vehicle):
    def __init__(self):
        self.check ="Hello test"
        Vehicle.__init__(self)
    
    def display(self):
        
        return (self.check, Vehicle.display(self))
    

Swift = Car()

x = Swift.display()

print(x)