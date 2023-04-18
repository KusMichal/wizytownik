from faker import Faker
fake = Faker()
fake.phone_number()
fake.email()
fake.name()



    
   



class Base_contact:
    base_contact = []
    buisenescontact = []
    def __init__(self,name,mail,priv_mobile_number):
        self.name = name
        self.mail = mail
        self.priv_mobile_number = priv_mobile_number

    
        
   
   
   
    def __str__(self) -> str:
        return str(self.name +" "+ self.mail)
    
    
    
    def contact(self):
        if Base_contact:
            return (f'Wybieram numer {self.priv_mobile_number} dzwonie do {self.name}')
        
    
   
    @property
    def name_len(self):
        return f'Długość Imienia i Nazwiska {self.name} równa się:  {len(self.name)}'
    
class BuisnessContact(Base_contact):
    buisenescontact = []
    def __init__(self, mobile_number, name, mail,):
        self.mobile_number = mobile_number
        super().__init__(name,mail)
    def contact(self):
        return (f'Wybieram numer {self.mobile_number} dzwonie do {self.name} ')


    def create_contacts(self,x):
        self.name = fake.name()
        self.mail = fake.email()
        self.priv_mobile_number = fake.phone_number()
        self.mobile_number = fake.phone.number()
        if x == base:
            base = Base_contact(self,self.name,self.mail,self.priv_mobile_number)
            self.base_contact.append(base)
        elif x == buisness:
            buisness = BuisnessContact(self, self.name,self.mail,self.mobile_number)
            self.buisenescontact.append(buisness)






