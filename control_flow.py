# if, elif, else

# loops - for, while loops
# why? don't repeat yourself, loops help us to ITERATE through data collections
# let's create a list to use for a loop to iterate through it

shopping_list = {"fruits", "milk", "cream", "bread","yogurt"}
print(shopping_list)
# print each item of the list as a list
for item in shopping_list: # for each loop iterates through list and prints each item
    print(item)
    if item == "bread": # checks if a particular item is in the list, then breaks out of the loop if it's true
        break

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
for book, content in library.items():
    print(book)
    print(content)
    print(book, content)

