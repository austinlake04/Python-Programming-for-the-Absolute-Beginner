# Trust Fund Buddy - Bad
# Demostrates a logical error

print(
"""
            Trust Fund Buddy
Totals your monthy spending so that your trust fund doesn't run out
(and you're forced to get a real job).

Please enter the requested, monthy costs. Since you're rich, ignore pennies and use only dollar amounts.

"""

car = input("Car Maintenance: ")
rent = input("Housing Costs: ")
insurance = input("Car/Health/Dental/Renter's: ")
gifts = input("Gifts: ")
food = input("Dining Out: ")
staff = input("Butlers, chefs, drivers, assistants, etc.: ")
games = input("Video Games: ")

total = car + rent + insurance + gifts + food + staff + games

print("\nGrand Total:", total)

input("\n\nPress the enter key to exit.")
