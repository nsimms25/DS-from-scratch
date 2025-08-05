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

random_num = random.randrange(10)
#print(random_num)
#Output: 6
#Explantion: random number from range(10)

random_nums = random.randrange(3, 6)
#print(random_nums)
#Output: 4
#Explanation: random number from range(3, 6)

range_one_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(range_one_to_ten)
#print(range_one_to_ten)
#Output: [9, 4, 6, 10, 8, 1, 3, 5, 7, 2]
#Explanation: random shuffle of list in place. 

one_friend = random.choice(["alice", "bob", "john"])
#print(one_friend)
#Output: bob
#Explanation: make a random choice of given list. 

"""
Regular Expressions
"""
import re

re_examples = [
    not re.match("a", "cat"),
    re.search("a", "cat"),
    not re.search("c", "dog"),
    3 == len(re.split("[ab]", "carbs")),
    "R-D-" == re.sub("[0-9]", "-", "R2D2")
]
#print(re_examples)
#Output: [True, <re.Match object; span=(1, 2), match='a'>, True, True, True]
#Explanation: re.match is True if the start of a string matches, 
# re.search checks any part for a match.

"""
Zip
"""
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
#print([pair for pair in zip(list1, list2)])
#Output: [('a', 1), ('b', 2), ('c', 3)]

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
#print(letters)
#print(numbers)
#Output: ('a', 'b', 'c') and (1, 2, 3)
