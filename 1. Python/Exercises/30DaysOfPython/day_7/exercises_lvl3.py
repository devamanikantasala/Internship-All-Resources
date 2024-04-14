#Task 1:
#Convert the age's list to a set and compare the length of the list and the set, which one is bigger?
age_list = [22, 19, 24, 25, 2, 6, 24, 25, 24]
age_set = set(age_list);

if(len(age_set) > len(age_list)):
    print("The Ages Set is bigger than Ages List");
else:
    print("The Ages List is bigger than Ages Set");

#Task 2:
#Explain the difference between the following data types : String, list, tuple, and set
'''
    String : It is a data type that only holds characters/group of characters which are enclosed withing single or double quotes. 
    str() is the built-in class in python that supports the strings in python.
'''
#For Eg:
string1 = "Hi! This is string example";

'''
    List : List is a ordered collection data type that holds a wide variety of data types in to a single unit. 
    List is mutable type that allows to perform operations to alter the data for further, list uses the square brackets, and different data types that are enclosed
    within [] which are seperated by commmas are the list items, it also encourages the concept of indexing, slicing and accessing the items with index start from 0 to n-1.
    And it also provides negative indexing to access the list item from backwards like indexs ranges from -1 to -n
    list() is the built-in class in python that supports the lists in python
'''
#For Eg:
list1 = ["Hi!", "Everyone", "This is a", "list", 1211, True, False] #We can add any type of data types in it..

'''
    Tuple : Tuple is also a ordered collection data type that holds a wide variety of data types in to a single unit.
    Tuple is immutable type that doesn't allow to perform operations to alter the data for further, tuples uses the parenthesis, and like list it does allow different data types 
    that are enclosed within () which are seperated by commas are tuple items, it also supports indexing, slicing and accessing the items with index starts from 0 to n-1. And
    it also provides negative indexing to access the tuple items from backwards like indexes ranges from -1 to -n
    tuple() is the built-in class in python that supports the tuples in python
'''
#For Eg:
tuple1 = ("Hi!", "Everyone", "This is a", "list", 1211, True, False, 134.2, 1239)

'''
    Set : Set is a unordered collection data type that holds a wide variety of data types in to a single unit.
    set is mutable type that allow to perform operations to add or remove the data for further, sets uses the curly braces, and like lists and tuple it does allow different data types 
    that are enclosed within {} which are seperated by commas are set items, it doesn't supports indexing, slicing and accessing.
    Relative to set theory the sets in python only holds the unique values in a unordered, these doesn't follow a certain order like lists and tuples in python..
    set() is the built-in class in python that supports the sets in python
'''
set1 = {"Hi!", "Everyone", "This is a", "list", 1211, True, False, "This is a"} # Here there are two similar items specified - "This is a", set in python only stores one item rather than storing both of them..


#Task 3:
# "I am a teacher and I love to inspire and teach people", How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
string2 = "I am a teacher and I love to inspire and teach people";
list2 = string2.split(" ");
set2 = set(list2);
print("There are : ", len(set2), " unique words");
