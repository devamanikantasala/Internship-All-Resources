#Task 1:
print("Task 1 : Declare an empty list");
my_list = [];

#Task 2: 
print("\n\nTask 2 : Declare a list with more than 5 items");
my_list = [1, 2, 3, 4, 5, "Deva Manikanta"];

#Task 3:
print("\n\nTask 3 : Find the length of your list");
print("The length of my list : ", len(my_list));

#Task 4:
print("\n\nTask 4 : Get the first item, the middle item and then the last item of the list");
print("The First Item : ", my_list[0]);
print("The Middle Item : ", my_list[int(len(my_list) / 2)]);
print("The Last item : ", my_list[-1]);

#Task 5:
print("\n\nTask 5 : Declare a list mixed_data_types, put your --> name, age, height, maritial status, address");
mixed_data_types = ["Deva Manikanta", 20, 150.5, "unmarried", "Palacole-53460"];

#Task 6:
print("\n\nTask 6 : Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle, and Amazon");
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"];

#Task 7:
print("\n\nTask 7 : Print the list using print()");
print("List = it_companies : ", it_companies);

#Task 8:
print("\n\nTask 8 : Print the number of companies in the list");
print("No.of companies : ", len(it_companies));

#Task 9:
print("\n\nTask 9 : Print the first, middle, and last company");
print("The First Company : ", it_companies[0]);
print("The Middle Company : ", it_companies[int(len(it_companies) / 2)]);
print("The Last Company : ", it_companies[-1]);

#Task 10:
print("\n\nTask 10 : Print the list after modifying one of the companies");
it_companies[0] = "Meta";
print("The Modified list : ", it_companies);

#Task 11:
print("\n\nTask 11 : Add an IT company to it_companies");
it_companies.append("Infosys");
print(it_companies);

#Task 12:
print("\n\nTask 12 : Insert an IT company in the middle of the companies list");
it_companies.insert(int(len(it_companies)/2) , "TCS");
print(it_companies);

#Task 13:
print("\n\nTask 13 : Change one of the it_companies names to uppercase");
import random as r;
random = r.randrange(0, len(it_companies));
it_companies[random] = it_companies[random].upper();
print("The Upper case converted for : ", it_companies[random]);

#Task 14: 
print("\n\nTask 14: Join the it_companies with a string \'#;\'");
string = '#; '.join(it_companies);
print(string);

#Task 15:
print("\n\nTask 15: Check if a certain company exists in the it_companies list");
is_meta_exists = ("Meta" or "META") in it_companies;
print("Does \'Meta\' or \'META\' exists in the list: ", is_meta_exists);

#Task 16:
print("\n\nTask 16: Sort the list using sort() method");
it_companies.sort();
print("Sorted : ", it_companies);

#Task 17:
print("\n\nTask 17: Reverse the list descending order using reverse() method");
it_companies.reverse();
print("Desending order : ", it_companies);

#Task 18:
print("\n\nTask 18: Slice out the first 3 companies from the list");
it_companies.sort();
print("The First 3 companies : ", it_companies[0:3]);

#Task 19
print("\n\nTask 19: Slice out the last 3 companies from the list:");
print("The Last 3 companies : ", it_companies[-3:]);

#Task 20
import math as m;
print("\n\nTask 20: Slice out the middle IT company or companies from the list");
print("The Middle companies : ", it_companies[int(m.floor(len(it_companies)/2)) : int(m.ceil((len(it_companies)/2)))]);

#Task 21
print("\n\nTask 21: Remove the first IT company from the list");
first_company = it_companies[0];
it_companies.remove(first_company);
print(f"After removing : {first_company} : {it_companies}");

#Task 22
print("\n\nTask 22: Remove the middle IT company or companies from the list");
middle_company = it_companies[int(len(it_companies) / 2)];
it_companies.remove(middle_company);
print(f"After removing : {middle_company} : {it_companies}");

#Task 23
print("\n\nTask 23: Remove the last IT Company from the list");
last_company = it_companies[-1];
it_companies.remove(last_company);
print(f"After removing : {last_company} : {it_companies}");

#Task 24
print("\n\nTask 24: Remove all IT companies from the list");
it_companies.clear();
print("The list : ", it_companies);

#Task 25:
print("\n\nTask 25: Destroy the IT Companies list");
try:
    del it_companies; #destroying aka deleting the list.
    print(it_companies); #throws an exception that list is not accessible.
except Exception as e:
    print(f"The list is not accessible it is removed or deleted!\nError : {e}");

#Task 26:
print("\n\nTask 26: Join the following lists:");
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'];
back_end = ['Node', 'Express', 'MongoDB'];
print(front_end);
print(back_end);
joined = front_end + back_end;
print("Joined : ", joined);

#Task 27:
print("\n\nTask 27: After joining the lists in task 26. Copy the joined list and assign it to a variable full_stack.\nThen insert Python and SQL after Redux");
full_stack = joined.copy();
full_stack.insert(full_stack.index("Redux") + 1, ["Python", "SQL"]);
print(full_stack);
