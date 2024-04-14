#Task 1:
#Write a function which generates a six digit/character
from random import random, randint;
import string as st;
def random_user_id():
    characters = st.ascii_letters + st.digits;
    i = 0;
    random_string_user_id = ""
    while (i < 6):
        random_index = randint(0, len(characters)-1);
        random_string_user_id += characters[random_index];
        i += 1;
    return random_string_user_id;

print("Task 1: Random 6 Digit/Character string --> ", random_user_id());

#Task 2:
#Modify the previous task. Declare a function named user_id_gen_by_user. It doesn't take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supported to be generated.
def user_id_gen_by_user():
    length_of_each = int(input("Enter the length of each ID : "));
    how_many = int(input("Enter how many IDs do you need : "));
    characters = st.ascii_letters + st.digits;
    random_string_user_ids = [];
    i = 0;
    id = ''
    while (i < how_many):
        j = 0;
        while (j < length_of_each):
            random_index = randint(0, len(characters)-1);
            id += characters[random_index];
            j += 1;
        random_string_user_ids.append(id);
        id = ''
        i += 1;
    
    for i in random_string_user_ids:
        print(i);

print("Task 2: Random N ids with N length ---> As Follows");
user_id_gen_by_user();

#Task 3:
#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    value_1 = randint(0, 255);
    value_2 = randint(0, 255);
    value_3 = randint(0, 255);
    print(f"rgb({value_1}, {value_2}, {value_3})");

print("Task 3: Random Rgb Color ---> ", end = "");
rgb_color_gen();
