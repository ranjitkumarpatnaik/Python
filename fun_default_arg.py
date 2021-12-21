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