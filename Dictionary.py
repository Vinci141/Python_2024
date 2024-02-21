'''
how to merge 2 dictionaries in python v3.9 and above
'''

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'e': 5, 'f': 6}

# one of the way is
d3 = d1 | d2
print(d3)

# alternative
d4 = d1.copy()
d4.update(d2)

print(d4)
