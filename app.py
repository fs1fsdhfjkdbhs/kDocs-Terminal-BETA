login = input("Please enter your password: ")


if login == "1helesa": #Change your password to another password, this is just the default password.
    print("Welcome to kDocs!")
else:
    login2 = input("Failed to login, please enter your correct password: ")
    if login2 == "1helesa": #Change your password to another password, this is just the default password.
        print("Welcome to kDocs!")
    else:
        login3 = input("Failed to login, please enter your correct password: ")
        if login3 == "1helesa": #Change your password to another password, this is just the default password.
            print("Welcome to kDocs!")
        else:
            print("Login failed, please try again by re-running the app.")

commandLine = input("∂ ")
cmdPRINT = "print"

if commandLine == cmdPRINT:
    cmdRESULT = input("Please enter what you want to print: ")
    if cmdRESULT == "":
        print("ERROR: Cannot print nothing. (ERROR CODE 1296)")
        print("Please re-run the script for another command.")
    else:
        print(cmdRESULT)
        print("Please re-run the script for another command.")
else:
    print("Invalid command, please re-run the script for another command.")
