class vehicle:
    def __init__(self,type,fare):
        self.type=type
        self.fare=fare
    def details(self):
        self.type=input("Enter the type:")
        self.fare=int(input("Enter the fare:"))
    def put_details(self):
        print(self.type,self.fare)
#f=vehicle('','')
#f.details()
#f.put_details()
class car():
    def __init__(self,availability,time):
        self.availability=availability
        self.time=time
    def cardetails(self):
        self.availability=input("Enter the slot:")
        self.time=input("Enter the Time:")
        
    def getcar(self):
        print(self.fare,self.availability,self.time)
    def caronly(self):
        print(self.availability,self.time)
class bike(vehicle,car):
    def __init__(self,wheeler):
        self.wheeler=wheeler
        
    def bikedet(self):
        self.wheeler=int(input("Enter the number of wheels:"))
    def putbikee(self):
        print(self.wheeler,self.time,self.fare,self.type)

#g=car('','')
#g.cardetails()
#g.caronly()
k=bike('')
k.details()
k.cardetails()
k.bikedet()
k.putbikee()