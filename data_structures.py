'''
* Data structures are used to store a collection of data.
* There are four types of built-in data structures.
        1) List  []
        2) Tuple ()
        3) Dictionary {} with key value pair
        4) Set {}

### LIST DATA STRUCTURE ###

my_list=[1,3,4,"python",5,7,8.3,5.0,5] #List is a combination of data

print(my_list,type(my_list))
print(my_list[1:5])
print(my_list[:])
print(my_list[3][3])
my_list[0]=63-3
print(my_list)
#print(dir(my_list))
count_5 = my_list.count(5)
print(count_5)

my_list.append(56) #it will append 56 at the end of the list
my_list.insert(1,29) #insert will place "29" at the index "1"
print(my_list)


### TUPLES ###
#How to define tuple

empty_tuple=()
my_tuple=(3,4,5)
#print(my_tuple)

#Tuple to boolean conversion

bool_empty_tuple = bool(empty_tuple)
bool_my_tuple = bool(my_tuple)
print(bool_empty_tuple)
print(bool_my_tuple)
my_tuple = (3,4,5,[7,8,9],10,11)
print(my_tuple)

#Accessing Tuple
print(my_tuple[3][1])

#Modifying a tuple
my_tuple[3][2]= 321
#my_tuple[1] = 654 cannot modify the values or item in a tuple but can change the list inside the tuple
print(my_tuple)

x=5,6,7 #adding a , converts a int data to a tuple
print(x,type(x))


### DICTIONARY ###

my_dict= {'fruit':'apple','animal':'lion','bird':'eagle',1:'one','two':2}
# disctionaries are always written in key value pairs, and in  {}

#Accessing a value from a dictionary
print(my_dict)
print(my_dict["fruit"])
print(my_dict.get('animal'))
print(my_dict.get('Three'))  
#This is the best way to get the key, as it wont throw error if the key is not present. It will return 'None'

#Adding a new key:value
my_dict['three']=3
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(dir(my_dict))


### Set Data Structure ###

my_set = {11,18,17,6,5,3,7,4,9,8}
print(my_set)
#printing a set will always produce the result in a order.
#It will only print the unique data and the duplicates will be removed by default.
#print(dir(my_set))

'''










