# Counter
# Demonstrates the range() function

print("Counting:")
for i in range(10):
    print(i, end="  ")

print("\n\nCounting in fives:")
for i in range(0, 50, 5):
    print(i, end="  ")

print("\n\nCounting backwards:")
for i in range(10, 0, -1):
    print(i, end="  ")

print("\n\nRepeating 'Hi!' 5 times:\n")
for i in range(5):
    print("Hi!")
    
input("\n\nPress the enter key to exit.")
