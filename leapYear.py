
while True:
    #input year to determine if it's a leap year or not
    try:
        year = int(input("Input a Year: "))
    except ValueError:
        print("Invalid input: Please enter a valid number integer year\n")

    #now runs only after verifying input
    else:
        if year % 4 != 0:
           print(f"{year} is a common year\n")
        elif year % 100 != 0:
            print(f"{year} is a leap year! *frog noises*\n")
        elif year % 400 != 0:
            print(f"{year} is a common year\n")
        else:
            print(f"{year} is a leap year! *frog noises*\n")

    zero=input("Enter 0 to exit the program or any other key to continue\n")

    if zero == '0':
        exit()


