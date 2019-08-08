# Exclusive Network
# Demonstrates logical operators and compound conditions

print("\tExclusive Computer Network")
print("\t\tMembers only!\n")

security = 0

username = ""
while not username:
    username = input("Username: ")

password = ""
while not password:
    password = input("Password: ")

if username == "19lakeaustin" and password == "191073495":
    print("Welcome, Austin.")
    security = 5
elif username == "Jake" and password == "Rome":
    print("Yo what's up bro.")
    security = 4
elif username == "Tejas" and password == "Chawla":
    print("Bojas, hows it going?")
    security = 3
elif username == "guest" or password == "guest":
    print("Welcome guest.")
    security = 1
else:
    print("Login failed. Access Denied.")

input("\n\nPress the enter key to exit.")
