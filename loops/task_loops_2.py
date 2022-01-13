#Working with for loop
'''
usr_str= input("Enter your string: ")
index=0
for each in usr_str:
    print(f"{each} --> {index}")
    index=index+1
'''
import os
req_path=input("Enter your required path: ")

if os.path.isfile(req_path):
    print(f"The given path is: {req_path} is a file. Please pass only directory path")
else:
    fnd=os.listdir(req_path)
    if len(fnd)==0:
        print("The given path is empty")
    else:
        req_ext=input("Enter your required extension: ")
        ext_file=[]
        for each in fnd:
            if each.endswith(req_ext):
                ext_file.append(each)
        if len(ext_file)==0:
            print(f"No files found with the: {req_ext} extension")
        else:
            print(f"The require files are: {ext_file}")
        