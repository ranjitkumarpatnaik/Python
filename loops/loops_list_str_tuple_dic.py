'''
For loop for string, list, tuple and dictionaries.
'''
my_str="Python"

print(my_str)
#To print each string in a separate line from a given string
#Method 1:
#print("\n".join(my_str))
#method 2: Using loop
for each in my_str:
    print(each)

my_list=[1,2,3,4,5]
list_tup=[(1,2),(3,4),(5,6),(7,8),(9,10)]

for f,s in list_tup:
    first_value=f
    print(first_value, type(f))

my_dict={'a':1,'b':2,'c':3,'d':4,'e':5}
for key,value in my_dict.items():
    print(key,value)
print(my_dict.items())

















