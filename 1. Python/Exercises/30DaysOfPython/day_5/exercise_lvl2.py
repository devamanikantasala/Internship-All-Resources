#Task 1
print("\n\nTask 1: The Following is a list of 10 students ages");
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24];
print(ages);

#Task 2
print("\n\nTask 2: Sort the list and find the min and max age");
ages.sort();
print("Min Age : ", min(ages));
print("Max Age : ", max(ages));

#Task 3
print("\n\nTask 3: Add the min age and max age again to the list");
ages.append(min(ages));
ages.append(max(ages));
print(ages);

#Task 4
import statistics as st; #pip install statistics
print("\n\nTask 4: Find the median age (one middle item or two middle items divided by two)");
ages.sort();
median = int(st.median(ages));
print("The median age : ", median);

#Task 5
print("\n\nTask 5: Find the average age");
average = sum(ages)/len(ages);
print("The average age : ", average);

#Task 6
print("\n\nFind the range of the ages");
range_ages = max(ages) - min(ages);
print("The Range of ages : ", range_ages);

#Task 7
print("\n\nCompare the value of (min-average) and (max-average), use abs() method");
print(f"Minimum => {min(ages)}\nMaximum => {max(ages)}\nAverage => {average}");
print(f"(Min - Average) > (Max - Average)\n{abs(min(ages)-average)} > {abs(max(ages)-average)} : {abs(min(ages)-average) > abs(max(ages)-average)}");
