#Task 1 : What is the most frequent word in the following paragraph
def get_items_of_values(dictionary, index):
    keys = []
    for key, value in dictionary.items():
        if value == index:
            keys.append(key);
    keys.sort();
    keys.reverse();
    return keys;

import re as r
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
paragraph = r.sub(r'\.', '', paragraph);
paragraph_set = set(paragraph.split(' '))
list_of_frequent_words = {}
for word in paragraph_set:
    pattern = r'\s'+word
    found_words = r.findall(pattern, paragraph);
    list_of_frequent_words[word] = len(found_words);
new_dict = dict(sorted(list_of_frequent_words.items(), key=lambda x : x[1], reverse=True));
values = list(set(new_dict.values()))
values.reverse();
new_dictionary = {}
for val in values:
    new_dictionary[val] = get_items_of_values(index=val, dictionary=new_dict);
new_list = [(key, value) for key, values in new_dictionary.items() for value in values]

print('[')
for index, item in enumerate(new_list):
    if index == len(new_list)-1:
        print(item);
    else:
        print(f"{item},");
print(']')

#Task 2: The Position of some particles on the horizontal x-axis are -12, -4, -3, -1 in negative direction, 0 at origin, 4, 8, in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

string = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0, at origin 4, and 8, in the positive direction.'
points = r.findall(r'-\d{1,2}|\d{1,2}', string);
print('The points : ', points);

sorted_points = sorted([int(i) for i in points]);
print('The sorted points : ', sorted_points);

distance = sorted_points[len(sorted_points)-1] - sorted_points[0]
print('The Distance : ', distance);