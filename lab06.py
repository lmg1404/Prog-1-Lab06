def print_menu():
    print("Menu")
    print("------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

def encoder(insert):
    new = ""
    for char in insert:
        val = int(char)
        val += 3
        new += str(val)
    return new

def decoder(yao):
    pass

def main():
    stored = ""
    while True:
        print_menu()

        option = input("Please enter an option: ")

        if option == "1":
            insert = input("Please enter you password to encode: ")
            stored = encoder(insert)
            print("You password has been encoded and stored!\n")
        elif option == "2":
            pass
        elif option == "3":
            break
        else:
            print("Please enter a valid option!")

if __name__ == "__main__":
    main()