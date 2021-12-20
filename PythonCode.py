import re
import string

filename = "CS210_Project_Three_Input_File.txt"     #assign the input file name
writeFile = "frequency.dat"                         #assign the output file name
f = open(filename, "r")                             #open and reads input data file
w = open(writeFile, "w")                            #open and writes to output file
data = f.read()                                     #read input file
list_of_items = data.split()                        #split the data into individual items & store them in a list
frequency = {}                                      #dictionary to store item:frequeny
        
#Method to return a list which contains each items and their quanities in the list
def get_frequency_of_each_item():

    #Calculating the quantity
    for item in list_of_items:
        frequency[item] = frequency.get(item,0)+1 
        
    return_string = "" 

    #Appending data to return string
    for item,freq in frequency.items():
        return_string += item + ": " + str(freq) + '\n' 

    #Write to frequency file
    w.write(return_string)
    #Print
    print(return_string)
               
#Method to returns a string which contains a specific item and its quantity 
def get_frequency_of_single_item(item_name):

    #Sets the input to capitalized first letter and lower case rest no matter the input
    item_name = item_name.capitalize()

    for item in list_of_items:
        frequency[item] = frequency.get(item,0)+1 
    
    #if statement if given item is present in the string
    if item_name in frequency:  
        print("Qty of " + item_name + " sold: ", end="")
        return frequency[item_name]

    #else statement if there is no match item
    else:
        print("Qty of " + item_name + " sold: ", end="")
        return 0
        
#Method to return a histogram which contains each items and their quanities in the list.   
def display_histogram():

    for item in list_of_items:
        frequency[item]= frequency.get(item,0)+1
        
    ans=""

    #appending item, '*' no.of times the item occures and aligning ':' for a unform look
    for item,freq in frequency.items():
         ans += '%15s' % item + ": " +  '*'* freq + '\n'
    
    w.write(ans)
    print(ans)

    
