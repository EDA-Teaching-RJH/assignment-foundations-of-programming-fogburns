nam = ["James T. Kirk","Spock","Troi","Worf","Jean-Luc Picard"]
rnk = ["Admiral","Commander","Captain","Commander","Leiutenant"]
all_rnk = ["Admiral","Captain","Leiutenant","Commander","Ensign"]
div = ["Command","Science","Command","Councelling","Security"]
all_div = ["Command","Science","Councelling","Security"]
id = ["NCC-1701-D","NCC-4682","NCC-0193-D","NCC-5138","NCC-1934-S"]
tbl = []
import re

def init_data():
    tbl.clear()
    for i in range(len(nam)):
        row = [nam[i],rnk[i],div[i],id[i]]
        tbl.append(row)
    print(f"{'Name':20} {'Rank':15} {'Division':15} {'ID':10}")
    for row in tbl:
        print(f"{row[0]:20} {row[1]:15} {row[2]:15} {row[3]:10}")

def new_user():
    while True:
        global user_nam
        user_nam = str(input("Enter your full name >>")).title().strip()
        if not re.match("^[A-Za-z\\s]*$", user_nam):
            print("Incorrect input\n**TRY AGAIN**")
        elif len(user_nam) > 20:
            print("Maximum 20 characters\n**TRY AGAIN**")
        else:
            print("**Accepted**")
            return user_nam

def add_nam():
    print("Enter members details:")
    while True:
        global new_nam
        new_nam = input("Full name >>").title().strip()
        if not re.match("^[A-Za-z\\s]*$", new_nam):
            print("Incorrect input\n**TRY AGAIN**")
        elif len(new_nam) > 20:
                print("Maximum 20 characters\n**TRY AGAIN**")
        else:
            print("**Accepted**")
            break

def add_rnk():
    while True: 
        global new_rnk
        new_rnk = input("Rank >>").title().strip()
        if new_rnk not in all_rnk:
            print("**INVALID RANK**\nChoose from: \n",all_rnk)
        else:
            print("**ADDED**")
            break