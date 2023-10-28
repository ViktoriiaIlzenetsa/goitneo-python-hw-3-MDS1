from collections import UserDict
from datetime import datetime
 


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    def __init__(self, name):
        self.value = name

class Phone(Field):
    def __init__(self, phone):
        self.value = phone

    def is_valid(self):
        if self.value.isdigit() and len(self.value) == 10:
            return True
        
class Birthday:
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, birthday):
        date_format = "%d.%m.%Y"
        try:
            date_of_birth = datetime.strptime(birthday, date_format).date() 
        except ValueError:
            print("Incorrect data format, should be DD.MM.YYYY")
        else:
            self.__value = date_of_birth
            print("Date of birth added")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday()

    def add_birthday(self, birthday):
        self.birthday = Birthday()
        self.birthday.value = birthday
        

    def add_phone(self, phone):
        self.phone = Phone(phone)
        self.phones.append(self.phone)
            
            
    def remove_phone(self, phone):
        for i in range(len(self.phones)):
            if self.phones[i].value == phone:
                del self.phones[i]

    def edit_phone(self, new_phone):
        self.phones[0] = Phone(new_phone)

    def find_phone(self, phone):
        for i in range(len(self.phones)):
            if self.phones[i].value == phone:
                return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value}"
    
class AddressBook(UserDict):
    def add_record(self, new_record):
        self.data[new_record.name.value] = new_record

    def find(self, name):
        return self.data[name]
            
    def delete(self, name):
        del self.data[name]