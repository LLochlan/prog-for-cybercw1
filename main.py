#Lochlan Greenhill
#Task5: Reusable Cyber Security Utilities using User-Defined Modules

import security_tools 

def main():
    # Ask the user to enter a pssword
    password = input("Enter a password: ")
    ip_address = input("Enter an IP address: ")

    # Validate the password
    is_password_valid, password_message = security_tools.password_validator(password)
    print(password_message)

    # Validate the IP address
    is_ip_valid, ip_message = security_tools.ip_address_validator(ip_address)
    print(ip_message)

    # Suggest a randomly generated strong password if the provided password is not strong
    if not is_password_valid:
        strong_password = security_tools.generate_strong_password()
        print(f"Suggested strong password: {strong_password}")

if __name__ == "__main__":
    main()


    