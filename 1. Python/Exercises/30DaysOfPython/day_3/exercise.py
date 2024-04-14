#Task 1 : Declare your age as integer variable
age = int(20);

#Task 2 : Declare your height as a float variable
height = float(152.3);

#Task 3 : Declare a variable that store a complex number
complex_value = complex(9 + 1j);

#Task 4
print("\nTask 4 : Write a script that prompts the user to enter base & height of the triangle and calculate the area of triangle");
triangle_base = float(input("Enter base: "));
triangle_height = float(input("Enter height: "));
triangle_area = 0.5 * triangle_base * triangle_height; 
print("The Area of the triangle: ", triangle_area);
print("\n");

#Task 5
print("\nTask 5 : Write a script that prompts the user to enter side a, b and c of the triangle. Calculate the perimeter of the triangle.");
side_a = float(input("Enter side a: "));
side_b = float(input("Enter side b: "));
side_c = float(input("Enter side c: "));
triangle_perimeter = side_a + side_b + side_c;
print("The Perimeter of the triangle is : ", triangle_perimeter);
print("\n");

#Task 6
print("\nTask 6 : Get Length and Width of a rectangle using prompt. Calculate its area and perimeter");
rectangle_length = float(input("Enter length: "));
rectangle_width = float(input("Enter width: "));
rectangle_area = rectangle_length * rectangle_width;
rectangle_perimeter = 2 * (rectangle_length + rectangle_width);
print("The Area of rectangle : ", rectangle_area);
print("The Perimeter of rectangle : ", rectangle_perimeter);
print("\n");

#Task 7
import math as m;
print("\nTask 7 : Get Radius of a cirlce using prompt. Calculate its area and circumference");
circle_radius = float(input("Enter radius: "));
circle_area = m.pi * (circle_radius ** 2);
circle_circumference = 2 * m.pi * circle_radius;
print("The Area of circle : ", circle_area);
print("The Circumference of circle : ", circle_circumference);
print("\n");


#Task 8
print("\nTask 8 : Calculate the slope, x-intercept and y-intercept of y = 2x-2");
# From y = ax + b
a, b = 2, -2;
slope_1 = a;
x_intercept = -b/a;
y_intercept = b;
print("The Slope : ", slope_1);
print("The x-intercept : ", x_intercept);
print("The y-intercept : ", y_intercept);
print("\n");

#Task 9
print("\nTask 9 : Find the slope and euclidean distance between point (2, 2) and point (6, 10)");
x1, x2 = 2, 6;
y1, y2 = 2, 10;
slope_2 = (y2-y1)/(x2-x1);
euclid_distance = m.sqrt(m.pow((x2-x1), 2) + m.pow((y2-y1), 2));
print("The Slope : ", slope_2);
print("The Euclid Distance : ", euclid_distance);
print("\n");

#Task 10
print("\nTask 10 : Compare the slopes in Task 8 and 9");
print("Slope in Task 8 as m1: ", slope_1);
print("Slope in Task 9 as m2: ", slope_2);
print("m1 > m2 : ", (slope_1 > slope_2), "and,\nm2 > m1 : ", (slope_2 > slope_1));
print("\n");

#Task 11
print("\nTask 11 : Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values\nfigure out at what x value y is going to be 0.");
x = int(input("Enter the value of x : "));
y = (x**2) + (6*x) + 9;
print("The value of y : ", y);

print("\nUsing different values from -20 to +20 to find out at what x value y is going to be 0.");
x = -20;
i = 1;
while(x <= 20):
    y = (x**2) + (6*x) + 9;
    if(y == 0):
        print(f"{i}. Y is 0 if X is {x}");
    i += 1;
    x += 1;
print("\n");




#Task 12
print("\nTask 12 : Find the length \'python\' and \'dragon\' and make a falsy comparision statement");
print("Length of \'python\' :  ", len("python"));
print("Length of \'dragon\' : ", len("dragon"));
print("Falsy Statement : \n\'python\' == \'dragon\' : ", ("python" == "dragon"));
print("\n");

#Task 13
print("\nTask 13: Use \'and\' operator to check if \"on\" is found in both \"python\" and \"dragon\"");
is_python = "on" in "python";
is_dragon = "on" in "dragon";
print("Answer: ", ("on" in "python") and ("on" in "dragon"));
print("\n");

#Task 14
print("\nTask 14: \"I hope this course is not full of jargon\". Use \'in\' operator to check if \"jargon\" is in the sentence");
print("Answer : ", ("jargon" in "I hope this course is not full of jargon"));
print("\n");

#Task 15
print("\nTask 15: There is no \"on\" in both \"dragon\" and \"python\"");
print("Result : ", (("on" not in  "dragon") and ("on" not in "python")));
print("\n");

#Task 16
print("\nTask 16 : Find the length of the text \'python\' and convert the value to float and convert it to string.");
len_python = len("python");
print("The length of Python : ", len_python , " type : ", type(len_python));
len_python = float(len_python);
print("The length of Python : ", len_python , " type : ", type(len_python));
len_python = str(len_python);
print("The length of Python : ", len_python , " type : ", type(len_python));
print("\n");

#Task 17
print("\nTask 17 : How do you check if a number is even or not using python?");
number = int(input("Enter the number : "));
if(number%2 == 0):
    print(f"The number - {number} is EVEN");
else:
    print(f"The number - {number} is ODD");
print("\n");
#Task 18
print("\nTask 18 : Check if the floor division of 7 by 3 is equal to the \"int\" converted value of 2.7");
if(7//3 == int(2.7)):
    print("Yes! Floor Division of 7 by 3 is equal to \'int\' converted value of 2.7");
else:
    print("No! Floor Division of 7 by 3 is equal to \'int\' converted value of 2.7");
print("\n");

#Task 19
print("\nTask 19 : Check if type of \'10\' is equal to type of 10");
if(type('10') == type(10)):
    print("Yes! The Data types are same!");
else:
    print("No! The Data types are not same!");
print("\n");

#Task 20
print("\nTask 20 : Check if int(9.8) is equal to 10");
if(int(9.8) == 10):
    print("Yes! int(9.8) is equal to 10");
else:
    print("No! int(9.8) is not equal to 10");
print("\n");

#Task 21
print("\nTask 21: Write a script that prompts the user to enter hours and rate per hour calculate pay of the person?");
hours = int(input("Enter hours : "));
rate_per_hour = int(input("Enter rate per hour : "));
weekly_earning = hours * rate_per_hour;
print("Your weekly earning is ", weekly_earning);
print("\n");

#Task 22
print("\nTask 22: Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years");
years_you_lived = int(input("Enter number of years you have lived : "));
if(years_you_lived >= 101):
    print("Average person lives maximum upto 100 years! so please enter valid value");
else:
    seconds_you_lived = years_you_lived * 365 * 24 * 60 * 60;
    print("You have lived for ", seconds_you_lived , " seconds.");
print("\n");

#Task 23
print("\nTask 23: Write a python script that displays given table in 3.Operators.pptx ");
i = 1;
while(i <= 5):
    j = 1;
    print(i, end = " ");
    print("1", end=" ");
    while(j <= 3):
        print(i**j, end=" ");
        j+=1;
    print("\n");
    i+=1;
print("\n");
