# Trust Fund Buddy - Good
# Demonstrates type conversion

print(
"""
                    Trust Fund Buddy
Totals your monthly spending so that your trust fund doesn't run out
(and you're forced to get a real job).

Please enter the requested, monthly costs. Since you're rich, ignore pennies and use only dollar amounts.

"""
)

car = int(input("Car Maintenace: "))
rent = int(input("Housing Costs: "))
gifts = int(input("Gifts: "))
food = int(input("Dining Out: "))
staff = int(input("Staff (butlers, chefs, drivers, assistants, etc.): "))
games = int(input("Video Games: "))

total = car + rent + gifts + food + staff + games

print("\nGrand Total:", total)

input("\n\nPress the enter key to exit.")
