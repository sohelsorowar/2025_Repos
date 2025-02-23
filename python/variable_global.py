

#Global Variables
#Variables that are created outside of a function 
# (as in all of the examples in the previous pages) are known as global variables.

#create a variable outside of a function and use it inside of the function

x = "Fantastic"

def myfunc():
    print(" Python is " + x)
myfunc()


#creating inside and outside variable in function
print("creating inside and outside variable in function  ")

a="awesome"

def my_function():
    a="fantastic"
    print("indise of function: python is "+a)
my_function()

print("outside of function: python is "+a)


#crate global variable inside of a function
print(" \ncrate global variable inside of a function\n")

def my_function():
    global c
    c = "fantastic inside of function"
my_function()
print(c)