# Storing the input data in listdata variable.
listdata =[1,2,3,3,3,3,4,5]
print("Sample List: ", listdata) # Printing the given sample list

# Creating a function by taking list input: 
def convertToList(listdata):
    return list(set(listdata))  # Using set() getting unique elements and using list() converting to list. 

# Calling the method and sending the list as input and priting the uniue list

print("Unique List: ", convertToList(listdata))  