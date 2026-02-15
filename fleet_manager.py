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

def up_rnk():
    up_id = input("Input valid ID\n>>").upper().strip().replace(" ","-")
    if up_id in id:
        index = id.index(up_id)
        print(f"**ACCEPTED**\nCurrent rank: {rnk[index]}")
        while True:
            new_rnk = input("What new rank do you want to assign?\n>>").capitalize().strip()
            if new_rnk in all_rnk:
                rnk[index] = new_rnk
                print("**COMPLETED**\nUpdated information:\n")
                init_data()
                break
            else:
                print("**INVALID RANK**\nChoose from:\n",all_rnk)
    else:
        print("**INVALID**\nChoose from existing ID's:\n",id)
        up_rnk()        

def search():
    while True:
        matches = []
        term = input("Search by term\n>>").strip()
        for i in range(len(nam)):
            if term.lower() in nam[i].lower():
                matches.append((nam[i], rnk[i], div[i], id[i]))
        if matches:
            print(f"**SEARCHING**\nShowing results for term: {term}")
            print(f"{'Name':20} {'Rank':15} {'Division':15} {'ID':10}")
            for match in matches:
                print(f"{match[0]:20} {match[1]:15} {match[2]:15} {match[3]:10}")
            break
        else:
            print("**NO MATCHES**")

def filter():
    while True:
        i_filter = []
        filter = input("Filter by division\n>>").strip()
        for i in range(len(div)):
            if filter.lower() in div[i].lower():
                i_filter.append((nam[i], rnk[i], div[i], id[i]))
        if i_filter:
            print(f"**SEARCHING**\nShowing results for division: {filter}")
            print(f"{'Name':20} {'Rank':15} {'Division':15} {'ID':10}")
            for match in i_filter:
                print(f"{match[0]:20} {match[1]:15} {match[2]:15} {match[3]:10}")
                menu()
        else:
            print("**INVALID**\nChoose from:\n",div)

def pay_roll():
    ad_p = int(rnk.count("Admiral"))*1500
    ad = rnk.count("Admiral")
    ca_p = int(rnk.count("Captain"))*1000
    ca = rnk.count("Captain")
    li_p = int(rnk.count("Lieutenant"))*850
    li = rnk.count("Lieutenant")
    co_p = int(rnk.count("Commander"))*750
    co = rnk.count("Commander")
    en_p = int(rnk.count("Ensign"))*500
    en = rnk.count("Ensign")
    total = ad_p+ca_p+li_p+co_p+en_p
    print("Each\nAdmiral - 1500 CR\nCaptain - 1000 CR\nLieuntenant - 850 CR\nCommander - 750\nEnsign - 500 CR")
    print("Total\n",ad,"Admiral(s)\n",ca,"Captain(s)\n",li,"Lieutenant(s)\n",co,"Commander(s)\n",en,"Ensign(s)\nTotal :",total)

def co_office():
    ca = rnk.count("Captain")
    co = rnk.count("Commander")
    print("Amount of officers;\nCaptain(s) -",ca,"\nCommander(s) -",co,"\nTotal :",co+ca)
