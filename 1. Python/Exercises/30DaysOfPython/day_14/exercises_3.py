from data import countries_data as cd;
#Task 1: Sort countries by name, by captial, by population
countries_data = cd.countries_data.copy()
countries_data.sort(key=lambda x: x['name'])
countries_data.sort(key=lambda x: x['capital'])
countries_data.sort(key=lambda x: x['population'])
print('Sorted based on name-capitial-population');
print('country-name|country-capital|country-population');
for country in countries_data:
    print(f"{country['name']}-------{country['capital']}-------{country['population']}");

#Task 2: Sort out the ten most spoken languages by location
print('\nTen Most Spoken Languages by locations');
def ten_most_spoken_langs():
    languages_of_all = []
    for country in cd.countries_data:
        for language in country['languages']:
            languages_of_all.append(language);
    unique_langs = set(languages_of_all);
    counts_of_unique_langs = {}
    for unique_lang in unique_langs:
        counts_of_unique_langs[unique_lang] = languages_of_all.count(unique_lang);
    sorted_based_on_language = sorted(counts_of_unique_langs.items(), key=lambda item: item[1], reverse=True);
    counts_of_unique_langs = {language:count_lang for (language, count_lang) in sorted_based_on_language}
    i = 1;
    ten_languages = []
    for language, counts in counts_of_unique_langs.items():
        if i <= 10:
            ten_languages.append(language);
            i += 1;
        else:
            break;
    # countries that speak ten languages
    countries_speak_top_10_languages = {}
    for language in ten_languages:
        locations = []
        for country in cd.countries_data:
            if language in country['languages']:
                locations.append(country['name']);
        countries_speak_top_10_languages[language] = sorted(locations)
    print('Ten Worlds most spoken languages:',ten_languages,'\n');
    for lang, countries in countries_speak_top_10_languages.items():
        print(f"{lang} : {countries}")
        print('\n')

ten_most_spoken_langs();

#Task 3: sort out the ten most populated countries

def ten_most_populated_countries():
    countries_data = cd.countries_data.copy()
    populations = {}
    for country in countries_data:
        populations[country['name']] = country['population'];
    new_sorted = sorted(populations.items(), key=lambda item: item[1], reverse=True)
    new_sorted = new_sorted[0:10];
    populations = {country:population for (country, population) in new_sorted}
    print('Top 10 most populated countries: \n')
    i = 1;
    for country, population in populations.items():
        print(f"{i}. {country} ---- {population}");
ten_most_populated_countries();