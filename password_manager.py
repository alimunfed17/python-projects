from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("keys.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("keys.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            username, password = data.split("|")
            print("Username: ", username + " | "  + "Password: ", fer.decrypt(password.encode()).decode())

def add():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("passwords.txt", "a") as f:
        f.write(username + "|" + fer.encrypt(password.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a password or view a password or q to quit (view, add) ? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue