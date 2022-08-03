# Data Collections
## Lists, Tuples & Dictionaries

### Lists
# what are lists? they are mutable (changeable)
# correct syntax []
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

# Tuples
# why? they are immutable
# Tuples (immutable) VS Lists (mutable)
# syntax for tuple ()
# use cases? (why would you want data to be unchangable?) place of birth, date of birth never change.

essential =  ("city", "DOB", "place of birth") # tuple example
print(essential) # printing typle
print(type(essential)) # printing type of tuple
print(essential[1]) # printing an index of a tuple
# essential[0] = "town" # this will throw and error. item assignment cannot occur with tuples. they are immutable.
mixed_tuple = ("city", 3, True) # you can have mixed tuples
print(mixed_tuple)

# Dictionaries
# syntax for dictionary/dict {}
# what is a dictionary? dictionaries can have all types of data collection
# dict work as "KEY : VALUE " pair with commas between the next pair

devops_student = { # dictionary example
    "key": "value",
    "name": "James",
    "Week" : 2, # you can make them mixed
    "Topic" : "tech",
    "Lesson names" : ["lists", "concatenating", "variables", "operators"]
}

print(devops_student) # printing dictioanry
print(devops_student["name"]) # printing individual keys from a dictionary, you must call the key
print(devops_student.keys()) # only print the keys
print(devops_student.values()) # only print the values

for item in devops_student: # you can use for each loops like this to print each key
    print(item)

devops_student.pop("name") # removes a key and its values from dictionary
del(devops_student["Week"]) # removes a key and its values from dictionary
devops_student["Lesson names"][1] = "casting" # reassigning an embedded lists value within a dictionary
print(devops_student)

# Control flow
## if, elif, else statements - conditional statements

weather = "sunny" # our dependent variable
if weather == "sunny": # starts by checking what the variable's value is
    print("you're gonna have a fun day!") # if it matches, it executes the code here
elif weather == "rainy": # if not, it will check this condition
    print("better bring an umbrella")
else:
    print("better start praying") # otherwise, if all other conditions aren't matched, this one will be executed

## psuedo coding
# writing code in a manner that both humans and machines can understand
# "write a story before you start filming a movie"






