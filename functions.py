from hashlib import sha512
from random import randint
import string
import json
import re


def signingUp(user_name, NAMES_DATA, USERS_DATA):
    letters = string.ascii_letters + str(string.digits)
    salt = "".join(letters[randint(0, len(letters) - 1)] for i in range(12))
    print("signing Up ......")
    userPassword, userEmail = inputPwd(), inputEmail()
    # hashing pwd
    hashedPwd = sha512(f"{userPassword}{salt}".encode()).hexdigest()
    # writing usersNames
    NAMES_DATA["names"].append(user_name)
    with open("./names_data.json", "w") as a:
        json_data = json.dumps(NAMES_DATA)
        a.write(json_data)

    # writing usersData
    write_data = {"salt": salt, "Password": hashedPwd, "Email": userEmail}
    USERS_DATA.__setitem__(user_name, write_data)
    with open("./users_data.json", "w") as a:
        json_data = json.dumps(USERS_DATA)
        a.write(json_data)
    print("signing Up successfully completed ;) ")


def checkPwd(name, salt, pwd, users):
    if users[name]["Password"] == sha512(f"{pwd}{salt}".encode()).hexdigest():
        return True
    else:
        return False


def checkName(name, usersNames):
    if name in usersNames:
        return True
    else:
        return False


def inputName():
    Name = str(input("Name : "))
    while not verifyName(Name):
        print("This name isn't valide! Try another name")
        Name = str(input("Name : "))
    return Name


def inputEmail():
    email = str(input("Email : "))
    emailRe = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,6}$"
    while not re.search(emailRe, email):
        print("!! email not valid")
        email = str(input("Email : "))
    return email


def inputPwd():
    pwd = str(input("Password : "))
    while verifyPwd(pwd) == False:
        pwd = str(input("Password : "))
    return pwd


def is_easyPwd(pwd):
    with open("easy_passwords.json", "r") as f:
        data = json.load(f)
        easyPwd = data["passwords"]
    if pwd in easyPwd:
        return True
    else:
        return False


def verifyPwd(pwd):
    verify = True
    if len(pwd) < 6:
        print("your password is too short")
        return False
    if is_easyPwd(pwd):
        print("Your passwords is too easy! try another one")
        return False
    i = 0
    nbOfSpecials = 0
    while verify == True and i < len(pwd):
        if "A" <= pwd[i].upper() <= "Z" or "0" <= pwd[i] <= "9":
            i += 1
        elif pwd[i] in {"#", "_", "-", "."}:
            nbOfSpecials += 1
            i += 1
        else:
            verify = False
    if nbOfSpecials == 0:
        print("your password should have at least one special character")
        verify = False
    return verify


def verifyName(name):
    i = 0
    verify = True
    while i < len(name) and verify == True:
        if (
            "A" <= name[i].upper() <= "Z"
            or "0" <= name[i] <= "9"
            or name[i] in {"_", ".", "-", "#"}
        ):
            i += 1
        else:
            verify = False
    return verify
