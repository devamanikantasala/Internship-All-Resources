#Task 1: names=['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
# Unpack the first five countries and store them in a variable called 'nordic_countries', store Estonia and Russia in 'es' and 'ru'
# respectfully
names=['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
names.reverse()
es, ru, *nordic_countries = names;
nordic_countries.reverse()
es, ru = ru, es
print(nordic_countries,'\n', es,'\n',ru);