# Task 1: Extract all incoming email addresses as a list from the email_exchanges_big.txt file.
import re as r
print('Task 1:\n')
path = 'G:\\Internship\\Internship-all-resources\\1. Python\\Exercises\\30DaysOfPython\\day_19\\data\\email_exchanges_big.txt'
email_pattern = r'^From:|From (\b[A-Za-z._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b)'
data = ''
with open(path, 'r') as emails_log:
    data = emails_log.read();
    emails_log.close()

incoming_emails = r.findall(email_pattern, data);
incoming_emails = list(set(incoming_emails));
incoming_emails.sort()
incoming_emails.reverse()
for index, email1 in enumerate(incoming_emails):
    print(f"{index+1}.{email1}");
print(f'\n\nTotally {len(incoming_emails)} incoming emails were found')

# Task 2: Find the most common words in English language. Call the name of your function 'find_most_common_words', it will take two
# parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in
# descending order.
print('\n\nTask 2: Printing testing file frequent words counts..')
clean_the_text = lambda data : r.sub(r'[~`!@#$%^&*()_\-\+=\{\}\[\]\|\\:;\"\',.?/]', '', data)
def get_words_counts(words):
    for word in words:
        if word == '':
            words.remove('');
    unique_words = set(words);
    counts = {}
    for word in unique_words:
        counts[word] = words.count(word);
    sorted_counts = sorted(counts.items(), key=lambda x : x[1], reverse=True);
    sorted_counts = [(count, word) for (word, count) in sorted_counts];
    return sorted_counts;

def find_most_common_words(path='G:\\Internship\\Internship-all-resources\\1. Python\\Exercises\\30DaysOfPython\\day_19\\data\\myData\\my_opinion.txt', top=0):
    import os as o
    import re as r
    data = ''
    if o.path.exists(path[0:path.rindex('\\')]):
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
find_most_common_words(path='G:\\Internship\\Internship-all-resources\\1. Python\\Exercises\\30DaysOfPython\\day_19\\data\\myData\\testing.txt',top=10);

# Task 3 : Use the function, find_most_frequent_words to find: 
# a) The ten most frequent words used in Obama's speech 
print('\n\nTask 3: ')
print('Obama\'s Speech:')
find_most_common_words(path='G:\\Internship\\Internship-all-resources\\1. Python\\Exercises\\30DaysOfPython\\day_19\\data\\obama_speech.txt', top=10);

# b) The ten most frequent words used in Michelle's speech 

print('Michelle\'s Speech:')
find_most_common_words(path='G:\\Internship\\Internship-all-resources\\1. Python\\Exercises\\30DaysOfPython\\day_19\\data\\michelle_obama_speech.txt', top=10);


# c) The ten most frequent words used in Trump's speech 

print('Trump\'s Speech:')
find_most_common_words(path='G:\\Internship\\Internship-all-resources\\1. Python\\Exercises\\30DaysOfPython\\day_19\\data\\donald_speech.txt', top=10);

# d) The ten most frequent words used in Melina's speech

print('Melina\'s Speech:')
find_most_common_words(path='G:\\Internship\\Internship-all-resources\\1. Python\\Exercises\\30DaysOfPython\\day_19\\data\\melina_trump_speech.txt', top=10);

#Task 4:Write a python application that checks similarity between two texts.
# It takes a file or a string as a parameter and it will evaluate the similarity of the two texts.
# For instance check the similarity between the transcripts of Michelle's and Melina's speech.
# You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). 
# List of stop words are in the 'data' directory
from data import stop_words;

