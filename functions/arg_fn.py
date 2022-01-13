#Functions with arguments and return value

#additions of two numbers
def get_addition(a,b): #Parameters/positional arguments
    result=a+b
    #print(f"The sum of two numbers is {a} and {b} is {result}")
    return result #returning result to main()
def get_multi(a,b):
    result=a*b
    return result

def main():
    a=eval(input("Enter your 1st number: "))
    b=eval(input("Enter your 2nd number: "))
    result=get_addition(a,b) #arguments, sending (a,b) values to the above functions
    multi=get_multi(a,b) 
    print(f"The sum of two numbers is {a} and {b} is {result} \n and their product is {multi}")
    return None
#print(result)

main()