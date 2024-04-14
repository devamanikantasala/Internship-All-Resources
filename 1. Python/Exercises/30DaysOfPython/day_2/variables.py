#Excercise Level 1
#Task 1 : Inside 30DaysOfPython create a folder called "day_2". Inside the folder create a file named 'variables.py'
#Task 2 : Write a python comment saying 'Day 2: 30 Days of python programming'

#Task 3 : Declare a first name variable and assign a value to it.
first_name = "Deva Manikanta"

#Task 4 : Declare a last name variable and assign a value to it.
last_name = "Sala"

#Task 5: Declare a full name variable and assign a value to it.
full_name = "Deva Manikanta Sala"

#Task 6: Declare a country variable and assign a value to it.
country = "India"

#Task 7: Declare a city variable and assign a value to it.
city = "Palacole"

#Task 8: Declare an age variable and assign a value to it.
age = 20

#Task 9: Declare a year variable and assign a value to it.
year = 2024

#Task 10: Declare a variable is_married and assign a value to it.
is_married = False;

#Task 11: Declare a variable is_true and assign a value to it.
is_true = True;

#Task 12: Declare a variable is_light_on and assign a value to it.
is_light_on = False;

#Task 13: Declare multiple variable on one line.
a, b, c = 10, 20, 30;

#Excercise Level 2
#Task 1 : Check the data type of all you variables using "type()" built-in function.

print("Type of first_name : ", type(first_name));
print("Type of last_name : ", type(last_name));
print("Type of full_name : ", type(full_name));
print("Type of country : ", type(country));
print("Type of city : ", type(city));
print("Type of age : ", type(age));
print("Type of year : ", type(year));
print("Type of is_married : ", type(is_married));
print("Type of is_true : ", type(is_true));
print("Type of is_light_on : ", type(is_light_on));
print("Type of a : ", type(a));
print("Type of b : ", type(b));
print("Type of c : ", type(c));
print("\n\n");

#Task 2 : Using the 'len()' built-in function, find the length of your first name

print(f"Length of First Name - \"{first_name}\": {len(first_name)}");

#Task 3 : Compare the length of your first name and your last name

print(f"\nThe Length of First Name - \"{first_name}\" : {len(first_name)} and Last Name - \"{last_name}\" : {len(last_name)}");
print(f"lengths of first_name > last_name: ", (len(first_name) > len(last_name)));
print(f"lengths of last_name > first_name: ", (len(last_name) > len(first_name)));

#Task 4 : Declare 5 as num_one and 4 as num_two

num_one, num_two = 5, 4;

# 4.a) Add num_one and num_two and assign the value to a variable total
total = num_one + num_two;
print("Total : ", total);

# 4.b) Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one;
print("Diff : ", diff);

# 4.c) Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one;
print("Product : ", product);

# 4.d) Divide num_one by num_two and assign the value to a variable division
division = num_one/num_two;
print("Division : ", division);

# 4.e) Use Modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one;
print("Remainder : ", remainder);

# 4.f) Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two;
print("Exp : ", exp);

# 4.g) Find the floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two;
print("Floor Division : ", floor_division);

#Task 5: The Radius of a Circle is 30 meters.

# 5.a) Calculate the area of circle and assign the value to a variable name of area_of_circle.
# 5.b) Calculate the circumference of a circle and assign the value of a variable name of circum_of_circle.
# 5.c) Take radius as user input and calculate the area and circumference

import math;
radius = float(input("\n\nEnter the radius : "));
area_of_circle = math.pi * (radius ** 2); # πr²
circum_of_circle = 2 * math.pi * radius; # 2πr
print(f"Area of Circle with radius({radius}) : ", area_of_circle);
print(f"Circumference of Circle with radius({radius}) : ", circum_of_circle);

#Task 6: Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names.

first_name = input("\n\nEnter your first name : ");
last_name = input("Enter your last name : ");
country = input("Enter your country name : ");
