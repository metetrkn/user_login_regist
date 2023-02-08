from time import sleep

# keeps program work until closed by user
key = True

while key:
    user_choose = input("""\t\t!Welcome!
Plase type:
1\t\t ==> To login
2\t\t ==> Register New User
any button\t ==> To exit\n
""")

    # opening account.txt file
    with open("/home/mete/Desktop/accounts.txt") as accounts:
        # reading all accounts and saving them into variable
        account_text = accounts.read()

        # separating each user information into list
        each_user = account_text.splitlines(False)

    # option login
    if user_choose == "1":
        # promting user to input username
        userName = input("\nEnter your username\t:")

        # promting user to input password
        password = input("Enter your password\t:")
        print()
            
        # username and password who try to login
        entre = userName + " " + password

        # checking user information from accounts.txt
        if entre in each_user:
            print("\nWelcome", userName)
            print("*"*30)
            sleep(2)
            key = False
            break

        else:
            print("Wrong username or password, please try it again!\n\n")

    # option registration
    elif user_choose == "2":
        # promting new user to input username and password
        new_user_name = input("\nPlease enter user name\t:")
        custom_defualt_password = input("\nPlease type 'd' to create automated password\notherwise type anything else\t:")

        # generating automated passord
        if custom_defualt_password.lower() == "d":
            # necessary imports
            import secrets
            import string

            # define the alphabet
            letters = string.ascii_letters
            digits = string.digits
            special_chars = string.punctuation

            alphabet = letters + digits + special_chars

            # fix password length
            pwd_length = 8

            # generate a password string
            new_user_password = ''
            for i in range(pwd_length):
                new_user_password += ''.join(secrets.choice(alphabet))
            
            # printing out new password for user
            print("\nYou new automated password is\t:", new_user_password, "\n\n")

        # creating custom passwordd
        else:
            new_user_password = input("\nInput your custom password\t:")

        # new user account info
        account = new_user_name + " " + new_user_password

        # saving new users information into accounts.txt   
        with open("/home/mete/Desktop/accounts.txt", "a") as accounts:
            accounts.write("\n" + account)

    # option exit
    else:
        print("\nExiting...\n")
        print("*"*30)
        sleep(2)
        key = False
            

    











