#Lochlan Greenhill
#Task3: IP Address Validator using functions


#get the IP address from the user
def get_ip():
    ip_address = input("Enter an IP address: ")
    
        #remove unecessary spaces from the input
    ip_address = ip_address.strip()
    return (ip_address)

#validate the IP address
def validate_ip(ip_address):
    dot_count = False 
    range_count = False
    length_count = False

    #check for atleast 4 numbers in the IP address
    if len(ip_address) >= 4:
        length_count = True
   
    #check for exactly three periods/dots
    if ip_address.count('.') != 3:
        print("Invalid IP address format. An IP address must contain exactly three periods.")
        dot_count = False
    else:
            dot_count = True

   
    #Check if all numbers extracted between periods/dots are less than 256 and more than or equal to 0 (value should be between 0 and 255). 
    if ip_address:
            octets = ip_address.split('.')
    
    for octet in octets:
            if not octet.isdigit() or not (0 <= int(octet) <= 255):
                print("Invalid IP address format. Each octet must be a number between 0 and 255.")
                return    

            else:
                range_count = True

    return (dot_count, range_count, length_count)  

#display the results of the validation
def output_results(dot_count, range_count, length_count):
    if dot_count and range_count and length_count:
        print("Valid IP address.")
    else:
        print("Invalid IP address.")



if __name__ == "__main__":
    ip_address = get_ip()
    dot_count, range_count, length_count = validate_ip(ip_address)
    output_results(dot_count, range_count, length_count)