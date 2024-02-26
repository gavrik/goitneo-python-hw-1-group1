DB = {}

def parce_input(input):
    cmd, *args = user_input.split()
    return cmd.lower(), *args

def add_contact_handler(args):
    if len(args) < 2:
        return "  Error: Wrong syntax!\n  Example: add UserName 12345678890"
    name, phone = args
    if name in DB.keys():
        return "  Contact is present in DB. Use change command instead"
    DB[name] = phone
    return " Contact added."

def change_contact_handler(args):
    if len(args) != 2:
        return "  Error: Wrong syntax!\n  Example: change UserName 12345678890"
    name, phone = args
    if name not in DB.keys():
        return "  Contact is not present in DB. Use add command instead"
    DB[name] = phone
    return " Contact updated"

def phone_contact_handler(args):
    if len(args) != 1:
        return "  Error: Wrong syntax!\n  Example: phone UserName"
    name = args[0]
    if name not in DB.keys():
        return "  The UserName is not present in DB"
    return " {}".format(DB[name])

def show_all():
    for c in DB:
        print(" {}: {}".format(c, DB[c]))
    

if __name__ == "__main__":
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        command, *args = parce_input(user_input)

        if command in ["close", "exit"]:
            print(" Good bye!")
            break
        elif command == "hello":
            print(" How can I help you?")
        elif command == "add":
            print(add_contact_handler(args))
        elif command == "change":
            print(change_contact_handler(args))
        elif command == "phone":
            print(phone_contact_handler(args))
        elif command == "all":
            show_all()
        else:
            print(" Invalid command.")
