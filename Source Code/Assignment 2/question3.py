# Storing input values in variable x
x = [23, 'Python', 23.98]
print(x) # prints the given data

type_values =[]  #Creating an empty list to store the types of data

# Looping through all the elements in 'x'
for i in range(len(x)): 
    type_values.append(type(x[i])) # Using append() function and type() function and  appending all the types to variable

print(type_values)