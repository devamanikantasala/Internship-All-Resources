# Task 1:
# Read the given (https://www.gutenberg.org/files/1112/1112-0.txt) url and find the 10 most frequent words.
print('\n\nTask 1: ')
import requests as re
from my_package import find_most_common_fx as fx;
response = re.get('https://www.gutenberg.org/files/1112/1112-0.txt')
data = response.text;
fx.find_most_common_words(path=data, top=10);

#Task 2:
# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find:
# a) the min, max, mean, median, standard deviation of cats weight in metric units
# b) the min, max, mean, median, standard deviation of cats lifespan in years
# c) Create a frequency table of country and breed of cats
response = re.get('https://api.thecatapi.com/v1/breeds')
data = response.json()
import json as js
formated_data = js.loads(js.dumps(data, indent=4));

print('\n\nTask 2: (a)')
weights = []
for each_data in formated_data:
    weights.append(each_data['weight']['metric']);
from my_package import myanynomous_fxs as fxs;
class_intervals_and_frequencies_weights = fxs.get_counts(weights);
class_intervals_and_frequencies_weights = sorted(class_intervals_and_frequencies_weights.items(), key=lambda x:x[0], reverse=True);
weights_2 = set()
for (x, y) in class_intervals_and_frequencies_weights:
    for metric_weights in y:
        weights_2.add(metric_weights);

# minimum
min_metric = min(weights_2);
# maximum
max_metric = max(weights_2)
del weights_2;
# mean
mean = fxs.eval_mean(class_intervals_and_frequencies_weights)
# median
median = fxs.eval_median(class_intervals_and_frequencies_weights);
#standard deviation
standard_deviation = fxs.eval_standard_deviation(class_intervals_and_frequencies_weights);

print(f'Cats Weights in metric units:\nClassIntervals : {fxs.get_ci_freqs(class_intervals_and_frequencies_weights)[0]} and,\nFrequencies : {fxs.get_ci_freqs(class_intervals_and_frequencies_weights)[1]}')
print(f'Minimum Metric Weight: {min_metric}')
print(f'Maximum Metric Weight: {max_metric}')
print(f'Mean of Cat weights : {mean}')
print(f'Median of Cats weights : {median}');
print(f'Standard Deviation of Cats weights : {standard_deviation}');

print('\n\nTask 2: (b)')
life_spans = []
for each_data in formated_data:
    life_spans.append(each_data["life_span"]);
class_intervals_and_frequencies_life_spans = fxs.get_counts(life_spans);
class_intervals_and_frequencies_life_spans = sorted(class_intervals_and_frequencies_life_spans.items(), key=lambda x : x[0], reverse=True);
life_spans_2 = set()
for (x, y) in class_intervals_and_frequencies_life_spans:
    for metric_weights in y:
        life_spans_2.add(metric_weights);
min_metric_life_span = min(life_spans_2);
max_metric_life_span = max(life_spans_2);
del life_spans_2;
mean_life_spans = fxs.eval_mean(class_intervals_and_frequencies_life_spans)
median_life_spans = fxs.eval_median(class_intervals_and_frequencies_life_spans)
standard_deviation_life_spans = fxs.eval_standard_deviation(class_intervals_and_frequencies_life_spans)
print(f'Cats Life Spans in Years:\nClassIntervals : {fxs.get_ci_freqs(class_intervals_and_frequencies_life_spans)[0]} and,\nFrequencies : {fxs.get_ci_freqs(class_intervals_and_frequencies_life_spans)[1]}')
print(f'Minimum Life Span Years: {min_metric_life_span}')
print(f'Maximum Life Span Years: {max_metric_life_span}')
print(f'Mean of Life Span Years : {mean_life_spans}')
print(f'Median of Life Span Years : {median_life_spans}');
print(f'Standard Deviation of Life Span Years : {standard_deviation_life_spans}');

print('\n\nTask 2: (c)')
countries = set()
for each_data in formated_data:
    countries.add(each_data['origin'])
country_specific_breeds = {}
for country in countries:
    breeds = []
    for each_data in formated_data:
        if each_data['origin'] == country:
            breeds.append(each_data['name']);
    # country_specific_breeds[str(country)+f'[{len(breeds)} breeds]'] = breeds;
    if len(breeds) > 1:
        country_specific_breeds[str(country)+f'[{len(breeds)} breeds]'] = breeds;
    else:
        country_specific_breeds[str(country)+f'[{len(breeds)} breed]'] = breeds;
country_specific_breeds = dict(sorted(country_specific_breeds.items(), key=lambda x:x[0]))
json_output = js.dumps(country_specific_breeds, indent=8);
print(json_output);

#Task 3:
# https://restcountries.com/v3.1/all
# Read the countries API and find
# a) the 10 largest countries
# b) the 10 most spoken languages
# c) the total number of languages in the countries API

response = re.get('https://restcountries.com/v3.1/all')
data = response.text;
data = js.loads(data)
print('\n\nTask 3: (a)')
#10 largest countries by area
countries_areas = {}
for country in data:
    countries_areas[country['name']['official']] = country['area']
countries_areas = dict(sorted(countries_areas.items(), key=lambda x: x[1], reverse=True))
countries_areas = dict(list(countries_areas.items())[0:10])
print('10 largest countries by area:')
countries_areas = js.dumps(countries_areas, indent=4);
print(countries_areas);
#10 largest countries by population
countries_population = {}
for country in data:
    countries_population[country['name']['official']] = country['population']
countries_population = dict(sorted(countries_population.items(), key=lambda x: x[1], reverse=True))
countries_population = dict(list(countries_population.items())[0:10])
print('10 largest countries by population:')
countries_population = js.dumps(countries_population, indent=4);
print(countries_population);
print('\n\nTask 3: (b)')
languages = []
for country in data:
    # for some countries 'languages' key is not recorded so.. to avoid 'KeyError', used exception handling..
    try:
        country_langs = list(country["languages"].values())
        languages.extend(country_langs);
    except KeyError as ke:
        pass;
languages_counts = fx.get_words_counts(languages);
del languages;
languages_counts = {language:str(str(number)+' countries') for (number,language) in languages_counts};
languages_counts_1 = dict(list(languages_counts.items())[0:10])
print('10 most spoken languages:')
languages_counts_1 = js.dumps(languages_counts_1, indent=4);
print(languages_counts_1);
print('\n\nTask 3: (c)')

print('Total languages in countries API is', len(languages_counts));

#Task 4:
print('\n\nTask 4:')
from bs4 import BeautifulSoup as BS;

# UCI is one of the most common places to get data sets for data science and machine learning. 
# Read the content of UCL ('https://archive.ics.uci.edu/datasets'). 
# Without additional libraries it will be difficult, so you may try it with BeautifulSoup4

response = re.get('https://archive.ics.uci.edu/datasets');
doc_holder = BS(response.text, 'html.parser')

title_of_webpage = (doc_holder.find('title')).get_text();
datasets = []
for tag in doc_holder.find_all('a'):
    if str(tag.get('href')).startswith('/dataset/'):
        if str(tag.get_text()) == ' ':
            pass;
        else:
            datasets.append(tag.get_text());

descriptions = []
for tag in doc_holder.find_all('p'):
    if 'truncate' in str(tag.get('class')):
        descriptions.append(tag.get_text());
attributes_of_datasets = []
for tag in doc_holder.find_all('span'):
    try:
        if 'truncate' in tag.get('class'):
            attributes_of_datasets.append(tag.get_text());
    except:
        pass;
website = {'url' : str(response.url),'title' : title_of_webpage, 'No.of Datasets' : len(datasets)}
updated_attributes = [attributes_of_datasets[i:i+4] for i in range(0, len(attributes_of_datasets), 4)]
count = 1;
while count <= len(datasets):
    try:
        website[str(f'dataset-{count}')] = {'name': datasets[count-1], 'description': descriptions[count-1], 'Add.Info' : updated_attributes[count-1]}
    except:
        pass
    count += 1;
website = js.dumps(website, indent=4);
print('Extracted Information and printing it as JSON..');
print(website);