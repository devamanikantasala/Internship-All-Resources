#Task 1:
#Create an empty dictionary called dog
dog = {}

#Task 2:
#Add name, color, breed, legs, age to the dog dictionary
dog['name'] = "Thomas"
dog['color'] = "white"
dog['breed'] = "german shephard"
dog['legs'] = 4
dog['age'] = 13

#Task 3:
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city, and address as keys for the dictionary
student = {
    'first_name' : "Deva Manikanta",
    'last_name' : "Sala",
    'gender' : "Male",
    'age' : 20,
    'marital_status' : 'Unmarried',
    'skills' : ["Java", "Python", "SQLite", "C", "AWS", "Cybersecurity"],
    'country' : "India",
    'city' : "Palakollu",
    'address' : "APHB colony, near TTD Kalyana mandapam, Palakollu"
}

#Task 4:
#Get the length of the student dictionary
print("The length of student dictionary : ", len(student));

#Task 5:
#Get the value of skills and check the data type if should be a list
print("Skills : ", student['skills']);
print("Type : ", type(student['skills']));

#Task 6:
#Modify the skills values by adding one or two skills
student['skills'].append("Machine Learning");
student['skills'].append("Data Science");

#Task 7:
#Get the dictionary keys as a list
student_dict_keys = list(student.keys());
print(student_dict_keys);

#Task 8:
#Get the dictionary values as a list
student_dict_values = list(student.values());
print(student_dict_values);

#Task 9:
student_dict_list = list(student.items());
print(student_dict_list);

#Task 10
#Delete one of the items in the dictionary
del student['address'];
print(student);

#Task 11
#Delete one of the dictionaries
del dog;
