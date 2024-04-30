#Task 1: Write a pattern which identifies if a string is a valid python variable
import re as r
def is_valid_variable(string):
    if r.match(r'^[a-zA-z]*[^-=+*%&\(\)/.,@#!~`\'\"<>?:;\{\}\[\]]\W{0,1}[a-zA-z]$', string):
        return True
    else:
        return False

print(is_valid_variable('first_name'));
print(is_valid_variable('first-name'));
print(is_valid_variable('1first_name'));
print(is_valid_variable('firstname'));
