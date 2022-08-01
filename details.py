def get_user_details():
    print("Hello! Please fill in the following...")
    print("first name: ")
    first_name = input()
    print("middle name: ")
    middle_name = input()
    print("last name: ")
    last_name = input()
    print("age: ")
    age = int(input())
    print("address: ")
    address = input()
    print_user_details(first_name, age, address, get_housenum(address))

def print_user_details(name, age, address, housenumber):
    print("Hello", name + "!\n\nYou are", str(age), "years old \n\nAnd live in", address, "Your house number is", housenumber)

def get_housenum(address):
    print("Original String : " + address)
    number = ""
    for instance in address:
        if instance.isdigit():
            number = number + instance
    return number

get_user_details()

