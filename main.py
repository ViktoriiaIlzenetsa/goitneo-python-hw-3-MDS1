import utils
from classes import AddressBook

def main():
    contacts = AddressBook()
    print("""Welcome to the assistant bot!
    Available commands:
        ° hello
        ° add <name> <phone number>
        ° change <name> <new phone number>
        ° phone <name>
        ° all
        ° add-birthday <name> <birthday(in format DD.MM.YYYY)>
        ° show-birthday <name>        
        ° birthdays
        ° close/exit""")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = utils.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(utils.add_contact(args, contacts))
        elif command == "change":
            print(utils.change_contact(args, contacts))
        elif command == "phone":
            print(utils.show_phone(args, contacts))
        elif command == "add-birthday":
            print(utils.add_birthday(args, contacts)) if utils.add_birthday(args, contacts) else False
        elif command == "show-birthday":
            print(utils.find_birthday(args, contacts))
        elif command == "birthdays":
            utils.get_birthdays_per_week(contacts)
        elif command == "all":
            utils.show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
