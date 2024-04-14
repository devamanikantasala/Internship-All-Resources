person = {
    'first_name' : 'Deva Manikanta',
    'last_name' : 'Sala',
    'age' : 20,
    'country' : 'India',
    'is_married' : False, 
    'skills' : ['Java', 'Python', 'Html', 'CSS', 'Sqlite', 'JavaScript'],
    'address' : {
        'colony' : 'APHB colony',
        'pincode' : '534260'
    }
}
#Question 1: Check if person dictionary has skills key, if so print out the middle skill in the skills list
try:
    if('skills' in person.keys()):
        print("Middle Skill : ", person['skills'][(int(len(person['skills']) / 2))]);
except Exception as E:
    pass;
#Question 2: Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if('skills' in person.keys()):
    if('Python' in person['skills']):
        print("Yes! He has python skill");
    else:
        print("No! He doesn't has python skill");
else:
    print("There are no skills of this person!");

#Question 3: If a person skills has only JavaScript and React print he is a frontend dev, 
# if the person skill has Node, Python, SQLite/MySql print he is a backend dev, 
# if he has both frontend and backend skills the print fullstack developer
# else print he holds unknown title

if('JavaScript' in person['skills'] and 'React' in person['skills']):
        if('Node' in person['skills'] and 'Python' in person['skills'] and ('Sqlite' in person['skills'] or 'Mysql' in person['skills'])):
            print("He is a Full Stack Developer");
        else:
            print("He is a Frontend Developer");
elif('Node' in person['skills'] and 'Python' in person['skills'] and ('Sqlite' in person['skills'] or 'Mysql' in person['skills'])):
    print("He is a Backend Developer");
else:
    print("Unknown Title");

#Question 4: If the person is married and if he lives in Finland, print the information
if(person['is_married'] and person['country'] == 'Finland'):
    print("Yes! The person is married and lives in Finland!");
elif(person['is_married'] == False and person['country'] != 'Finland'):
    print("No! The person is not married and doesn't lives in Finland!");
    print("He lives in", person['country']);
else:
    print("There is no appropriate information!");
