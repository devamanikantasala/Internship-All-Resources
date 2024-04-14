#Task 1:
#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list.
import random as r;
def shuffle_list(list_of_items):
    i = 0;
    random_index = [];
    shuffled_list = [];
    while (i < len(list_of_items)):
        random_index_var = r.randint(0, len(list_of_items)-1);
        if random_index_var in random_index:
            continue;
            i -= 1;
        else:
            shuffled_list.append(list_of_items[random_index_var]);
        random_index.append(random_index_var)
        i += 1;
    return (shuffled_list);

print("Task 1: The Shuffled List of ['Hi', 'This', 'is', 'Deva Manikanta'] -->",shuffle_list(['Hi', 'This', 'is', 'Deva Manikanta']))
print("Task 1: The Shuffled List of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -->",shuffle_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]));
print("Task 1: The Shuffled List of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -->",shuffle_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]));

#Task 2:
#Write a function which returns a array of seven random numbers in a range of 0-9. All the numbers must be unique.
def array_of_seven_random_numbers():
    i = 0;
    seven_random_numbers = [];
    added = [];
    while (i < 7):
        random_number = r.randint(0,9);
        if random_number in added:
            continue;
            i -= 1;
        else:
            seven_random_numbers.append(random_number);
        added.append(random_number);
        i += 1;
    return seven_random_numbers;

print("Task 2: The 7 random unique numbers -->", array_of_seven_random_numbers());
