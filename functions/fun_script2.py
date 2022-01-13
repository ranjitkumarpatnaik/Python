#Using fun_script1 in fun_script2

import fun_script1

def prod(a,b):
    print(f"The product is: {a*b}")
    return None

def main():
    x=10
    y=20

    prod(x,y)
    fun_script1.add(x,y) #calling addition function from script1
    fun_script1.sub(x,y) #calling substraction functions
    return None
    
if __name__=="__main__": #Name variable
    main()