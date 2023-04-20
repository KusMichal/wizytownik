from faker import Faker
fake = Faker()
fake.phone_number()
fake.email()
fake.name()


class Contact:
    def __init__(self,name,mail):
        self.name = name
        self.mail = mail
    def label_lenght(self):
        return(f'Długość Imienia i Nazwiska {self.name} równa się:  {len(self.name)}')

    def contact(self):
        return(f'Wybieram numer {self.mobile_number} dzwonie do {self.name}.')
    
    def __str__(self) -> str:
        return str(self.name +" "+ self.mail)   
         
class Base_contact(Contact):
    
    def __init__(self,name,mail,priv_mobile_number):
        super().__init__(name,mail)
        self.priv_mobile_number = priv_mobile_number

    def contact(self):
        return(f'Wybieram numer {self.priv_mobile_number} dzwonie do {self.name}.')
    
    def all_contact(self):
        for i in base_contact:
            print(i)
        
class BuisnessContact(Contact):

    def __init__(self,mobile_number,name,mail):
        self.mobile_number = mobile_number
        super().__init__(name,mail)
    def contact(self):
        return(f'Wybieram numer {self.mobile_number} dzwonie do {self.name}.')    
    
    def all_contact(self):
        for i in buisenescontact:
            print(i)


Kacper = Base_contact(name="Kacepr Hus", priv_mobile_number="+48500444025", mail="kksu@gp.pl")  
Karolina = BuisnessContact(name="Karolina His", mobile_number ="+48002145654",mail ="khis@gg.pl")

buisenescontact = [Karolina]
base_contact = [Kacper]

def  create_contacts():
    x = int(input("Jaką wizytówke chcesz dodać 1- Buisness , 2 Base"))
    y = int(input("Ile wizytówek chcesz dodać? "))
    while y != 0:
        name = fake.name()
        mail = fake.email()
        mobile_number = fake.phone_number()
        priv_mobile_number = fake.phone_number()
    
        if x == 1:
            contact = BuisnessContact(mail,name,mobile_number)
            buisenescontact.append(contact)
        elif x == 2:
            contact = Base_contact(name,priv_mobile_number,mail)
            base_contact.append(contact)
        y -= 1
        if y == 0:
            break
        
#create_contacts()


Base_contact.all_contact(base_contact)
print(Base_contact.contact(Kacper))

