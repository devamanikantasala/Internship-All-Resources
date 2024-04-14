#Task 1
#Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word 'land'.
from data import countries as c;
countries_ends_with_land = []
for country in c.countries:
    if(country.endswith("land")):
        countries_ends_with_land.append(country);

print("Countries ends with land : ", countries_ends_with_land);

#Task 2
#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(-1, -(len(fruits)+1), -1):
    reversed_fruits.append(fruits[i]);

fruits = reversed_fruits;
print("Reversed : ", fruits);

#Task 3
#Go to data folder and use the countries_data.py file
from data import countries_data as cd;

#1. What are the total number of languages in the data
languages = 0;
for item in cd.countries_data:
    languages += len(item['languages'])

print("The Total number of languages : ", languages);

#2. Find the ten most spoken languages from the data
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
counts = counts[0:10];
i = 0;
ten_most_spoken_languages = []
while(i < len(counts)):
    for language, count in counts_of_unique_languages.items():
        if(count == counts[i]):
            ten_most_spoken_languages.append(language);
    i += 1;
print("Ten Most spoken languages : ", ten_most_spoken_languages);

#3. Find the ten most populated countries in the world
population_of_countries = []
for item in cd.countries_data:
    population_of_countries.append(item['population'])

population_of_countries.sort();
population_of_countries.reverse();
population_of_countries = population_of_countries[0:10];

i = 0;
ten_most_populated_countries = [];
while(i < len(population_of_countries)):
    for item in cd.countries_data:
        if(item['population'] == population_of_countries[i]):
            ten_most_populated_countries.append(item['name']);
    i += 1;

print("Ten Most Populated Countries: ", ten_most_populated_countries);
