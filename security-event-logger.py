#Lochlan Greenhill
#Task2: Security Event Logger


#get the security event log 
def get_security_event():
    return input("Please Enter the security event message: ")


def main() -> None:
    security_event = get_security_event()

    # Check for failed event
    failed_event = "Yes" if "failed" in security_event.lower() else "No"
    print(f"Failed event: {failed_event}")

    # Check for login event
    login_event = "Yes" if "login" in security_event.lower() else "No"
    print(f"Login event: {login_event}")

    # look for an ip address by looking at a group of text that begins and ends with a number and is atleast 5 characters long ]
    ip_address = None
    for word in security_event.split():
        if len(word) >= 5 and word[0].isdigit() and word[-1].isdigit():
            ip_address = word
            break


    print(f"ip address: {ip_address}")


    # Display warning messages based on events
    if failed_event == "Yes":
        print("Warning: A failed security event was detected.")
    if login_event == "Yes":
        print("Login activity detected.")
    
    if failed_event == "Yes" and login_event == "Yes":
        print("Action: Investigate the failed login attempt")


if __name__ == "__main__":
    main()