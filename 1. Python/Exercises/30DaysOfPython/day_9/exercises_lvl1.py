#Task 1:
#Get user input, and print the appropriate message if user is 18 or older give feedback : You are old enough to drive. If below 18 give feedback to wait for missing amount of years
try:
    age = int(input("Enter your age: "))
    if(age >= 18):
        print("You are old enough to drive");
    else:
        print(f"You need {18-age} more years to learn to drive");
except ValueError as T:
    print("Invalid Input is given");
#Task 2:
#Compare the values of my_age and your_age using if..else. Who is older me or you?, use input function to get the age as input. You can use a nested condition to print 'year' for 1 year diff. in age, and 'years' for bigger differences and a custom text if my_age =  your_age
my_age = 20;
try:
    your_age = int(input("Enter your age: "));
    if(my_age < your_age):
        age_diff = your_age - my_age;
        if(age_diff > 1):
            print("You are ", age_diff, " years older than me.");
        if((age_diff <= 1) and (age_diff != 0)):
            print("You are ", age_diff, " year older than me.");
    elif(my_age > your_age):
        age_diff = my_age - your_age;
        if(age_diff > 1):
            print("I am ", age_diff, " years older than you");
        if((age_diff <= 1) and (age_diff != 0)):
            print("I am ", age_diff, " year older than you");
    else:
        print("Your age is equal to mine!");
except ValueError as e:
    print("Invalid Input");
#Task 3:
#Get two number from the user input. If a is greater than b return a is greater than b, if a is less than b return a is smaller than b, else a is equal to b
try:
    a = int(input("Enter the number one : "));
    b = int(input("Enter the number two : "));
    if(a > b):
        print(a , "is greater than", b);
    elif(b > a):
        print(a, "is less than", b);  
    else:
        print(a, "is equal to", b);
except ValueError as e:
    print("Invalid Input");
