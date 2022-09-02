import json
import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

select = input("Select version: 1 or 2: ")

if select == "1":
    data = '''
    {
        "name" : "Joe",
        "phone" : {
            "type" : "intl",
            "number" : "+1 734 303 4456"
        },
        "email" : {
            "hide" : "yes"
        }
    }'''

    info = json.loads(data)
    print("Name:", info["name"])
    print("Hide:", info["email"]["hide"])

elif select == "2":
    data = '''
    [
        { "id" : "001",
        "x" : "2",
        "name" : "Joe"
        } , 
        { "id" : "009",
        "x" : "7",
        "name" : "Chuck"
        }
    ]'''

    info = json.loads(data)
    print('User count:', len(info))

    for item in info:
        print("Name", item["name"])
        print("Id", item["id"])
        print("Attribute", item["x"])

else:
    print("Not a valid selection")