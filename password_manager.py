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
        for row in reader:
            data.append(row)
    
        for index, row in enumerate(data):
            if index != 0:
                row[2] = caesar_encrypt(row[2])

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__ == "__main__":
    encrypt_passwords_in_file("examples/example2.csv")

#Parte 3

def change_password(filename: str, website: str, password: str) -> bool:
    with open(filename, "r") as file:
        reader = csv.reader(file)
        reader = list(reader)

    found = False

    for index, row in enumerate(reader):
        if index != 0 and row:  
            if row[0] == website:
                row[2] = caesar_encrypt(password)
                found = True
                break

    if not found:
        return False

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(reader)

    return True
  
if __name__ == "__main__":
    change_password("examples/example3.csv", "testsite.com", "newsecurepass")

#Parte 4

def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    encrypted_password = caesar_encrypt(password)

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([website_name, username, encrypted_password])

        if __name__ == "__main__":
            add_login("examples/example4.csv", "newsite.com", "newuser", "newpassword")
