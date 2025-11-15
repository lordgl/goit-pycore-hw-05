from typing import Callable

from colorama import Fore, Style

from task4_helpers import (
    validate_name,
    validate_phone_number,
    input_error,
    write_to_db,
    check_contact_exists,
    display_success_message,
    validate_args_count,
)


def greeting() -> str:
    return "Hello, How can I assist you today?"


@input_error
def add_contact(name: str, phone_number: str, contacts_db: dict) -> bool:
    """Adds a new contact to the CONTACTS_DB."""
    if check_contact_exists(name, contacts_db):
        raise ValueError(f"Contact {name} already exists.")
    if not validate_name(name):
        raise ValueError("Invalid name format. Name should contain only alphabetic characters.")
    if not validate_phone_number(phone_number):
        raise ValueError(
            "Invalid phone number format. It should start with '+' followed by 7-15 digits or "
            "'0' followed by 6-14 digits."
        )

    write_to_db(name, phone_number, contacts_db)
    return True


@input_error
def change_contact(name: str, new_phone_number: str, contacts_db: dict) -> bool:
    """Changes the phone number of an existing contact."""
    if not check_contact_exists(name, contacts_db):
        raise ValueError("Contact not found.")
    if not validate_phone_number(new_phone_number):
        raise ValueError(
            "Invalid phone number format. It should start with '+' followed by 7-15 digits or "
            "'0' followed by 6-14 digits."
        )

    write_to_db(name, new_phone_number, contacts_db)
    return True


def close() -> str:
    return "Goodbye! Have a great day!"


def list_contacts(contacts: dict) -> str:
    """
    Lists all contacts in a formatted string.
    Args:
        contacts (dict): A dictionary of contacts with names as keys and phone numbers as values.
    Returns:
        str: A formatted string of all contacts.
    """
    if not contacts:
        return "No contacts found."
    result = "Contacts List:\n"
    for name, number in contacts.items():
        result += f"{name}: {number}\n"
    return result.strip()


@input_error
def handle_hello(args: list[str]) -> None:
    """ 
    Handles the 'hello' command to greet the user and display a greeting message.
    Args:
        args (list[str]): List of arguments provided with the command.
    Raises:
        ValueError: If unexpected arguments are provided.
    """
    validate_args_count(args, 0, "hello")
    print(f"{Style.BRIGHT}{Fore.CYAN}{greeting()}")


@input_error
def handle_add(args: list[str], contacts_db: dict) -> None:
    """ 
    Handles the 'add' command to add a new contact to the CONTACTS_DB and display a success message.
    Args:
        args (list[str]): List of arguments provided with the command.
        contacts_db (dict): The contacts database to add the new contact to.
    Raises:
        ValueError: If the contact already exists or if the input format is invalid.
    """
    validate_args_count(args, 2, "add [name] [phone_number]")
    name, phone_number = args
    if add_contact(name, phone_number, contacts_db):
        display_success_message(f"Contact {name} added with phone number {phone_number}")


@input_error
def handle_change(args: list[str], contacts_db: dict) -> None:
    """ 
    Handles the 'change' command to update an existing contact's phone number and display a success message.
    Args:
        args (list[str]): List of arguments provided with the command.
        contacts_db (dict): The contacts database to update the contact in.
    Raises:
        ValueError: If the contact does not exist or if the input format is invalid.
    """
    validate_args_count(args, 2, "change [name] [new_phone_number]")
    name, new_phone_number = args
    if change_contact(name, new_phone_number, contacts_db):
        display_success_message(f"Contact {name} updated with new phone number {new_phone_number}")


@input_error
def handle_phone(args: list[str], contacts_db: dict) -> None:
    """
    Handles the 'phone' command to retrieve and display a contact's phone number.
    Args:
        args (list[str]): List of arguments provided with the command.
        contacts_db (dict): The contacts database to retrieve the contact from.
    Raises:
        ValueError: If the contact does not exist or if the input format is invalid.
    """
    validate_args_count(args, 1, "phone [name]")
    name = args[0]
    if name not in contacts_db:
        raise ValueError(f"Contact {name} not found.")
    print(
        f"{Style.BRIGHT}{Fore.BLUE}{name}"
        f"{Style.RESET_ALL}{Fore.BLUE}'s phone number is {Style.BRIGHT}{contacts_db[name]}"
    )


@input_error
def handle_all(args: list[str], contacts_db: dict) -> None:
    """
    Handles the 'all' command to display all contacts in the CONTACTS_DB.
    Args:
        args (list[str]): List of arguments provided with the command.
        contacts_db (dict): The contacts database to list contacts from.
    Raises:
        ValueError: If unexpected arguments are provided.
    """
    validate_args_count(args, 0, "all")
    contacts = list_contacts(contacts_db)
    print(f"{Fore.YELLOW}{contacts}")


@input_error
def handle_exit(args: list[str]) -> None:
    """
    Handles the exit commands to terminate the application and display a goodbye message.
    Args:
        args (list[str]): List of arguments provided with the command.
    Raises:
        ValueError: If unexpected arguments are provided.
    """
    validate_args_count(args, 0, "exit/close/bye/q")
    print(f"{Style.BRIGHT}{Fore.MAGENTA}{close()}")
    raise SystemExit


@input_error
def handle_menu(args: list[str], menu_provider: Callable[[], str]) -> None:
    """
    Handles the 'menu' command to display the main menu options to the user.
    Args:
        args (list[str]): List of arguments provided with the command.
        menu_provider (Callable[[], str]): A callable that returns the menu string.
    Raises:
        ValueError: If unexpected arguments are provided.
    """
    validate_args_count(args, 0, "menu")
    print(menu_provider())
