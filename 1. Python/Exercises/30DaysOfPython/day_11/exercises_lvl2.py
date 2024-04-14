#Task 1:
#Declare a function named evens_and_odds. It takes a positive integer as a parameter and it counts number of even and odds from 1 to number.
def evens_and_odds(number):
    count_even, count_odd = 0, 0
    for i in range(number+1):
        if(i % 2 == 0):
            count_even += 1;
        else:
            count_odd += 1;
    return str("Even :{" + str(count_even) + "}" + " Odd :{" + str(count_odd) + "}");
print("Task 1: Count Evens and Odds from 1 to 100 : ", evens_and_odds(100));

#Task 2:
#Call your function factorial, it takes a whole number as a parameter and it return factorial of the number
def factorial(number):
    if (number == 1):
        return 1;
    elif (number == 0):
        return 0;
    else:
        return number * (factorial(number-1));

print("Task 2: The factorial of 5 is:", factorial(5));

#Task 3:
#Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(variable):
    if variable is None or len(variable) == 0:
        return True;
    else:
        return False;

print("Task 3: A --> [1,2] is empty? :", is_empty([1,2]));
print("Task 3: A --> [] is empty? :", is_empty([]));

#Task 4:
''' Write different functions which take lists. 
    They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
'''
def calculate_mean(values_list):
    mean = sum(values_list)/len(values_list);
    return mean;

def calculate_median(values_list):
    values_list.sort();
    median = 0;
    if (len(values_list) % 2 == 1):
        median = values_list[len(values_list)//2];
    else:
        median = (values_list[len(values_list)//2 - 1] + values_list[len(values_list)//2]) /2;
    
    return median;

def calculate_mode(values_list):
    counts = [];
    for i in values_list:
        counts.append(values_list.count(i));
    counts.sort();
    counts.reverse();
    for i in values_list:
        if(counts[0] == values_list.count(i)):
            return i;

def calculate_range(values_list):
    range = max(values_list) - min(values_list);
    return range;

def calculate_variance(values_list):
    mean = calculate_mean(values_list);
    variance = sum((x - mean)**2 for x in values_list) / len(values_list);
    return variance;

import math as m
def calculate_std(values_list):
    standard_deviation = m.sqrt(calculate_variance(values_list));
    return standard_deviation;

print("Task 4:");
print("Mean --> [1, 2, 3, 4, 5] :", calculate_mean([1, 2, 3, 4, 5]));
print("Median --> [1, 2, 3, 4, 5] : ", calculate_median([1, 2, 3, 4, 5]));
print("Mode --> [1, 2, 2, 3, 3, 4, 2, 2, 4, 5] : ", calculate_mode([1, 2, 2, 3, 3, 4, 2, 2, 4, 5]));
print("Range --> [1, 2, 3, 4, 5] : ", calculate_range([1, 2, 3, 4, 5]));
print("Variance --> [1, 2, 3, 4, 5] :", calculate_variance([1, 2, 3, 4, 5]));
print("Standard Deviation --> [1, 2, 3, 4, 5] :", calculate_std([1, 2, 3, 4, 5]));
