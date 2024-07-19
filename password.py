### This is password generator only Aa12345-Zz12345
import string
#script 1 for Aa12345-Zz12345
def generate_passwords():
    passwords = []
    for first_char in string.ascii_uppercase:
        for second_char in string.ascii_lowercase:
            password = f"{first_char}{second_char}12345"
            passwords.append(password)
    return passwords

passwords = generate_passwords()

with open("passwords.txt", "w") as file:
    for password in passwords:
        file.write(password + "\n")
