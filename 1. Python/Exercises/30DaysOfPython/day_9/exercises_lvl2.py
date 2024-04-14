#Task 1
# Write a code which gives grade to students according to their scores
try:
    score = int(input("Enter your score: "));
    if(score <= 100 and score >= 80):
        print("Grade : A");
    elif(score <= 89 and score >= 70):
        print("Grade : B");
    elif(score <= 69 and score >= 60):
        print("Grade : C");
    elif(score <= 59 and score >= 50):
        print("Grade : D");
    else:
        print("Grade : F");
except ValueError as e:
    print("Invalid Input is given");
#Task 2
# Check if the season is Autumn, Winter, Spring or Summer. 
#     September, October, November - Autumn
#     December, January, February - Winter
#     March, April, May - Spring
#     June, July, August - Summer

try:
    Summer = {'January' : 1, 'February' : 2, 'December' : 12}
    Autumn = {'September' : 9, 'October' : 10, 'November' : 11}
    Winter = {'March' : 3, 'April' : 4, 'May' : 5}
    Spring = {'June' : 6, 'July' : 7, 'August' : 8}
    month = input("Enter your month or month number: ");
    if(month.isnumeric()):
        month = int(month);
        if(month in Summer.values()):
            print(month, "is in Summer Season");
        elif(month in Autumn.values()):
            print(month, "is in Autumn Season");
        elif(month in Winter.values()):
            print(month, "is in Winter Season");
        elif(month in Spring.values()):
            print(month, "is in Spring Season");
        else:
            print(month, "is invalid month!");
    else:
        if(month in Summer.keys()):
            print(month, "is in Summer Season");
        elif(month in Autumn.keys()):
            print(month, "is in Autumn Season");
        elif(month in Winter.keys()):
            print(month, "is in Winter Season");
        elif(month in Spring.keys()):
            print(month, "is in Spring Season");
        else:
            print(month, "is invalid month!");
except Exception as e:
    print("Invalid Input!");

#Task 3:
#Based on the user input if a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print - That fruit already exist in the list
fruits = ['banana', 'orange', 'mango', 'lemon'];
try:
    fruit = input("Enter the fruit name : ");
    if(fruit.isnumeric() or fruit.isdecimal() or fruit.isdigit()):
        raise ValueError;
    elif(fruit.lower() in fruits):
        print("That fruit already exist in the list");
    else:
        fruits.append(fruit);
        print("New Fruit added!");
        print("New List :", fruits);
except ValueError as E:
    print("Invalid Fruit Name!");
