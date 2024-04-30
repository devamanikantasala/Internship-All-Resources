#Task 1 : Clean the following text after cleaning, count 3 most frequent words in the string
import re as r
clean_the_text = lambda sentence : r.sub(r'[~`!@#$%^&*()_\-\+=\{\}\[\]\|\\:;\"\',.?/]', '', sentence)

def three_most_frequent_words(string):
    words = string.split(' ');
    frequent_words = set(words);
    most_frequent_words = {}
    for word in frequent_words:
        most_frequent_words[word] = words.count(word);
    output = sorted(most_frequent_words.items(), key=lambda items:items[1], reverse=True);
    most_frequent_words = dict(output);
    del output;
    values = list(set(most_frequent_words.values()))
    values.sort()
    values.reverse();
    output = {}
    for value in values:
        words = []
        for key, values in most_frequent_words.items():
            if values == value:
                words.append(key)
        words.sort()
        words.reverse()
        output[value] = words
    final_output=[(key, value) for key, values in output.items() for value in values]
    return f'The 3 Most frequent words : {final_output[0]}, {final_output[1]}, {final_output[2]}'
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = clean_the_text(sentence)
print(f'The Cleaned Text : \'{cleaned_text}\'');

print(three_most_frequent_words(cleaned_text));
