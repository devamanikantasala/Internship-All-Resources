#Globally used this path

path = 'G:\\Internship\\Internship-all-resources\\1. Python\\Exercises\\30DaysOfPython\\day_19\\data'

# Task 1: Write a function which count number of lines and number of words in a text file.
# a) Read obama_speech.txt file and count number of lines and words
# b) Read michelle_obama_speech.txt file and count number of lines and words
# c) Read donald_speech.txt file and count number of lines and words
# d) Read melina_trump_speech.txt file and count number of lines and words from the 'data' folder
print('Task 1:');
import os as o;
def get_count_of_number_of_words(path):
    with open(path,'r') as file:
        lines = file.read().splitlines();
        print(f'The No.of Lines: {len(lines)}');
        file.close();
    with open(path, 'r') as file:
        words = file.read()
        print(f'There are {len(words)} words in the file.');
        file.close();

files = o.listdir(path);
files.sort();
dont_print_these = ['countries_data.json','email_exchanges_big.txt', 'stop_words.py', 'myData', '__pycache__', 'romeo_and_juliet.txt', 'hacker_news.csv']
i = -1;
index = 1
while(i != 0):
    print('\nChoose which file you want insights:\n');
    for file in files:
        if file in dont_print_these:
            continue;
        else:
            print(f'{index}.\t{file}');
            index += 1
    print('0.\tExit')
    i = int(input('Your choice: '));
    if(i == 1):
        get_count_of_number_of_words(str(path+'\\donald_speech.txt'));
        break;
    elif(i == 2):
        get_count_of_number_of_words(str(path+'\\melina_trump_speech.txt'));
        break;
    elif(i == 3):
        get_count_of_number_of_words(str(path+'\\michelle_obama_speech.txt'));
        break;
    elif(i == 4):
        get_count_of_number_of_words(str(path+'\\obama_speech.txt'));
        break;
    else:
        print('You Choose Exit Bye..');
        break;

#Task 2: Read the countries_data.json file in 'data' directory, create a function that finds the 'n' most spoken languages
print('\n\nTask 2: ')
def most_spoken_languages(filename = str(path+'\\countries_data.json'), n=0):
    import json as js;
    data = ''
    with open(filename, 'r', encoding='utf-8') as jsonFile:
        data = jsonFile.read()
        jsonFile.close();
    countries_data = js.loads(data);
    # print(countries_data);
    languages_of_world = []
    for country in countries_data:
        for language in country['languages']:
            languages_of_world.append(language);
    unique_languages = set(languages_of_world);
    counts = {}
    for language in unique_languages:
        counts[language] = languages_of_world.count(language);
    sorted_languages_based_on_counts = sorted(counts.items(), key=lambda item:item[1], reverse=True);
    sorted_languages_based_on_counts = [(value, key) for (key, value) in sorted_languages_based_on_counts];
    i = 0;
    print('[')
    while i < n:
        if i == n-1:
            print(f'\t{sorted_languages_based_on_counts[i]}');
        else:
            print(f'\t{sorted_languages_based_on_counts[i]},');
        i += 1
    print(']')
most_spoken_languages(n = 10);

#Task 3: Read the countries_data.json file in 'data' directory, create a function that creates a list of 'n' most populated countries
print('\n\nTask 3:');
def most_populated_countries(filename= str(path+'\\countries_data.json'), n=0):
    import json as js
    data = ''
    with open(filename, 'r', encoding='utf-8') as jsonFile:
        data = jsonFile.read()
        jsonFile.close()
    countries_data = js.loads(data);
    populations_of_countries = {}
    for country in countries_data:
        populations_of_countries[country['name']] = country['population'];
    populations_of_countries = sorted(populations_of_countries.items(), key=lambda item: item[1], reverse=True);
    final_list = []
    for (country, population) in populations_of_countries:
       final_list.append({'country':country, 'population':population});
    i = 0
    print('[')
    while i < n:
        if i == n-1:
            print(f'\t{final_list[i]}');
        else:
            print(f'\t{final_list[i]},');
        i += 1
    print(']');
most_populated_countries(n=10);