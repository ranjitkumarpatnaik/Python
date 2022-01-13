'''
#Basic Operations on strings
name= "Ranjit"
age = 100
passion= "Something random"
print(f'my name is: {name} \nmy age is: {age} \nmy passion is: {passion}')



#Case conversion
string="Python STRiNg"
lower_case=(string.lower())
print(string.lower())
print(string.upper())
print(lower_case)


#Boolean result operation on strings
my_string = "Hello"
print(my_string.startswith('K'))
print(my_string.startswith('H'))
print(my_string.endswith('p'))
print(my_string.islower())
print(my_string.isupper())
#print(dir(my_string)) to know the operations that can be performed on my_strings



#join and centeroperations
a='python'
b="-".join(a)
c="*".join(a)
d="\n".join(a)
print(f'{b} \n{c} \n{d}' )
print("\t".join(a))



#center: after the varibale pass ".center(value)"
my_string1 = "python"
my_string2 = "python scripting"
my_string3 = "string operations"
print(f"{my_string1.center(30)}\n{my_string2.center(35)}\n{my_string3.center(40)}")



#strip and split operations
#strip will remove the extra spaces or unwanted characters,numbers etc from starting or ending. 
a="python    "
b="PyThOn"
c="Python232"
print(f"{a.strip()} \n{b.strip('n')} \n{c.strip('2')} \n{a.strip('pyth')}")
#Split operation will split the string/variable into list operator
d="python is easy to learn and it is very popular"
print(d.split('is'))
print(d.split())



#count,index and find operations on strings
a="python is easy and it is a popular language"
print(f"counting perticular character : {a.count('is')} \n{a.count('i')}")
print(f"checking the index:  \n{a.index('p')} \n{a.index('p',1)} \n{a.index('p',25)}")
print(f"using find instead of index: {a.find('e',1)}")

'''









