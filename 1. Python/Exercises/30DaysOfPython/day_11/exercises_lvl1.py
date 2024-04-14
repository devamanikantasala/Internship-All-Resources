#Task 1:
#Declare a function add_two_numbers. It should take two parameters and it returns a sum
def add_two_numbers(a, b):
    return (int(a)+int(b));
print("Task 1: Sum of 1 and 2 : ", add_two_numbers(1, 2));

#Task 2:
#Declare the area of circle is calculated as follows: area = π * (r^2). Write a function that calculates area_of_circle
import math as m;
def area_of_circle(radius):
    return (m.pi*(float(radius)**2));
print("Task 2: Radius 5: Area of Circle is : ", area_of_circle(5.0));

#Task 3:
#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number. If not do give a reasonable feeback.
def add_all_nums(*numbers):
    all_are_same_type = all(isinstance(number, int) for number in numbers);
    if(all_are_same_type):
        return sum(numbers);
    else:
        return "All values are not same type";

print("Task 3: Sum of 1, 2, 3: ", add_all_nums(1, 2, 3));
print("Task 3: Sum of 1, \'Deva\', 3: ", add_all_nums(1, 'Deva', 3));

#Task 4:
#Write a function that converts °C to °F like convert_celsius_to_fahrenheit
def convert_celcius_to_fahrenheit(degrees):
    return float(degrees * (9/5) + 32);

print("Task 4: 354°C in °F : ", convert_celcius_to_fahrenheit(354));

#Task 5:
#Write a function called check_season, it takes a month parameter and returns the season: Autumn, Winter, Spring, or Summer
def check_season(month):
    Summer = ['january', 'february', 'december']
    Autumn = ['september', 'october', 'november']
    Winter = ['march', 'april', 'may']
    Spring = ['june', 'july', 'august']
    month = str(month).lower();
    if(month in Summer):
        return "Summer";
    elif(month in Autumn):
        return "Autumn";
    elif(month in Winter):
        return "Winter";
    elif(month in Spring):
        return "Spring";
    else:
        return "Invalid Month";

print("Task 5: January is in", check_season("January"), "season");

#Task 6:
#Write a function called calculate_slope which return the slope of a linear equation.
def calculate_slope(equation):
    # linear equation -> y = mx + b;
        #eq -> y = mx + b
    equation = equation.replace(" ", "");
    parts = equation.split("=");
    
    if(parts[0].strip() != 'y' or len(parts) != 2):
        return "Invalid Linear Equation : Expected format -- y = mx + b";
    
    parts[1] = parts[1].strip();
    index_of_x = parts[1].index('x');
    slope = parts[1][0:index_of_x];
    try:
        slope = float(slope);
        return slope;
    except ValueError as ve:
        return "Invalid Slope value is given! Try again!";

print("Task 6: The slope of linear equation (y = -532x + 67): ", calculate_slope("y = -532x + 67"));

#Task 7:
#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(equation):
    try:
        parts = equation.split("=")
        j = 0;
        for i in parts:
            parts[j] = i.strip()
            j += 1;

        if (int(parts[1]) != 0 and int(parts[1]) > 0):
            parts[0] += ' - ' + parts[1];
            parts[1] = '0';
        elif (int(parts[1]) != 0 and int(parts[1]) < 0):
            parts[0] += ' + ' + parts[1][1];
            parts[1] = '0';
        else:
            pass;

        parts[0] = parts[0].replace(" ", '');
        a = 0;
        if(parts[0][0:parts[0].index('x^2')] == '-'):
            a = -1;
        elif(parts[0][0:parts[0].index('x^2')] == ''):
            a = +1;
        elif (parts[0][0:parts[0].index('x^2')] != '-') and (parts[0][0:parts[0].index('x^2')] != ''):
            a = int(parts[0][0:parts[0].index('x^2')])
        else:
            a = 0;

        b = 0;
        if(parts[0][(parts[0].index('^2')+1)+1 : parts[0].rindex('x')]) == '-':
            b = -1;
        elif(parts[0][(parts[0].index('^2')+1)+1 : parts[0].rindex('x')]) == '+':
            b = +1
        elif(parts[0][(parts[0].index('^2')+1)+1 : parts[0].rindex('x')]) != '-' or (parts[0][(parts[0].index('^2')+1)+1 : parts[0].rindex('x')]) != '+' :
            b = int(parts[0][(parts[0].index('^2')+1)+1: parts[0].rindex('x')])     
        else:
            b = 0;
        # c = int(parts[0][parts[0].rindex('x')+1: ]);
        c = 0;
        if(parts[0][parts[0].rindex('x')+1: ] == ''):
            c = 0;
        else:
            c = int(parts[0][parts[0].rindex('x')+1: ]);

        import math as m;
        discriminant = (b**2) - (4*a*c);
        if(discriminant > 0):
            print("Real Roots".upper());
            root_1 = (-(float(b)) + m.sqrt(discriminant)) / (2.0*a)
            root_2 = (-(float(b)) - m.sqrt(discriminant)) / (2.0*a)
            print("Equation : ", equation);
            print("|a =", a , "|b =", b, "|c =", c, "|");
            print("Solution Set : {", root_1, ",", root_2, "}");
        elif(discriminant == 0):
            print("Equal Roots".upper());
            roots = -float(b)/(2.0*a);
            print("Equation : ", equation);
            print("|a =", a , "|b =", b, "|c =", c, "|");
            print("Solution Set : {", roots, ",", roots, "}");
        else:
            print("Imaginary Roots".upper());
            print("Equation : ", equation);
            print("|a =", a , "|b =", b, "|c =", c, "|");
            print("Expensive Computation");
    except Exception as E:
        print("Error Occured : " , E, "\nOr else please enter the equation in format : ax^2 + bx + c = 0/or/ax^2 + bx = c");    

print("Task 7 --> RESULT is as follows: ");
solve_quadratic_eqn("2x^2 - 4x = 9");

#Task 8:
#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list_of_items):
    j = 1;
    for i in list_of_items:
        print("Item -", j , ": ", i);
        j += 1;

print("Task 8 --> RESULT is as follows");
print_list(['Hi', 'Hello', 'Vanakam', 'Adabhbarsey', 'Namasthe', 'Ciao']);

#Task 9:
#Declare a function named reverse_list. It takes an array as a parameter and it should return the reverse of the array (use loop).
def reverse_list(list_of_items):
    reversed_list = [];
    for i in range(len(list_of_items)-1, -1, -1):
        reversed_list.append(list_of_items[i]);
    return reversed_list;

print("Task 9 : Actual list --> [1, 2, 3, 4, 5], Reversed List --> ", end = "");
print(reverse_list([1,2,3,4,5]));

#Task 10:
def capitalize_list_items(list_of_items):
    new_list = []
    for i in list_of_items:
        new_list.append(i.capitalize());
    return new_list;

print("Task 10 : Actual list --> ['ab cd', 'ef gh', 'ij kl'], Reversed List --> ", end = "");
print(capitalize_list_items(['ab cd', 'ef gh', 'ij kl']));

#Task 11:
#Declare a function named add_item. It takes a list and an item as parameter. It returns a list with the item added at the end.
def add_item(list_of_items, item):
    list_of_items.append(item);
    return list_of_items;

print("Task 11: Actual List --> [1, 2, 3, 4, 5] Add:6, Added List --> ", end="");
print(add_item([1,2,3,4,5], 6));

#Task 12:
#Declare a function named remove_item. It takes a list and an item as paramter. It returns a list with the item removed at the end.
def removed_item(list_of_items, item):
    list_of_items.remove(item);
    return list_of_items;

print("Task 12: Actual List --> [1, 2, 3, 4, 5] Remove:4, Removed List --> ", end="");
print(removed_item([1,2,3,4,5], 4));

#Task 13:
def sum_of_numbers(upto_number):
    sum = 0;
    for i in range(upto_number+1):
        sum += i;
    return sum;

print("Task 13: Sum of numbers from 1 to 5:", sum_of_numbers(5));

#Task 14:
#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(upto_number):
    sum = 0;
    for i in range(upto_number+1):
        if i%2 != 0:
            sum += i;
    return sum;

print("Task 14: Sum of odd numbers from 1 to 5:", sum_of_odds(5));

#Task 15:
#Declare a function named sum_of_evens. It takes a number parameter and it adds all the even numbers in that range.
def sum_of_evens(upto_number):
    sum = 0
    for i in range(upto_number+1):
        if(i%2 == 0):
            sum += i;
    return sum;

print("Task 15: Sum of even numbers from 1 to 5:", sum_of_evens(5));
