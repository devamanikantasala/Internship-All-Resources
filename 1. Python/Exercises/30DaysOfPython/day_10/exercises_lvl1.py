#Task 1
#Iterate 0 to 10 using for loop, do the same using while loop
#For Loop
print("Using For Loop : ", end = " ");
for i in range(0, 11):
    if(i == 10):
        print(i);
    else:
        print(i, end=",");
#While Loop
i = 0;
print("Using While Loop : ", end = " ");
while(i <= 10):
    if(i == 10):
        print(i);
    else:
        print(i, end=",");
    
    i += 1;

#Task 2:
#Iterate 10 to 0 using for loop and while loop
print("Using for loop : ", end="");
for i in range(10 , -1, -1):
    if(i == 0):
        print(i);
    else:
        print(i, end = ",");

i = 10;
print("Using while loop : ", end="");
while(i >= 0):
    if(i == 0):
        print(i);
    else:
        print(i, end = ",");
    i -=  1;

#Task 3: Write a loop that makes seven calls to print(), so we get traingle pattern:
i = 1
while(i <= 7):
    for j in range(1, i+1):
        print("#", end = "");
    print();
    i += 1;

#Task 4:
# Use nested loops to create the following
for i in range(1, 9):
    for j in range(1, 9):
        print("# ", end = "");
    print();

#Task 5:
#Print the following pattern
for b in range(0, 11):
    print(b,"x", b, "=", (b*b));

#Task 6:
#Iterate through the list ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] using for loop and print out the items:
for i in ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']:
    print(i);

#Task 7:
#Use for loop to iterate from 0 to 100 and print only even numbers
print("Even Numbers from 0 to 100:");
for i in range(0, 101):
    if(i % 2 == 0):
        if(i == 100):
            print(i);
        else:
            print(i, end=",");
    else:
        continue;
#Task 8:
#Use for loop to iterate from 0 to 100 and print only odd numbers
print("Odd Numbers from 0 to 100:");
for i in range(0, 101):
    if(i % 2 != 0):
        if(i == 99):
            print(i);
        else:
            print(i, end=",");
    else:
        continue;
