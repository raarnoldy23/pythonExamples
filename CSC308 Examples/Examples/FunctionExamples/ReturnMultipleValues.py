
def main():
    first_name, last_name = name()
    print("Welcome! ", first_name, last_name)


def name(): 
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return first, last


main() 
