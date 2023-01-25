# Getting the number of students through input from the user
N = int(input("Enter No of Students: "))

# Creating an empty list to store weights in lbs
weights_lbs = []

# Reading weights of the students using for loop
for i in range(N):
    input_weights = float(input(f"Enter the weights of student {i+1} in lbs: "))  # Using input() getting input from the user
    weights_lbs.append(input_weights)  # Adding the student weights retrived  from user using append()
print("Weights in lbs: ", weights_lbs)
# Creating an empty list to store weights in kilograms
weights_kgs = []

#  Converting weights from lbs to kilograms:
for weight in weights_lbs:  # Traversing through weights_lbs to get individual weights
    weight_kg = weight * 0.453592  # Multiplying each weights * 0.453592 to convert to kilograms
    weights_kgs.append(round(weight_kg, 2))  # Rounding off the weight and Adding all the converted weights in kgs 

# Printing the weights in kilograms
print("Weights in Kilograms: ", weights_kgs)
