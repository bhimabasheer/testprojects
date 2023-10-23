class student:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def get_student(self):
        return f'Name:{self.name} ,Age:{self.age},Address: {self.address}'
     

class Address:
    def __init__(self,state,city):
        self.state=state
        self.city=city
    def get_val(self):
        return f'{self.state} {self.city}'
        
    
f=Address('kerala','kottayam')
g=student('Faisal','31',f.get_val())
print(g.get_student())



