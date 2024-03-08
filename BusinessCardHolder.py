from faker import Faker
from datetime import datetime

fake = Faker()

class BaseContact:
    
    def __init__(self, name, surname, phone_number, email):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email
        self._name_length = 0

    @property
    def name_length(self):
        return f"{len(self.name)} {len(self.surname)}"

    #@name_length.getter
    #def name_length(self):
    #    return f"{len(self.name)} {len(self.surname)}" 

    def __str__(self):
        return f'{self.name} {self.surname} {self.phone_number} {self.email}'
    
    def __repr__(self):
        return f'''Name={self.name}, Surname={self.surname}, Name_len={self.name_length}, Phone number={self.phone_number}, E-mail={self.email}'''
    
    def __eq__(self, other):
        return (self.name == other.name and self.surname == other.surname and
                self.phone_number == other.phone_number and self.email == other.email)
    
    def contact(self):
        return print(f"Wybieram numer {self.phone_number} i dzwonie do {self.name} {self.surname}")


class BusinessContact(BaseContact):

    def __init__(self, position, company, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.work_phone = work_phone

    def contact(self):
        return print(f"Wybieram numer {self.work_phone} i dzwonie to {self.name} {self.surname}")
    

## Function 
    
def create_contacts(type, amount):
    list_of_new_instances = []
    for i in range(amount):
        if type == BaseContact:
            temp = BaseContact(name=fake.name(), surname=fake.last_name(), phone_number=fake.phone_number(), email=fake.email())
        elif type == BusinessContact:
            temp = BusinessContact(name=fake.name(), surname=fake.last_name(), phone_number=fake.phone_number(), email=fake.email(),
                                   position=fake.job(), company=fake.company(), work_phone=fake.phone_number())
        list_of_new_instances.append(temp)
    
    return list_of_new_instances

def measure_time(func):
    time_str = datetime.now()
    def wrapper():
        result = func()
        return result
    time_stop = datetime.now()
    dif = time_stop - time_str
    print(f" Time of the process in sec: {dif.total_seconds()}")
    return wrapper

@measure_time
def create_1000_contacts():
    contacts = []
    for i in range(1000):
        temp = BusinessContact(name=fake.name(), surname=fake.last_name(), phone_number=fake.phone_number(), email=fake.email(),
                                   position=fake.job(), company=fake.company(), work_phone=fake.phone_number())
        contacts.append(temp)
    return contacts

if __name__ == "__main__":
    list_1000 = create_1000_contacts()

        
    house = BaseContact(name="Greg", surname="House", email="greg.house@princeton-plainsboro.com", phone_number=fake.phone_number())
    cameron = BaseContact("Allison", "Cameron", fake.phone_number(), "allison.cameron@princeton-plainsboro.com")
    foreman = BusinessContact(name="Eric", surname="Foreman", email="forman@princeton-plainsboro.com", phone_number="+10123456789",
                        position="Neurologist", company="Hospital Princeton-Plainsboro", work_phone="+19876543210")
    chase = BusinessContact(name="Robert", surname="Chase", position="surgen", company="Hospital Princeton-Plainsboro",
                        email="robert.chase@princeton-plainsboro.com", work_phone=fake.phone_number(), phone_number=fake.phone_number())
    wilson = BusinessContact(name="James", surname="Wilson", position="Oncologist", phone_number=fake.phone_number(), work_phone=fake.phone_number(),
                      email="james.wilson@princeton-plainsboro.com", company="Hospital Princeton-Plainsboro")

    cameron.contact()
    foreman.contact()


    cameron.name = "Penelopia"
    print(foreman.__repr__())
    print(cameron.__repr__())

    new_instances = create_contacts(BaseContact, 3)

    print(new_instances[0])

    new_inst_Business = create_contacts(BusinessContact, 10)