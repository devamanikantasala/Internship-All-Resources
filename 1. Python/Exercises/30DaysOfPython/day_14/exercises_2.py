countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Task 1: Use map() to create a new list by changing each country to uppercase in the countries list
new_list_countries = list(map((lambda string: string.upper()), countries));
print('Upper Cased : ', new_list_countries);

#Task 2: Use map() to create a new list by changing each number to its square in the numbers list
new_list_numbers = list(map((lambda num: num**2), numbers));
print('Squared Numbers : ', new_list_numbers);

#Task 3: Use map() to create a new list by changing each name to uppercase in the names list
new_list_names = list(map((lambda string: string.upper()), names));
print('Upper Cased : ', new_list_names);

#Task 4: Use filter to filter out the countries containing 'land'
def containing_land(string):
    if string.find('land') != -1:
        return True;
    return False;
countries_containing_land = list(filter(containing_land, countries));
print('Countries Containing LAND:', countries_containing_land)

#Task 5: Use filter() to filter out the countries having exactly six characters
def only_six_characters(string):
    if len(string) == 6:
        return True;
    return False;

countries_names_having_exactly_6_letters = list(filter(only_six_characters, countries));
print('Countries names having 6 letters :', countries_names_having_exactly_6_letters);

#Task 6: Use filter() to filter out countries containing six letters and more in the country list;
def morethan_six_characters(string):
    if len(string) >= 6:
        return True;
    return False;

countries_names_having_morethan_6_letters = list(filter(morethan_six_characters, countries));
print('Countries names having more than 6 letters :', countries_names_having_morethan_6_letters);

#Task 7: Use filter() to filter out the countries starting with an 'E'
def is_country_startswith_E(country):
    if country.startswith('E'):
        return True;
    return False;
countries_startswith_E = list(filter(is_country_startswith_E, countries))
print('Countries starts with E:', countries_startswith_E);

#Task 8 : Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
apply_square = lambda a : a ** 2;
is_even = lambda a : a%2==0;
perform_sum = lambda a,b: a+b;
from functools import reduce;
data = [i for i in range(1, 21)];
total = reduce(perform_sum, list(filter(is_even, list(map(apply_square, data)))));
print('The sum of squared-even numbers from 1-20 is:', total);

#Task 9: Declare a function called get_string_lists which takes a list as a parameter and then return a list containing only string items
data = [i for i in range(1, 21)]
data.insert(2, 'Deva')
data.insert(3, 'Jeevan')
data.insert(4, 'Adithya')
is_string = lambda i: isinstance(i, str) 
get_string_list = lambda list_of_values : list(filter(is_string, list_of_values));
print('From the list',data, '\nAll string items:',get_string_list(data))

#Task 10: Use reduce() to sum all the numbers in the numbers list
data = [i for i in range(1, 21)];
# iam here again using perform_sum lambda function
total = reduce(perform_sum, data);
print(f"Numbers from {min(data)} to {max(data)} Total is:",total);

#Task 11: Use reduce to concatenate all the countries and to produce this sentence : 
#Estonia, Finland, Sweden, Denmark, Norway and Iceland are north European countries
def concatenate(string1, string2):
    if string2 == countries[len(countries)-1]:
        return str(string1 +' and '+ string2);
    else:
        return str(string1 +', '+ string2);
string = str(reduce(concatenate, countries)) + ' are north European Countries';
print(f'From the list : {countries}:\n{string}');    

#Task 12: Declare a function called categorize_countries that returns a list of countries with some common pattern
from data import countries as c;
filter_stan = lambda country: country.find('stan') != -1
filter_island = lambda country: country.find('island') != -1
filter_ia = lambda country: country.endswith('ia');
filter_land = lambda country: country.find('land') != -1;

countries_pattern = {}
countries_pattern['land'] = list(filter(filter_land, c.countries));
countries_pattern['ia'] = list(filter(filter_ia, c.countries));
countries_pattern['island'] = list(filter(filter_island, c.countries));
countries_pattern['stan'] = list(filter(filter_stan, c.countries));

for pattern, countries in countries_pattern.items():
    print(f'The countries which have {pattern} pattern : {countries}');


#Task 13: Create a function returning a dictionary, where keys stand for starting letters of countries and value
countries_first_letters_unique = set()
for country in c.countries:
    countries_first_letters_unique.add(country[0].upper());
countries_first_letters_unique = sorted(countries_first_letters_unique);
# print(countries_first_letters_unique);

alphabetical_countries = {}
for letter in countries_first_letters_unique:
    get_country_name = lambda country_name : letter.lower() == country_name[0].lower()
    alphabetical_countries[letter] = list(filter(get_country_name, c.countries));

for letter, countries in alphabetical_countries.items():
    print(f'------------{letter}------------')
    i = 1
    for country in countries:
        print(f'{i}. {country}');
        i += 1;

#Task 14: Declare a get_first_ten_countries function - it returns a list of first ten countries
get_first_ten_countries = lambda : c.countries[0:10];
print('The first ten countries: ', get_first_ten_countries());

#Task 15: Declare a get_last_ten_countries function - it returns a list of last ten countries
get_last_ten_countries = lambda : c.countries[-10:];
print('The last ten countries: ', get_last_ten_countries());