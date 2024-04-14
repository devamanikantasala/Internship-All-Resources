#Task 1:
#Write a function called is_prime, which checks if a number is prime
def is_prime(number):
    if(number < 2):
        return False;
    i = 2;
    import math as m;
    while(i <= int(m.sqrt(number))):
        if (number % i == 0):
            return False;
        i += 1;
    return True;

print("Task 1: Is 57 is a prime number -->", is_prime(57));

#Task 2:
#Write a function which checks if all items are unique in the list.
def is_all_items_unique(values_list):
    for i in values_list:
        if (i in values_list) and (values_list.count(i) > 1):
            return False;
    return True;

print("Task 2: All items in this list [1, 6, 2, 3, 4, 7, 5] are unique -->", is_all_items_unique([1, 6, 2, 3, 4, 7, 5]));
print("Task 2: All items in this list [1, 1, 2, 2, 3, 4, 4] are unique -->", is_all_items_unique([1, 1, 2, 2, 3, 4, 4]));

#Task 3:
#Write a function which checks if all the items of the list are of the same data type.
def is_all_items_same_type(values_list):
    for i in values_list:
        if not isinstance(i, type(values_list[0])):
            return False
            break;
    return True;

print("Task 3: Are the values are of same type in this [1, 2, 3, 4, 5, 6] list? -->", is_all_items_same_type([1, 2, 3, 4, 5, 6]));
print("Task 3: Are the values are of same type in this [\'Deva\', \'Manikanta\', 12119003, 20] list? -->", is_all_items_same_type(['Deva', 'Manikanta', 12119003, 20]));

#Task 4:
#Write a function which check if provided variable is a valid python variable.
def is_identifier(string):
    if(string.isidentifier()):
        return True;
    else:
        return False;
print("Task 4: Is the identifier \'12DevaManikanta\' valid? -->", is_identifier("12DevaManikanta"));
print("Task 4: Is the identifier \'name_of_student\' valid? -->", is_identifier("name_of_student"));

#Task 5:
#A) Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
from data import countries_data as cd;
def most_spoken_languages():
    languages_spoken = []
    for item in cd.countries_data:
        for language in item['languages']:
            languages_spoken.append(language);

    unique_languages = set(languages_spoken);
    counts_of_unique_languages = {}
    for language in unique_languages:
        counts_of_unique_languages[language] = languages_spoken.count(language);
    counts = list(counts_of_unique_languages.values());
    counts.sort();
    counts.reverse();
    counts = counts[0:20];
    i = 0;
    twenty_most_spoken_languages = []
    while(i < len(counts)):
        for language, count in counts_of_unique_languages.items():
            if(count == counts[i]):
                twenty_most_spoken_languages.append(language);
        i += 1;
    return twenty_most_spoken_languages;
print("\n\nTask 5.A: Top 20 most spoken languages : \n", most_spoken_languages());

#B) Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
from data import countries_data as cd;
def most_populated_countries():
    population_of_countries = []
    for item in cd.countries_data:
        population_of_countries.append(item['population'])

    population_of_countries.sort();
    population_of_countries.reverse();
    population_of_countries = population_of_countries[0:20];

    i = 0;
    twenty_most_populated_countries = [];
    while(i < len(population_of_countries)):
        for item in cd.countries_data:
            if(item['population'] == population_of_countries[i]):
                twenty_most_populated_countries.append(item['name']);
        i += 1;
    return twenty_most_populated_countries;
print("\n\nTask 5.B: Top 20 most populated countries:\n", most_populated_countries());
