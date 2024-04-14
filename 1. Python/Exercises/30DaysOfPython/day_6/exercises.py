#Exercise Level 1:
print("EXERCISE LEVEL 1")
#Task 1:
print("Task 1: Create an empty tuple");
my_tuple = ();

#Task 2:
print("\n\nTask 2: Create a tuple containing names of your sisters and yours brothers");
my_brothers = ("Deva", "Manikanta", "Jeevan", "Adithya");
my_sisters = ("Surekha", "Swathi", "Rajeswari", "Swapna");

#Task 3:
print("\n\nTask 3: Join brothers and sisters tuples and assign it to sibilings");
my_sibilings = my_brothers + my_sisters;

#Task 4:
print("\n\nTask 4: How many sibilings do you have?");
print(f"I have  {len(my_sibilings)} sibilings!");

#Task 5:
print("\n\nTask 5: Modify the sibilings tuple and add the name of your father and mother and assign it to family_members");
try:
    my_sibilings.append("Mallikarjuna"); #Adding father name to the end of my_sibilings tuple
except Exception as e:
    print("Modifying tuple is not possible");
    print("Error!", e);

#hence creating a new tuple and adding my_sibilings to it
family_members = ("Mallikarjuna", "Suguna") + my_sibilings;
print("The Family members tuple : ", family_members);

#Exercise : Level 2
#Task 1:
print("\n\nEXERCISE LEVEL 2");
print("\n\nTask 1: Unpack sibilings and parents from family_members");
father_name, mother_name, *sibilings = family_members;
print("Unpacked : ", father_name,"-", mother_name,"-",sibilings);

#Task 2:
print("\n\nTask 2: Create fruits, vegetables, and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp");
fruits = ("Apple", "Banana", "Cherry", "Dragon Fruit");
vegetables = ("Potato", "Brinjal", "Radish", "Tomato");
non_vegetables = ("Chicken", "Mutton", "Fish", "Shrimp");
food_stuff_tp = fruits + vegetables + non_vegetables;
print("The Food Stuff Tuple : ", food_stuff_tp);

#Task 3:
print("\n\nTask 3: Change the about food_stuff_tp tuple to a food_stuff_lt list");
food_stuff_lt = list(food_stuff_tp);
print("The Food Stuff List : ", food_stuff_lt);

#Task 4:
print("\n\nTask 4: Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list");
print("The Middle item of the tuple : ", food_stuff_tp[int(len(food_stuff_tp) / 2)]);
print("The Middle item of the list : ", food_stuff_lt[int(len(food_stuff_lt) / 2)]);

#Task 5:
print("\n\nTask 5: Slice out the first three items and last three items from food_stuff_li list");
print("The first three items : ", food_stuff_lt[0:3]);
print("The last three items : ", food_stuff_lt[-3:]);

#Task 6:
print("\n\nTask 6: Delete the food_stuff_tp tuple completely");
try:
    del food_stuff_tp;
    print("Trying to access! food_stuff_tp....");
    print(food_stuff_tp);
except Exception as e:
    print("Exception raised and hence the tuple is deleted....");
    print("Exception :", e);

#Task 7:
print("\n\nTask 7: Check if an item exists in tuple");
nordic_contries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden");
print("Tuple : ", nordic_contries);
print("Estonia is in the above tuple : ", ("Estonia" in nordic_contries));
print("Iceland is in the above tuple : ", ("Iceland" in nordic_contries));
