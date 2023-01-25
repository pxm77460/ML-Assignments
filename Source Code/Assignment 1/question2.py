# Dog Dictionary
dog = {}  # An empty list which does have any values
# Adding name, color, breed , legs and age to the dog list with keys and values
dog['name'] = "Tommy"
dog['color'] = "White"
dog['breed'] = "Seyomond"
dog['legs'] = 4
dog['age'] = 2
print("Dog Dictionary: ", dog)
# Creating Student Dictionary by adding first_name, last_name, gender, age, marital_status, skills as a list
# country, city and address as keys and added values respectively.
student = {
    'first_name': 'Pavankalyan',
    'last_name' : 'Magam',
    'gender' : 'Male',
    'age' : 23,
    'marital_status' : 'Single',
    'skills' : ['Python', 'Java'],
    'country': 'USA',
    'city' : 'Overland Park',
    'address': '7575 W 106TH ST '
}
print("Length of Student Dictionary: ", len(student))  # This will give length of the student list
print("Type of Student Skills: ", type(student['skills']))  # This will give the type of student skills value in the student list
student['skills'].append("MongoDB")  # Adding skills to the student list using append() method.
student['skills'].append("Spring Boot")   # Adding skills to the student list using append() method.
student_keys = list(student.keys())  # Using Built in class list() to convert student dictionary keys to a list
print("Keys: ", student_keys)
student_values = list(student.values())  # Using Built in class list() to convert student dictionary values to a list
print("Values: ", student_values)