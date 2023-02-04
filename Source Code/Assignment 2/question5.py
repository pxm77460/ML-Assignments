input ='The quick Brow Fox'  # Taking the give data to the input variable
#Creating caseCheck method by taking input as parameter:
def caseCheck(input):
    # Initialising the variable to store upper case and lower case
    upperCaseCount = 0
    lowerCaseCount = 0

    # Traversing through the loop for the input.
    for value in input:
        if(value.isupper()): # Using built in isUpper() checking the element is Upper case and increasing the count
            upperCaseCount += 1
        elif(value.islower()):# Using built in isLower() checking the element is Upper case and increasing the count
            lowerCaseCount += 1
    
    print("No. of Upper-case characters: ", upperCaseCount) # Printing the Upper Case Count
    print("No. of Lower-case Characters: ", lowerCaseCount) # Printing the Lower Case Count
  
caseCheck(input)

