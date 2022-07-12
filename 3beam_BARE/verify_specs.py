# Sherry Wong
# This code verifies that all .txt files requested by 
# specs.txt exist in the current directory.

import os

myfiles = os.listdir()
specs = open('specs.txt')
for item in specs:
    item = item.strip() #remove trailing newline
    if("/" in item): 
        item = item.split('/')[1]
    if(".txt" in item):
        if not(item in myfiles):
            print(item + "\t NOT FOUND")
        else:
            print(item + "\t found")
print("Finished.")
