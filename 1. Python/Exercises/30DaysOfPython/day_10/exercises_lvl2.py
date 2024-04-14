#Task 1
#Use for loop to iterate from 0 to 100 and print the sum of all numbers
sum = 0
for i in range(0, 101):
    sum += i;

print("The Sum of all numbers from 0 to 100: ", sum);

#Task 2
#Use for loop to iterate from 0 to 100 and print the sum of all evens and odds seperately
sum_of_even = 0
sum_of_odd = 0
for i in range(0, 101):
    if(i % 2 == 0):
        sum_of_even += i;
    else:
        sum_of_odd += i;

print("Sum of Even numbers from 0 to 100: ", sum_of_even, "\nSum of Odd numbers from 0 to 100: ", sum_of_odd);
