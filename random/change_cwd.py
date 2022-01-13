#Execption handling, changing pwd.
#How to change current working directory in python?

'''import os
req_path=input("Enter your required path: ")
print("The current directory is: ",os.getcwd())
#Try block and except for exception handling
try:
    os.chdir(req_path)
    print("New path is: ",os.getcwd())
except FileNotFoundError:
    print("File not found")
except NotADirectoryError:
    print("Given path is a file path, cannot change pwd")
except PermissionError:
    print("You dont have access for the path")
except Exception as e:
    print(e)
'''

############ USING FUNCTIONS ################
import os
def main():
    req_path=input("Enter your required path: ")
    print("The current directory is: ",os.getcwd())
#Try block and except for exception handling
    try:
        os.chdir(req_path)
        print("New path is: ",os.getcwd())
    except FileNotFoundError:
        print("File not found")
    except NotADirectoryError:
        print("Given path is a file path, cannot change pwd")
    except PermissionError:
        print("You dont have access for the path")
    except Exception as e:
        print(e)
    return None

if __name__=="__main__":
    main()


