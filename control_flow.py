# if, elif, else

# loops - for, while loops
# why? don't repeat yourself, loops help us to ITERATE through data collections
# let's create a list to use for a loop to iterate through it

# shopping_list = {"fruits", "milk", "cream", "bread","yogurt"}
# print(shopping_list)
# # print each item of the list as a list
# for item in shopping_list: # for each loop iterates through list and prints each item
#     print(item)
#     if item == "bread": # checks if a particular item is in the list, then breaks out of the loop if it's true
#         break

# create a dictionary with 6 key value pairs
# use for loop to iterate through it
# print only keys
# print only values
# print key with matching value
library = {
    "maths" : "1+2=17",
    "science" : "gravitational physics",
    "religion" : "islam, buddhism, hinduism, rastafari",
    "sports" : "badminton",
    "music" : "drake, kanye, shiloh dynasty, lucky day",
    "eonomics" : "macro scale inflation"
}

for book, content in library.items(): # creates the key, value pair as variables in the for loop and iterates through the keys
    print(book) # prints the key
    print(content) # prints the value
    print(book, content) # prints the key, value pair

# use case of multiple conditions
# create a list with in values  1-4
# iterate through the list using for loop
# find 3 and print if found
# or list number greater than 3, print gone too far
# otherwise print too soon

numbers = [1,2,3,4] # list of numbers
for number in numbers: # loops through numbers checking for 3 is present, acts if so, if not, and if none
    if number == 3:
        print(number,": found")
    elif number < 3:
        print(number, ": gone too far!")
    else:
        print("too soon")


# While loops
# mostly used as a monitor rather than handling items
# similar to for loops, however keep going until a condition is met.


# iterate while number is less than 10
# print the number with message stating it's working
# print number with message stating it's working
# number + 1
number = 0

while number < 10: # iterates adding to a number until it equals 10
    print(f"It's working the number is {number}!")
    number += 1

user_prompt = True

while user_prompt: # checks if it must still prompt the user for a valid age input, print when satisfied.
    age = input("please enter your age: ")
    if age.isdigit() and int(age) < 117:
        print(f"your are {age} years old")
        user_prompt = False
