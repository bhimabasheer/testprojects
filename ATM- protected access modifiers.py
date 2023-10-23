class ATM:
    def __init__(self,username,pin,bankname):
        self._username=username
        self._pin=pin
        self.bankname=self.bankname
    def get_details(self):
        self._username=input("Enter the name:")
        self._pin=input("Enter the pin:")
        self.bankname=input("Enter the bankname:")
    def set_details(self):
        print(self._username,self._pin,self.bankname)
class serialnumber(ATM):
    def __init__(self,_serialNo):
        self._serialNo=_serialNo
    def set_serialnumber(self):
        self._serialNo+=1
        print(self.bankname,self.set_serialnumber)
f=serialnumber('','','')
f.get_details()
f.set_details()

    
    