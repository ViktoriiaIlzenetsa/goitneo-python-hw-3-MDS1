from classes import Record, Phone
from collections import defaultdict, OrderedDict
from calendar import day_name
from datetime import datetime

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error! Name not found."
        except ValueError:
            return "Enter correct data please."
        except IndexError:
            return "Enter user name"
        
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contact = Record(name)
    number = Phone(phone)
    if number.is_valid():
        if name in contacts.keys():
            contacts[name].add_phone(phone)
            return "Such a contact with this name already exists. Contact added"
        else:
            contact.add_phone(phone)
            contacts.add_record(contact)
            return "Contact added."    
    else:
        return "The phone number is not correct. Please enter the correct one"
    
    
@input_error
def change_contact(args, contacts):
    name, phone = args
    number = Phone(phone)
    if number.is_valid():
        if name in contacts.keys():
            contacts[name].edit_phone(phone)
            return "Contact updated."
        else:
            return "Error! Name not found."
    else:
        return "The phone number is not correct. Please enter the correct one"

    
@input_error
def show_phone(args, contacts):
    name = args[0]
    phones_list = contacts.find(name).phones
    return f"{'; '.join(p.value for p in phones_list)}"

def show_all(contacts):
    for name, record in contacts.data.items():
        print(record)

@input_error
def add_birthday(args, contacts):
    name, birthday = args
    if name in contacts.keys():
        contacts[name].add_birthday(birthday) 
    else:
        return "Error! Name not found."
    
@input_error    
def find_birthday(args, contacts):
    name = args[0]
    data_of_birth = contacts.find(name).birthday
    return data_of_birth.value

def get_birthdays_per_week(contacts):
    dict_of_birthdays = defaultdict(list)
    today = datetime.today().date()
    contacts_items_wt_none = dict(filter(
        lambda item: item[1].birthday.value is not None,
        contacts.data.items()
        ))     
    for name, record in contacts_items_wt_none.items():
        birthday = record.birthday.value
        birthday_this_year = birthday.replace(year = today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year = today.year + 1)
        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            if birthday_this_year.weekday() in (5, 6):
                dict_of_birthdays[abs((-today.weekday())%7)].append(name)
            else:
                dict_of_birthdays[abs((birthday_this_year.weekday() - today.weekday())%7)].append(name)
    ordered_birthdays_dict = OrderedDict(sorted(dict_of_birthdays.items()))
    for weekday, names in ordered_birthdays_dict.items():
        print(f"{day_name[(weekday + today.weekday())%7]}: ", end ='')
        print(*names, sep = ", ")



if __name__ == "__main__":
    pass