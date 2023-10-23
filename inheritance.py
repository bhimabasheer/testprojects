class vehicle:
    def __init__(self,type,fare):
        self.type=type
        self.fare=fare
    def details(self):
        self.type=input("Enter the type:")
        self.fare=input("Enter the fare:")
    def put_details(self):
        print(self.type,self.fare)
f=vehicle('','')
f.details()
f.put_details()
class car(vehicle):
    def __init__(self,availability,time):
        self.availability=availability
        self.time=time
    def cardetails(self):
        self.availability=input("Enter the slot:")
        self.time=input("Enter the Time:")
        self.fare=input("Enter the fare:")
    def getcar(self):
        print(self.fare,self.availability,self.time)
    def caronly(self):
        print(self.availability,self.time)

g=car('','')
g.cardetails()
g.getcar()
g.caronly()