#Display given string at left/right/center of a line in a title format
import os
width=os.get_terminal_size().columns
given_str= input("Enter your string:  ")
print(f'\n{given_str.ljust(width).title()} \n{given_str.center(width).title()} \n{given_str.rjust(width).title()}')
