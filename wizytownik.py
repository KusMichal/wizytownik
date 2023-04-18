from faker import Faker
fake = Faker()
fake.phone_number()
fake.email()
fake.name()

class Base_contact:
    base_contact = []
    
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

    def __init__(self, mobile_number,name,mail):
        super().__init__(name,mail)
        self.mobile_number = mobile_number
        
    def contact(self):
        return (f'Wybieram numer {self.mobile_number} dzwonie do {self.name} ')


    def create_contacts(y):
        name = fake.name()
        mail = fake.email()
        mobile_number = fake.phone_number()
        for i in range(y):
            buisness = BuisnessContact(name,mail,mobile_number)
            buisenescontact.append(buisness)
buisenescontact = []

BuisnessContact.create_contacts(2)


