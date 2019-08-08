# Random Access
# Demonstrates string indexing

import random

word = 'index'

print('The word is: ', word, '\n')

high = len(word)
low = -len(word)
      
for i in range(10):
    position = random.randrange(low, high)
    print('word[', position, ']\t', word[position])

print('\n')
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])

print('\n')
print(word[-1])
print(word[-2])
print(word[-3])
print(word[-4])
print(word[-5])

input('\n\nPress the enter key to exit.')
