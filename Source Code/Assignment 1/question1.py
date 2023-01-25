ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]  # List containing 10 students ages
ages.sort()  # Sorting the list of ages in Ascending sorting order
print("Sorted Ages: ", ages)  # Displaying sorted ages
# Minimum Age
min_age = ages[0]  # After sorting the first index will contain the minimum Age.
print("Minimum Age: ", min_age)
#Maximum Age
max_age = ages[len(ages)-1]  # After sorting the last index will contain the Maximum Age.
print("Maximum Age: ", max_age)
# Adding minimum age and maximum again to the list using append() method
ages.append(min_age)  
ages.append(max_age)  
print("Ages after adding Min age and Max Age:", ages)
# Median 
mid_value = len(ages) // 2  # Finding the middle index in the list
# List contains even items which means we will have two middle values, using ages[mid_value] we can get the first middle value 
# from the left using ages[-mid-1] we can get the second middle from the right then divide them by 2.
median = (ages[mid_value] + ages[-mid_value-1]) / 2   
print("Median of Ages: ", median)
# Average
average = sum(ages) / len(ages)  # Using pre-defined sum() to add all the ages then dividing it by the total ages len(ages) will give the total length
print("Average Age: ", average)
# Range
range_ages = max_age - min_age  # From Maximum age subtracting minimum age we can get Range of ages
print("Range of Ages: ", range_ages)

