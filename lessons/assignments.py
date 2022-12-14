import re
import socket
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import json
import ssl
import sqlite3

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
    elif number == "9":
        c9()
    elif number == "10":
        c10()
    elif number == "11":
        c11()
    elif number == "12":
        c12()
    elif number == "13":
        c13()
    elif number == "15":
        c15()
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

def c9():
    print("Chapter 9: Dictionaries\n")
    print("Input file name when prompted.\nFunction returns the user who sent the most emails along with the number.\n")
    input("Press enter to continue...\n")

    name = input("Enter file:")
    if len(name) < 1:
        name = "mbox-short.txt"

    handle = open(name)
    emails = []
    counts = {}
    highest = 0

    for line in handle:
        if line.startswith("From "):
            x = line.split()
            emails.append(x[1])

    for email in emails:
        counts[email] = counts.get(email, 0) + 1

    for k, v in counts.items():
        if v > highest:
            highest = v
            winner = k

    print(winner, highest)

def c10():
    print("Chapter 10: Tuples\n")
    print("Input file name when prompted.\nFunction returns distribution by hour of the day for each of the messages.\n")
    input("Press enter to continue...\n")

    name = input("Enter file:")
    if len(name) < 1:
        name = "mbox-short.txt"

    handle = open(name)
    hours = []
    times = {}

    for line in handle:
        if line.startswith("From "):
            # Append to "hours" the first two digits of the fifth indexed word on the line
            hours.append((line.split()[5])[slice(2)])

    for hour in hours:
        times[hour] = times.get(hour, 0) + 1

    sorted_items = sorted(times.items())

    for item in sorted_items:
        print(item[0], item[1])

def c11():
    print("Chapter 11: Regular Expressions\n")
    print("Input file name when prompted.\nFunction returns sum of numbers within file.\n")
    input("Press enter to continue...\n")

    fname = input("Enter file name: ")
    if len(fname) < 1:
        fname = "regex_sum_1632431.txt"

    handle = open(fname)
    nums = []
    total = 0

    for line in handle:
        if re.search("[0-9]+", line):
            nums.append(re.findall("[0-9]+", line))

    for item in nums:
        for i in item:
            total += int(i)

    print(total)

def c12():
    print("Chapter 12: Network Programming\n")
    x = input("Select an exercise: 12.1, 12.2 or 12.3.\n")
    if x == "12.1":
        x12_1()
    elif x == "12.2":
        x12_2()
    elif x == "12.3":
        x12_3()
    else:
        print("Input either 12.1, 12.2 or 12.3.")

def x12_1():
    print("Input a webpage when prompted.\nDefault page: http://data.pr4e.org/intro-short.txt\nFunction retrieves data from webpage.\n")
    input("Press enter to continue...\n")

    page = input("Input a webpage. For default, press enter: ")
    if len(page) < 1:
        page = "http://data.pr4e.org/intro-short.txt"

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(("data.pr4e.org", 80))
    unencoded = "GET " + page + " HTTP/1.0\r\n\r\n"
    cmd = unencoded.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode())

    mysock.close()

def x12_2():
    print("Input a webpage when prompted.\nDefault page:\nhttp://py4e-data.dr-chuck.net/comments_1632433.html\nFunction sums numbers from webpage.\n")
    input("Press enter to continue...\n") 

    url = input("Input webpage. For default, press enter: ")
    if len(url) < 1:
        url = "http://py4e-data.dr-chuck.net/comments_1632433.html"

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("span")
    sum = 0

    for tag in tags:
        sum += int(tag.contents[0])

    print(sum)

def x12_3():
    print("Input a webpage when prompted.\nDefault page:\nhttp://py4e-data.dr-chuck.net/known_by_Fikret.html\nFunction follows URL trail to retrieve name.\n")
    input("Press enter to continue...\n") 

    url = input("Input webpage. For default, press enter: ")
    num = int(input("Input number of cycles: "))
    pos = int(input("Input position: ")) - 1
    names = []

    if len(url) < 1:
        url = "http://py4e-data.dr-chuck.net/known_by_Abdullah.html"

    cycle(url, num, pos, names)
    print(names[num - 1])

def cycle(url, num, pos, names):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")

    if num > 0:
        url = (tags[pos].get("href", None))
        num -= 1
        names.append(tags[pos].contents[0])
        cycle(url, num, pos, names)

    return names

def c13():
    print("Chapter 13: Using Web Services\n")
    x = input("Select an exercise: 13.1, 13.2 or 13.3.\n")
    if x == "13.1":
        x13_1()
    elif x == "13.2":
        x13_2()
    elif x == "13.3":
        x13_3()
    else:
        print("Input either 13.1, 13.2 or 13.3.")

def x13_1():
    print("Access XML document and sum the inner text of all count tags.\n")
    input("Press enter to continue...")

    url = input("Location: ")
    if len(url) < 1:
        url = "http://py4e-data.dr-chuck.net/comments_42.xml"
    print('Retrieving', url)

    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    tree = ET.fromstring(data.decode())
    results = tree.findall(".//count")
    counts = []

    for entry in results:
        counts.append(int(entry.text))

    print("Count:", len(results))
    print("Sum:", sum(counts))

def x13_2():
    print("Access JSON document and sum the inner text of all count tags.\n")
    input("Press enter to continue...")

    url = input("Enter location: ")
    if len(url) < 1:
        url = "http://py4e-data.dr-chuck.net/comments_42.json"
    print("Retrieving", url)

    uh = urllib.request.urlopen(url)
    data = uh.read()
    print("Retrieved", len(data), "characters")

    info = json.loads(data)
    counts = []

    for entry in info["comments"]:
        counts.append(int(entry["count"]))

    print("Count:", len(counts))
    print("Sum:", sum(counts))

def x13_3():
    print("Collect place id data from API\n")
    input("Press enter to continue...")

    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        address = input('Enter location: ')
        if len(address) < 1: break
        parms = dict()
        parms['address'] = address

        if api_key is not False: parms['key'] = api_key
        url = serviceurl + urllib.parse.urlencode(parms)
        print('Retrieving', url)

        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')

        js = json.loads(data)
        id = js["results"][0]["place_id"]
        print("Place id", id)

def c15():
    print("Chapter 15: Databases\n")   
    x = input("Select an exercise: 15.1, 15.2, 15.3, or 15.4.\n")
    if x == "15.1":
        x15_1()
    elif x == "15.2":
        x15_2()
    elif x == "15.3":
        x15_3()
    elif x == "15.4":
        x15_4()
    else:
        print("Input either 15.1, 15.2, 15.3, or 15.4.")

def x15_1():
    print("Create and populate table, then fetch hex from first row.\n")
    input("Press enter to continue...")

    conn = sqlite3.connect("ages.sqlite")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS ages (name VARCHAR(128), age INTEGER)")
    cur.execute("DELETE FROM ages")
    cur.execute("INSERT INTO ages (name,age) VALUES('Lucia', 26);")
    cur.execute("INSERT INTO ages (name,age) VALUES('Milos', 13)")
    cur.execute("INSERT INTO ages (name,age) VALUES('Demmi', 34)")
    cur.execute("INSERT INTO ages (name,age) VALUES('Mayra', 25)")
    cur.execute("INSERT INTO ages (name,age) VALUES('Olufunke', 18)")
    data = cur.execute("SELECT hex(name || age) AS X FROM ages ORDER BY X")

    conn.commit()
    print(data.fetchone())

    cur.close()
    
def x15_2():
    print("Create and populate table, then fetch hex from first row.\n")
    input("Press enter to continue...")

    conn = sqlite3.connect('counts.sqlite')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Counts')

    cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

    fname = input('Enter file name: ')
    if (len(fname) < 1): 
        fname = 'mbox.txt'

    fh = open(fname)
    for line in fh:
        if not line.startswith('From: '): 
            continue
        pieces = line.split()
        email = pieces[1]
        org = email.split("@")[1]
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (org,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                        (org,))
        conn.commit()

    sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

    for row in cur.execute(sqlstr):
        print(str(row[0]), row[1])

    cur.close()


def x15_3():
    print("Create and populate 4 tables with non-repeating entries in a database using iTunes XML file.\n")
    input("Press enter to continue...")
    conn = sqlite3.connect('trackdb.sqlite')
    cur = conn.cursor()

    # Make some fresh tables using executescript()
    cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;
    DROP TABLE IF EXISTS Genre;

    CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE
    );

    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY 
            AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    );
    ''')

    fname = input('Enter file name: ')
    if (len(fname) < 1):
        fname = 'Library.xml'

    # <key>Track ID</key><integer>369</integer>
    # <key>Name</key><string>Another One Bites The Dust</string>
    # <key>Artist</key><string>Queen</string>

    def lookup(d, key):
        found = False
        for child in d:
            if found:
                return child.text
            if child.tag == 'key' and child.text == key:
                found = True
        return None

    stuff = ET.parse(fname)
    all = stuff.findall('dict/dict/dict')
    for entry in all:
        if (lookup(entry, 'Track ID') is None): 
            continue

        name = lookup(entry, 'Name')
        artist = lookup(entry, 'Artist')
        album = lookup(entry, 'Album')
        count = lookup(entry, 'Play Count')
        rating = lookup(entry, 'Rating')
        length = lookup(entry, 'Total Time')
        genre = lookup(entry, 'Genre')

        if name is None or artist is None or album is None or genre is None: 
            continue

        cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES ( ? )", (artist,))
        cur.execute("SELECT id FROM Artist WHERE name = ? ", (artist, ))
        artist_id = cur.fetchone()[0]

        cur.execute("INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )", (album, artist_id))
        cur.execute("SELECT id FROM Album WHERE title = ? ", (album, ))
        album_id = cur.fetchone()[0]

        cur.execute("INSERT OR IGNORE INTO Genre (name) VALUES ( ? )", (genre,))
        cur.execute("SELECT id FROM Genre WHERE name = ? ", (genre, ))
        genre_id = cur.fetchone()[0]

        cur.execute("INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES ( ?, ?, ?, ?, ?, ? )", (name, album_id, genre_id, length, rating, count))

        conn.commit()

def x15_4():
    print("Retrieve string from JSON data based on query.\n")
    input("Press enter to continue...")

    conn = sqlite3.connect('rosterdb.sqlite')
    cur = conn.cursor()

    # Do some setup
    cur.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Member;
    DROP TABLE IF EXISTS Course;

    CREATE TABLE User (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name   TEXT UNIQUE
    );

    CREATE TABLE Course (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title  TEXT UNIQUE
    );

    CREATE TABLE Member (
        user_id     INTEGER,
        course_id   INTEGER,
        role        INTEGER,
        PRIMARY KEY (user_id, course_id)
    )
    ''')

    fname = input('Enter file name: ')
    if len(fname) < 1:
        fname = 'roster_data.json'

    # [
    #   [ "Charley", "si110", 1 ],
    #   [ "Mea", "si110", 0 ],

    str_data = open(fname).read()
    json_data = json.loads(str_data)

    for entry in json_data:
        name = entry[0]
        title = entry[1]
        role = int(entry[2])

        cur.execute('''INSERT OR IGNORE INTO User (name)
            VALUES ( ? )''', ( name, ) )
        cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
        user_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Course (title)
            VALUES ( ? )''', ( title, ) )
        cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
        course_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Member
            (user_id, course_id, role) VALUES ( ?, ?, ? )''',
            ( user_id, course_id, role ) )

        conn.commit()

    data = cur.execute('''SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
        User JOIN Member JOIN Course 
        ON User.id = Member.user_id AND Member.course_id = Course.id
        ORDER BY X LIMIT 1''')

    readable = data.fetchone()[0]
    print(readable)

    cur.close()


main()