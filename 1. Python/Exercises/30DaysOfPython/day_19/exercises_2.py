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
clean_the_text = lambda data : r.sub(r'[\n~`!@#$%^&*()_\-\+=\{\}\[\]\|\\:;\"\',.?/]', '', data)
def get_words_counts(words):
    unique_words = set(words);
    unique_words.discard('')
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

#Task 4:
# Write a python application that checks similarity between two texts.
# It takes a file or a string as a parameter and it will evaluate the similarity of the two texts.
# For instance check the similarity between the transcripts of Michelle's and Melina's speech.
# You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). 
# List of stop words are in the 'data' directory
print('\n\nTask 4: ');
import re as r
clean_text = lambda text : r.sub(r'[\'\n~`!@#$%^&*()\+=\{\}\[\]\|\\:;\",.?/]', '', text);
def remove_support_words(text):
    from data import stop_words as sw;
    i = 0;
    list_of_text = text.split()
    while i < len(list_of_text):
        if list_of_text[i] in sw.stop_words:
            list_of_text.pop(i);
        else:
            i += 1
    return ' '.join(list_of_text);
def similarity_evaluation(text1, text2):
    words_text1 = set(text1.split())
    words_text2 = set(text2.split())
    # Reference taken from Geeks for Geeks Jaccard similarity logic
    intersection = len(words_text1.intersection(words_text2))
    union = len(words_text1.union(words_text2))
    if union == 0.0:
        return 0.0
    similarity = intersection/union
    return int(similarity*100)

def check_similiarity(path1='G:\\Internship\\Internship-all-resources\\1. Python\\Exercises\\30DaysOfPython\\day_19\\data\\michelle_obama_speech.txt'
                      ,path2 = 'G:\\Internship\\Internship-all-resources\\1. Python\\Exercises\\30DaysOfPython\\day_19\\data\\melina_trump_speech.txt'):
    import os as o
    actual_path1, actual_path2 = '', ''
    try:
        actual_path1 = path1[0:path1.rindex('\\')]
        actual_path2 = path2[0:path2.rindex('\\')]
    except ValueError:
        pass;
    if o.path.exists(actual_path1) and o.path.exists(actual_path2):
        data1 , data2 = '', ''
        with open(path1, 'r') as file1:
            data1 = file1.read()
            file1.close()
        with open(path2, 'r') as file2:
            data2 = file2.read()
            file2.close()
        
        removed_text1 = remove_support_words(clean_text(data1))
        removed_text2 = remove_support_words(clean_text(data2))

        similarity_score = similarity_evaluation(removed_text1, removed_text2);
        print(f'Similarity Score : {similarity_score}')
    elif o.path.exists(actual_path1) and isinstance(path2, str):
        data1 = ''
        with open(path1, 'r') as file1:
            data1 = file1.read()
            file1.close()
        removed_text1 = remove_support_words(clean_text(data1))
        removed_text2 = remove_support_words(clean_text(path2));
        similarity_score = similarity_evaluation(removed_text1, removed_text2);
        print(f'Similarity Score : {similarity_score}')
    
    elif o.path.exists(actual_path2) and isinstance(path1, str):
        data2 = ''
        with open(path2, 'r') as file2:
            data2 = file2.read()
            file2.close()
        removed_text2 = remove_support_words(clean_text(data2))
        removed_text1 = remove_support_words(clean_text(path1));
        similarity_score = similarity_evaluation(removed_text1, removed_text2);
        print(f'Similarity Score : {similarity_score}')
    
    elif isinstance(path1, str) and isinstance(path2, str):
        removed_text1 = remove_support_words(clean_text(path1));
        removed_text2 = remove_support_words(clean_text(path2));
        similarity_score = similarity_evaluation(removed_text1, removed_text2);
        print(f'Similarity Score : {similarity_score}')
    
    else:
        print('Invalid Data is given');

check_similiarity(path1='G:\\Internship\\Internship-all-resources\\1. Python\\Exercises\\30DaysOfPython\\day_19\\data\\obama_speech.txt', path2='Hello fellas im your new english teacher')

# Task 5 : Find the 10 most repeated words in the romeo_and_juliet.txt
print('\n\nTask 5: ')
# using the find_most_common_words() function from task 2
find_most_common_words(path='G:\\Internship\\Internship-all-resources\\1. Python\\Exercises\\30DaysOfPython\\day_19\\data\\romeo_and_juliet.txt', top=10);

#Task 6 : Read the hacker_news.csv file and find out: 
# a) Count the number of lines containing python or Python 
# b) Count the number lines containing JavaScript, javascript or Javascript 
# c) Count the number lines containing Java and not JavaScript
print('\n\nTask 6: ');
import csv as c;
data = ''
with open('G:\\Internship\\Internship-all-resources\\1. Python\\Exercises\\30DaysOfPython\\day_19\\data\\hacker_news.csv', encoding='utf-8') as file:
    data = c.reader(file, delimiter=',');
    lines_has_python = 0;
    lines_has_javascript = 0;
    lines_has_java = 0;
    import re as r
    for rows in data:
        for val in rows:
            lines_has_python += len(r.findall(r'\b[Pp]ython\b', val))
            lines_has_javascript += len(r.findall(r'\b[Jj]ava[Ss]cript\b', val))
            lines_has_java += len(r.findall(r'\b[Jj]ava\b', val))
    print('The Lines containing Python/python :', lines_has_python)
    print('The Lines containing javascript/JavaScript/Javascript :', lines_has_javascript)
    print('The Lines containing Java :', lines_has_java)
    file.close();
