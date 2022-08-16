from time import sleep as wait

userInfo = {
    "Player",
    "Player_Tag",
    "Player_Guild",
    "Player_Username",
    "Player_Enemy"
}


userInfo.remove("Player_Enemy")

print("Loading Script..")
wait(5)
print("Script Loaded!")
wait(2)
print("Loading Terminal..")
wait(7)
print("Terminal Loaded!")
wait(2)
print("Loading User Info..")
wait(6)
print("Player User Loaded!")
wait(2)
print("Loading kDocs Assets..")
wait(5)
print("kDocs Assets Loaded!")
wait(2)
print("Loading Files..")
wait(6)
print("Files Loaded!")
wait(2)
print("Connecting to C:Drive..")
wait(10)
print("C:Drive has been connected!")
wait(2)
print("Connecting Terminal With Computer Files..")
wait(12)
print("Terminal has connected with Files!")
wait(2)
print("Connecting..")
wait(6)
print("Connection has been successfull!")
wait(3)
securityTrial1 = input("Please enter your password to continue: ")

if securityTrial1 == "1helesa": #Change your password to another password, this is just the default password.
    print("Checking output..")
    wait(5)
    print("Login Complete! Welcome to kDocs! You can now go to app.py to run code.")
else:
    print("Checking output..")
    wait(5)
    print("Login Imcomplete. ")
    wait(2)
    securityTrial2 = input("Please try again: ")
    if securityTrial2 == "1helesa": #Change your password to another password, this is just the default password.
        print("Checking output..")
        wait(5)
        print("Login Complete! Welcome to kDocs! You can now go to app.py to run code.")
    else:
        print("Checking output..")
        wait(5)
        print("Login Imcomplete.")
        wait(2)
        securityTrial3 = input("Please try again: ")
        if securityTrial3 == "1helesa": #Change your password to another password, this is just the default password.
            print("Checking output..")
            wait(5)
            print("Login Complete! Welcome to kDocs! You can now go to app.py to run code.")

        else:
            print("Checking output..")
            wait(5)
            print("Login Imcomplete, please run the file to try again.")

