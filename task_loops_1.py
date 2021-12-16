#Read a directory path and identify all files and directories
#Standard imports
import sys 
import os 
path=input("Enter your directory path: ") #Taking user input by using input()
if os.path.exists(path): #Checking if the path exists or not
    fd=(os.listdir(path)) #saving the path to variable "fd"
else:
    print("Enter a valid path...")
    sys.exit() #If path is invalid, script will exit
print("\nFiles and Directories under the path are: ",fd)

#Fetching complete path
for each in (fd):
    fetchpath=os.path.join(path,each) #joining the file/dir to the path dynamically
    if os.path.isfile(fetchpath):
        print(f"\n{fetchpath} is a file")
    else:
        print(f"\n{fetchpath} is a directory")




