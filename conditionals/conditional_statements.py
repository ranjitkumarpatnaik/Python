#If,else,elif conditions:

usr_str=input("Enter your string: ")
usr_cnf=input("Do you wnat to convert it to title format yes/no : ")

if usr_cnf=='yes':
    print(usr_str.title())
elif usr_cnf=='no':
    print(usr_str)
else:
    print('Wrong Input!!! Exiting')