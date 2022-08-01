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