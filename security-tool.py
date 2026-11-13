#Lochlan Greenhill
#Task1: Security Tool


#ask user to select a security function
def getfunction ():

    #try ask user to select a security function 1-4
    try:
        selection = int(input("""Welcome
Please select a security function (1-4)
    1. Security Event Counter
    2. Brute-Force Simulation
    3. Login Authentication
    4. Exit
    """))
    except ValueError:
        print("Please enter a valid input in number form.")
        return getfunction()

    #make sure user input is between 1 and 4
    if selection < 1 or selection > 4:
        print("Invalid input. Please enter a number between 1 and 4.")
        return getfunction()

    else:
            return selection   

    return (selection)

#security event counter function 
def security_event_counter():
    #create a variable to store the correct password and counters for correct and incorrect passwords
    correct_password = "password123"
    correct_count = 0
    incorrect_count = 0

    #ask user to enter the password 10 times and count the number of correct and incorrect passwords
    for i in range(10):
        password = input("Please enter the password: ")
        if password == correct_password:
            correct_count += 1
        else:
            incorrect_count += 1
    #print the results
    print(f"Correct passwords: {correct_count}")
    print(f"Incorrect passwords: {incorrect_count}")
    if correct_count > 0:
        percentage = (incorrect_count / 10) * 100
        print(f"The percentage of incorrect passwords is : {percentage}%")
        if percentage > 50:
            print("ALERT: The password was incorrect more than 50% of the time.")

    return()

#brute-force simulation function
def brute_force_simulation():
    #create a variable to store the correct password and a counter for the number of attempts
    correct_password = "password123"
    max_attempts = 10
    attempts = 0
    
    #ask user to enter the password until they get it correct or they reach the maximum number of attempts
    while attempts < max_attempts:
        password = input("Please enter the password: ")
        attempts += 1
        #check if the password is correct and print the appropriate message 
        if password == correct_password:
            print("Access granted.")
            break
        else:
            print(f"Incorrect password. You have {max_attempts - attempts} attempts left.")

    return()

#login authenticator function
def login_authentication():
    correct_username = "admin"
    correct_password = "password123"
    max_attempts = 3
    attempts = 0
    #ask user to enter the username and password until they get it correct or they reach the maximum number of attempts
    while attempts < max_attempts:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        attempts += 1
        #check if the username and password are correct and print the appropriate message
        if username == correct_username and password == correct_password:
            print("Correct Login .")
            break
        else:
            print(f"Login failed. You have {max_attempts - attempts} attempts left.")
    #if the user reaches the maximum number of attempts, print a message that the account is frozen for 24 hours
    if attempts == max_attempts:
        print("Account is frozen for 24 hours due to too many failed login attempts.")

    return()

#exit function
def exit_program():
    #print a message that the program is exiting and exit the program
    print("Exiting the program. Goodbye!")
    exit()





#main program 
if __name__ == "__main__":
    while True:
        selection = getfunction()

        if selection == 1:
            security_event_counter()
        elif selection == 2:
            brute_force_simulation()
        elif selection == 3:
            login_authentication()
        elif selection == 4:
            exit_program()  
    

