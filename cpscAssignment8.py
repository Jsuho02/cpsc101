# main()- first function requesting decimal or hexadecimal input
def program_start():
    
    while True:
        choose = input("Will you be entering a decimal or hexa decimal value? (d/h): ")

        if choose == 'd':
            num_str = input("Please enter your decimal number: ")
            num = int(num_str)
            print(f"Your number is {num}.")
        
    