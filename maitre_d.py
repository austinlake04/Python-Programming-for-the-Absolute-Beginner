# Maitre D'
# Demonstrates treating a value as a condition

print("Welcome to the Chateau D' Food")
print("It seems we are quite full this evening.\n")

money = int(input("How many dollars do you slip the Maitre D'? "))

if money != 0:
    print("Ah, right this way sir.")
else:
    print("The wait is about 2 hours. Is that ok?")

input("\n\nPress the enter key to exit.")
