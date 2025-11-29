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

        elif choice == 'h':
            num_str = input("Please enter your hexadecimal number.")
            try:
                int(num_str,16)
                print(f"Your hexadecimal value is {num_str}")
                return choice, num_str
            except ValueError:
                print("That is not a valid hexadecimal number!")
        else:
            print("Please choose d for decimal or h for hexadecimal input!")

if __name__ == "__main__":
    program_start()

