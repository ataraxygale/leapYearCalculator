#input year to determine if it's a leap year or not
try:
    year = int(input("Input a Year: "))
except ValueError:
    print("Invalid input: Please enter a valid number integer year")

#now runs only after verifying input
else:
    if year % 4 != 0:
       print("This is a common year")
    elif year % 100 != 0:
        print("This is a leap year! *frog noises*")
    elif year % 400 != 0:
        print("This is a common year")
    else:
        print("This is a leap year! *frog noises*")






























