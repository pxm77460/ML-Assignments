
sisters = ('Ramya', 'Kavya', 'Laxmi')  # Creating a tuple with names of sisters
brothers = ('Ramesh', 'Venkat', 'Hari')  # Creating a tuple with names of brothers
print("Sisters: ", sisters)
print("Brothers: ", brothers)
siblings = sisters + brothers  # Joining sisters tuple and brothers tuple to siblings variable
print("Siblings: ", siblings)
print("No of Siblings: ", len(siblings))  # Printing No of Siblings.

# Modifying the siblings tuple and adding the father and mother names by using + operator and assigning to family_members variable
family_members = siblings + ("Jagadiswara Rao", "Nageswaramma")  

print("Family Members:", family_members)  # Printing family members

