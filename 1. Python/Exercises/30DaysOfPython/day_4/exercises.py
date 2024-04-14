#Task 1
print("\nTask 1 : Concatenate the String \'Thirty\', \'Days\', \'Of\', \'Python\' to single String");
string = "Thirty";
string += " Days "+"Of"+" Python";
print(string);

#Task 2
print("\nTask 2 : Concatenate the String \'Coding\', \'For\', \'All\' to single String");
string1 = "Coding";
string1 += " For" + " All";

#Task 3
print("\nTask 3 : Declare a variable named company and assign it to an initial value \'Coding For All\'");
company = "Coding For All";

#Task 4
print("\nTask 4 : Print the variable company using print()");
print("Company : ", company);

#Task 5
print("\nTask 5 : Print the length of company string using len() method and print()");
print("Length of \'", company , "\' is : ", len(company));

#Task 6
print("\nTask 6 : Change all the character to uppercase letters.");
upperCase_company = company.upper();
print("Company Variable Upper Case : ", upperCase_company);

#Task 7
print("\nTask 7 : Change all the characters to lowercase letters.");
lowerCase_company = upperCase_company.lower();
print("Company Variable Lower Case : ", lowerCase_company);

#Task 8
print("\nTask 8 : Use capitalize(), title(), swapcase() methods to format the value of the string \'Coding For All\'.");
company = "coding for all";
print("Actual String : ", company);
print("capitalize() : ", company.capitalize());
print("title() : ", company.title());
print("swapcase() : ", company.swapcase());

#Task 9
print("\nTask 9 : Cut out the first word of \'Coding For All\'");
print("First word : ", company[0:6]);

#Task 10
print("\nTask 10 : Check if \'Coding For All\' string contains a word \'Coding\' using the string methods.");
string = "Coding For All";
if(string.find("Coding") != -1):
    print("Yes! There is a substring \'Coding\' in Coding For All");
else:
    print("No! There is no substring \'Coding\' in Coding For All");

#Task 11
print("\nTask 11: Replace the word \'Coding\' in the string \'Coding For All\' to \'Python\'");
string = string.replace("Coding", "Python");
print("Replaced String : ", string);

#Task 12
print("\nTask 12: Change \'Python For Everyone\' to \'Python For All\' using the replace method or other methods");
string = "Python For Everyone"
string = string.replace("Everyone", "All");
print("Replaced String : ", string);

#Task 13
print("\nTask 13: Split the string \'Coding For All\' using space as the seperator (split()) ");
string = "Coding For All"
string_splited = string.split(" ");
print("The Splitted String : ", string_splited);

#Task 14
new_string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon";
print("Task 14: \'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon\' split the string at the comma");
new_string_splited = new_string.split(",");
print("Splited : ", new_string_splited);

#Task 15
print("\nTask 15: What is the character at the index 0 in the string \'Coding For All\'.");
print("Character at index 0 is : ", string[0]);

#Task 16
print("\nTask 16: What is the last index of the string \'Coding For All\'");
print("Last index of the string \'", string, "\' : ", (len(string) - 1));

#Task 17
print("\nTask 17: What character is at index 10 in \"Coding For All\" string");
print("Character at index 10: ", string[10]);

#Task 18
print("\nTask 18: Create an acronym or an abbrevation for the name \'Python For Everyone\' ");
string1 = "Python For Everyone";
string1_split = string.split(" ");
acronym = string1_split[0][0] + string1_split[1][0] + string1_split[2][0];
print("The Acronym for \'Python For All\' : ", acronym);

#Task 19
print("\nTask 19: Create an acronym or an abbrevation for the name \'Coding For All\'");
string2 = "Coding For All";
string2_split = string.split(" ");
acronym1 = string2_split[0][0] + string2_split[1][0] + string2_split[2][0];

#Task 20
print("\nTask 20: Use index() to determine the position of the first occurrence of C in Coding For All");
index = string2.index('C');
print("The Index of C in first occurance : ", index);

#Task 21
print("\nTask 21: Use index() to determine the position of the first occurance of F in Coding For All");
index1 = string2.index('F');
print("The Index of F in second occurance : ", index1);

#Task 22
print("\nTask 22: Use rfind() to determine the position of the last occurance of l in Coding For All People");
index2 = "Coding For All People".rfind('l');
print("The last occurance of l : ", index2);

#Task 23
print("\nTask 23: Use index() or find() to find the position of the first occurrence of the word \'because\' in the following sentence:\n\'You cannot end a sentence with because because because is a conjunction\'");
print("The First Occurance : ", ("You cannot end a sentence with because because because is a conjunction").index("because"));

#Task 24
print("\nTask 24: Use rindex() to find the position of the last occurrence of the word because in the following sentence:\n\'You Cannot end a sentence with because because because is a conjunction\'");
print("The last occurrence is at : ", ("You Cannot end a sentence with because because because is a conjunction").rindex('because'));


#Task 25
print("\nTask 25: Slice out the phrace \'because because because\' in the following sentence:\n\'You Cannot end a sentence with because because because is a conjunction\'");
print("Sliced : ", ("You Cannot end a sentence with because because because is a conjunction")[31:55]);

#Task 26
print("\nTask 26: Find the position of the first occurance of the word \'because\' in the following sentence: \n\'You Cannot end a sentence with because because because is a conjunction\'");
print("First Occurance is at : ", ("You Cannot end a sentence with because because because is a conjunction").index('because'));

#Task 27 : repeated task - actual task : Task 25

#Task 28
print("\nTask 28: Does \'Coding For All\' starts with a substring \'Coding\'");
print("Is it? : ", ("Coding For All").startswith("Coding"));

#Task 29
print("\nTask 29: Does \'Coding For All\' ends with a substring \'Coding\'");
print("Is it? : ", ("Coding For All").endswith("Coding"));

#Task 30
print("\nTask 30: \'\tCoding For All   \', remove the left and right trailing spaces in the given string");
print("Output : \'", ('    Coding For All    ').strip(), "\'");

#Task 31
print("\nTask 31: Which one of the following variables return True when we use the method isidentifier()");
print("1. 30DaysOfPython : ", ('30DaysOfPython').isidentifier());
print("1. thirty_days_of_python : ", ('thirty_days_of_python').isidentifier());

#Task 32
print("\nTask 32: The Following list contains the names of some of python libraries:\n['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'].Join the list with a hash with space string");
modules_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'];
joined_string = '# '.join(modules_list);
print("Output: ",joined_string);

#Task 33
print("\nTask 33: Use the new line espace sequence to seperate different sentences");
print("Iam enjoying this challenge.\nI just wonder what is next.");


#Task 34
print("\nTask 34: Use a tab escape sequence to add tabspaces between..");
print("Name\t\tAge\tCountry\tCity");
print("Asabeneh\t250\tFinland\tHelsinki");

#Task 35
print("\nTask 35: Use the string formatting method to display the message - more details in 4.Strings.pptx file");
string = "{} = {}\n{} = {} * {} ** {}\n{} {} {} {} {}".format("radius", 10, "area", 3.14, "radius", 2, "The area of a circle with radius", 10, "is", 314, "meters square.")
print(string);

#Task 36
print("\nTask 36: Make the following using string formatting methods - more details in 4.Strings.pptx file");
print(f"{8} + {6} = {8+6}\n{8} - {6} = {8-6}\n{8} * {6} = {8*6}\n{8} / {6} = {8/6:.2f}\n{8} % {6} = {8%6}\n{8} // {6} = {8//6}\n{8} ** {6} = {8**6}");
