def main():
    number = input("Chapter Number: ")
    if number == "2":
        c2()
    elif number == "3":
        c3()
    elif number == "4":
        c4()
    elif number == "5":
        c5()
    else:
        print("No assignments of that number found.")

def c2():
    print("Chapter 2: Variables, Expressions and Statements\n")
    x = input("Select an exercise: 2.2 or 2.3?\n")
    if x == "2.2":
        x2_2()
    elif x == "2.3":
        x2_3()
    else:
        print("Input either 2.2 or 2.3.")

def x2_2():
    input("When prompted, input your name for a greeting in the terminal.\nPress enter to continue...\n")
    name = input("Enter your name\n")
    print("Hello,", name)

def x2_3():
    input("When prompted, input hours and rate to calculate pay.\nPress enter to continue...\n")
    hrs = input("Enter Hours: ")
    rate = input("Enter Rate: ")
    try:
        fhrs = float(hrs)
        frate = float(rate)
    except (ValueError):
        print("Input a number for both hours and rate")
    pay = fhrs * frate
    print("Pay:", pay)

def c3():
    print("Chapter 3: Conditional Execution\n")
    x = input("Select an exercise: 3.1 or 3.3?\n")
    if x == "3.1":
        x3_1()
    elif x == "3.3":
        x3_3()
    else:
        print("Input either 3.1 or 3.3.")

def x3_1():
    input("When prompted, input hours and rate to calculate pay.\nThis calculation will include overtime at time and a half.\nPress enter to continue...\n")
    hrs = input("Enter Hours: ")
    h = float(hrs)
    rate = input("Enter Rate: ")
    r = float(rate)

    if h <= 40:
        pay = h * r
    else:
        ot_hrs = h % 40
        reg_pay = 40 * r
        ot_pay = ot_hrs * r * 1.5
        pay = ot_pay + reg_pay
    print(pay)

def x3_3():
    input("When prompted, input a decimal score between 0.0 and 1.0 for a grade.\nPress enter to continue...\n")
    score = input("Enter Score: ")
    s = float(score)
    if not s >= 0 or not s <= 1:
        print("Error")
    else:
        if s >= 0.9:
            print("A")
        elif s >= 0.8:
            print("B")
        elif s >= 0.7:
            print("C")
        elif s >= 0.6:
            print("D")
        else:
            print("F")

def computepay(h, r):
    if h <= 40:
        value = h * r
    else:
        ot_hrs = float(h % 40)
        ot_pay = ot_hrs * r * 1.5
        reg_pay = 40 * r
        value = reg_pay + ot_pay
    return value

def c4():
    print("Chapter 4: Functions\n")
    input("When prompted, input hours and rate to calculate pay.\nThis calculation will include overtime at time and a half.\nPress enter to continue...\n")
    hrs = input("Enter Hours: ")
    h = float(hrs)
    rate = input("Enter Rate: ")
    r = float(rate)
    p = computepay(h, r)
    print("Pay", p)

def c5():
    print("Chapter 5: Loops and Iterations\n")
    input("When prompted, input a number. To stop, type \"done\".\nThe function will return the highest and lowest numbers.\nPress enter to continue...\n")
    largest = None
    smallest = None
    while True:
        num = input("Enter a number: ")
        if num == "done":
            break
        try:
            n = int(num)
        except:
            print("Invalid input")
        if largest == None:
            largest = n
        if smallest == None:
            smallest = n
        if n > largest:
            largest = n
        elif n < smallest:
            smallest = n
    print("Maximum is", largest)
    print("Minimum is", smallest)


main()