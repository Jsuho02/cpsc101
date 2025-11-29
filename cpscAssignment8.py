# main()- first function requesting decimal or hexadecimal input
def program_start():
    
    while True:
        choice = input("Will you be entering a decimal or hexa decimal value? (d/h): ")

        if choice == 'd':
            num_str = input("Please enter your decimal number: ")
            try:
                num = int(num_str)
                print(f"Your number is {num}.")
                return choice, num_str
            except ValueError:
                print("That is not a valid decimal number!")


