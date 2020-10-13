#Creted by Pooja
#On 5 March 2020
#Implementation of library usefull data collection using string manipulation in python.
books = {}
borrowers = {}
checkouts = [] 
x="""Books
APM-001~Advanced Potion-Making
GWG-001~Gadding With Ghouls
APM-002~Advanced Potion-Making
DMT-001~Defensive Magical Theory
DMT-003~Defensive Magical Theory
GWG-002~Gadding With Ghouls
DMT-002~Defensive Magical Theory
Borrowers
SLY2301~Hannah Abbott
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2306~Malcolm Baddock
SLY2307~Marcus Belby
SLY2308~Katie Bell
SLY2309~Sirius Orion Black
Checkouts
SLY2304~DMT-002~2019-03-27
SLY2301~GWG-001~2019-03-27
SLY2308~APM-002~2019-03-14
SLY2303~DMT-001~2019-04-03
SLY2301~GWG-002~2019-04-03
EndOfInput"""
nextline = x.strip()
while nextline.find("Books") < 0:
    nextline = x.strip()
nextline = x.strip()
while nextline.find("Borrowers") < 0:
    (accession_number,title) = nextline.split('~')
    books[accession_number] = title
    nextline = x.strip()
nextline = x.strip()
while nextline.find("Checkouts") < 0:
    (username,fullname) = nextline.split('~')
    borrowers[username] = fullname
    nextline = x.strip()
nextline = x.strip()
while nextline.find("EndOfInput") < 0:
    (username,accession_number,due_date) = nextline.split('~')
    checkoutline = due_date+"~"+borrowers[username]+"~"+accession_number+"~"+books[accession_number]
    checkouts.append(checkoutline)
    nextline = x.strip()
for checkoutline in sorted(checkouts):
    print(checkoutline)
