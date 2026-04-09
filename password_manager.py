import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename : str) -> None:
    with open (filename,"r") as file:
        original_password = file.read().strip()
    encrypted_password = caesar_encrypt(original_password)

    with open (filename,"w") as file:
        file.write(encrypted_password)

if __name__ == "__main__":
    encrypt_single_pass("examples/example1.txt")


def encrypt_passwords_in_file(filename: str) -> None:
    """TODO: Parte 2."""
    pass


def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    pass


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass
