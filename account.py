import json


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open('users.json.') as f:
        accounts = json.load(f)

    for account in accounts:
        if account['username'] == username and account['password'] == password:
            print("Login successful!")
            return

    print("Invalid username or password.")


def register():
    username = input("Choose a username: ")
    password = input("Choose a password: ")

    with open('users.json', 'r+') as f:
        try:
            accounts = json.load(f)
        except json.decoder.JSONDecodeError:
            accounts = []

        for account in accounts:
            if account['username'] == username:
                print("Username already exists. Please choose a different one.")
                return

        accounts.append({'username': username, 'password': password})
        f.seek(0)
        json.dump(accounts, f, indent=4)
        f.truncate()

    print("Registration successful!")


def account_management():
    choice = input("Enter '1' to login or '2' to register: ")

    if choice == '1':
        login()
    elif choice == '2':
        register()
    else:
        print("Invalid choice.")


account_management()


