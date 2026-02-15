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

def add_div():
    while True:
        global new_div
        new_div = input("Division >>").title().strip()
        if new_div not in div:
            print("**INVALID DIVISION**\nChoose from:\n",all_div)
        else:
            print("**ADDED**")
            break

def add_id():
        new_id = input("ID >>").upper().strip().replace(" ","-")
        if new_id in id:
            print("**ID ALREADY EXISTS**\n**TRY AGAIN**")
            add_id()
        else:
            print("**ID ASSIGNED**\n",new_id)
            print("Are these details correct\n",f'{new_nam:20}',f'{new_rnk:15}',f'{new_div:15}',f'{new_id:10}')
            while True:
                v = input("Y/N>>")
                if v == "Y" or v == "y":
                    print("**MEMBER ADDED**")
                    nam.append(new_nam)
                    rnk.append(new_rnk)
                    div.append(new_div)
                    id.append(new_id)
                    break
                elif v =="N" or v == "n":
                    print("**DELETING DETAILS**")
                    add_mem()
                else:
                    print("**INVALID INPUT**")
                    add_id()
        
def add_mem():
    add_nam()
    add_rnk()
    add_div()
    add_id()

def rem_mem():
    while True:
        global id
        rem_id = input("Input valid ID\n>>").upper().strip().replace(" ","-")
        if rem_id in id:
            print("**ACCEPTED**\n**REMOVING**")
            indi = [i for i, value in enumerate(id) if value == rem_id]
            for index in sorted(indi, reverse=True):
                del nam[index]
                del rnk[index]
                del div[index]
                del id[index]
            print("**COMPLETED**\nUpdated list of members:\n")
            init_data()
            break
        else:
            print("**INVALID**\nChoose from existing ID's:\n",id)
