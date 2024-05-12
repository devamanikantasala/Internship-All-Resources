import re as r
import os as o
clean_the_text = lambda data : r.sub(r'[\n~`!@#$%^&*()_\-\+=\{\}\[\]\|\\:;\"\',.?/]', '', data)
def get_words_counts(words: list):
    unique_words = set(words);
    unique_words.discard('')
    counts = {}
    for word in unique_words:
        counts[word] = words.count(word);
    sorted_counts = sorted(counts.items(), key=lambda x : x[1], reverse=True);
    sorted_counts = [(count, word) for (word, count) in sorted_counts];
    return sorted_counts;
def find_most_common_words(path='G:\\Internship\\Internship-all-resources\\1. Python\\Exercises\\30DaysOfPython\\day_19\\data\\myData\\my_opinion.txt', top=0):
    data = ''
    absolute_path = ''
    try:
        absolute_path = path[0:path.rindex('\\')];
    except:
        pass;
    if o.path.exists(absolute_path):
        with open(path, 'r') as file:
            data = file.read()
            file.close()
        data = clean_the_text(data)
        words = data.split(' ');
        counts = get_words_counts(words)
        print(' [')
        for i in range(top):
            if i == top-1:
                print(f'\t\t{counts[i]}');
            else:
                print(f'\t\t{counts[i]},');
        print(' ]');
        
    elif isinstance(path, str):
        data = clean_the_text(path)
        words = data.split(' ')
        counts = get_words_counts(words);
        print(' [')
        for i in range(top):
            if i == top-1:
                print(f'\t\t{counts[i]}');
            else:
                print(f'\t\t{counts[i]},');
        print(' ]');
    else:
        print('Invalid Type of data is given');