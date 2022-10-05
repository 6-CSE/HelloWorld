# Python3 code to demonstrate working of
# Scramble strings in list
# using list comprehension + sample() + join()
from random import sample

# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# Scramble strings in list
# using list comprehension + sample() + join()
res = [''.join(sample(ele, len(ele))) for ele in test_list]

# printing result
print("Scrambled strings in lists are : " + str(res))
