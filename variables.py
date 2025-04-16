#VARIABLES
# Variables: are containers that store data values


#(1) Creation of variables
name = "Ravi"
age = 23
print(name)
print(age)


''' (2) Casting: To specify the datatype for a variable
in python we can do it by casting'''
age = float(23) #now age= 23.0
print(age)
age=str(23) #now age="23"(string)
print(age)


# (3) type() : To get the type of variable
print(type(name))
print(type(age))

''' 
(4) Rules for python variables:
    (1) Variables must start with letter or by underscore.
    (2) A variable should only contain alpha-numeric or underscore character's.'
    (3) Variable names are case sensitive.
    (4) Variable names cannot be any keywords in python.
'''

''' 
(5) MultiWord Variable names:
    (1)CamelCase: except the first each word start with a capital letter.
    Eg: programmingLanguage = "Python"

    (2)PascalCase: each word start with capital letter.
    Eg: ProgrammingLanguage = "Python"

    (3)SnakeCase: Each word is seperated by an underscore.
    Eg: programming_language = "Python"
'''

#(6) Multiple variables in single line
c1,c2,c3 = "India","England", "Japan"
print(c1)
print(c2)
print(c3)

#6(i) Assigning same value to multiple variables
x1=x2=x3=18
print(x1)
print(x2)
print(x3)

#(7) Unpacking a collection
continents = ["Asia", "SouthAmerica", "Africa"]
ct1,ct2,ct3 = continents
print(ct1)
print(ct2)
print(ct3)

#(8) Output Variable: you can use + operator or (variable seperated by comma) to combine multiple variables
print(ct1,ct2,ct3)
print(ct1+ct2+ct3) # no space between variables

#Combining string and integer with + compiler throws an error
age=23
name="ravi"
print(name+age)# error as age is integer and name is string.

# So best way to combine variables without errors is by using ","
print(age,name)