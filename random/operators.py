
 #Arithmetic Opertarors
a=8
b=2
c=a+b #Addition
d=a-b #Substraction
e=a*b #Multiplication
f=a/b #Division
g=a%b #Modulo:remainder
h=a//b #Floor Division:rounds off the value to the lower value
i=a**b #Exponential: finds the square
print(f'\n{c},\n{d},\n{e},\n{f},\n{g},\n{h},\n{i}')


#Assignment Operator
a=b
a+=b #a=a+b
a-=b #a=a-b
a*=b #a=a*b
a/=b #a=a/b
a%=b #a=a%b


#Comparision Operators
a=4
b=5
# Types of operators are >,<,==, !=,>=,<=


#Identity and Membership Operators
#identity operator is used to find the type of:class/type/object
#We have two type of operatos i.e is,is not
a=5
b=6
c='Hi'
print(type(a) is type(b))
print(type(a) is type(c))
print(type(a) is not type(b))

#Membership operator is used to validate the membership of a value
#operators in membership is 'in'
x=[4,5,6,7]
print(90 in x)
print(5 in x)


#Logical Operators: used to combine multiple conditions.
#Three types of logical operators: and, or, not

#And operator:It returns True if both the conditions are true.

a=3>1
b=[3,4,5]
c=1<3
d=3>3
print(a and 1 in b) #False because 3>1 is true but 1 is not a member of b. So False.

#Or operator returns true if either of the operand is true
print(a or c)
print(c or d)

#not operator interchange the logic based on requirement. Eg 1>2 is ffalse, but using not we can assign it True
a=1>2
print(a)
print(not a)







































