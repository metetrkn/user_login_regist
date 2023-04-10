from time import sleep
import secrets
import string
from os import getcwd

# Flag to keep the program running until closed by the user
key = True

while key:
    # Prompt user to choose an option: login, register or exit
    user_choose = input("""\t\t!Welcome!
Please type:
1\t\t ==> To login
2\t\t ==> Register New User
any button\t ==> To exit\n
""")

    # Read existing accounts from the accounts.txt file, can be changed based on data location
    with open(getcwd() + "/accounts.txt") as accounts:
        account_text = accounts.read()
        each_user = account_text.splitlines(False)  # Separate each user's information into a list
        print(each_user)

    # Option: Login
    if user_choose == "1":
        # Prompt user to enter their username and password
        userName = input("\nEnter your username\t:")
        password = input("Enter your password\t:")
        print()

        # Concatenate username and password
        entre = userName + " " + password

        # Check if the entered username and password match any in accounts.txt
        if entre in each_user:
            print("\nWelcome", userName)
            print("*"*30)
            sleep(2)
            key = False
        else:
            print("Wrong username or password, please try it again!\n\n")

    # Option: Registration
    elif user_choose == "2":
        # Prompt new user to enter their username
        new_user_name = input("\nPlease enter user name\t:")

        # Prompt new user to choose between an automated password or a custom one
        custom_defualt_password = input("\nPlease type 'd' to create an automated password\notherwise type anything else\t:")

        # Generate an automated password
        if custom_defualt_password.lower() == "d":
            # Define the alphabet
            letters = string.ascii_letters
            digits = string.digits
            special_chars = string.punctuation
            alphabet = letters + digits + special_chars

            # Set password length
            pwd_length = 8

            # Generate password string
            new_user_password = ''.join(secrets.choice(alphabet) for _ in range(pwd_length))

            # Print the new password for the user
            print("\nYou new automated password is\t:", new_user_password, "\n\n")

        # Create a custom password
        else:
            new_user_password = input("\nInput your custom password\t:")

        # Save the new user's information to accounts.txt
        new_account = new_user_name + " " + new_user_password
        with open(getcwd() + "/accounts.txt", "a") as n_accounts:
            n_accounts.write("\n" + new_account)

    # Option: Exit
    else:
        print("\nExiting...\n")
        print("*"*30)
        sleep(2)
        key = False