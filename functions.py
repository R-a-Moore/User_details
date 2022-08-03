# what is a function?
# self encased code which can be called to and run independantly
# syntax Def 'name'():

def greet_user():
    print("welmcome", get_name())

def get_name():
    return input("please enter your name: ")

greet_user()


# create a function called add that takes 2 args as int
# add both values and display the result
def add(x,y): # takes in variables, checks if they're numbers, adds them
    if x.isdigit() and y.isdigit():
        print(int(x)+int(y))

add(input("please enter a number: "), input("please enter a number: ")) # calls add function with user inputed numbers to manipulate
