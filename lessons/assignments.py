number = input("Chapter Number: ")

if number == "2":
    while True:
        x = input("Which Exercise?\n")
        if x == "2.2":
            name = input("Enter your name\n")
            print("Hello", name)
            break
        elif x == "2.3":
            hrs = input("Enter Hours: ")
            rate = input("Enter Rate: ")
            fhrs = float(hrs)
            frate = float(rate)
            pay = fhrs * frate
            print("Pay:", pay)
            break
        else:
            print("Input either 2.2 or 2.3.")

else:
    print("No assignments of that number found")