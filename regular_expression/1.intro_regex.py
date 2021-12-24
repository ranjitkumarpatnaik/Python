'''What is Regular expression (RegEx)

    Regex is a procedure in any language to look for a specified
    pattern in a given text.

Pattern:    It is a sequence of characters, which reperesnts multiple
            string.
            Ex: 'i[st]' => is, it
                'python[23]' =>python2, python3

'''
my_str="Python is simple and it is easy"
#print(my_str.split("is"))
#print(my_str.split("it"))

import re #re module to use regex
print(re.split("i[st]",my_str)) #splitting the string from is, it







