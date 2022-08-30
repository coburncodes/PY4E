def main():
    while True:
        number = input("Chapter Number: ")
        if number == "2":
            c2()
        elif number == "3":
            c3()
        elif number == "4":
            c4()
        else:
            print("No assignments of that number found.")
        break

def c2():
    while True:
        x = input("Which Exercise?\n")
        if x == "2.2":
            x2_2()
        elif x == "2.3":
            x2_3()
        else:
            print("Input either 2.2 or 2.3.")
        break
        
def x2_2():
    while True:
        name = input("Enter your name\n")
        print("Hello", name)
        break

def x2_3():
    while True:
        hrs = input("Enter Hours: ")
        rate = input("Enter Rate: ")
        fhrs = float(hrs)
        frate = float(rate)
        pay = fhrs * frate
        print("Pay:", pay)
        break

def c3():
    while True:
        x = input("Which Exercies?\n")
        if x == "3.1":
            x3_1()
            
        elif x == "3.3":
            x3_3()
            
        else:
            print("Input either 3.1 or 3.3.")
        break

def x3_1():
    while True:
        hrs = input("Enter Hours:")
        h = float(hrs)
        rate = input("Enter Rate:")
        r = float(rate)

        if h <= 40:
            pay = h * r
        else:
            ot_hrs = h % 40
            reg_pay = 40 * r
            ot_pay = ot_hrs * r * 1.5
            pay = ot_pay + reg_pay
            print(pay)
        break

def x3_3():
    while True:
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
        break

# Chapter 4 helper function
def computepay(h, r):
    if h <= 40:
        value = h * r
    else:
        ot_hrs = float(h % 40)
        ot_pay = ot_hrs * r * 1.5
        reg_pay = 40 * r
        value = reg_pay + ot_pay
    return value

# Chapter 4 function
def c4():
    hrs = input("Enter Hours:")
    h = float(hrs)

    rate = input("Enter Rate:")
    r = float(rate)
    p = computepay(h, r)

    print("Pay", p)

main()