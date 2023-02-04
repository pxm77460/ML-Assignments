n = 5 # Initialising n with 5 to print the patterns

#Upper Triangle

# Looping through the range upto n =5 and every time incrementing the index by one.
for i in range(n):  
    for j in range(i+1): # incrementing the index by 1
        print("*", end='') # This will print the star
    print() # This will give new line

#Lower Triangle
# Looping from the last index to get the max and subtracting it -1 to get print next value.
for i in range(n):
    for j in range(n-i-1): # Subtracting the index by 1
        print("*", end='')
    print()  # This will give new line