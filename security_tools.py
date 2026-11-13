#Lochlan Greenhill
#Task5: Reusable Cyber Security Utilities using User-Defined Modules


import string
import random 



#password validator function that checks if the input password meets certain security criteria.
def password_validator(password):
    # Check for minimum length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
    # Check for variety
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    if not (has_upper and has_lower and has_digit and has_symbol):
        return False, "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one symbol."
    
    return True, "Password is valid."

#ip address validator function that checks if the input is a valid IPv4 address.
def ip_address_validator(ip_address):
    # Remove unnecessary spaces from the input
    ip_address = ip_address.strip()  
    # Check for exactly three periods/dots
    if ip_address.count('.') != 3:
        return False, "Invalid IP address format. An IP address must contain exactly three periods."
    
    # Split the IP address into octets
    octets = ip_address.split('.')
    
    # Check if all numbers extracted between periods/dots are less than 256 and more than or equal to 0 (value should be between 0 and 255).
    for octet in octets:
        if not octet.isdigit() or not (0 <= int(octet) <= 255):
            return False, "Invalid IP address format. Each octet must be a number between 0 and 255."
    
    return True, "IP address is valid."

#strong password generator function that creates a random password that meets the security criteria.
def generate_strong_password() -> str:
    # Generate a strong random password of length between 10 and 16 characters
    length = random.randint(10, 16)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password



