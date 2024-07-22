from helpers import input_error, input_validate_args

@input_error
@input_validate_args(["name", "phone"])
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args

    if name in contacts:
        raise IndexError("Contact is already exist. Use \"change\" command to update the contact.")

    contacts[name] = phone

    return "Contact added."

@input_error
@input_validate_args(["name", "phone"])
def change_contact(args: list, contacts: dict) -> str:
    name, phone = args

    if name not in contacts:
        raise KeyError("Contact doesn't exist.")

    contacts[name] = phone

    return "Contact updated."

@input_error
@input_validate_args(["name"])
def show_phone(args: list, contacts: dict) -> str:
    name = args[0]

    if name not in contacts:
        raise KeyError("Contact doesn't exist.")

    return contacts[name]

@input_error
def all_contacts(contacts: dict) -> str:
    if not contacts:
        raise IndexError("Contacts dictionary is empty.")

    command_output = "Contacts list:"

    for name, phone in contacts.items():
        command_output += f"\n{name}: {phone}"

    return command_output
