
#python allows to assing multiple values

x,y,z = "orange", "Banana", "Mango"
print(x)
print(y)
print(z)

#one value to multiple variables
x=y=z= "Orange"
print(x)
print(y)
print(z)

#Unpack Collection
#If you have a collection of values in a list, tuple etc.
#  Python allows you to extract the values into variables. This is called unpacking.

fruits =["apple","orange","banana"]
x,y,z = fruits
print(x)
print(y)
print(z)