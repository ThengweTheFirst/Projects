from xml.dom import UserDataHandler
from datetime import date
import sys
 

def user_details():
    """
    Prompt user input
    """
    # Allowing the user to input their first name.
    first_name = input("Insert first name ").lower()
    # Check if the user input is valid.
    while first_name.strip() == "":
        # Checking if the is any input. if the isn't any.
        print("Invalid first name.")
        # then allow the user to try again.
        first_name = input("Insert first name ").lower()
    while first_name.isdigit():
        # Checking if the user input is a number . if so
        print("Invalid first name.")
        # Then allow the user to try again.
        first_name = input("Insert first_name ").lower()
        # Check if the user didn't repeat the same mistake
        if first_name.isdigit():
            print("Invalid first name. Please try again.")
            first_name = input("Insert first_name ").lower()
            if first_name.isdigit():
                print("Invalid user input")
                sys.exit()
            else:
                pass
        else:
            pass
    while first_name.isalpha():
        # Checking if the user input is an alphabet. if true we check the length of the user input.
        if len(first_name) == 1:
            first_name = first_name + "oo"
        elif len(first_name) == 2:
            first_name = first_name + "o"
        else:
            pass
        break

    # Allowing the user to insert their last name.
    last_name = input("Insert last name ")
    # Checking if the user input is valid.
    while last_name.strip() == "":
        print("Invalid last name.")
        last_name = input("Insert last name ")
    while last_name.isdigit():
        print("Invalid last_name.")
        last_name = input("Insert last name ")
        if last_name.isdigit():
            print("Invalid last_name.")
            last_name = input("Insert last name ")
            if last_name.isdigit():
                print("Invalid last name.")
                sys.exit()
            else:
                pass
        else:
            pass
    while last_name.isalpha():
        if len(last_name) == 1:
            last_name = last_name + "oo"
        elif len(last_name) == 2:
            last_name = last_name + "o"
        else:
            pass
        break

    # Allowing the user to insert their cohort year.
    cohort = input("Insert cohort year ")
    # Checking if the user input is valid.
    while cohort != str(date.today().year):
        print("Invalid cohort year.")
        cohort = input("Insert cohort year ")
        if cohort != str(date.today().year):
            print("Invalid cohort year.")
            cohort = input("Insert cohort year ")
            if cohort != str(date.today().year):
                print("Invalid cohort year.")
                cohort = input("Insert cohort year ")
                if cohort != str(date.today().year):
                    print("Invalid cohort year.")
                    quit()
                else:
                    pass
            else:
                pass
        else:
            pass
        
        break

    # Allowing the user to input their campus.
    final_campus = input("Insert campus ").lower()
    # Creating a dictionary which shows available options for campus.
    campus = {
        "JHB": "Johannesburg",
        "DBN": "Durban",
        "CPT": "Cape Town",
        "PHO": "Phokeng"
        }
    # Checking if the user input is valid.
    if final_campus == "jhb":
        final_campus = campus["JHB"]
    elif final_campus == "dbn":
        final_campus = campus["DBN"]
    elif final_campus == "cpt":
        final_campus = "Cape town"
    elif final_campus == "pho":
        final_campus = campus["PHO"]
    else:
        print("Invalid campus")
        # Giving the user a second chance.
        final_campus = input("Insert campus ")
        if final_campus.lower() == "jhb":
            final_campus = campus["JHB"]
        elif final_campus.lower() == "dbn":
            final_campus = campus["DBN"]
        elif final_campus.lower() == "cpt":
            final_campus = "Cape town"
        elif final_campus.lower() == "pho":
            final_campus = campus["PHO"]
        else:
            print("Invalid campus")
            sys.exit()

    print(f"First name: {first_name.capitalize()}\nLast name: {last_name.capitalize()}")
    print(f"Cohort Year: {cohort}\nFinal Campus: {final_campus}")
    print(f"Final username:\n{create_user_name(first_name, last_name, cohort, campus, final_campus) }")
    

def create_user_name(first_name, last_name, cohort, campus, final_campus):
    # Generating a username and returning it.
    username = first_name[-3:] + last_name[:3] + user_campus(campus, final_campus) + str(cohort)
    print(username)
    print("The follow is the username format\n last three letters of the first name")
    print("first three letters of the last name\n the campus abbreviation\n and the cohort year at the end")
    # To check if the username is correct.
    check = input("Is your username correct: y/n")
    if check != "y" or "yes":
        # Allowing the user to insert the correct username.
        final_username = input("Insert correct username")
    else:
        final_username = username
    return final_username


def user_campus(campus, final_campus):
    # Creating a list with keys from the dictionary campus.
    campus = ["JHB", "DBN", "CPT", "PHO"]
    # Validating the keys so that they can appear in the generated username.
    if final_campus == "Johannesburg":
        final_campus = campus[0]
    elif final_campus == "Durban":
        final_campus = campus[1]
    elif final_campus == "Cape town":
        final_campus = campus[2]
    elif final_campus == "Phokeng":
        final_campus = campus[-1]
    else:
        pass
    
    return final_campus


if __name__ == '__main__':
    user_details()
    
