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

#Parte 2 

def encrypt_passwords_in_file(filename: str) -> None:
    with open(filename, "r") as file:
        reader = csv.reader(file)
        data = []
        for file in reader:
            data.append(row)
    
        for index, row in enumerate(data):
            encrypted_password = caesar_encrypt(row[2])
            data[index][2] = encrypted_password
    
    with open(filename, "w") as file:
        writer = csv.writer(file)
        for row in data:
            encrypted_password = caesar_encrypt(row[2])
            writer.writerow([row[0], row[1], encrypted_password])  

if __name__ == "__main__":
    encrypt_passwords_in_file("examples/example2.csv")



#Parte 3

def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    pass


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass
