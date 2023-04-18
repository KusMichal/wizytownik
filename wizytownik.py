from faker import Faker
from faker.providers import DynamicProvider

book_provider = DynamicProvider(provider_name = "book",elements=["Buisness Contact", "Base Contact"])
fake = Faker()
fake.add_provider(book_provider)
fake.name()
fake.phone_number()
fake.company()
fake.email()

def create_contacts(x):
    for i in range(x):
        print(fake.book())
        print(fake.name())
        print(fake.phone_number())
        print(fake.company())
        print(fake.email())



class AdressBook:
    def __init__(self,name,last_name,company,proffesion,mail):
        self.name = name
        self.last_name = last_name
        self.company = company
        self.proffesion = proffesion
        self.mail = mail
    def __str__(self) -> str:
        return str(self.name +" "+ self.last_name +" "+ self.mail)
    
    
    def contact(self):
        if AdressBook:
            return (f'Kontaktuje się z {self.company} ,{self.name}, {self.last_name}, {self.proffesion}, {self.mail}')
        
    
    def adress_list(adress):
        for i in adress:
            print(i)

    @property
    def name_len(self):
        return f'Długość Imienia {self.name} i Nazwiska {self.last_name} równa się:  {len(self.name)} {len(self.last_name)}'
    
class Base_contact(AdressBook):
    def __init__ (self,priv_mobile_number,*args, **kwargs):
        self.priv_mobile_number = priv_mobile_number
        super().__init__(*args,**kwargs)
    def contact(self):
        if Base_contact:
            return (f'Wybieram numer {self.priv_mobile_number} dzwonie do {self.name} {self.last_name}')

class BuisnessContact(Base_contact):
    def __init__(self, mobile_number, name, last_name, mail, company, proffesion):
        self.mobile_number = mobile_number
        super().__init__(name, last_name, mail, company, proffesion)
    def contact(self):
        return (f'Wybieram numer {self.mobile_number} dzwonie do {self.name} {self.last_name}')
   

adress1 = AdressBook(name="Patrycja",last_name="Adamska",company="Mikrotechnik",proffesion="Conservation Worker",mail="patrycjaadamska@teleworm.us")
adress2 = AdressBook(name="Łucja",last_name="Chmielewska",company="Big D Supermarkets",proffesion="Customer services manager",mail="lucjachmielewska@rhyta.com")
adress3 = AdressBook(name="Bogusława",last_name="Kwiatkowska",company="Stratabiz",proffesion="Museum Director",mail="boguslawakwiatkowska@rhyta.com")
adress4 = AdressBook(name="Justyna",last_name="Pawłowska",company="Grodins",proffesion="Sciences Manager",mail="justynapawlowska@armyspy.com")
adress5 = AdressBook(name="Felicjan",last_name="Sawicki",company="Tweeter",proffesion="Transmission engineer",mail="felicjansawicki@armyspy.com")
adress6 = Base_contact(name="Wojciech",last_name="Rutkowski",company="Alexanders",proffesion="Building Worker", mail="wojciechrutkowski@thyta.com",priv_mobile_number="+48782958407")

adress = [adress1,adress2,adress3,adress4,adress5,adress6]
by_name = sorted(adress, key=lambda Adress_book: Adress_book.name)
print(adress1.contact())
print(AdressBook.adress_list(adress))
print(adress2.name_len)
print(adress6.contact())
print(adress6.name_len)
create_contacts(3)
