#Task 1 : Explain the difference between map(), filter(), and reduce()
print('---------------------- T A S K ----- 1 ------------------------------------------')
#map() function is a type of higher order function that allows two arguments first one function.. and second one iterable object of python like...
#map() function maps the passed function and applies it to the each item of iterable that is passed to. map() function..
#For example:
import math as m
numbers = [i for i in range(1, 11)]; # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_factorials = map(lambda num: m.factorial(num), numbers);
for number, factorial in zip(numbers, numbers_factorials):
    print(f"{number}'s factorial : {factorial}");

#filter() function is also a function that comes under the category of higher order functoin that allows two arguments first one is function..
#and the second one is iterable object in python... unlike map() it allows the iterable to be filtered based on certain condition... if the condition is evaluated True..
#then it adds it to the target variable otherwise it continues..
#For example:

#here i am defining a function is_prime that evaluates True if it is... Prime or False if it is not Prime
def is_prime(num):
    if num < 2:
        return True;
    else:
        for i in range(2, int(m.sqrt(num))+1):
            if num%i == 0:
                return False;
        return True;

#now I am taking a list of numbers from 10 to 20 numbers
numbers = [i for i in range(10, 21)]; #[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
prime_numbers = filter(is_prime, numbers);
print(f'Prime Numbers from 10-20: {list(prime_numbers)}')

#reduce() function is a special case function which is under functools module and like map() and filter() function
#it also takes two arguements like 1-function, 2-iterable object.. and performs a certain option whereas if only the function takes two arguments.. and it only returns the last value and a single value;

#For example
# I am declaring a function that returns the sum of numbers and sum of length of strings
def find_sum(val, val1):
    if isinstance(val, str) and isinstance(val1, str):
        return len(val) + len(val1);
    elif isinstance(val, int) and isinstance(val1, int):
        return val + val1
    elif isinstance(val, str):
        if isinstance(val1, int):
            return val1 + len(val);
    elif isinstance(val, int):
        if isinstance(val1, str):
            return val + len(val1);
    else:
        return 0;
import functools as fc;
list_values = ['Deva', 4, 'Jeevan', 5, 6, 'Mallikarjuna'] 
'''
    [
        1st time: 
            val = 'Deva' --> len('Deva') --> 4 
            val1 = 4 ......................> 4 (+)
            Total                            8
        
        2nd time:
            val = 8 ............................> 8
            val1 = 'Jeevan' --> len('Jeevan') --> 6 (+)
            Total                                 14

        3rd time:
            val = 14 ....... 14
            val1 = 5 .......  5 (+)
            Total            19

        4th time:
            val = 19 ....... 19
            val1 = 6 .......  6 (+)
            Total            25
        
        5th time:
            val = 25 ........................................ 25
            val1 = 'Mallikarjuna' --> len('Mallikarjuna') --> 12 (+)
            Total                                             37
        
        Final Return Value 37
    ]
'''
length = fc.reduce(find_sum, list_values);
print(f'The length of each item in the list {list_values}: {length}')

#Task 2: Explain the difference between higher order function, closure and decorator.
print('---------------------- T A S K ----- 2 ------------------------------------------')
#-----------------------------
# Higher Order Function
#-----------------------------
# In Python Functions are stated as first class objects and in python each function is treated as an individual object
# In Python functions can be passed as parameter and can be returned as an object.. the function that calls or returns the function
# is called 'Higher Order Function'

# Generally, Higher Order Functions has two use cases:
# 1. Passing Function as argument -- For example:
# I am having a dictionary which holds the key:value as base:height of one triangle
traingles = {25:35, 45:67, 78:43, 23:13, 89:98}

def calculate_area():
    area_of_triangles = [];
    for base, height in traingles.items():
        area_of_triangles.append((0.5 * base * height));
    return area_of_triangles;

def output_printer(list_of_areas):
    i = 0;
    for base, height in traingles.items():
        print(f'Triangle-{i+1}|Base:{base}|Height:{height}|Area:{list_of_areas[i]}');
        i += 1;

def caller(function1, function2): #here passing a function as an argument
    area_of_triangles = function1();
    function2(area_of_triangles);

caller(calculate_area, output_printer);
#Here Higher Order Function is caller()

# 2. Returning Function from a function -- for example
# Again lets consider calculating area, and volume, and perimeter of the triangle now by returning the function
def perimeter(side_a, side_b, side_c):
    return side_a + side_b + side_c;
def area(base, height):
    return (0.5 * base* height);
def volume(base, height, length):
    return (0.5 * base * height * length);

def caller_function(function):
    return function #here we are returning the function.. as an object..

#here caller_function is HOF.
choice = int(input('What do you want to find of Triangle\n1.perimeter\n2.area\n3.volume\nYour Choice: '));
if(choice == 1):
    fx_perimeter = caller_function(perimeter); # here we are using the fx_perimeter as reference to the actual perimeter function..
    sides = str(input('Enter sides a, b, c: ')).split(',')
    a,b,c = [int(i.strip()) for i in sides]
    var_perimeter = fx_perimeter(a, b, c);
    print('Perimeter : ', var_perimeter);
elif(choice == 2):
    fx_area = caller_function(area);
    base, height = int(input('Enter the base : ')), int(input('Enter the height : '));
    var_area = fx_area(base, height);
    print('Area : ', var_area);
elif(choice == 3):
    fx_volume = caller_function(volume);
    base, height, length = int(input('Enter the base : ')), int(input('Enter the height : ')), int(input('Enter the lenght : '));
    var_volume = fx_volume(base, height, length);
    print('Volume : ', var_volume);
else:
    print('Invalid Choice!');

#-----------------------------
# Closures
#-----------------------------
# Closures is a advanced functions topic in python.. where this is completely focused on defining inner functions in a python function
# Closures a partly are considered to be extension for the concept of higher order function.

# For example:
def wish_him_or_her_happy_diwali(pronoun):
    if(pronoun == 'he' or pronoun == 'him'):
        return 'I am wishing you a happy diwali ra mawa!'
    elif(pronoun == 'she' or pronoun == 'her'):
        return 'I am wishing you a happy diwali chelli/akka!'
    else:
        return f'Nee \'{pronoun}\' pronoun naku ardham kavatledhu\nNinnu em analo naku teliyatledhu ra bhai! Sarley Happy Diwali...anyway'

def asalina_function(function_arg):
    def piluvu_asalina_function():
        pronouns = str(input('Enter your pronoun: he/him | she/her: ')).split('/');
        first_pronoun, *next_pronoun = [i.strip() for i in pronouns];
        message = function_arg(first_pronoun);
        print(f'{function_arg.__name__} returned - \'{message}\'');
    return piluvu_asalina_function;


test_chestuna = asalina_function(wish_him_or_her_happy_diwali);
test_chestuna();

#-----------------------------
# Decorator
#-----------------------------
# Decorators are the more advanced concept where it is very useful under the perspective whenever we want to change the functionality
# without changing the actual function code..

#For example:
def debug(function):
    def inner_function(*args, **kwargs):
        output = function(*args, **kwargs);
        print(output);
    return inner_function;
@debug
def function_test(*args, **kwargs):
    return (f'Arguments : {args} total {len(args)}\nAnd Keyword arguments : {kwargs} total {len(kwargs)}');
function_test(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, name='Deva', college='YN College', course='BCA', age=20, married=False);

#Task 3: Define a call function before map, filter, or reduce.
print('---------------------- T A S K ----- 3 -------------------------------------------')
# Iam using is_prime function which is defined at the top.. is_prime()
apply_square = lambda num : num**2;
find_sum1 = lambda a,b : a+b;

def apply_the_function(function_main):
    def inner1(type):
        if type=='map':
            def inner(function, data):
                print('Map Function Testing');
                result = function_main(function, data);
                print(f'function_name : \'{function_main.__name__}\' is executing..');
                print(f'Mapping Numbers by sqauring from {min(data)}-{max(data)}....');
                print(result);
            return inner;
        elif type=='filter':
            def inner(function, data):
                print('Filter Function Testing');
                result = function_main(function, data);
                print(f'function_name : \'{function_main.__name__}\' is executing..');
                print(f'Filtering Prime Numbers from {min(data)}-{max(data)}....');
                print(result);
            return inner;
        elif type=='reduce':
            def inner(function, data):
                print('Reduce Function Testing');
                result = function_main(function, data);
                print(f'function_name : \'{function_main.__name__}\' is executing..');
                print(f'Reducing Numbers to total from {min(data)}-{max(data)}....');
                print('Total : ', result);
            return inner;
        else:
            return 'Invalid Function choosen';
    return inner1
@apply_the_function
def filtering(function, data):
    return list(filter(function, data));
filterer = filtering(type='filter')
data = [i for i in range(1, 21)]
filterer(is_prime, data)
print();
@apply_the_function
def mapping(function, data):
    return list(map(function, data));
mapper = mapping(type='map')
mapper(apply_square, data)
print();
@apply_the_function
def reducing(function, data):
    return (fc.reduce(function, data));
reducer = reducing(type='reduce');
reducer(find_sum1, data);
#Task 4: Use a for loop to print the each country in the countries list.
print('---------------------- T A S K ----- 4 -------------------------------------------')

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def for_printer():
    def output(datum):
        i = 1;
        if isinstance(datum, list):
            for data in datum:
                print(f'{i}-item: {data}');
                i += 1;
        else:
            print('Invalid Data');
    return output;

countries_printer_holder = for_printer()
countries_printer_holder(countries);

#Task 5: Use a for to print the each name in the names list.
print('---------------------- T A S K ----- 5 -------------------------------------------')
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
names_printer_holder = for_printer();
names_printer_holder(names);

#Task 6: Use a for to print the each number in the numbers list.
print('---------------------- T A S K ----- 6 -------------------------------------------')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_printer_holder = for_printer();
numbers_printer_holder(numbers);