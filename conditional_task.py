#Task: Read a number between 1-10 and display it in words
#The task is solved in two ways:

#Way1:The Noob's Way
'''
num=eval(input("Enter Your Number between 1-10: "))

if num==1:
    print("One")
elif num==2:    
    print("Two")
elif num==3: 
    print("Three")
elif num==4:
    print("Four")
elif num==5:
    print("Five")
elif num==6:
    print("Six")
elif num==7:
    print("Seven")
elif num==8:
    print("Eight")
elif num==9:
    print("Nine")
elif num==10:
    print("Ten")
elif num not in [1,2,3,4,5,6,7,8,9,10]:
    print("Number not in range, exiting")
else:
    print("Wrong Input!!! Exiting")

#Way2- The expected way:
#Solvig the task using List and Dictionary

num=[1,2,3,4,5,6,7,8,9,10]
word={1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten'}
input_num=eval(input("Enter your number between 1-10: "))

if input_num in num:
    print(word.get(input_num))
else:
    print("Number not in range, exiting")

'''