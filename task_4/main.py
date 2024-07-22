from commads import add_contact, change_contact, show_phone, all_contacts

COMMAND_EXIT = ("close", "exit")
COMMAND_HELLO = "hello"
COMMAND_ADD = "add"
COMMAND_CHANGE = "change"
COMMAND_PHONE = "phone"
COMMAND_ALL = "all"

def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        command, args = parse_input(user_input)

        if command in COMMAND_EXIT:
            print("Good bye!")
            break

        elif command == COMMAND_HELLO:
            print("How can I help you?")

        elif command == COMMAND_ADD:
            print(add_contact(args, contacts))

        elif command == COMMAND_CHANGE:
            print(change_contact(args, contacts))

        elif command == COMMAND_PHONE:
            print(show_phone(args, contacts))

        elif command == COMMAND_ALL:
            print(all_contacts(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
