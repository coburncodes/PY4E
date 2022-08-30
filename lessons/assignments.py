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
    elif number == "6":
        c6()
    elif number == "7":
        c7()
    elif number == "8":
        c8()
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

def c4():
    print("Chapter 4: Functions\n")
    input("When prompted, input hours and rate to calculate pay.\nThis calculation will include overtime at time and a half.\nPress enter to continue...\n")
    hrs = input("Enter Hours: ")
    h = float(hrs)
    rate = input("Enter Rate: ")
    r = float(rate)
    p = computepay(h, r)
    print("Pay", p)

def computepay(h, r):
    if h <= 40:
        value = h * r
    else:
        ot_hrs = float(h % 40)
        ot_pay = ot_hrs * r * 1.5
        reg_pay = 40 * r
        value = reg_pay + ot_pay
    return value

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

def c6():
    print("Chapter 6: Strings\n")
    text = "X-DSPAM-Confidence:    0.8475"
    print("Uses string methods find() and slice()\nto extract number from the following text:")
    print(text, "\n")
    input("Press enter to continue...\n")
    start = text.find(":")
    str = text[slice(start + 1, len(text))]
    stripped = str.strip()
    num = float(stripped)
    print(num)

def c7():
    print("Chapter 7: Files\n")
    print("When prompted, input name of file within current directory.\nFunction finds each line that begins with \"X-DSPAM-Confidence\"\nThen, the function returns the average of all these values.\n")
    input("Press enter to continue...\n")
    fname = input("Enter file name: ")
    try:
        fh = open(fname)
    except:
        print("Could not open file.")
        quit()
    total = 0
    count = 0
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        else:
            idx = line.find(":")
            x = slice(idx + 1, len(line))
            num = line[x].strip()
            n = float(num)
            total += n
            count += 1
    try:
        avg = total / count
    except:
        print("Operation failed. Try again.")
        quit()
    print("Average spam confidence:", avg)

def c8():
    print("Chapter 8: Lists\n")
    x = input("Select an exercise: 8.4 or 8.5\n")
    if x == "8.4":
        x8_4()
    elif x == "8.5":
        x8_5()
    else:
        print("Input either 8.4 or 8.5.")

def x8_4():
    print("When prompted, input name of file within current directory.\nFunction sorts each word in file.\n")
    input("Press enter to continue...\n")
    fname = input("Enter file name: ")
    try:
        fh = open(fname)
    except:
        print("File could not be opened")
        quit()
    lst = list()
    for line in fh:
        words = line.split()
        for word in words:
            if not word in lst:
                lst.append(word)
    lst.sort() 
    print(lst)

def x8_5():
    print("When prompted, input name of file within current directory.\nFunction parses email addresses from each line.\n")
    input("Press enter to continue...\n")
    fname = input("Enter file name: ")
    if len(fname) < 1:
        fname = "mbox-short.txt"
    try:
        fh = open(fname)
    except:
        print("Could not open file")
        quit()
    count = 0
    for line in fh:
        if line.startswith("From "):
            x = line.split()
            print(x[1])
            count += 1   
    print("There were", count, "lines in the file with From as the first word")


main()