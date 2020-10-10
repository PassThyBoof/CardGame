import json
import os


wins = 1


def write_json_file(data):
    with open('users.json', 'w') as users_file_dump:
        json.dump(data, users_file_dump, indent=4)


def read_json_file():
    with open("users.json") as users_file:
        data = json.load(users_file)
    return data


def valid_username():
    looping = True
    username = ""
    print("Username can only be between 4 and 24 characters")
    while looping:
        username = input("Enter a username :")
        if 4 <= len(username) <= 24:
            if os.stat("users.json").st_size > 0:
                data = read_json_file()
                if username == data.get(username, {"": ""}).get("username"):
                    print("Username[{0}] taken, choose a different one".format(username))
                else:
                    looping = False
            else:
                looping = False
        else:
            print("Username[{0}] invalid".format(username))
    print("Your username is {0}".format(username))
    return username


def valid_password():
    print("Password can only be between 8 and 32 characters")
    password = input("Enter a  password :")
    while not 8 <= len(password) <= 32:
        print("Password did not fit requirements")
        password = input("Enter a new password :")
    return password


def sign_up():
    print("******************* Sign in ********************")
    username = valid_username()
    password = valid_password()
    user_write = {username: {"username": username, "password": password, "wins": wins}}
    if os.stat("users.json").st_size == 0:
        write_json_file(user_write)
    else:
        data = read_json_file()
        data.update(user_write)
        write_json_file(data)
    print("")


def login():
    print("******************** Login *********************")
    username = input("Enter your username :")
    password = input("Enter your password :")
    if os.stat("users.json").st_size == 0:
        print("Error no users in the database, signup then login")
        sign_up()
    else:
        data = read_json_file()
        user = data.get(username, {"none": "none"})
        if username == user.get("username", "none"):
            if password == user.get("password", "none"):
                return username
        else:
            print("Username[", username, "] or password was incorrect")
        print("")
        return False
