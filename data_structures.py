'''
* Data structures are used to store a collection of data.
* There are four types of built-in data structures.
        1) List  []
        2) Tuple ()
        3) Dictionary {} with key value pair
        4) Set {}
'''
''' LIST DATA STRUCTURE '''
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
