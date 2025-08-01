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
