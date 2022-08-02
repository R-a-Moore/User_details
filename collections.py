# Data Collections
## Lists, Tuples & Dictionaries

### Lists
# what are lists?
# corect syntax []
# lists are mutable (changeable)
# indexing same concept allies

shopping_list = ["eggs", "milk", "croissants", "apple juice", "bell peppers"] # list
for item in shopping_list: # for each loop to print each item in list
    print(item)

print(type(shopping_list))# find out the type of shopping list
print(len(shopping_list))# find out the length of shopping list

shopping_list.append("a reason to live") # how to add to our shopping list
shopping_list.remove("croissants") # how to remove from a list
print(shopping_list)

mixed_list = [1, 5, 3, "two", "things", False, 3.14] # you can make lists with different data types in them
print(mixed_list)
# slicing up lists
print(mixed_list[1:5]) # 3 : 5