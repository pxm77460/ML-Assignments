# Storing the elements in the list with variable name my_list
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


n = len(my_list) # Finding the length using the length function

# Looping through the loop from the '1' index as it is odd index upto the total length
# mentioned '2' to skip the next index(positive index). to display odd index

for i in range(1, n, 2):
    print(my_list[i]) # prints the odd index.