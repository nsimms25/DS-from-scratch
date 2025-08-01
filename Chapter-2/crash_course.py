"""
Chapter 2 is a Python Crash Course.
"""

names = ["Alice", "Bob", "Charlie", "Debbie"]

"""
# not Pythonic
for i in range(len(names)):
    print(f"name {i} is {names[i]}")

# also not Pythonic
i = 0
for name in names:
    print(f"name {i} is {names[i]}")
    i += 1
"""
# Pythonic
for i, name in enumerate(names):
    value = True
    #print(f"name {i} is {name}")

"""
Randomness
"""
import random
random.seed(34)

four_uniform_randoms = [random.random() for _ in range(4)]
#print(four_uniform_randoms)
#Output: [0.5289353829404123, 0.5857468547498617, 0.8433262052335756, 0.8986446412645931]
#Explanation: uniform number between 0 and 1.

