'''
====range() function====
========================
It is a built in funchtion, which generates range of only integers as list.

syntax: range(start,stop,step)
    3-arguments ===> By default start=0, step=required intervals
'''
my_list=[1,2,3,"mango",4,5,6,7,"apple",8,9,10,11,12,13,14,"banana",15,16,17,18,19,20,21]

'''
print(len(my_list)) #to find the length of my_list
print(range(len(my_list))) #Range of index values of my_list
print(list(range(len(my_list)))) #To convert the range values to list and print
'''

for each in range(len(my_list)):
    print(f"Index --> {each}  Value --> {my_list[each]}")
    
    '''
    Taking each variable's index from range of my_list and
    that index variable I am Substituting with the help of my list,
    so that I am getting the value of index 0.....23
    '''