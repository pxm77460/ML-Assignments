it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}   # Creating a Set with it_companies names
A = {19, 22, 24, 20, 25, 26}  # Creating a Set with variable name 'A'
B = {19, 22, 20, 25, 26, 24, 28, 27} # Creating a Set with variable name 'B'
age = [22, 19, 24, 25, 26, 24, 25, 24]  # Creating a Set with values of ages
# Finding the Length of it_companies
print("Length of IT Companies: ", len(it_companies))
# Adding 'Twitter; it_companies using add()
it_companies.add('Twitter')
print("After Adding IT Companies: ", it_companies)
# Inserting multiple IT companies to the Set using update()
it_companies.update('IBM', 'Accenture', 'NVIDIA')
print("After Adding Multiple IT Companies: ", it_companies)
it_companies.remove('IBM')  # Removed IT company Accenture
print("After removing IT Company: ", it_companies)

#  What is the difference between remove() and discard()
# The main difference between remove() and discard() is that remove() will give an error if the elements does not exist in the set
# discard() will not give any error if the element not found. It will does nothing.

#  Joining sets A and B by using union()
C = A.union(B)
print("After joining A and B", C)

# Finding A intersection B using intersection()
print("Intersection: ", A.intersection(B))

# Finding A is Subset of B
print(A.issubset(B))  # True. A is Subset of B

#  Finding whether A and B  disjoint Sets
print(A.isdisjoint(B)) # False A and B are not Disjoint

# Joining  A with B and B with A using union()
A.union(B)
B.union(A)

# Finding the symmetric difference between A and B
print("Symmetric Difference:", A.symmetric_difference(B))

# Deleting Sets Completely using del keyword
del it_companies
del A
del B

# Converting ages to a Set
ages = set(age)
list_length = len(age)
set_length = len(ages)
# Displaying the lenghts of list and set
print("List Length: ", list_length)
print("Set Length: ", set_length)

# Comparing the length of the list and set.
if list_length == set_length:
    print("The lengths of list and set are equal")
else:
    print("The lengths of list and set are unequal because Set does contain duplicate values")

