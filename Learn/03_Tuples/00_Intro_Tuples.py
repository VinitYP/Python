# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Which is written inside " ( ) "

tup = ("Mango", "Bananas", "Apple")
print(tup)

"""
    Same as list but here tuples can't change, update 
    1. but operation like len, del can successfully executed
"""
print(len(tup))
del tup
print(tup)
