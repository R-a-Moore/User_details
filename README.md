# Instructions for User_Details

1. create method which gets all variables (first_name, age, address, etc), using the `input()` function, and the `print()` function.
2. then call to a function which uses a for loop to check through each character in the address string, using the `.isdigit()` function to check if the current character in the string is a digit, if so it is concatenated onto a variable which is used to store all of the discovered integers.
3. Once complete with the for loop, return the value of the integers found.
4. using the `print()` function, display the user details, using `,` and `+` between strings.

## How to Create a .gitignore file

.gitignore files allow you to have a directory where git will not attempt to interact with when you are bashing in a pycharm project. 

To make a .gitignore file all you need to do is right-click anywhere on your project explorer in pycharm, create a new blank file and name it `.gitignore`.

## Concatenating & Casting

In python you may need to merge two separate sentences together into one. This is called concatenating. There are two methods for this;
- `,`
- `+`
adding either of these between texts or variables will concatenate them together.

When programming you may also need to turn one datatype into another, for example a string into an integer or vice versa. You can do this with `str("you data/variable")`. Note that you can replace the "str" with any data type that you want to cast the data to.

Additionally, you may want to slice a string. This is presenting a specific portion of your string, for example;
```commandline
my_string = "hello i have a string"
print(myString[-5]
```
This will present 5th character (starting from 0), in the string starting from right to left.

Alternately, if you want to present a left/right portion of a string;
```commandline
my_string = "hello i have a string"
print(myString[:5]
```
Note that you can place the colon `:` anywhere within the square brackets, switching which side of the ratio is being cut.

## Collections

In python (and other programming languages), you can create variables which contain multiple pieces of data. These are known as lists.

To create a list in python you need to use `[]` encapsulating the multiple data you want to make. For example:

```shopping_list = ["eggs", "milk", "croissants", "apple juice", "bell peppers"] # list```

You can use a for each loop to present each item, like this:
```commandline
for item in shopping_list: # for each loop to print each item in list
    print(item)
```
Or you can just print it out like normal, which will print the entirel ist:
```commandline
print(shopping_list)
```

If you want to get the type of data and the length of the list:

```commandline
print(type(shopping_list))# find out the type of shopping list
print(len(shopping_list))# find out the length of shopping list
```

If you want to add an item or remove an item from a list:

```commandline
shopping_list.append("a reason to live") # how to add to our shopping list
shopping_list.remove("croissants") # how to remove from a list
print(shopping_list)
```

You can also make lists hold multiple different types of data, as such: 
```commandline
mixed_list = [1, 5, 3, "two", "things", False, 3.14] # you can make lists with different data types in them
print(mixed_list)

```
If you want to use slicing in lists, it looks like this:
```
# slicing up lists
print(mixed_list[1:5]) # 3 : 5
```
Using the same `[:]` and/or `[-0]` functions, you can grab sub-arrays or individual peices of the list.

## DoR

## DoD