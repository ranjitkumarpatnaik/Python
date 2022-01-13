#functions with default arguments

def display(a=7):
    print("The value of a is: ",a)
    return None

display(4)
display(5)
#display() will give error because we are not passing any value
#To overcome such case where it is not dependent on the user input, we can assign the value of a. Eg: a=7
#In case you are not passing any value it will give default value as 7
display()

def add(a,b=0): #You have to pass the default argument at the end
    sum=a+b
    print("\nThe sum is: ",sum)
    return None

add(4,5)
add(5)
add(7) #here value of a is 7 but value of b is default that is 0, untill specified.


def working_on(user="root"):
    print(f"\nLogged in as: {user}")
    return None
working_on("admin") #specify user as admin,spiderman,ironman to check

#Functions with keyword based arguments

def user_arg(a,b):
    print(f"a= {a}")
    return None

user_arg(4,5) #a=4,b=5
user_arg(b=5,a=4) #We want a=4,b=5 always even when we change the positions



#Functions with variable length arguments:

def arg_var(*data): # adding * will make the code to accept multiple arguments
    for each in data:
        print(type(each))
    return None
arg_var(4)
arg_var(5,5)
arg_var("hi",4.5,7)

#functions with variable length keyword-based arguments
def key_arg(**karg):
    print("\n",karg)
    return None

key_arg(a=4,b=5)
key_arg(a=7,b=8,c=9)
key_arg(x=2,y="Hi",z=6.7,user="root") #inside the function we are getting the passed variable as a dictionary









