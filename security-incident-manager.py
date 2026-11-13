#Lochlan Greenhill
#Task4: Security Incident Manager Using Dictionaries


#created a function to manage security incidents using dictionaries
def security_incident_manager():
    #create a dictionary containing a username, IP address, event type and risk level
    indident_dictionary = {"username": "user123", "ip_address": "192.168.50.1", "event_type": "Unauthorized Access", "risk_level": "High"}
    
    return indident_dictionary


#made a function to display the username and IP address from the dictionary
def display_username_ip(incident_dictionary):
    #display the username and IP address
    print("Username:", incident_dictionary["username"])
    print("IP Address:", incident_dictionary["ip_address"])


#made a function to add a new field called status to the dictionary
def add_status(incident_dictionary):
    #add a new field called status
    incident_dictionary["status"] = "Open"
    return incident_dictionary


#made a function to update the risk level of the incident
def update_risk_level(incident_dictionary, new_risk_level):
    #update the risk level
    incident_dictionary["risk_level"] = new_risk_level
    return incident_dictionary


#made a function to remove the status field from the dictionary
def remove_status(incident_dictionary):
    #remove the status field from the dictionary
    del incident_dictionary["status"]
    return incident_dictionary


#made a function to display all remaining keys and values in the dictionary
def display_remaining(incident_dictionary):
    #display all remaining keys and values
    for key, value in incident_dictionary.items():
        print(key + ":", value)


#made a function to display the total number of key-value pairs in the dictionary
def display_total_pairs(incident_dictionary):
     #display the total number of key-value pairs
     print("Total number of key-value pairs:", len(incident_dictionary))

#main function
if __name__ == "__main__":
    incident_dictionary = security_incident_manager()
    display_username_ip(incident_dictionary)
    incident_dictionary = add_status(incident_dictionary)
    incident_dictionary = update_risk_level(incident_dictionary, "Medium")
    incident_dictionary = remove_status(incident_dictionary)
    display_remaining(incident_dictionary)
    display_total_pairs(incident_dictionary)
