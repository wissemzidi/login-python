from functions import inputName, checkName, checkPwd, signingUp
import json

# ======= Main function ======= #
def main():
    # opening files
    with open("./names_data.json", "r") as f:
        NAMES_DATA = json.load(f)
    with open("./users_data.json", "r") as f:
        USERS_DATA = json.load(f)
    usersNames = NAMES_DATA["names"]
    users = USERS_DATA

    # inputs
    userName = inputName()

    if checkName(userName, usersNames):
        salt = USERS_DATA[userName]["salt"]
        is_logedin = False
        while not is_logedin:
            user_pwd = str(input("your password please : "))
            if checkPwd(userName, salt, user_pwd, users):
                is_logedin = True
                print("Logged In successfully ;)")
            else:
                print("wrong password")
                if input("do you want to exit Y/N : ").upper() in {"Y", "YES", "OK"}:
                    exit()
    else:
        print("This user Name was not found")
        is_singUp = str(input("Do you want singUp Y/N :"))
        if is_singUp.upper() == "Y" or is_singUp.upper() == "YES":
            signingUp(userName, NAMES_DATA, USERS_DATA)
    pass


# ========= execution ======== #
if __name__ == "__main__":
    main()
