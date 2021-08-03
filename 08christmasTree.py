
#get tree heigh
tree_height = int(input("Enter Christmas tree height:"))
number_of_spaces = tree_height - 1
number_of_spaces_last_line = number_of_spaces
number_of_hashes = 1
#create new line for tree height
for i in range(0,tree_height):
    #print spaces before hashes
    for j in range(0,number_of_spaces):
        #end = " " is the syntax for printing in same line
        print('',end = " ")
    number_of_spaces = number_of_spaces - 1
    #print hashes and increase number of hashes by 2 for each line
    for k in range(0,number_of_hashes):
        print('#',end = "")
    number_of_hashes = number_of_hashes + 2
    print('')
#this is for the stem
for l in range(0,number_of_spaces_last_line):
    print('',end = " ")
print('#')
    
