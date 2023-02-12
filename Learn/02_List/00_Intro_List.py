# Lists are used to store multiple items in a single variable.
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], than [1], than [2] and so on etc.

shoplist = ["Mango", "Apple", "Grapes"]
print(shoplist)

# Accessing list from their indexes
print(shoplist[2])  # Grapes

# Getting from range 0 to till before 3
print(shoplist[0:3])

# Adding new element
shoplist.append("Bananas")
print(shoplist)

# Updating list
shoplist[0]="Cheery"
print(shoplist)

# Delete element from list
del shoplist[0]
print(shoplist)

# Combining two list
shoplist = ["Mango", "Apple", "Grapes"]
list = ["Carrot","Reddish"]
print(shoplist+list)



