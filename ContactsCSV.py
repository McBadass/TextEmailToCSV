__author__ = 'McBadass'

# Change this to file location
fileName = "D:\Documents\contacts.txt"

fileToRead = open(fileName, 'r').readlines()
fileToRead = fileToRead[0].split(";")
contacts = []


def clean_up(string):  # Removes unnecessary symbols from a single string
    string = string.replace("\'", "")
    string = string.replace("<", "")
    string = string.replace(">", "")
    string = string.rstrip()
    string = string.lstrip()
    return string


for items in fileToRead:
    if "<" in items:  # If there is a full name and email address
        items = items.split("<")  # Split up name and email
        if "," in items[0]:  # If full name contains a comma, meaning last-first
            fullName = items[0].split(",")
            if len(fullName) == 2:
                fullName[0], fullName[1] = fullName[1], fullName[0]
                items[0] = fullName[0] + fullName[1]
            else:  # More than 1 comma
                print("Too many commas!")
                SystemExit

            for i in items:
                i = clean_up(i)
                contacts.append(i)
        else:  # Name does not contain comma
            for i in items:
                i = clean_up(i)
                contacts.append(i)

    else:
        items = clean_up(items)
        contacts.append("")
        contacts.append(items)

outFile = open("D:\Documents\exportedContacts.csv", 'w')

outFile.write("Full Name, Email\n")
x = 0
while x < len(contacts):
    outFile.write(contacts[x] + "," + contacts[x+1] + "\n")
    x += 2
outFile.close()